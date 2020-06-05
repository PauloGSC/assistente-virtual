import argparse
import cv2 as cv
from glob import glob
import os
from os import path
from random import seed, randrange as rre
from screeninfo import get_monitors

# gerando uma nova seed aleatória

seed()

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

with open(cls) as c:
	classes = c.read().splitlines()

# obtendo tamanho máximo da janela

fat = 0.75
W = int(get_monitors()[0].width * fat)
H = int(get_monitors()[0].height * fat)

# controlando o 'slideshow'

pos = 0
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

				bgr = (rre(256), rre(256), rre(256))
				cv.rectangle(img, tl, br, bgr, 3)

				# desenhando o nome da classe relativa à 'bounding box'

				size = label["w"] / 140
				txt = classes[label["cls"]]
				corner = (tl[0]+5, tl[1]+22)
				font = cv.FONT_HERSHEY_PLAIN
				thick = 2 if size > 0.7 else 1
				cv.putText(img, txt, corner, font, size, bgr, thick, 16)

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
