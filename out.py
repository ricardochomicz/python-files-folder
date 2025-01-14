import os

# Obtém o diretório de trabalho atual (current working directory)
cwd = os.getcwd()

# Cria uma lista de pastas no diretório atual, verificando se cada item é um diretório
folder_list = [i for i in os.listdir(cwd) if os.path.isdir(i)]

# Itera sobre cada pasta na lista de pastas
for folder in folder_list:
    # Cria o caminho completo para a pasta atual
    path = os.path.join(cwd, folder)

    # Lista todos os arquivos dentro da pasta atual
    files = os.listdir(path)

    # Itera sobre cada arquivo na lista de arquivos
    for file in files:
        # Cria o caminho completo de origem (de onde o arquivo será movido)
        from_path = os.path.join(path, file)
        # Cria o caminho completo de destino (para onde o arquivo será movido)
        to_path = os.path.join(cwd, file)

        # Move o arquivo da pasta atual para o diretório raiz
        os.replace(from_path, to_path)

    # Remove a pasta vazia após mover todos os arquivos
    os.rmdir(path)