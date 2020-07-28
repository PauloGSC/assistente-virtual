import argparse
from glob import glob
import os
import os.path as path
from random import seed, sample
from shutil import copy


seed()


psr = argparse.ArgumentParser(description="""
    Script para obter uma amostra fixa do dataset, de forma estratificada.
""")

psr.add_argument("ds", help="Diretório raiz.")
psr.add_argument("n", type=int, help="Tamanho da amostra.")
psr.add_argument("dd", help="Diretório destino.")

args = psr.parse_args()

# obtendo argumentos

n = args.n

# normalizando paths

ds = path.abspath(path.expanduser(args.ds))
dd = path.abspath(path.expanduser(args.dd))

# criando diretório destino, se não existir

if not path.exists(dd): os.makedirs(dd)

# obtendo total de imagens e criando subdiretórios-destino

os.chdir(ds)

tot_img = 0
with os.scandir() as scan:
    for ent in scan:
        if ent.is_dir():
            tot_img += len(glob(path.join(ent.name, "*.jpg")))

            sub_dd = path.join(dd, ent.name)
            if not path.exists(sub_dd): os.mkdir(sub_dd)

# amostrando de forma estratificada

with os.scandir() as scan:
    for ent in scan:
        if ent.is_dir():
            os.chdir(ent.name)

            imgs = glob("*.jpg")
            imgs.sort()
            n2 = round(len(imgs) / tot_img * n)
            print("{} / {} * {} = {}".format(len(imgs), tot_img, n, n2))
            samp = sample(imgs, n2)

            lbls = []
            for i in samp:
                lab = path.splitext(i)[0] + ".txt"
                if path.exists(lab):
                    lbls.append(lab)
            samp.extend(lbls)
            samp.sort()

            for s in samp:
                sub_dd = path.join(dd, ent.name)
                copy(s, sub_dd)

            os.chdir("..")
