import argparse
from glob import glob
import os
import os.path as path
from subprocess import run, DEVNULL

# obtendo argumentos da linha de comando

psr = argparse.ArgumentParser(description="""
    Script para remover informações EXIF de imagens.
""")

psr.add_argument("p", help="Caminho das imagens.")

p = psr.parse_args().p

# normalizando paths

p = path.abspath(path.expanduser(p))

# removendo EXIF

os.chdir(p)

com1 = "exiftool -all= *.jpg"
run(com1, shell=True)

com2 = "rm *.jpg_original"
run(com2, shell=True, stderr=DEVNULL)
