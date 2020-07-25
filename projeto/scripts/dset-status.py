"""
Script para mostrar as estatísticas do dataset.
"""

from collections import defaultdict
from glob import glob
import os
import os.path as path
from shutil import get_terminal_size
from sys import argv

# entrando na pasta dataset

scr = path.abspath(path.expanduser(path.dirname(argv[0])))
os.chdir(scr)
os.chdir("../../projeto/dataset")

# obtendo estatísticas de cada subdiretório

stats = dict()
with os.scandir(".") as scan:
    for entry in scan:
        if entry.is_dir():
            name = entry.name
            os.chdir(name)

            dic = defaultdict(int)

            lbls = glob("*.txt")
            if "classes.txt" in lbls: lbls.remove("classes.txt")

            dic["i"] = len(glob("*.jpg"))
            dic["l"] = len(lbls)
            dic["%"] = int(dic["l"]/dic["i"] * 100)
            for l in lbls:
                a = open(l)
                dic["o"] += len(a.readlines())
                a.close()

            stats[name] = dic

            os.chdir("..")

# estatísticas totais

tot = defaultdict(int)
for d in stats.values():
    tot["i"] += d["i"]
    tot["l"] += d["l"]
    tot["o"] += d["o"]
tot["%"] = int(tot["l"]/tot["i"] * 100)

stats["TOTAL"] = tot

# imprimindo estatísticas

w = get_terminal_size().columns

print()
print("ESTATÍSTICAS".center(w, "_"))
for n, d in stats.items():
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
