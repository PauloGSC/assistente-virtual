## Elaboração e coleta do dataset inédito

### Forma de coleta

- Para cada objeto, um único vídeo com cerca de __20s__ mostrando o objeto de vários ângulos

### Abrangência de situações distintas

- Para garantir mais variedade às imagens coletadas, ocasionalmente haverá variação na iluminação e no cenário do ambiente de coleta
- Nos vídeos, haverá alternância da distância entre a câmera e o(s) objeto(s), de modo que a rede aprenda a reconhecer objetos de vários tamanhos

### Extração das imagens

- Para cada vídeo, são extraídas __1,5 imagens por segundo__ (para evitar tanta repetição entre os frames)
- Cada imagem é analisada cuidadosamente; imagens muito borradas, sem foco ou com qualidade ruim são descartadas
