# Instruções para agentes

Antes de alterar o projeto:

1. Leia `.specify/memory/constitution.md` e `README.md`.
2. Localize a spec em `specs/` relacionada à tarefa. Se for uma funcionalidade
   nova ou mudança relevante sem spec, crie `specs/NNN-nome-curto/` usando os
   modelos em `.specify/templates/`.
3. Registre comportamento esperado e critérios de aceite em `spec.md` antes de
   implementar. Use `plan.md` e `tasks.md` para mudanças que envolvam mais de um
   passo.
4. Implemente em etapas pequenas ligadas aos critérios de aceite. Não marque
   tarefas como concluídas sem conferir o comportamento correspondente.
5. Ao mudar comportamento, regras do jogo, instalação ou publicação, atualize a
   spec e `README.md` na mesma alteração.

## Regras do projeto

- A interface e o conteúdo são em português brasileiro.
- Preserve a arquitetura estática em HTML, CSS e JavaScript sem dependências,
  framework, backend ou serviços externos, a menos que uma spec aprovada
  justifique a mudança.
- A comparação de palavras ignora acentos. Mudanças no vocabulário devem
  documentar fonte, licença e normalização.
- Mantenha o jogo utilizável em telas pequenas, com teclado e toque; preserve
  foco visível, nomes acessíveis e suporte a movimento reduzido.
- Não alegue testes, inspeção no navegador ou critérios verificados sem tê-los
  executado. Registre limitações e verificações pendentes em `tasks.md`.
- Preserve alterações preexistentes do usuário e limite cada mudança ao escopo
  da tarefa.

## Estrutura principal

- `index.html`: jogo, estilos e lógica.
- `.specify/memory/constitution.md`: princípios permanentes.
- `.specify/templates/`: modelos para novas funcionalidades.
- `specs/`: especificações, planos e tarefas por funcionalidade.
- `DESIGN.md`: identidade visual e tokens.
