# Plano: documentar o jogo atual

## Resumo técnico

O jogo é uma página estática. HTML, CSS, vocabulário e lógica estão juntos em
`index.html`; `manifest.webmanifest`, `icon.svg` e `sw.js` dão suporte ao PWA.
Não existe build, framework, API ou banco de dados.

## Arquivos e áreas afetadas

- `index.html`: interface, entrada, sorteio, validação, pontuação e estatísticas.
- `manifest.webmanifest`, `icon.svg`, `sw.js`: instalação e cache do PWA.
- `README.md`: execução, publicação e processo SDD.

## Decisões

- A spec registra o comportamento atual como baseline; não propõe funcionalidades
  online que ainda não existem.
- O vocabulário é curado e local. Expandir ou substituir a fonte exige uma spec
  com proveniência e licença.

## Verificação

Esta pasta documenta a baseline e não declara uma rodada de testes ou inspeção
manual do navegador. Em futuras mudanças, confira os critérios afetados e anote
o resultado em `tasks.md`.

