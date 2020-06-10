"""
Script para mostrar as estatísticas do dataset.
"""

from collections import defaultdict
from glob import glob
from shutil import get_terminal_size
from sys import argv
import os
from os import path

scr = path.abspath(path.expanduser(path.dirname(argv[0])))
dset = path.join(path.dirname(scr), "dataset")
os.chdir(dset)

# estatísticas dos carros

os.chdir("carros")
car = defaultdict(int)
lbls = glob("*.txt")
if "classes.txt" in lbls: lbls.remove("classes.txt")

car["i"] = len(glob("*.jpg"))
car["l"] = len(lbls)
car["%"] = int(car["l"] / car["i"] * 100)
for l in lbls:
    a = open(l)
    car["o"] += len(a.readlines())
    a.close()

os.chdir("..")

# estatísticas das garrafas

os.chdir("garrafas")
gar = defaultdict(int)
lbls = glob("*.txt")
if "classes.txt" in lbls: lbls.remove("classes.txt")

gar["i"] = len(glob("*.jpg"))
gar["l"] = len(lbls)
gar["%"] = int(gar["l"] / gar["i"] * 100)
for l in lbls:
    a = open(l)
    gar["o"] += len(a.readlines())
    a.close()

os.chdir("..")

# estatísticas das xícaras

os.chdir("xicaras")
xic = defaultdict(int)
lbls = glob("*.txt")
if "classes.txt" in lbls: lbls.remove("classes.txt")

xic["i"] = len(glob("*.jpg"))
xic["l"] = len(lbls)
xic["%"] = int(xic["l"] / xic["i"] * 100)
for l in lbls:
    a = open(l)
    xic["o"] += len(a.readlines())
    a.close()

os.chdir("..")

# estatísticas dos múltiplos

os.chdir("mult")
mul = defaultdict(int)
lbls = glob("*.txt")
if "classes.txt" in lbls: lbls.remove("classes.txt")

mul["i"] = len(glob("*.jpg"))
mul["l"] = len(lbls)
mul["%"] = int(mul["l"] / mul["i"] * 100)
for l in lbls:
    a = open(l)
    mul["o"] += len(a.readlines())
    a.close()

os.chdir("..")

# estatísticas totais

tot = dict()
tot["i"] = car["i"] + gar["i"] + xic["i"] + mul["i"]
tot["l"] = car["l"] + gar["l"] + xic["l"] + mul["l"]
tot["%"] = int(tot["l"] / tot["i"] * 100)
tot["o"] = car["o"] + gar["o"] + xic["o"] + mul["o"]

# imprimindo estatísticas

w = get_terminal_size().columns

dics = dict(CARROS=car, GARRAFAS=gar, XICARAS=xic, MULTIPLOS=mul, TOTAL=tot)

print()
print("ESTATÍSTICAS".center(w, "_"))
for n, d in dics.items():
    print()
    print("-"*w)
    print("|{}|".format(n.center(w-2)))
    print("-"*w)
    print("|{}|{}|".format("Imagens".center(w//2-2), str(d["i"]).center(w//2-1)))
    print("|{}|{}|".format("Labels".center(w//2-2), str(d["l"]).center(w//2-1)))
    print("|{}|{}|".format("Imagens rotuladas".center(w//2-2), (str(d["%"])+"%").center(w//2-1)))
    print("|{}|{}|".format("Objetos".center(w//2-2), str(d["o"]).center(w//2-1)))
    print("-"*w)
print()
