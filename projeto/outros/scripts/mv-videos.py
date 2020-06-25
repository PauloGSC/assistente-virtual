import argparse
from glob import glob
import os
import os.path as path

# obtendo argumentos da linha de comando

psr = argparse.ArgumentParser("""
	Script para mover vídeos de um local para outro.
	Os vídeos tambem sao renomeados, de acordo com os parâmetros passados. """,
	formatter_class=argparse.RawDescriptionHelpFormatter
)

psr.add_argument("ps", help="Diretório com os vídeos.")
psr.add_argument("pd", help="Diretório destino dos vídeos.")
psr.add_argument("pfx",  help="Prefixo para renomear os vídeos.")
psr.add_argument("-i", type=int, default=1,
				 help="Início da numeração dos vídeos. (default=1).")
psr.add_argument("-ext", default="mp4",
				 help="Extensão dos vídeos. (default=mp4).")

args = psr.parse_args()

# normalizando os paths

ps = path.abspath(path.expanduser(args.ps))
pd = path.abspath(path.expanduser(args.pd))

# criando diretório-destino, se for necessário

if not path.exists(pd): os.makedirs(pd)

# obtendo a lista de vídeos

os.chdir(ps)
vids = glob("*.{}".format(args.ext))
vids.sort()

# renomeando os vídeos (e movendo-os ao mesmo tempo)

ctr = args.i
for v in vids:
	novo = path.join(pd, "{}-{}.{}".format(args.pfx, str(ctr).zfill(3), args.ext))
	os.rename(v, novo)
	ctr += 1
