import argparse
from glob import glob
import os
import os.path as path
from random import seed, sample


seed()


psr = argparse.ArgumentParser(description="""
    Script para dividir o dataset em 'train' e 'test', de forma estratificada.
""")

psr.add_argument("ds", help="Diretório raiz.")
psr.add_argument("p", type=float,
                 help="Porcentagem dos dados para o diretório de 'train' (0 <= p <= 1).\
                       O restante irá para o diretório 'test'.")
psr.add_argument("-dd", default="", help="Diretório para guardar os subdiretórios 'train' e 'test'.")

args = psr.parse_args()

# obtendo argumentos

ds, p, dd = args.ds, args.p, args.dd if args.dd else args.ds

# normalizando paths

ds = path.abspath(path.expanduser(ds))
dd = path.abspath(path.expanduser(dd))

# criando diretório destino, se não existir

if not path.exists(dd): os.makedirs(dd)

tr = path.join(dd, "train")
te = path.join(dd, "test")
if not path.exists(tr): os.mkdir(tr)
if not path.exists(te): os.mkdir(te)

# dividindo o dataset

os.chdir(ds)
with os.scandir() as scan:
    for ent in scan:
        if ent.is_dir():
            os.chdir(ent.name)

            imgs = glob("*.jpg")
            imgs.sort()

            n = round(p * len(imgs))
            train = sample(imgs, n)
            lbls = [path.splitext(im)[0]+".txt" for im in train]
            train.extend(lbls)
            for d in train:
                new = path.join(tr, d)
                os.rename(d, new)

            test = os.listdir()
            test.sort()
            for d in test:
                new = path.join(te, d)
                os.rename(d, new)

            os.chdir("..")
