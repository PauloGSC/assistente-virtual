"""
Script para decidir os cenários que serão usados no coleta de imagens com múltiplos objetos.
Será executado apenas uma vez (o resultado será gravado no arquivo mult.txt).
"""

import random

random.seed()

obj = ["caixa", "xicara", "carro"]
cnt = {obj[0]:0, obj[1]:0, obj[2]:0, "NULO":0}

with open("t.txt", "w") as t:
	for f in range(1, 101):
		n = random.randint(2,3)
		res = [o for o in random.sample(obj, n)]
		if n == 2: res.append("NULO")
		for o in res: cnt[o] += 1
		random.shuffle(res)
		line = str(f).rjust(3) + ") "
		line += res[0].center(8) + " | "
		line += res[1].center(8) + " | "
		line += res[2].center(8)
		t.write(line + "\n")
		
	t.write("-"*34 + "\n")
	for k, v in cnt.items():
		t.write(str(k) + " = " + str(v) + "\n")
		
