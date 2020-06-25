import argparse
import cv2 as cv
from glob import glob
import numpy as np
import os
import os.path as path
from sys import argv
from time import perf_counter as perf

# funções utilitárias

def xywh2xyxy(bb, W, H):
    c, x, y, w, h = bb
    x *= W
    y *= H
    w *= W
    h *= H
    tl = (int(x - w/2), int(y - h/2))
    br = (int(x + w/2), int(y + h/2))
    bb2 = [c, *tl, *br]
    return bb2

# obtendo timestamp inicial

tsi = perf()

# obtendo argumentos da linha de comando

psr = argparse.ArgumentParser(description="""
    Script para gerar o heatmap do dataset.
""")

psr.add_argument("-s", type=int, default=416, help="Tamanho do heatmap (default=416).")

size = psr.parse_args().s

# entrando na pasta do dataset

scr = path.abspath(path.expanduser(path.dirname(argv[0])))
os.chdir(scr)
os.chdir("../../projeto/dataset")

# inicializando heatmap

print("Inicializando heatmap...")
ts1 = perf()

heatmap = np.zeros((size, size), dtype=np.uint8)

ts2 = perf()
print("Heapmap inicializado em {:.1f}s.".format(ts2-ts1))

# obtendo as bounding boxes

print("Obtendo bounding boxes...")
ts1 = perf()

bbs = dict(carros=[], garrafas=[], mult=[], xicaras=[])

for k in bbs.keys():
    os.chdir(k)

    lbs = glob("*.txt")
    if "classes.txt" in lbs: lbs.remove("classes.txt")

    for lb in lbs:
        lf = open(lb)
        lines = lf.read().splitlines()
        lf.close()
        for li in lines:
            b = li.split()
            b = [int(b[0]), float(b[1]), float(b[2]), float(b[3]), float(b[4])]
            b = xywh2xyxy(b, size, size)
            bbs[k].append(b)

    os.chdir("..")

ts2 = perf()
print("Bounding boxes obtidas em {:.1f}s".format(ts2-ts1))

# gerando o heatmap

print("Gerando heatmap...")
ts1 = perf()

for _ in bbs.values():
    for bb in _:
        for i in range(bb[1], bb[3]):
            for j in range(bb[2], bb[4]):
                heatmap[i,j] += 1

ts2 = perf()
print("Heatmap gerado em {:.1f}s".format(ts2-ts1))

# normalizando os pixels de 0-255

print("Normalizando os pixels...")
ts1 = perf()

maxi = np.amax(heatmap)
for i in range(size):
    for j in range(size):
        norm = 255 - (heatmap.item((i, j)) * 255 // maxi)
        heatmap.itemset((i, j), norm)

ts2 = perf()
print("Pixels normalizados em {:.1f}s".format(ts2-ts1))

# mostrando o heatmap

tsf = perf()
print("Tempo total de execução: {:.1f}s".format(tsf-tsi))

cv.imshow("HEATMAP", heatmap)
cv.waitKey(0)
cv.destroyAllWindows()
