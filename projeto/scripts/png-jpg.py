import argparse
import os
from os import path
from subprocess import run

# obtendo argumentos da linha de comando

psr = argparse.ArgumentParser(description="""
    Script para converter arquivos .png para .jpg.
""")

psr.add_argument("p", help="Caminho dos arquivos.")
psr.add_argument("-q", default=100, type=int, help="Qualidade do jpeg (default=100).")

args = psr.parse_args()

p = args.p
q = args.q

# normalizando paths

p = path.abspath(path.expanduser(p))

# convertendo arquivos

os.chdir(p)

com1 = "mogrify -format jpg -quality {} *.png".format(q)
run(com1, shell=True)

# excluindo arquivos .png

com2 = "rm *.png"
run(com2, shell=True)
