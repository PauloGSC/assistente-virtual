import argparse
import os

# usando o argparser para a linha de comando

psr = argparse.ArgumentParser("""
	Script para mover vídeos de um local para outro.
	Os vídeos tambem sao renomeados, de acordo com os parâmetros passados.
	""",
	formatter_class=argparse.RawDescriptionHelpFormatter
)

psr.add_argument("pv",
				 help="Diretório com os vídeos.")
psr.add_argument("pd",
				 help="Diretório destino dos vídeos.")
psr.add_argument("px",
				 help="Prefixo para renomear os vídeos.")
psr.add_argument("-i", type=int, default=1,
				 help="Início da numeração dos vídeos. \
				 	   (default=1).")
psr.add_argument("-ext", default="mp4",
				 help="Extensão dos vídeos. \
				 	   (default=mp4).")

args = psr.parse_args()

# renomeando os vídeos (e movendo-os ao mesmo tempo)

os.chdir(args.pv)

vids = [v for v in os.listdir() if v.endswith("." + args.ext)]
vids.sort()
ctr = args.i
for v in vids:
	pd = args.pd+"/" if args.pd[-1] != "/" else args.pd
	novo = pd + args.px + "-" + str(ctr).zfill(3) + "." + args.ext
	os.rename(v, novo)
	ctr += 1
