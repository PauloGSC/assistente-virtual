import argparse
from glob import glob
import os
import os.path as path
from subprocess import run

# usando o argparser para a linha de comando

psr = argparse.ArgumentParser(description="""
	Script para remover todas as trilhas de áudio de um ou mais vídeos."""
)

psr.add_argument("ps", help="Caminho com o(s) vídeo(s) (arquivo ou diretório).")
psr.add_argument("pd", help="Diretório para guardar os vídeos sem áudio.")
psr.add_argument("-ev", nargs="*", default=["mp4"],
				 help="Lista com as extensões dos vídeos. (default=['mp4'])")

args = psr.parse_args()

# normalizando os paths

ps = path.abspath(path.expanduser(args.ps))
pd = path.abspath(path.expanduser(args.pd))

# criando diretório-destino, se necessário

if not path.exists(pd): os.makedirs(pd)

# obtendo o(s) vídeo(s)

vids = []
if path.isfile(ps):
	vids.append(path.basename(ps))
elif path.isdir(ps):
	os.chdir(ps)
	for e in args.ev:
		vs = glob("*.{}".format(e))
		vids.extend(vs)
vids.sort()

print(vids)

# removendo o áudio dos vídeos e salvando-os

for v in vids:
	p1 = path.join(ps, v)
	p2 = path.join(pd, v)
	com = "ffmpeg -i {} -an {}".format(p1, p2)
	run(com, shell=True)
