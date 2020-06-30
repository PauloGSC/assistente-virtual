import argparse
from collections import defaultdict
from copy import deepcopy
from datetime import datetime
from glob import glob
import numpy as np
import os
import os.path as path
from sys import argv
from time import perf_counter as perf

import cv2 as cv

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
    Script para gerar os heatmaps do dataset.
""")

psr.add_argument("-s", type=int, default=416, help="Tamanho dos heatmaps (default=416).")
psr.add_argument("p", help="Caminho para salvar os heatmaps.")

args = psr.parse_args()
size = args.s
pth = args.p

# normalizando paths

pth = path.abspath(path.expanduser(pth))

# entrando na pasta do datasetpth

scr = path.abspath(path.expanduser(path.dirname(argv[0])))
os.chdir(scr)
os.chdir("../../projeto/dataset")

# obtendo as bounding boxes

print("Obtendo bounding boxes...")
ts1 = perf()

bbs = defaultdict(list)
with os.scandir(".") as scan:
    for entry in scan:
        if entry.is_dir():
            name = entry.name
            os.chdir(name)

            lbls = glob("*.txt")
            lbls.sort()
            if "classes.txt" in lbls: lbls.remove("classes.txt")

            for lbl in lbls:
                with open(lbl) as lf:
                    lines = lf.read().splitlines()
                for li in lines:
                    b = li.split()
                    b = [int(b[0]), float(b[1]), float(b[2]), float(b[3]), float(b[4])]
                    b = xywh2xyxy(b, size, size)
                    bbs[name].append(b)

            #bbs[name].sort()
            os.chdir("..")

ts2 = perf()
print("Bounding boxes obtidas em {:.1f}s".format(ts2-ts1))

# gerando os heatmaps

print("Gerando heatmaps...")
ts1 = perf()

templ = np.zeros((size, size), dtype=np.int)
hmaps = dict.fromkeys(bbs, deepcopy(templ))

for d, bb in bbs.items():
    for b in bb:
        hmaps[d][b[1]:b[3], b[2]:b[4]] += 1
print(hmaps["train"][160:170, 150:160])
# print(hmaps["val"][205:215, 205:215])
# total = deepcopy(templ)
# for h in hmaps.values():
#     total = np.add(total, h)
# hmaps["TOTAL"] = total
#
# print(hmaps)

ts2 = perf()
print("Heatmap gerado em {:.1f}s".format(ts2-ts1))
#
# # normalizando os pixels de 0-255
#
# print("Normalizando os pixels...")
# ts1 = perf()
#
# norm = lambda v, maxi: 255 - (v*255 // maxi)
# for d, h in hmaps.items():
#     maxi = np.amax(h)
#     hmaps[d][:] = norm(hmaps[d][:], maxi)
#
# ts2 = perf()
# print("Pixels normalizados em {:.1f}s".format(ts2-ts1))
#
# # salvando os heatmaps
#
# print("Salvando heatmaps...")
# ts1 = perf()
#
# for d, h in hmaps.items():
#     now = datetime.now().strftime("%d-%m-%Y-%H:%M:%S")
#     fname = "{0}-{1}x{1}-{2}.jpg".format(d, size, now)
#     cv.imwrite(path.join(pth, fname), h)
#
# ts2 = perf()
# print("Heatmaps salvos em {:.1f}s.".format(ts2-ts1))
#
# # tempo total de execução
#
# tsf = perf()
# print("Tempo total de execução: {:.1f}s".format(tsf-tsi))
