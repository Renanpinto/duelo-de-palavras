# Spec: vocabulário ampliado

- **Status:** implementada; conferência em navegador pendente
- **Data:** 2026-11-17

## Problema

A lista local pequena rejeita muitos palpites válidos em português brasileiro,
mesmo quando as pessoas reconhecem palavras comuns.

## Resultado esperado

O jogo aceita uma lista substancialmente maior de palpites portugueses de 4 a 7
letras, sem aumentar a chance de sortear palavras raras como resposta. A lista
fica em arquivo separado, é carregada localmente e funciona offline após o cache.

## Requisitos funcionais

- **RF-1:** O jogo aceita formas de palavras de 4 a 7 letras extraídas de uma
  lista de frequência pt-BR licenciada, além das listas atuais.
- **RF-2:** A lista nova é armazenada em arquivo de dados separado e distribuída
  localmente, sem chamada a serviço externo durante a partida.
- **RF-3:** A comparação mantém normalização sem acentos, caixa ou duplicatas.
- **RF-4:** As palavras sorteadas continuam vindo das listas atuais curadas por
  categoria; a fonte ampliada serve para validar palpites.
- **RF-5:** Palavras no plural e formas verbais conjugadas não infinitivas são
  removidas do vocabulário aceito; verbos no infinitivo podem permanecer.
- **RF-6:** A fonte, licença, atribuição e filtros da lista derivada ficam
  documentados junto aos dados e no README.
- **RF-7:** A digitação e a comparação não exigem acentos; casas corretas e a
  palavra revelada preservam a grafia acentuada original da resposta.
- **RF-8:** Ao selecionar uma casa no tabuleiro em tela pequena, a página rola
  até deixar o teclado virtual visível.

## Critérios de aceite

- **CA-1:** Palavras portuguesas de 4, 5, 6 e 7 letras presentes na nova lista
  passam pela validação.
- **CA-2:** Formas com acentos continuam podendo ser digitadas sem acentos.
- **CA-3:** Tokens fora de 4 a 7 letras ou que contenham caracteres que não
  sejam letras são descartados da lista derivada.
- **CA-4:** Formas plurais e verbos conjugados que não estejam no infinitivo são
  descartados do vocabulário aceito; formas infinitivas são preservadas.
- **CA-5:** Nenhuma palavra da fonte ampliada entra no sorteio automaticamente.
- **CA-6:** A lista é carregada de arquivo local e está incluída no cache offline.
- **CA-7:** A documentação identifica FrequencyWords, corpus OpenSubtitles 2018,
  licença CC BY-SA 4.0 e as alterações feitas para este jogo.
- **CA-8:** A resposta `limão` aceita o palpite `limao`; letras corretas são
  exibidas como `LIMÃO` durante a revelação e a resposta final aparece como
  `Limão`.
- **CA-9:** Tocar numa casa fora da área visível do teclado rola a página para
  exibir todas as teclas, sem rolar se o teclado já estiver visível e respeitando
  a preferência por movimento reduzido.

## Estados e casos de borda

- Palavra duplicada após normalização de acentos: manter uma entrada.
- Uma forma com mais de uma interpretação lexical (por exemplo, uma forma que
  também seja substantivo e forma verbal) pode ser removida se a fonte registrar
  a mesma forma como plural ou conjugação; a lista final não contém duplicatas.
- Arquivo indisponível: jogo segue com o vocabulário local atual e informa a
  limitação sem travar a interface.
- Tela pequena/offline: arquivo fica em cache; não há novas dependências.

## Fora de escopo

- Substituir as palavras de resposta curadas ou sortear qualquer entrada da lista
  de frequência.
- Cobrir todas as palavras ou variantes existentes em português.
- Fazer atualização dinâmica ou consultar serviços remotos.

## Referências

- [FrequencyWords](https://github.com/hermitdave/FrequencyWords): lista de
  frequência, com conteúdo sob CC BY-SA 4.0, derivado do corpus OpenSubtitles.
- [fserb/pt-br](https://github.com/fserb/pt-br): léxico e listas de flexões
  auxiliares, usados para filtrar os palpites.
- `specs/003-teclado-e-revelacao/spec.md`: regras atuais do vocabulário local.
