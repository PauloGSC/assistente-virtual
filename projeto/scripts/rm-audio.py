import argparse
from glob import glob
import os
from os import path
from subprocess import call

# usando o argparser para a linha de comando

psr = argparse.ArgumentParser(description="""
	  Script para remover todas as trilhas de áudio de um ou mais vídeos.""",
	  formatter_class=argparse.RawDescriptionHelpFormatter
)

psr.add_argument("ps", help="Caminho do diretório com os vídeos.")
psr.add_argument("pd", help="Caminho para guardar os vídeos sem áudio.")
psr.add_argument("-ext", default="mp4", help="Extensão dos vídeos. (default=mp4)")

args = psr.parse_args()

# normalizando os paths

ps = path.abspath(path.expanduser(args.ps))
pd = path.abspath(path.expanduser(args.pd))

# criando diretório-destino, se necessário

if not path.exists(pd): os.makedirs(pd)

# obtendo a lista de vídeos

os.chdir(ps)
vids = glob("*.{}".format(args.ext))
vids.sort()

# removendo o áudio dos vídeos e salvando-os

for v in vids:
	p1 = path.join(ps, v)
	p2 = path.join(pd, v)
	com = "ffmpeg -i {} -an {}".format(p1, p2)
	call(com, shell=True)
