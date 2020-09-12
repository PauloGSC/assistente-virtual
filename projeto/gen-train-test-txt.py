# Script para gerar os arquivos train.txt e test.txt
# com os caminhos das respectivas imagens


import os
import os.path as path
from sys import argv


# entrando no diretório deste script

os.chdir(path.dirname(path.abspath(path.expanduser(argv[0]))))

# gerando os arquivos

os.chdir("data")

for s in ("train", "test"):
    txt = s + ".txt"
    open(txt, "w").close() # truncar o arquivo
    file = open(txt, "w")

    imgs_path = path.join(s, "images")
    imgs = os.listdir(imgs_path)
    imgs.sort()
    for i in imgs:
        full_path = path.join("data", imgs_path, i)
        file.write(full_path + "\n")

    file.close()
