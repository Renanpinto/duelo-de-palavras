# Constituição do Duelo de Palavras

Estes princípios guiam especificações e mudanças implementadas com auxílio de
agentes de programação.

## 1. O comportamento vem antes do código

Toda funcionalidade nova ou mudança relevante precisa de uma spec com critérios
de aceite observáveis antes da implementação. Se o comportamento mudar durante o
trabalho, atualize a spec antes de continuar.

## 2. Simplicidade compatível com o produto

O jogo é um aplicativo estático, sem framework ou backend. Preserve essa forma
sempre que ela atender aos critérios. Não introduza dependências, serviços,
contas ou sincronização sem uma necessidade descrita e aceita na spec.

## 3. Português brasileiro e regras de palavras

A interface é escrita em português brasileiro. A comparação de palavras ignora
acentos, mas a lista de respostas e as tentativas aceitas devem pertencer ao
vocabulário português definido pelo produto. Mudanças no vocabulário precisam
registrar fonte, licença e regras de normalização na spec ou no plano.

## 4. O jogo precisa funcionar em telas pequenas

Toda interação deve funcionar com toque, mouse e teclado quando aplicável. Casas
selecionáveis, controles e diálogos precisam de nomes acessíveis, foco visível e
estados compreensíveis sem depender apenas de cor. Respeite a preferência por
movimento reduzido.

## 5. Critérios de aceite guiam a conferência

Cada tarefa se liga a um ou mais critérios da spec. Ao concluir, confira os
critérios afetados no navegador; registre limitações ou verificações pendentes em
`tasks.md`. Não alegue uma conferência que não foi executada.

## 6. Documentação acompanha o produto

Quando uma mudança alterar regras, instalação, publicação ou estrutura do
projeto, atualize README.md e a spec correspondente na mesma alteração.

## Como alterar esta constituição

Uma proposta pode ser feita em qualquer spec. Registre a motivação, quais
princípios mudam e o impacto nas funcionalidades existentes antes de editar este
arquivo. Preserve princípios que continuam válidos e mantenha as specs
consistentes com a versão aprovada.

