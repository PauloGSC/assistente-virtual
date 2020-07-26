import argparse
from glob import glob
import os
import os.path as path

# obtendo argumentos da linha de comando

psr = argparse.ArgumentParser(description="""
    Script para numerar imagens e labels que possuam nomes não-numerados.
""")

psr.add_argument("p", help="Caminho dos arquivos.")
psr.add_argument("pfx", help="Prefixo para renomear.")
psr.add_argument("n1", type=int)
psr.add_argument("-n2", type=int, default=0)

args = psr.parse_args()

p = args.p
pfx = args.pfx
n1 = args.n1
n2 = args.n2

# normalizando paths

p = path.abspath(path.expanduser(p))

# obtendo lista de imagens

os.chdir(p)
imgs = glob("*.jpg")
imgs.sort()

# renomeando os arquivos numericamente

for i1 in imgs:
	n11 = str(n1).zfill(3)
	n22 = str(n2).zfill(3)

	temp = "{}-{}-{}".format(pfx, n11, n22)
	i2 = "{}.jpg".format(temp)
	r2 = "{}.txt".format(temp)

	os.rename(i1, i2)

	r1 = "{}.txt".format(path.splitext(i1)[0])
	if path.exists(r1): os.rename(r1, r2)

	n2 += 1
