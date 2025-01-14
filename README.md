## Organizador de Arquivos por Tipo
- Este repositório contém scripts Python para organizar arquivos em um diretório. Há dois scripts principais:
    - `in.py`: Agrupa arquivos em pastas com base em suas extensões.
    - `out.py`: Move todos os arquivos de subpastas para o diretório raiz e remove as subpastas vazias.

## Script 1: Organizar arquivos por extensão
### Descrição:
- Este script organiza os arquivos do diretório atual em pastas, agrupando-os por extensão. Por exemplo, todos os arquivos .txt serão movidos para uma pasta chamada txt.

### Como usar:
- Certifique-se de que o script esteja no mesmo diretório que os arquivos que deseja organizar.
- Execute o script usando o comando `python in.py`.
- Os arquivos serão movidos para pastas com o mesmo nome das extensões.

### Cuidados:
- Se já existir uma pasta com o nome da extensão, o script lançará um erro.
- Arquivos sem extensão ou com mais de um ponto (por exemplo, arquivo.novo.txt) podem causar comportamentos inesperados.
- O script não lida com exceções, como permissões de acesso ou erros de leitura/escrita.

## Script 2: Organizar arquivos no diretório raiz
### Descrição:
- Este script move todos os arquivos de subpastas para o diretouro raiz e remove as subpastas vazias.

### Como usar:
- Certifique-se de que o script esteja no mesmo diretório que os arquivos que deseja organizar.
- Execute o script usando o comando `python out.py`.