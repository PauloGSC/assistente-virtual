import argparse
from glob import glob
import os
import os.path as path
from subprocess import run

# obtendo argumentos da linha de comando

psr = argparse.ArgumentParser(description="""
	Script para extrair frames de um ou mais vídeos-fonte.
	Caso -t e -to sejam passadas, -t tem prioridade."""
)

psr.add_argument("ps", help="Caminho do diretório dos vídeos.")

psr.add_argument("-ev", nargs="*", default="['mp4']",
				 help="Lista com as extensões dos vídeos. (default=['mp4'])")
psr.add_argument("-ss", default="00:00",
				 help="Posição para iniciar a extração. (default=00:00)")
psr.add_argument("-t", default="",
				 help="Duração da extração, por padrão em segundos.")
psr.add_argument("-to", default="",
				 help="Posição para parar a extração.")
psr.add_argument("-r", type=float, default=1.5,
				 help="Frames a serem extraídos por segundo. (default=1.5)")

psr.add_argument("-q", type=int, default=1,
				 help="Qualidade dos frames extraídos. (default=1)")
psr.add_argument("-ef", default="jpg",
				 help="Extensão dos frames extraídos. (default=jpg)")
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
	p1 = path.join(ps, v)
	pref = path.splitext(v)[0]
	fr = "{}-%03d.{}".format(pref, args.ef)
	p2 = path.join(pd, fr)

	com = "ffmpeg -i {0} -ss {1} {5} {6} -r {2} -q {3} {4}"\
		  .format(p1, args.s, args.r, args.q, p2,
		  		  "-t "+args.t if args.t else "",
				  "-to "+args.to if args.to else "")
	run(com, shell=True)

# geralmente os dois primeiros frames do vídeo sao muito parecidos
# assim, exclui-se o primeiro frame de cada vídeo

# obtendo frames -001

# os.chdir(pd)
# rem = glob("*-001.{}".format(args.ef))
# rem.sort()
# for r in rem:
# 	os.remove(r)
#
# # renomeando os arquivos para compensar a falta dos arquivos -001
#
# arqs = os.listdir()
# arqs.sort()
#
# for f in arqs:
# 	num = int(f[f.rfind("-")+1:f.rfind(".")])
# 	rep = f[f.rfind("-")+1:]
# 	ant = str(num-1).zfill(3) + "." + args.ef
# 	novo = f.replace(rep, ant)
# 	os.rename(f, novo)
