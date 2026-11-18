# Vocabulário de palpites

`palavras-pt-br.txt` contém atualmente 6.140 palpites únicos; é uma lista
auxiliar, não uma lista de respostas. As respostas continuam nas categorias
curadas em `index.html`.

## Fontes e atribuição

- FrequencyWords, variante `pt_br_50k.txt` de 2018, baseada no corpus
  [OpenSubtitles 2018](https://opus.nlpl.eu/OpenSubtitles2018.php):
  [repositório e créditos](https://github.com/hermitdave/FrequencyWords).
  O conteúdo da lista é licenciado sob
  [Creative Commons Atribuição-CompartilhaIgual 4.0 Internacional
  (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).
- As listas de formas conjugadas e infinitivos usadas para filtrar a fonte vêm
  da coleção [fserb/pt-br](https://github.com/fserb/pt-br), distribuída sob
  MIT no repositório de origem.

## Alterações aplicadas

Esta lista foi filtrada para tokens alfabéticos com 4 a 7 letras, normalizada
para caixa alta sem acentos, deduplicada e removida de formas verbais conjugadas
fora do infinitivo e de possíveis plurais. Os itens também são cruzados com o
léxico pt-BR de fserb/pt-br. Homógrafos com uso não verbal comum, como `CASA` e
`PORTA`, são preservados por exceções explícitas no script. Como a comparação
ignora acentos e as fontes não marcam classe gramatical em todos os itens, a
filtragem é aproximada; por exemplo, formas como `PAIS` não podem distinguir
`país` de `pais`.

O arquivo derivado é disponibilizado sob CC BY-SA 4.0, com atribuição às fontes
acima e indicação das alterações. Para reproduzi-lo, baixe os arquivos de origem
pt_BR de FrequencyWords e fserb/pt-br e execute:

```bash
python3 tools/filter-word-list.py \
  caminho/pt_br_50k.txt caminho/lexico caminho/conjugacoes caminho/verbos
```

O programa do jogo não depende de Python; o script é apenas uma ferramenta de
manutenção do arquivo de dados.
