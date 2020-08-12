import argparse
from glob import glob
import os
import os.path as path
from subprocess import run, DEVNULL

# obtendo argumentos da linha de comando

psr = argparse.ArgumentParser(description="""
    Script para remover informações EXIF de arquivos.
""")

psr.add_argument("p", help="Diretório com os arquivos.")

p = psr.parse_args().p

# normalizando paths

p = path.abspath(path.expanduser(p))

# removendo EXIF

os.chdir(p)

com1 = "exiftool -all= *"
run(com1, shell=True)

com2 = "rm *original"
# caso nenhum arquivo teve seus metadados removidos,
# não haverá arquivos *_original; nesse caso, o programa resulta em erro e,
# portanto, deve-se silenciá-lo (redirecionando para /dev/null)
run(com2, shell=True, stderr=DEVNULL)
