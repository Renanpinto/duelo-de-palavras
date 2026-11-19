# Duelo de Palavras

Jogo de palavras em português brasileiro, feito com HTML, CSS e JavaScript sem
framework ou servidor. O aplicativo pode ser instalado como PWA e guarda as
estatísticas no aparelho de cada pessoa.

## Rodar localmente

Com Python 3 instalado, execute na raiz do projeto:

```bash
python3 -m http.server 8000
```

Abra <http://localhost:8000>. Para parar o servidor, use `Ctrl+C` no terminal.
Também é possível abrir `index.html` diretamente, mas o servidor local permite
verificar o service worker e o comportamento de instalação do PWA.

## Como jogar

- Escolha uma categoria e um tamanho de palavra entre 4 e 7 letras.
- Preencha as casas clicando na posição desejada e digitando pelo teclado físico
  ou virtual.
- O teclado virtual segue o padrão QWERTY da referência, com apagar no fim da
  segunda linha e Enter largo no fim da terceira; o apagar usa um ícone
  compacto e o teclado virtual não inclui Ç.
- Envie a tentativa com Enter. Você tem até seis tentativas.
- Verde indica letra no lugar certo; amarelo indica letra em outra posição; cinza
  indica letra ausente. Não é necessário digitar acentos para validar a palavra;
  casas corretas e o resultado revelado preservam os acentos da resposta, como
  em `Limão`.
- Em telas pequenas, tocar numa casa seleciona a posição e rola a página até o
  teclado virtual ficar visível.
- As respostas sorteadas ficam nas listas de categoria curadas em `index.html`.
  Para validar palpites, o jogo também carrega `data/palavras-pt-br.txt`, com
  cerca de 70 mil palavras de 4 a 7 letras, incluindo plurais e verbos conjugados
  que podem ser tentados. A lista é local e fica em cache para uso offline; ela
  não entra no sorteio. As respostas vêm das listas curadas, sem plurais
  conhecidos ou formas verbais conjugadas fora do infinitivo. A comparação
  ignora acentos; a lista ainda não cobre todo o português. Fonte, licença,
  filtros e limitações estão em `data/README.md`.
- Cada aparelho tem suas próprias partidas e estatísticas. O jogo ainda não
  sincroniza uma partida entre duas pessoas.

## Estrutura do projeto

```text
index.html                    Jogo, estilos e lógica
manifest.webmanifest          Metadados do PWA
icon.svg                      Ícone vetorial da marca, cabeçalho e PWA
sw.js                         Cache offline
data/palavras-pt-br.txt       Palpites adicionais locais
data/README.md                Fonte, licença e filtros do vocabulário
tools/filter-word-list.py     Ferramenta de manutenção do vocabulário
DESIGN.md                     Direção visual e tokens
.specify/memory/              Princípios permanentes do projeto
.specify/templates/           Modelos de spec, plano e tarefas
specs/                        Especificações versionadas por funcionalidade
```

## Fluxo de SDD para vibecoding

Este repositório usa um fluxo manual e leve de Spec-Driven Development. Os
artefatos seguem a convenção de constituição, especificação, plano e tarefas do
[GitHub Spec Kit](https://github.com/github/spec-kit), sem depender da CLI.

Para cada funcionalidade nova ou mudança relevante:

1. Leia `.specify/memory/constitution.md` e as especificações que a mudança toca.
2. Crie `specs/NNN-nome-curto/spec.md` a partir de
   `.specify/templates/spec-template.md`. Descreva o problema, o comportamento
   esperado e critérios de aceite observáveis antes de pedir código.
3. Crie `plan.md` e `tasks.md` a partir dos respectivos modelos. Escolha a solução
   mais simples que atenda à spec e divida a execução em passos pequenos.
4. Peça ao agente para implementar apenas as tarefas dessa spec e marcar cada
   tarefa concluída conforme avança.
5. Confira os critérios de aceite no navegador, incluindo celular e teclado
   quando afetados. Registre o resultado em `tasks.md` e atualize a documentação
   se o comportamento mudou.

Uma especificação não é um pedido para construir tudo de uma vez. Se a ideia
mudar durante a implementação, atualize primeiro a spec e os critérios afetados.
Não marque uma tarefa como concluída sem conferir o comportamento correspondente.

### Prompt inicial sugerido

> Leia `README.md`, `.specify/memory/constitution.md` e a spec em
> `specs/NNN-nome-curto/`. Compare os critérios de aceite com o código atual.
> Implemente em tarefas pequenas, atualize `tasks.md` e informe quais critérios
> foram verificados e quais ainda precisam de conferência manual.

## Publicar no Cloudflare Pages

O projeto é estático e pode ser publicado sem etapa de build. Crie um projeto
Pages com a pasta do repositório como diretório raiz, sem comando de build e sem
diretório de saída adicional. Depois do deploy, abra a URL no celular e use a
opção do navegador para instalar ou adicionar o jogo à tela inicial.

## Limites atuais

- Não há backend, conta de usuário ou placar sincronizado.
- O sorteio é independente em cada aparelho; ainda não existe uma sala de duelo
  compartilhada.
- A validação combina as listas curadas com cerca de 24 mil palpites da lista
  local. Ela inclui plurais e verbos conjugados, mas não é um dicionário
  completo; a normalização sem acento também junta formas como `pais` e `país`.
  Os detalhes estão em `data/README.md`.
- As estatísticas ficam no `localStorage` do navegador.
