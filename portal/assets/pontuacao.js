// Grade de pontuação das 8 travas, do ângulo do diagnóstico: qual nota existe,
// qual dimensão ainda não tem nota e qual diagnóstico fecha cada uma.
// O dado vem de travas-data.js, gerado por .claude/scripts/build_travas_data.py.
// Esta camada só desenha: nenhum número é digitado aqui.
(function () {
  var esc = function (s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  };

  // Quem fecha cada trava, de 02-diagnostico/auditorias-contratadas.md.
  // É a única parte desta tela que não sai do gerador, porque o mapa
  // diagnóstico → trava vive no documento de escopo, não no placar.
  var FECHA = {
    'Cegueira':     [{ n: 'vii', o: 'Rastreamento', st: 'fechado' }],
    'Exposição':    [{ n: 'vi', o: 'Mídia paga', st: 'aberto' }, { n: 'ii', o: 'CRO e SEO', st: 'aberto' },
                     { n: 'v', o: 'Orgânico', st: 'aberto' }, { n: 'iii', o: 'GEO', st: 'aberto' }],
    'Atenção':      [{ n: 'iv', o: 'Criativos', st: 'aberto' }, { n: 'vi', o: 'Mídia paga', st: 'aberto' },
                     { n: 'v', o: 'Orgânico', st: 'aberto' }, { n: 'iii', o: 'GEO', st: 'aberto' }],
    'Interesse':    [{ n: 'viii', o: 'Páginas de captura', st: 'aberto' }, { n: 'ii', o: 'CRO e SEO', st: 'aberto' },
                     { n: 'i', o: 'CRM', st: 'parcial' }],
    'Qualificação': [{ n: 'ix', o: 'Pré-vendas', st: 'aberto' }, { n: 'vi', o: 'Mídia paga', st: 'aberto' }],
    'Compromisso':  [{ n: 'ix', o: 'Pré-vendas', st: 'aberto' }, { n: 'viii', o: 'Páginas de captura', st: 'aberto' }],
    'Decisão':      [{ n: 'ix', o: 'Pré-vendas', st: 'aberto' }],
    'Retenção':     [{ n: 'i', o: 'CRM', st: 'parcial' }]
  };

  var letra = function (nome) {
    var m = String(nome).match(/^\(([A-E])\)/);
    return m ? m[1] : '?';
  };
  var soLetra = function (nome) {
    return String(nome).replace(/^\([A-E]\)\s*/, '');
  };

  function celula(dim) {
    if (dim.nota === null || dim.nota === undefined) {
      return '<td class="pt-nota pt-vazia" title="dimensão ainda sem nota: o diagnóstico que a fecha não fechou">' +
             '<span aria-hidden="true">·</span><span class="sr-so-leitor">sem nota</span></td>';
    }
    var teto = dim.nota >= 3 ? ' pt-teto' : '';
    return '<td class="pt-nota' + teto + '" title="' + esc(soLetra(dim.nome)) + '">' + dim.nota + '</td>';
  }

  function linha(t) {
    var cols = t.dimensoes.map(celula).join('');
    var quem = (FECHA[t.nome] || []).map(function (d) {
      return '<span class="pt-dg pt-' + d.st + '">(' + d.n + ') ' + esc(d.o) + '</span>';
    }).join('');
    var fechada = t.pontuadas === t.total_dimensoes;
    var soma = fechada
      ? '<b>' + t.score_total + '</b> de ' + t.maximo_praticavel
      : '<span class="pt-parcial">' + t.pontuadas + ' de ' + t.total_dimensoes + ' notas</span>';
    var norm = fechada && t.normalizado_25 !== null && t.normalizado_25 !== undefined
      ? String(t.normalizado_25).replace('.', ',') + ' / 25'
      : '<span class="pt-parcial" title="soma incompleta não pode ser normalizada nem comparada">não comparável</span>';
    return '<tr class="' + (fechada ? 'pt-fechada' : '') + '">' +
      '<th scope="row">' + esc(t.nome) + '</th>' + cols +
      '<td class="pt-soma">' + soma + '</td>' +
      '<td class="pt-norm">' + norm + '</td>' +
      '<td class="pt-quem">' + quem + '</td></tr>';
  }

  function monta() {
    var alvo = document.getElementById('pontuacao');
    if (!alvo || typeof TRAVAS === 'undefined') return;
    var ts = TRAVAS.travas;
    var fechadas = ts.filter(function (t) { return t.pontuadas === t.total_dimensoes; });
    var notas = ts.reduce(function (n, t) { return n + t.pontuadas; }, 0);
    var cabecalho = ts[0].dimensoes.map(function (d) {
      return '<th scope="col" class="pt-dim">' + letra(d.nome) + '</th>';
    }).join('');

    alvo.innerHTML =
      '<div class="scrollx pt-caixa"><table class="pt-grade">' +
      '<thead><tr><th scope="col">Trava</th>' + cabecalho +
      '<th scope="col">Soma</th><th scope="col">Na escala do método</th>' +
      '<th scope="col">Fecha com</th></tr></thead><tbody>' +
      ts.map(linha).join('') + '</tbody></table></div>' +
      '<p class="pt-rodape"><b>' + notas + ' de 40 notas atribuídas</b> · ' +
      fechadas.length + ' das 8 travas com as cinco dimensões fechadas (' +
      fechadas.map(function (t) { return esc(t.nome); }).join(' e ') + '). ' +
      'Dado gerado em ' + esc(TRAVAS.meta.gerado_em) + ', o mesmo do placar em Destrava Receita.</p>';
  }

  if (document.readyState !== 'loading') monta();
  else document.addEventListener('DOMContentLoaded', monta);
})();
