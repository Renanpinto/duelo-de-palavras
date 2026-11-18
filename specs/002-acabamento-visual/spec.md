# Spec: acabamento visual do jogo

- **Status:** implementada; conferência visual pendente
- **Data:** 2026-11-17

## Problema

A seta dos seletores parece encostada à borda, o contador de partida ocupa espaço
sem ajudar a jogar e a marca atual é apenas a letra “D”.

## Resultado esperado

A tela mantém foco no jogo, com controles mais equilibrados e uma marca vetorial
consistente entre o cabeçalho e a instalação PWA.

## Requisitos funcionais

- **RF-1:** A seta dos seletores tem espaçamento visual confortável da borda, sem
  remover o comportamento acessível do seletor nativo.
- **RF-2:** O contador “Partida livre · #X” não aparece.
- **RF-3:** O texto de destaque é “Desafio de agora.”
- **RF-4:** O cabeçalho usa um ícone vetorial da marca no lugar do “D”.
- **RF-5:** O rodapé deixa de exibir “Feito para duas pessoas competitivas. 💜” e
  mantém a informação de que o progresso fica salvo no aparelho.
- **RF-6:** O ícone atualizado é utilizado também como ícone da aplicação PWA.

## Critérios de aceite

- **CA-1:** As setas dos dois seletores ficam visualmente afastadas da borda e os
  menus continuam abrindo e selecionando opções normalmente.
- **CA-2:** Não existe contador de partida visível na barra de controles.
- **CA-3:** A chamada aparece como “Desafio de agora.”, sem a frase antiga.
- **CA-4:** O cabeçalho mostra o novo ícone, sem a letra “D”, e o mesmo arquivo
  vetorial é referenciado como favicon e ícone PWA.
- **CA-5:** O rodapé mantém “Seu progresso fica salvo neste aparelho.” e remove a
  frase sobre duas pessoas competitivas.

## Fora de escopo

- Alterar regras, vocabulário, pontuação ou funcionamento dos seletores.
- Criar arte raster ou adicionar dependências externas.

