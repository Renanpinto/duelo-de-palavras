# Spec: vocabulário ampliado

- **Status:** implementada; conferência em navegador pendente
- **Data:** 2026-11-19

## Problema

A lista local pequena rejeita muitos palpites válidos em português brasileiro,
mesmo quando as pessoas reconhecem palavras comuns.

## Resultado esperado

O jogo aceita uma lista substancialmente maior de palpites portugueses de 4 a 7
letras, sem aumentar a chance de sortear palavras raras como resposta. A lista
fica em arquivo separado, é carregada localmente e funciona offline após o cache.

## Requisitos funcionais

- **RF-1:** O jogo aceita formas de palavras de 4 a 7 letras extraídas de fontes
  pt-BR licenciadas, além das listas atuais.
- **RF-2:** A lista nova é armazenada em arquivo de dados separado e distribuída
  localmente, sem chamada a serviço externo durante a partida.
- **RF-3:** A comparação mantém normalização sem acentos, caixa ou duplicatas.
- **RF-4:** As palavras sorteadas continuam vindo das listas atuais curadas por
  categoria; a fonte ampliada serve para validar palpites.
- **RF-5:** Respostas sorteadas não são plurais nem verbos conjugados fora do
  infinitivo.
- **RF-6:** Palpites podem usar formas plurais e verbais conjugadas se estiverem
  na fonte de vocabulário; essas formas não são rejeitadas apenas por serem
  flexionadas.
- **RF-7:** A fonte, licença, atribuição e filtros de cada lista derivada ficam
  documentados junto aos dados e no README.
- **RF-8:** A digitação e a comparação não exigem acentos; casas corretas e a
  palavra revelada preservam a grafia acentuada original da resposta.
- **RF-9:** Ao selecionar uma casa no tabuleiro em tela pequena, a página rola
  até deixar o teclado virtual visível.

## Critérios de aceite

- **CA-1:** Palavras portuguesas de 4, 5, 6 e 7 letras presentes na nova lista
  passam pela validação.
- **CA-2:** Formas com acentos continuam podendo ser digitadas sem acentos.
- **CA-3:** Tokens fora de 4 a 7 letras ou que contenham caracteres que não
  sejam letras são descartados da lista derivada.
- **CA-4:** Uma forma plural ou verbal conjugada presente na fonte pode ser
  submetida como palpite, mas não é escolhida como resposta.
- **CA-5:** Nenhuma palavra da fonte ampliada entra no sorteio automaticamente.
- **CA-6:** A lista é carregada de arquivo local e está incluída no cache offline.
- **CA-7:** A documentação identifica FrequencyWords/OpenSubtitles (CC BY-SA
  4.0), fserb/pt-br (MIT), atribuições e alterações feitas para este jogo.
- **CA-8:** A resposta `limão` aceita o palpite `limao`; letras corretas são
  exibidas como `LIMÃO` durante a revelação e a resposta final aparece como
  `Limão`.
- **CA-9:** Tocar numa casa fora da área visível do teclado rola a página para
  exibir todas as teclas, sem rolar se o teclado já estiver visível e respeitando
  a preferência por movimento reduzido.
- **CA-10:** O arquivo local tem pelo menos 60 mil palpites únicos de 4 a 7
  letras, após normalização e deduplicação.

## Estados e casos de borda

- Palavra duplicada após normalização de acentos: manter uma entrada.
- Uma forma plural ou conjugada pode ser aceita como palpite, mesmo se também
  tiver outra interpretação lexical; respostas permanecem nas listas curadas.
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
- [fserb/pt-br](https://github.com/fserb/pt-br): léxico pt-BR e formas de
  conjugação, publicados no repositório sob MIT.
- `specs/003-teclado-e-revelacao/spec.md`: regras atuais do vocabulário local.
