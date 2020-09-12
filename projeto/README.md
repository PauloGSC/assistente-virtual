# Projeto

Para detectar os objetos (carrinho, DTC e xícara) em imagens/vídeos:

1) Instalar as bibliotecas necessárias:

```shell
pip3 install -Ur requirements.txt
```

2.1) Para detectar imagens, colocar os arquivos no diretório `/projeto/data/samples/img`

2.2) Para detectar vídeos, colocar os arquivos no diretório `/projeto/data/samples/vid`

3) Escolher uma das quatro estratégias na pasta `/estrategias` e baixar o respectivo arquivo de peso (presentes nos arquivos `pesos.txt`)

4) Mover o arquivo de pesos para dentro do diretório `/projeto/weights/assistente`

5) Executar o arquivo `/projeto/detect.py`, passando os argumentos necessários;  para obter uma lista dos argumentos possíveis, executar:

```shell
# cd no diretório assistente-virtual/projeto
python3 detect.py --help
```

- Como outra opção, pode-se abrir o _notebook_ `/projeto/treinamento.ipynb` no ambiente do Google Colab, que fornece GPUs online para treinamento/detecção mais rápidos
- Os passos para detecção são similares aos acima, e o _notebook_ também possui instruções informativas para guiar o processo
