import argparse
from collections import defaultdict as defdict
import csv
import os, os.path as path


psr = argparse.ArgumentParser(description="""
    Script para formatar logs de detecções realizadas pelo modelo.
    O log deve estar no formato original gerado pelo modelo:
        <n-frame> <id-classe> <conf> <localizacao>
    O log formatado possuirá o seguinte formato (em CSV):
        <n-frame>,<id-classe>,<total-adjacentes>""",
    formatter_class=argparse.RawDescriptionHelpFormatter
)

psr.add_argument("p", help="Caminho do arquivo de log.")

args = psr.parse_args()

# normalizando paths

p = path.abspath(path.expanduser(args.p))

# obtém o conteúdo do arquivo de entrada

arq_entrada = open(p)
entrada = arq_entrada.read().splitlines()
arq_entrada.close()

# 1) extrai as classes presentes no log

classes = set()
for linha in entrada:
    cls = int(linha.split()[1])
    classes.add(cls)
classes = list(classes)

# 2) transformando o arquivo de log em um dicionário
# - o dicionário é orientado aos frames, e não linhas

dicio = defdict(list)

for linha in entrada:
    n_frame = int(linha.split()[0])
    id_classe = int(linha.split()[1])

    dicio[n_frame].append(id_classe)

# 3) iterando sobre o dicionário, e gerando logs formatados

logs = []

frames = list(sorted(dicio.keys()))
for classe in classes:
    # log: <n_frame>,<id_classe>,<total_adjacentes>
    log_atual = [-1, classe, -1]

    for i, n_frame in enumerate(frames):
        if i == 0 or n_frame == frames[i-1]+1: # possível continuidade
            if classe in dicio[n_frame]: # continua ou recomeça
                if log_atual[2] == -1: # recomeça
                    log_atual[0] = n_frame # grava nº do frame

                # de qualquer modo, incrementa contador de adjacências
                log_atual[2] += 1

            else: # interrompe possível sequência (objeto ausente)
                if log_atual[2] > -1: # havia uma adjacência em andamento
                    logs.append(log_atual.copy())
                    log_atual = [-1, classe, -1] # reseta

        else: # interrompe possível sequência (pulo entre frames)
            if log_atual[2] > -1: # havia uma adjacência em andamento
                logs.append(log_atual.copy())
                log_atual = [-1, classe, -1] # reseta

    # verifica se havia uma última adjacência pendente
    if log_atual[2] > -1: # havia uma adjacência em andamento
        logs.append(log_atual.copy())
        log_atual = [-1, classe, -1] # reseta, supérfluo

# 4) ordena os logs

logs.sort()

# 5) escreve os logs no CSV de saída

# caminho do arquivo CSV de saída

caminho_saida = path.splitext(p)[0] + ".csv"

# escrevendo no arquivo de saída

arq_saida = open(caminho_saida, "w", newline="")
escritor = csv.writer(arq_saida)

escritor.writerows(logs)

arq_saida.close()
