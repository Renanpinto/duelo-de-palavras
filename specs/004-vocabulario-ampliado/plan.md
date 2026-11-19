# Plano: vocabulário ampliado

## Resumo técnico

Unir listas pt-BR licenciadas, filtrar tokens de 4 a 7 letras, normalizar e
deduplicar em `data/palavras-pt-br.txt`. O jogo carrega o arquivo
localmente durante a inicialização e aguarda a carga se a pessoa enviar um
palpite antes dela terminar. As formas normalizadas se juntam às palavras
curadas para validação; as listas de respostas também deixam de conter plurais
conhecidos e formas conjugadas fora do infinitivo.

## Arquivos e áreas afetadas

- `data/palavras-pt-br.txt`: lista derivada de palpites.
- `data/README.md`: fonte, licença, atribuição e filtros aplicados.
- `index.html`: carregamento local assíncrono, validação sem acentos, grafia
  original na revelação e rolagem do teclado após selecionar uma casa.
- `sw.js`: cache offline do novo arquivo.
- `README.md`: vocabulário, origem e limite de respostas curadas.

## Decisões

- Fontes: FrequencyWords pt_BR, baseada em OpenSubtitles 2018 (CC BY-SA 4.0),
  mais `lexico` e `conjugações` de fserb/pt-br (MIT); os avisos ficam em
  `data/README.md` e `data/LICENSE-fserb-MIT.txt`.
- Transformação: manter apenas tokens alfabéticos de 4 a 7 letras, deduplicar
  após remoção de acentos e caixa; registrar que a lista foi filtrada e
  normalizada.
- A lista de frequência só valida palpites. Respostas continuam sendo listas
  curadas por categoria para evitar sorteios raros.
- Cada resposta mantém texto original acentuado e chave normalizada separada;
  uma casa marcada correta mostra a letra original da resposta.
- Toques nas casas rolam até o teclado apenas quando ele não está todo visível;
  movimento reduzido usa rolagem imediata.
- Arquivo local e cache do service worker preservam o funcionamento estático e
  offline. Se o carregamento falhar, o jogo continua com a lista atual.

## Sequência de implementação

1. Unir as fontes licenciadas, preservar plurais e conjugações nos palpites,
   filtrar por tamanho e registrar atribuição e licenças.
2. Integrar carregamento local com fallback e validação normalizada.
3. Atualizar cache, README, spec e tarefas.
4. Conferir os critérios de aceite no navegador.

## Riscos e compatibilidade

- As fontes incluem palavras raras; o arquivo ampliado não é usado para sortear
  respostas.
- A normalização sem acentos colapsa formas distintas como `pais`/`país`; a
  lista de palpites mantém apenas uma forma normalizada.
- Carregar um arquivo extra aumenta a transferência inicial, mas o arquivo é
  texto estático e permanece em cache depois do primeiro carregamento.

## Verificação

- Conferir palavras acentuadas e sem acento, comprimentos 4–7 e fallback.
- Conferir funcionamento offline e tamanho de viewport móvel.
- Registrar pendências caso a conferência no navegador não seja possível.
