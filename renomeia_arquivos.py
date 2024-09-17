import os

# Define o diretório onde deseja renomear os arquivos e pastas
dir_path = r'C:\Users\Arthur\Desktop\Descomplica\Pensamento Computacional Aplicado'

# Percorre todos os arquivos e subpastas
for root, dirs, files in os.walk(dir_path):
    # Renomeia as pastas
    for dir_name in dirs:
        new_dir_name = dir_name.replace(" ", "_")
        old_dir_path = os.path.join(root, dir_name)
        new_dir_path = os.path.join(root, new_dir_name)
        os.rename(old_dir_path, new_dir_path)

    # Renomeia os arquivos
    for file_name in files:
        new_file_name = file_name.replace(" ", "_")
        old_file_path = os.path.join(root, file_name)
        new_file_path = os.path.join(root, new_file_name)
        os.rename(old_file_path, new_file_path)

print("Renomeação concluída!")

