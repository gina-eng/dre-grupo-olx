# Acessos e Ferramentas

**E-mail oficial para liberação de todos os acessos:** `gina@v4company.com`
**Nível de permissão solicitado:** leitura / visualização (padrão do método).
**Conta de domínio OLX (desde 24/08):** `rafael.corazza-ext@olxbr.com`, compartilhada no time da V4
por enquanto. É por ela que passa tudo o que o Grupo OLX restringe a e-mail corporativo, e é para ela
que os acessos novos do lado da OLX devem ser concedidos.

> **Regra do método:** a ausência de um acesso **não bloqueia** o projeto, mas é registrada como
> **evidência diagnóstica** de maturidade e possível trava. Nenhum diagnóstico é feito com base em
> suposição quando o acesso não está disponível.

## 1. Data room (Google Drive)

| Item | Detalhe |
|---|---|
| Link | <https://drive.google.com/drive/folders/1Hrj2w5RlHbJaEVvLK0caHF9hx8LCPq44> |
| Dono | Grupo OLX |
| Restrição | Arquivos restritos a quem tem e-mail corporativo `@olxbr.com` |
| Status | 🟡 **Parcialmente liberado (24/08).** A primeira das 3 contas `@olxbr.com` foi criada: `rafael.corazza-ext@olxbr.com`, credenciais enviadas por `ga-account@olxbr.com`. Faltam as de Anselmo Bueno e Guilherme Monteiro. |
| Ação | ✅ Aberto e testado em 24/08: primeiro lote baixado, 9 arquivos dos blocos E e I. Índice em [`assets/originais/README.md`](../assets/originais/README.md). Cobrar as outras 2 contas no kick-off. |
| Material já baixado | Bloco E: 8 peças da campanha Mês do Corretor 2026 (SP, consideração, RE). Bloco I: 1 teste A/B da LP Anuncie ZAP. |
| Senha | **Não fica neste repositório.** Gerenciador de senhas da V4. Trocar no primeiro acesso e ligar 2FA: ela circulou por e-mail e por chat. |

## 2. Contas de mídia (Google / Meta)

| Unidade | Conta | ID | Status (14/09/2026) |
|---|---|---|---|
| Imóveis | VR09 · ZAP+ MCC VivaReal | 526-656-0190 | 🟢 Ingerindo. 23 campanhas, R$ 2,75 mi |
| Imóveis | VR · ZAP+ | 612188193108418 | 🟢 **Aprovada no lote de 10/09, ingerindo desde 12/09** |
| Autos | OLX \| Autos \| B2B | 1742214902479721 | 🟢 **Aprovada no lote de 10/09, ingerindo desde 12/09** |

> ✅ **Situação em 14/09: as três contas ingerem.** As duas contas de Meta pedidas em 21/08 foram
> aprovadas no lote de 10/09 e o V4MOS saiu de `data: []`. A recoleta de 14/09, sobre 01/01/2025 a
> 14/09/2026, devolve **90 campanhas, 1.079 anúncios e R$ 7.375.303,34 no Meta**, contra 23
> campanhas e R$ 2.746.029,59 no Google. **O Meta pesa 2,7 vezes o Google**, o inverso da leitura
> que este documento carregava desde agosto.
>
> 🔴 **Corrigido em 16/09 pelo [diagnóstico (vi)](../02-diagnostico/diagnostico-vi-midia-paga.md).** O export
> direto mostrou **5 contas de Google Ads** e R$ 17,45 mi na mesma janela: o V4MOS cobre **15,7%** do Google e
> **1,5% do que ele vê é B2B**. A razão entre Meta e Google não é conhecida.
>
> Duas ressalvas seguem de pé, e são as que importam para o diagnóstico (vi):
>
> - **Nenhuma das três contas separa B2B de B2C.** 90,4% do investimento de Meta está em campanhas
>   com sufixo `_pf`, a mesma nomenclatura que no Google levanta a hipótese de consumidor final
>   ([PENDÊNCIAS 12](../PENDENCIAS.md)). Isso não é conclusão, é nomenclatura sem confirmação.
> - **O portfólio pode ser maior que as duas contas.** A lista de contas de anúncio de
>   `New OLX Brasil` nunca foi recebida, então R$ 7,38 mi é piso, não total
>   ([PENDÊNCIAS 11](../PENDENCIAS.md)).
>
> O GA4 mostrou que existem ao menos **7 outras contas de Google Ads** na operação do grupo, nenhuma
> liberada. Ver [PENDÊNCIAS 12](../PENDENCIAS.md).

## 3. Acessos previstos por frente (solicitados, status a consolidar)

| Frente | Acesso | Status |
|---|---|---|
| CRM Marketing | Salesforce Marketing Cloud (visualização) | ⚪ A confirmar |
| CRO/SEO | Google Search Console de cada propriedade B2B | 🟠 Sem concessão (verificado 31/08) |
| CRO/SEO | Ferramenta de SEO interna (SEMrush / Ahrefs / similar) | ⚪ A confirmar · pode não existir |
| Mídia paga | Google Ads (leitura) | 🟡 Só a MCC VR09 (526-656-0190). O GA4 revelou 7 outras contas vinculadas ao ZapImóveis, ver PENDÊNCIAS 12 |
| Mídia paga | Meta Ads (leitura) | 🟡 Em liberação |
| Redes sociais | Meta Business Suite (analista) | ⚪ A confirmar |
| Redes sociais | LinkedIn Company Page(s) | ⚪ A confirmar |
| Redes sociais | Demais canais ativos (YouTube, TikTok…) | ⚪ A confirmar |
| Tracking | GA4 · propriedade(s), nível analista | ✅ **Liberado em leitura (31/08)**, 26 propriedades em 3 contas: Grupo OLX `285763706`, OLX `70177409`, Viva Real `126375`. Nível de permissão **a confirmar** na interface, ver PENDÊNCIAS 13 |
| Tracking | GTM · contêiner(es) publicados, leitura | 🟠 Sem concessão (verificado 31/08) |
| LPs / Conversão | Ferramenta de comportamento (Hotjar / Clarity / similar) | ⚪ A confirmar · pode não existir |
| Pré-vendas / Comercial | CRM comercial (leitura) | ⚪ A confirmar |
| Pré-vendas / Comercial | Ferramenta de sales engagement (se houver) | ⚪ A confirmar |
| Pré-vendas / Comercial | Gravações de calls de qualificação (10–15 recentes) | ⚪ A confirmar |

**Legenda:** ✅ liberado · 🟡 em andamento · 🟠 pendente do lado do cliente · ⚪ não iniciado · 🔴 negado/inexistente

## 4. Ferramentas V4

| Ferramenta | Uso | Link |
|---|---|---|
| V4.Marketing | Cockpit do cliente: ciclo, fase, trava, comitês, métricas de throughput. Preenchimento obrigatório na Semana 1 | - |
| Sistema Destrava Receita (RevenueFlow) | Elaboração e revisão do Forecast | <https://v4-revenueflow.lovable.app/> |
| HOPS / MKT.Lab | Pipeline operacional do franqueado | - |
| Banco de Evidências | Repositório de artefatos curados por trava e setor | - |

## 5. Governança de credenciais (cláusulas 5.7–5.10 do contrato)

- Credenciais usadas **única e exclusivamente** para a finalidade contratual.
- Acesso restrito a profissionais estritamente necessários, sob compromisso de confidencialidade.
- Troca de senhas periódica e **obrigatória** ao término da prestação ou em suspeita de incidente.
- Armazenamento residual pós-contrato: **máximo 30 dias**, depois eliminação segura ou anonimização.
- A OLX pode solicitar revogação ou alteração das credenciais a qualquer tempo.
- Encarregado de Proteção de Dados V4: `lgpd@v4company.com.br`
