# Spec: jogo atual

- **Status:** baseline documentado
- **Data:** 2026-11-13

## Problema

Jogadores querem um desafio rápido de adivinhar uma palavra em português, sem
conta ou instalação obrigatória.

## Resultado esperado

A pessoa escolhe categoria e tamanho, preenche uma tentativa, recebe indicação
visual das letras e pode continuar até acertar ou esgotar seis tentativas.

## Histórias de usuário

- Como jogador, quero escolher uma categoria e palavras de 4 a 7 letras para
  ajustar o desafio.
- Como jogador, quero escolher a casa que vou preencher e receber feedback por
  letra para entender cada tentativa.
- Como jogador, quero abrir o jogo no celular e manter minhas estatísticas nesse
  aparelho.

## Requisitos funcionais

- **RF-1:** O jogo oferece seis tentativas e permite escolher palavras de 4, 5,
  6 ou 7 letras.
- **RF-2:** A pessoa pode preencher pelo teclado físico ou virtual e selecionar
  diretamente uma casa da linha atual.
- **RF-3:** Uma tentativa só é aceita se estiver completa e pertencer ao
  vocabulário local do jogo. Acentos são normalizados para comparar palavras.
- **RF-4:** Cada letra recebe estado correto, presente ou ausente, considerando
  letras repetidas sem contar ocorrências extras.
- **RF-5:** O jogo apresenta categorias, instruções, resultado e opção de iniciar
  outra partida.
- **RF-6:** Estatísticas ficam salvas localmente por navegador/aparelho.
- **RF-7:** A página pode ser instalada como PWA e usa service worker quando
  servida em contexto compatível.

## Critérios de aceite

- **CA-1:** Ao escolher um tamanho, o tabuleiro e a validação usam o mesmo número
  de casas.
- **CA-2:** Ao clicar numa casa vazia da linha atual e digitar uma letra, ela
  aparece naquela posição.
- **CA-3:** Uma tentativa incompleta ou fora do vocabulário recebe uma mensagem
  e não consome uma linha.
- **CA-4:** Uma tentativa válida mostra o feedback de cor por posição e mantém as
  letras no tabuleiro.
- **CA-5:** Acertar ou esgotar as seis tentativas apresenta o resultado e permite
  começar outra partida.
- **CA-6:** Partidas concluídas atualizam estatísticas locais.

## Estados e casos de borda

- Tentativa incompleta ou palavra não reconhecida deve permanecer editável.
- Letras duplicadas não podem receber feedback amarelo além da quantidade
  existente na resposta.
- Alterar categoria ou tamanho inicia uma partida nova.
- Cada aparelho sorteia sua própria palavra; ainda não há sala compartilhada.

## Fora de escopo

- Login, servidor, placar sincronizado ou sala de duelo online.
- Dicionário completo de português ou palavras dinâmicas obtidas de serviço
  externo.
- Desafio diário com resposta compartilhada.

## Referências

- Implementação atual: `index.html`, `manifest.webmanifest`, `sw.js`.
- Direção visual: `DESIGN.md`.
- Guia do projeto e fluxo SDD: `README.md`.

