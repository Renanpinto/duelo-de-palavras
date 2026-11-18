# Plano: teclado e revelação das tentativas

## Resumo técnico

A validação atual usa a união das palavras normalizadas do objeto `WORDS` em
`index.html`. Expandir a lista local com palavras comuns e as três palavras
apontadas. Acrescentar estado de revelação para animar a linha enviada e bloquear
entrada até a sequência terminar. Reorganizar as teclas para o arranjo da
referência sem cedilha, usando um ícone de apagar para caber no celular.

## Arquivos e áreas afetadas

- `index.html`: vocabulário local, temporização de animação, teclado virtual e
  estilos de revelação.
- `sw.js`: nova versão do cache para clientes PWA receberem a implementação.
- `specs/003-teclado-e-revelacao/`: critério, plano e rastreamento das tarefas.

## Decisões

- O vocabulário permanece manual e embutido; a origem atual é o objeto `WORDS`
  do próprio jogo, não um dicionário do sistema. `POMBO`, `PORTA` e `POLVO` foram
  sugeridas pelo usuário; não há cópia de uma base externa nesta mudança.
- A cedilha não entra no teclado virtual. A normalização física continua ignorando
  acentos.
- A revelação é sequencial da esquerda para a direita, respeita movimento
  reduzido e impede input concorrente.
- A versão do cache offline será atualizada para invalidar o HTML antigo já
  instalado em aparelhos.

## Verificação

Conferir a lista, o arranjo de teclas e os estados de bloqueio no código. A
inspeção da animação depende de abrir o jogo num navegador.

