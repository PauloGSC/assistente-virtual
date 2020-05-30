import argparse
import os
from os import path

def getPfx(a):
	pfx = a[:a.find("-")]
	return pfx

def getn1(a):
	n1 = int(a[a.find("-")+1:a.rfind("-")])
	return n1

def getn2(a):
	n2 = int(a[a.rfind("-")+1:a.rfind(".")])
	return n2

def getExt(a):
	ext = a[a.rfind(".")+1:]
	return ext

psr = argparse.ArgumentParser(description="""
	Script para corrigir a numeração dos arquivos quando há 'saltos' entre os números (ex.: 1, 2, 4, 5, 6, 9, ...).""",
	formatter_class=argparse.RawDescriptionHelpFormatter
)

psr.add_argument("p", help="Caminho dos arquivos.")

p = psr.parse_args().p
p = path.abspath(path.normpath(p))

os.chdir(p)
arqs = os.listdir()
arqs.sort()

pfx = getPfx(arqs[0])
ext = getExt(arqs[0])

i1 = 1
i2 = 1
c = 0
while c < len(arqs):
	a = arqs[c]
	r1 = getn1(a)
	r2 = getn2(a)

	ren = pfx + "-" + str(i1).zfill(3) + "-" + str(i2).zfill(3) + "." + ext
	os.rename(a, ren)

	if c < len(arqs)-1:
		new1 = getn1(arqs[c+1])
		if new1 > r1:
			i1 += 1
			i2 = 1
		else:
			i2 += 1

	c += 1
