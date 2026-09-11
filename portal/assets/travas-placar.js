// Monta o Placar das 8 Travas a partir de travas-data.js.
// Usado por destrava/identificar. O dado vem do gerador
// .claude/scripts/build_travas_data.py, esta camada só desenha.
(function () {
  var esc = function (s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  };

  // Os textos do dossiê vêm com parágrafos separados por linha em branco.
  var partes = function (txt) {
    return String(txt).split(/\n\s*\n/).filter(function (p) { return p.trim(); });
  };
  var paras = function (txt) {
    return partes(txt).map(function (p) { return '<p>' + esc(p.trim()) + '</p>'; }).join('');
  };

  // O texto do dossiê fica inteiro, um clique abaixo do resumo em linguagem
  // direta. A tela nunca substitui a fonte: ela dá uma porta de entrada.
  var dobra = function (rotulo, txt) {
    if (!txt) return '';
    return '<details class="mais"><summary>' + rotulo + '</summary>' +
           '<div class="prosa">' + paras(txt) + '</div></details>';
  };

  var itens = function (txt) {
    var partes = [], atual = '', nivel = 0;
    for (var i = 0; i < txt.length; i++) {
      var c = txt.charAt(i);
      if (c === '(') nivel++;
      else if (c === ')') nivel = Math.max(0, nivel - 1);
      if (c === ';' && nivel === 0) { partes.push(atual); atual = ''; continue; }
      atual += c;
    }
    partes.push(atual);
    return partes.map(function (x) { return x.trim(); }).filter(Boolean);
  };

  // Vira lista so quando a lista existe de fato. Com uma ou duas partes o
  // paragrafo continua sendo a forma certa.
  var talvezLista = function (txt) {
    var ps = partes(txt);
    if (ps.length > 1) return paras(txt);
    var xs = itens(ps[0] || txt);
    if (xs.length < 3) return paras(txt);
    return '<ul class="falta-lista">' + xs.map(function (x) {
      return '<li>' + esc(x.replace(/\.$/, '')) + '</li>';
    }).join('') + '</ul>';
  };

  var pill = function (nota, extra) {
    var vazia = nota === null || nota === undefined;
    return '<span class="d ' + (vazia ? 'vazio' : 'n' + nota) + ' ' + (extra || '') + '">' +
           (vazia ? '·' : nota) + '</span>';
  };

  var br = function (n, casas) {
    return n === null || n === undefined ? null : n.toFixed(casas).replace('.', ',');
  };

  // "(A) Alcance mensal" vira "Alcance mensal": a letra é indexação interna.
  var limpo = function (nome) { return nome.replace(/^\([A-E]\)\s*/, ''); };

  var lista = function (itens) {
    if (itens.length === 1) return itens[0];
    return itens.slice(0, -1).join(', ') + ' e ' + itens[itens.length - 1];
  };

  // Opcional: a data da leitura costuma vir na barra de título da página.
  var carimbo = document.getElementById('carimbo');
  if (carimbo) {
    carimbo.textContent = 'leitura de ' + ((TRAVAS.meta || {}).gerado_em || 'data não declarada');
  }

  var fechadas = TRAVAS.travas.filter(function (t) { return t.score_total !== null; });
  var baixa = TRAVAS.travas.filter(function (t) { return t.confiabilidade === 'baixa'; });
  var semEvid = TRAVAS.travas.reduce(function (a, t) {
    return a + t.dimensoes.filter(function (d) { return d.nota === null; }).length;
  }, 0);
  var totalDim = TRAVAS.travas.reduce(function (a, t) { return a + t.dimensoes.length; }, 0);

  document.getElementById('resumo').innerHTML = [
    ['', fechadas.length + ' de ' + TRAVAS.travas.length,
      'travas com as cinco notas fechadas. As outras seis não têm soma'],
    ['alerta', semEvid + ' de ' + totalDim,
      'pontos que ficaram sem nota, por falta de evidência para avaliar'],
    ['alerta', baixa.length + ' de ' + TRAVAS.travas.length,
      'travas cuja leitura ainda é frágil e pode mudar'],
    ['', TRAVAS.teto_por_dimensao + ' de 5',
      'nota máxima que a evidência de hoje autoriza dar']
  ].map(function (k) {
    return '<div class="kpi ' + k[0] + '"><div class="v">' + k[1] + '</div>' +
           '<div class="l">' + k[2] + '</div></div>';
  }).join('');

  var seta = '<svg class="seta" width="12" height="12" viewBox="0 0 24 24" fill="none" ' +
    'stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" ' +
    'aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg>';

  document.getElementById('placar').innerHTML = TRAVAS.travas.map(function (t) {
    var faltando = t.dimensoes.filter(function (d) { return d.nota === null; })
                              .map(function (d) { return limpo(d.nome); });

    // Uma frase por trava, montada a partir dos números e nunca escrita à mão.
    var frase;
    if (!faltando.length) {
      frase = 'Os cinco pontos foram avaliados. Soma <b>' + t.score_total + ' de ' +
        t.maximo_praticavel + '</b>, com nota média de ' + br(t.media_por_dimensao, 1) +
        ' por ponto.';
    } else {
      frase = '<b>' + faltando.length + (faltando.length === 1 ? ' dos 5 pontos ficou' : ' dos 5 pontos ficaram') +
        ' sem nota</b> por falta de evidência: ' +
        '<span class="falta">' + esc(lista(faltando)) + '</span>. Por isso esta trava não tem soma, ' +
        'e o que foi avaliado deu nota média de ' + br(t.media_por_dimensao, 1) + '.';
    }

    var soma = t.score_total !== null
      ? '<b>' + t.score_total + '</b> de ' + t.maximo_praticavel + '<span class="sub">soma</span>'
      : '<span class="nulo">sem soma</span><span class="sub">falta evidência</span>';

    var pre = t.nome === 'Cegueira'
      ? ' <span class="pre">pré-condição</span>' : '';

    var dims = t.dimensoes.map(function (d) {
      return '<div class="dim"><div class="dim-h">' +
        pill(d.nota, 'dim-nota') +
        '<span class="nome">' + esc(limpo(d.nome)) + '</span>' +
        '<span class="tag">' + (d.natureza === 'ausente' ? 'sem evidência' : 'avaliado') +
        '</span></div>' + paras(d.evidencia) + '</div>';
    }).join('');

    return '<details class="linha"><summary>' +
      '<span class="tv">' + seta + esc(t.nome) + pre + '</span>' +
      '<span class="dims">' + t.dimensoes.map(function (d) { return pill(d.nota); }).join('') +
      '</span>' +
      '<span class="num">' + soma + '</span>' +
      '<span class="conf ' + esc(t.confiabilidade) + '">' +
      (t.confiabilidade === 'baixa' ? 'leitura frágil' : 'leitura parcial') + '</span>' +
      '</summary><div class="corpo">' +
      '<p class="diagnose">' + frase + '</p>' +
      (t.politica_implicita
        ? '<h4>A política que sustenta esta trava</h4><div class="politica"><p>' +
          esc(t.politica_implicita) + '</p></div>'
        : '') +
      '<h4>O que falta para fechar</h4>' + talvezLista(t.o_que_falta) +
      dobra('Ver a conta da nota e a leitura de método',
            t.escala + '\n\n' + t.interpretacao) +
      '<h4>Os cinco pontos, um a um</h4>' + dims +
      '</div></details>';
  }).join('');

  document.getElementById('gate-detalhe').innerHTML =
    dobra('Ver a regra e o que falta trava por trava', TRAVAS.gate_consolidacao);

  [['candidata', TRAVAS.candidata_a_restricao, 'Ver o que caiu, argumento por argumento'],
   ['naoconclusiva', TRAVAS.por_que_nao_e_conclusiva, 'Ver as seis razões, em ordem de peso'],
   ['denominador', TRAVAS.alerta_denominador_publicacao, 'Ver as duas leituras e as fontes']
  ].forEach(function (b) {
    document.getElementById(b[0]).innerHTML = b[1]
      ? dobra(b[2], b[1])
      : '<p class="fonte">Não registrado no dossiê.</p>';
  });
})();
