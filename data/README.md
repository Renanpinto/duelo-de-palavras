# Vocabulário de palpites

`palavras-pt-br.txt` contém atualmente 69.570 palpites únicos de 4 a 7 letras.
Inclui formas plurais e verbos conjugados para que possam ser tentados. Esse
arquivo não é usado para sortear respostas; o sorteio continua nas categorias
curadas em `index.html`.

## Fontes e licenças

- FrequencyWords, `content/2018/pt_br/pt_br_50k.txt`, baseado no corpus
  [OpenSubtitles 2018](https://opus.nlpl.eu/OpenSubtitles2018.php):
  [repositório e créditos](https://github.com/hermitdave/FrequencyWords). O
  conteúdo é licenciado sob
  [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- `lexico` e `conjugações` da coleção
  [fserb/pt-br](https://github.com/fserb/pt-br), publicados sob MIT no
  repositório de origem. A licença MIT e seu aviso de copyright estão em
  [LICENSE](LICENSE-fserb-MIT.txt).

## Alterações aplicadas

As três fontes foram unidas. Foram mantidos tokens compostos apenas por letras,
com 4 a 7 letras; a comparação remove acentos e converte para caixa alta, e
duplicatas após normalização foram descartadas. Plurais e verbos conjugados
permanecem disponíveis como palpites. Como as listas incluem palavras raras,
nomes, gírias e ruído de transcrição, elas só validam palpites e não entram no
sorteio.

O arquivo derivado é disponibilizado sob CC BY-SA 4.0, com atribuição às fontes
acima e indicação das alterações. Para reproduzi-lo, baixe os três arquivos de
origem e execute:

```bash
python3 tools/filter-word-list.py \
  caminho/pt_br_50k.txt caminho/lexico caminho/conjugacoes
```

O programa do jogo não depende de Python; o script serve apenas para atualizar
o arquivo de dados.
