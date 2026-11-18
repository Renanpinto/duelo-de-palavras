# Plano: acabamento visual do jogo

## Resumo técnico

Manter os seletores nativos, ocultar sua seta visual padrão e desenhar uma seta
decorativa insetada no wrapper. Remover o elemento e a atualização JavaScript do
contador, trocar os textos pedidos, substituir o “D” por uma imagem SVG e
versionar as referências do ícone no favicon, manifest e cache offline.

## Arquivos e áreas afetadas

- `index.html`: textos, wrapper dos seletores e marca do cabeçalho.
- `icon.svg`: desenho vetorial do tabuleiro com as letras DUEL.
- `manifest.webmanifest`: versão do ícone PWA e cores de tema.
- `sw.js`: cache versionado para atualizar o ícone offline.
- `README.md`: descrição atualizada do ícone.

## Decisões

- SVG foi escolhido para preservar nitidez em favicon, cabeçalho e PWA sem
  dependências.
- O dropdown continua nativo; apenas seu indicador visual será substituído por
  um chevron CSS com mais espaço à direita.

## Verificação

- Conferir referências do ícone em HTML, manifest e service worker.
- Conferir os textos e a remoção do contador por busca estática.
- Inspeção visual completa depende de abrir o site atualizado no navegador.

