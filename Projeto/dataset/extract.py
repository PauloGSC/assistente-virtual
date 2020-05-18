# script para extrair frames de um ou mais videos-fonte

# este script utiliza o programa ffmpeg, eh necessario te-lo instalado para funcionar

# para o script funcionar, a estrutura de pastas deve ser a seguinte:
# - frames (pasta para guardar os frames extraidos)
# - videos (pasta com os videos)
# extract.py (este arquivo)

import os

# lista de videos a serem analisados

extVideo = ".mp4"

vids2 = os.listdir("videos")
vids2.sort()
vids = []
for v in vids2:
	if v.endswith(extVideo):
		vids.append(v)

# parametros para a extracao

# offset do inicio da extracao, em segundos
start = 2
# numero de frames a serem extraidos por segundo
rate = 2

# script de extracao das frames
# os frames serao extraidos para a pasta "frames", com o nome de cada frame sendo nome_do_video-numero_do_frame

extFrame = ".png"

for v in vids:
	pref = v[:v.find(".")]
	comm = "ffmpeg -i videos/{} -ss {} -r {} frames/{}-%03d{}".format(v, start, rate, pref, extFrame)
	os.system(comm)

# geralmente os dois primeiros frames do video sao muito parecidos
# assim, exclui-se o primeiro frame de cada video

os.chdir("frames")

files = os.listdir()
files.sort()

toDel = []
for f in files:
	if f.endswith("-001" + extFrame):
		toDel.append(f)
for f in toDel:
	os.remove(f)

# renomear os arquivos para compensar a falta dos arquivos 001

files = os.listdir()
files.sort()

for f in files:
	num = f[f.rfind("-")+1:f.rfind(".")]
	rep = num + extFrame
	pred = str(int(num)-1).zfill(3) + extFrame
	new = f.replace(rep, pred)
	os.rename(f, new)
