import argparse
from glob import glob
import os
import os.path as path

import cv2 as cv

from screeninfo import get_monitors

# obtendo os argumentos da linha de comando

psr = argparse.ArgumentParser(description="""
	  Script para visualizar os rótulos de uma imagem.
	  Os rótulos devem estar no formato YOLO (<classe> <x> <y> <w> <h>).
	  O arquivo com os rótulos deve possuir o mesmo nome da imagem e formato 'txt'.
	  Caso o diretório com os rótulos seja omitido, assume-se que os rótulos estão no mesmo diretório das imagens.""",
	  formatter_class=argparse.RawDescriptionHelpFormatter
)

psr.add_argument("pi", help="Diretório com as imagens.")
psr.add_argument("cls", help="Arquivo com as classes.")
psr.add_argument("-pl", help="Diretório com os rótulos.")
psr.add_argument("-ei", default="jpg", help="Extensão das imagens (default=jpg).")
psr.add_argument("-s", default="0", help="Início do slideshow (default=0).")

args = psr.parse_args()

pi = args.pi
pl = pi if args.pl is None else args.pl

# normalizando paths

pi = path.abspath(path.expanduser(pi))
cls = path.abspath(path.expanduser(args.cls))
pl = path.abspath(path.expanduser(pl))

# obtendo a lista de imagens

os.chdir(pi)
imgs = glob("*.{}".format(args.ei))
imgs.sort()

# obtendo as classes

# with open(cls) as c:
# 	classes = c.read().splitlines()

# cor para cada classe

cor = {0:(100, 0, 0), 1:(0, 100, 0), 2:(0, 0, 100)}

# obtendo tamanho máximo da janela

fat = 0.75
W = int(get_monitors()[0].width * fat)
H = int(get_monitors()[0].height * fat)

# setando início do slideshow

if args.s.isdigit():
	pos = int(args.s)
else:
	args.s = path.basename(args.s)
	pos = imgs.index(args.s) if args.s in imgs else 0

# controlando o 'slideshow'

while True:

	# imagem atual e label dessa imagem

	curi = imgs[pos]
	curl = curi[:curi.rfind(".")] + ".txt"

	pci = path.join(pi, curi)
	pcl = path.join(pl, curl)

	img = cv.imread(pci)

	# obtendo dimensões da imagem

	w = img.shape[1]
	h = img.shape[0]

	# analisando a label, caso exista

	if path.exists(pcl):
		with open(pcl) as l:
			for line in l.read().splitlines():

				# extraindo as informações de cada 'bounding box' da label

				lab = [n for n in line.split()]
				label = dict(cls=int(lab[0]), x=float(lab[1]), y=float(lab[2]),
							 w=float(lab[3]), h=float(lab[4]))

				# desnormalizando as coordenadas e medidas

				label["x"] *= w
				label["y"] *= h
				label["w"] *= w
				label["h"] *= h

				# calculando as coordenadas para desenhar a 'bounding box'

				tl = (label["x"]-label["w"]/2, label["y"]-label["h"]/2)
				br = (label["x"]+label["w"]/2, label["y"]+label["h"]/2)
				tl = (int(tl[0]), int(tl[1]))
				br = (int(br[0]), int(br[1]))

				# desenhando a 'bounding box'

				bgr = cor[label["cls"]]
				cv.rectangle(img, tl, br, bgr, thickness=10)

				# desenhando o retângulo de fundo do texto

				# txt = str(label["cls"]) # classes[label["cls"]]
				# fontFace = cv.FONT_HERSHEY_PLAIN
				# fontScale = 5
				# thick = 5
				# line = cv.LINE_AA
				#
				# corn1 = (tl[0]+10, tl[1]+75)
				# w2, h2 = cv.getTextSize(txt, fontFace, fontScale, thick)[0]
				# corn2 = (corn1[0]+w2+5, corn1[1]-h2-15)
				#
				# cv.rectangle(img, corn1, corn2, bgr, cv.FILLED)
				#
				# # desenhando o texto
				#
				# org = (corn1[0]+5, corn1[1]-5)
				#
				# cv.putText(img, txt, org, fontFace, fontScale, (255, 255, 255), thick, line)

	# ajustando tamanho da janela

	cv.namedWindow(curi, cv.WINDOW_KEEPRATIO)

	ww = w
	wh = h
	if w > W and h <= H:
		ww = W
	elif w <= W and h > H:
		wh = H
	elif w > W and h > H:
		if w-W >= h-H:
			ww = W
		else:
			wh = H

	cv.resizeWindow(curi, ww, wh)

	# mostrando a imagem

	cv.imshow(curi, img)

	# verificando a próxima ação do usuário

	key = cv.waitKey(0)
	if key in [27, 113]: # ESC ou Q
		break
	elif key == 81: # <-
		pos = len(imgs)-1 if pos == 0 else pos-1
	elif key == 83: # ->
		pos = 0 if pos == len(imgs)-1 else pos+1

	# removendo a janela anterior

	cv.destroyWindow(curi)

cv.destroyAllWindows()
