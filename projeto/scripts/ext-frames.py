import argparse
from glob import glob
import os
from os import path
from subprocess import call

# obtendo argumentos da linha de comando

psr = argparse.ArgumentParser(description="""
	Script para extrair frames de um ou mais vídeos-fonte."""
)

psr.add_argument("ps", help="Caminho do diretório dos vídeos.")
psr.add_argument("-ev", default="mp4",
				 help="Extensão dos vídeos. (default=mp4)")
psr.add_argument("-p", type=int, help="Primeiro vídeo a ser analisado.")
psr.add_argument("-u", type=int, help="Último vídeo a ser analisado.")
psr.add_argument("-s", type=float, default=2.0,
				 help="Offset do início do vídeo. (default=2.0)")
psr.add_argument("-r", type=float, default=1.5,
				 help="Frames a serem extraídos por segundo. (default=1.5)")
psr.add_argument("-ef", default="jpg",
				 help="Extensão dos frames extraídos. (default=jpg)")
psr.add_argument("-q", default=1,
				 help="Qualidade dos frames extraídos. (default=1)")
psr.add_argument("pd", help="Caminho do diretório dos frames.")

args = psr.parse_args()

# normalizando paths

ps = path.abspath(path.expanduser(args.ps))
pd = path.abspath(path.expanduser(args.pd))

# criando diretório-destino, se necessário

if not path.exists(pd): os.makedirs(pd)

# obtendo a lista de vídeos

os.chdir(ps)
vids = glob("*.{}".format(args.ev))
vids.sort()

# extraindo os frames

for v in vids:
	num = int(v[v.find("-")+1:v.find(".")])
	if (args.p is None or args.p <= num) and (args.u is None or num <= args.u):
		p1 = path.join(ps, v)
		pref = v[:v.find(".")]
		fr = "{}-%03d.{}".format(pref, args.ef)
		p2 = path.join(pd, fr)
		com = "ffmpeg -i {} -ss {} -r {} -q:v {} {}"\
			  .format(p1, args.s, args.r, args.q, p2)
		call(com, shell=True)

# geralmente os dois primeiros frames do vídeo sao muito parecidos
# assim, exclui-se o primeiro frame de cada vídeo

# obtendo frames -001

os.chdir(pd)
rem = glob("*-001.{}".format(args.ef))
rem.sort()
for r in rem:
	os.remove(r)

# renomeando os arquivos para compensar a falta dos arquivos 001

arqs = os.listdir()
arqs.sort()

for f in arqs:
	num = int(f[f.rfind("-")+1:f.rfind(".")])
	rep = f[f.rfind("-")+1:]
	ant = str(num-1).zfill(3) + "." + args.ef
	novo = f.replace(rep, ant)
	os.rename(f, novo)
