import argparse
from glob import glob
import os
from os import path

# obtendo argumentos da linha de comando

psr = argparse.ArgumentParser(description="""
    Script para renomear arquivos .JPG para .jpg.
""")

psr.add_argument("p", help="Caminho dos arquivos.")

args = psr.parse_args()

p = args.p

# normalizando paths

p = path.abspath(path.expanduser(p))

# obtendo lista de arquivos

os.chdir(p)
arqs = glob("*.JPG")
arqs.sort()

# renomeando JPG para jpg

for a in arqs:
    pfx = path.splitext(a)[0]
    novo = "{}.jpg".format(pfx)
    os.rename(a, novo)
