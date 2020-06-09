import argparse
from glob import glob
import os
from os import path

# funções utilitárias

getPfx = lambda a: a[:a.find("-")]
getn1 = lambda a: int(a[a.find("-")+1:a.rfind("-")])

# obtendo argumentos da linha de comando

psr = argparse.ArgumentParser(description="""
	Script para corrigir a numeração das imagens/labels
	quando há 'saltos' entre os números (ex.: 1, 2, 4, 5, 6, 9, ...)."""
)

psr.add_argument("p", help="Caminho dos arquivos.")

args = psr.parse_args()

p = args.p

# normalizando paths

p = path.abspath(path.expanduser(p))

# obtendo a lista de imagens

os.chdir(p)
imgs = glob("*.jpg")
imgs.sort()

# corrigindo a numeração

pfx = getPfx(imgs[0])

i1 = 0
i2 = 0
c = 0
while c < len(imgs):
	temp = "{}-{}-{}".format(pfx, str(i1).zfill(3), str(i2).zfill(3))

	ai = imgs[c]
	ni = temp + ".jpg"
	os.rename(ai, ni)

	al = path.splitext(ai)[0] + ".txt"
	nl = temp + ".txt"
	if path.exists(al): os.rename(al, nl)

	c += 1

	if c < len(imgs):
		prox1 = getn1(imgs[c])
		r1 = getn1(ai)
		if prox1 > r1:
			i1 += 1
			i2 = 0
		else:
			i2 += 1
