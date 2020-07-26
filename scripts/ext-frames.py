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

psr.add_argument("ps", help="Caminho com o(s) vídeo(s) (arquivo ou diretório).")

psr.add_argument("-ev", nargs="*", default=["mp4"],
				 help="Lista com as extensões dos vídeos. (default=['mp4'])")
psr.add_argument("-ss", default="00:00",
				 help="Posição para iniciar a extração. (default=00:00)")
psr.add_argument("-t", default="",
				 help="Duração da extração, por padrão em segundos.")
psr.add_argument("-to", default="",
				 help="Posição para parar a extração.")
psr.add_argument("-r", type=float, default=2.0,
				 help="Frames a serem extraídos por segundo. (default=2.0)")

psr.add_argument("-q", type=int, default=1,
				 help="Qualidade dos frames extraídos. (default=1)")
psr.add_argument("-ef", default="jpg",
				 help="Extensão dos frames extraídos. (default=jpg)")
psr.add_argument("pd", help="Diretório para guardar os frames.")

args = psr.parse_args()

# normalizando paths

ps = path.abspath(path.expanduser(args.ps))
pd = path.abspath(path.expanduser(args.pd))

# criando diretório-destino, se necessário

if not path.exists(pd): os.makedirs(pd)

# obtendo o(s) vídeo(s)

vids = []
if path.isfile(ps):
	vids.append(path.basename(ps))
	ps = path.dirname(ps)
elif path.isdir(ps):
	os.chdir(ps)
	for e in args.ev:
		vs = glob("*.{}".format(e))
		vids.extend(vs)
vids.sort()

# extraindo os frames

for v in vids:
	p1 = path.join(ps, v)
	pref = path.splitext(v)[0]
	fr = "{}-%03d.{}".format(pref, args.ef)
	p2 = path.join(pd, fr)

	com = "ffmpeg -y -i {0} -ss {1} {5} {6} -r {2} -q {3} {4}".format(
				p1, args.ss, args.r, args.q, p2,
		  		"-t "+args.t if args.t else "",
				"-to "+args.to if args.to else "")
	run(com, shell=True)

# os número identificador dos frames (%03d) começa em 001
# o script abaixo renomeia os frames para começar com 000

os.chdir(pd)

imgs = os.listdir()
imgs.sort()
for i in imgs:
	n2 = int(path.splitext(i)[0][i.rfind("-")+1:])
	i2 = "{}{}{}".format(i[:i.rfind("-")+1],
						 str(n2-1).zfill(3),
						 path.splitext(i)[1])
	os.rename(i, i2)

# geralmente os dois primeiros frames do vídeo sao muito parecidos
# assim, exclui-se o primeiro frame de cada vídeo

# obtendo frames -000

rem = glob("*-000.{}".format(args.ef))
rem.sort()
for r in rem:
	os.remove(r)

# renomeando os arquivos para compensar a falta dos arquivos -000

imgs = os.listdir()
imgs.sort()
for i in imgs:
	n2 = int(path.splitext(i)[0][i.rfind("-")+1:])
	i2 = "{}{}{}".format(i[:i.rfind("-")+1],
						 str(n2-1).zfill(3),
						 path.splitext(i)[1])
	os.rename(i, i2)
