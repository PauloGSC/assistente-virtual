import argparse
import os

# usando o argparser para a linha de comando

psr = argparse.ArgumentParser(description="""
	  Script para remover todas as trilhas de áudio de um ou mais vídeos.
	  Este script utiliza o programa 'ffmpeg'; para instalá-lo, execute 'sudo apt install ffmpeg'.""",
	  formatter_class=argparse.RawDescriptionHelpFormatter
)

psr.addArgument("vca",
				help="Caminho do diretório com os vídeos.")
psr.addArgument("vsa",
				help="Caminho para guardar os vídeos sem áudio.")
psr.addArgument("-ev", default="mp4",
				help="Extensão dos vídeos.\
					  (default=mp4)")

args = psr.parse_args()

# removendo o áudio dos vídeos e salvando-os

os.chdir(args.vca)
vids = [v for v in os.listdir() if v.endswith("."+args.ev)]

for v in vids:
	vsa = args.vsa+"/" if not args.vsa.endswith("/") else args.vsa
	novo = vsa + v
	com = "ffmpeg -i {vca} -an {vsa}".format(vca=v, vsa=novo)
	os.system(com)
	
