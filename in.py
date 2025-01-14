import os

# Obtém o diretório de trabalho atual (current working directory)
cwd = os.getcwd()

# Lista todos os itens (arquivos e pastas) no diretório atual
full_list = os.listdir(cwd)

# Filtra a lista para incluir apenas arquivos, excluindo arquivos com extensão .py
files_list = [i for i in full_list if os.path.isfile(i) and '.py' not in i]

# Extrai as extensões dos arquivos e cria uma lista de tipos únicos (sem duplicatas)
types = list(set([i.split('.')[1] for i in files_list]))

# Para cada tipo de arquivo, cria uma pasta com o nome da extensão
for file_type in types:
    os.mkdir(file_type)

# Move cada arquivo para a pasta correspondente à sua extensão
for file in files_list:
    # Cria o caminho de origem (local atual do arquivo)
    from_path = os.path.join(cwd, file)
    # Cria o caminho de destino (pasta com o nome da extensão)
    to_path = os.path.join(cwd, file.split('.')[-1], file)

    # Move o arquivo para a pasta correspondente
    os.replace(from_path, to_path)