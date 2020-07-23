import argparse
from glob import glob
import os
import os.path as path
from subprocess import run

# usando o argparser para a linha de comando

psr = argparse.ArgumentParser(description="""
	  Script para remover todas as trilhas de áudio de um ou mais vídeos.""",
	  formatter_class=argparse.RawDescriptionHelpFormatter
)

psr.add_argument("ps", help="Caminho com o(s) vídeo(s) (arquivo ou diretório).")
psr.add_argument("pd", help="Diretório para guardar os vídeos sem áudio.")
psr.add_argument("-ext", nargs="*", default="['mp4']",
				 help="Lista com as extensões dos vídeos. (default=[mp4])")

args = psr.parse_args()

# normalizando os paths

ps = path.abspath(path.expanduser(args.ps))
pd = path.abspath(path.expanduser(args.pd))

# criando diretório-destino, se necessário

if not path.exists(pd): os.makedirs(pd)

# obtendo a lista de vídeos

if path.isfile(ps):
	vids = [ps]
elif path.isdir(ps):
	os.chdir(ps)
	vids = glob("*.{}".format(args.ev))
	vids.sort()

# removendo o áudio dos vídeos e salvando-os

for v in vids:
	p1 = path.join(ps, v)
	p2 = path.join(pd, v)
	com = "ffmpeg -i {} -an {}".format(p1, p2)
	run(com, shell=True)
