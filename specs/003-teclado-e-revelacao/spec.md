# Spec: teclado e revelação das tentativas

- **Status:** implementada; conferência em navegador pendente
- **Data:** 2026-11-17

## Problema

O vocabulário curto recusa palavras portuguesas comuns, e o teclado visual não
segue o arranjo pedido na referência. A tentativa também muda todas as casas para
suas cores de uma só vez, sem revelar o resultado de forma gradual.

## Resultado esperado

Palavras comuns em português são aceitas, e cada tentativa válida revela as cores
letra a letra. O teclado virtual segue o arranjo da imagem fornecida.

## Requisitos funcionais

- **RF-1:** As palavras `pombo`, `porta` e `polvo` são aceitas como palpites de
  cinco letras.
- **RF-2:** Ao enviar uma tentativa válida, as casas da linha revelam seus estados
  em sequência, da esquerda para a direita.
- **RF-3:** Durante a revelação, não é possível editar ou enviar outra tentativa.
- **RF-4:** O teclado virtual tem três linhas: `QWERTYUIOP`; `ASDFGHJKL` com um
  ícone compacto de apagar no fim; `ZXCVBNM` com Enter largo à direita. Não
  inclui `Ç`.
- **RF-5:** Letras digitadas no teclado físico continuam normalizadas sem
  acentos.

## Critérios de aceite

- **CA-1:** Os palpites `POMBO`, `PORTA` e `POLVO` passam pela validação com
  tamanho de cinco letras.
- **CA-2:** Após Enter, a cor das casas é revelada uma a uma na ordem de leitura.
- **CA-3:** Não é possível alterar a linha durante a animação; ao terminar, o
  próximo palpite pode ser digitado.
- **CA-4:** O teclado visual reproduz a ordem e posição da referência, usa ícone
  compacto e acessível para apagar, e não inclui tecla `Ç`.
- **CA-5:** Digitar letras acentuadas pelo teclado físico continua comparando
  sem acentos.
- **CA-6:** Em viewport de celular, as teclas cabem na largura disponível e Enter
  continua visualmente mais largo que as teclas de letra.

## Fora de escopo

- Trocar o vocabulário por um dicionário completo ou conectar a um serviço online.
- Alterar regras de pontuação, tamanho de palavras ou número de tentativas.

