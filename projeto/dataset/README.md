## Coleta do dataset

### Acompanhamento da coleta

| Objeto    | Total | Coletados |
|:---------:|:-----:|:---------:|
| Caixas    |   104 |       104 |
| Xícaras   |   100 |       100 |
| Carros    |   100 |       100 |
| Múltiplos |   100 |        37 |

### Versionamento

- Versão 1: vídeos inalterados
- Versão 2: imagens retiradas dos vídeos da versão 1, refinadas e devidamente rotuladas

### Visão geral

- Serão coletadas imagens de objetos de 3 classes (caixas, xícaras e carrinhos de brinquedo)
- Cada classe possui ~100 amostras distintas entre si
- Adicionalmente, ~100 cenários contendo múltiplos (2 ou 3) objetos também serão registrados

### Forma de coleta

- Para cada objeto, um único vídeo com cerca de __20s__ mostrando o objeto de vários ângulos (o mesmo vale para os cenários com múltiplos objetos)

### Abrangência de situações distintas

- Para garantir mais variedade às imagens coletadas, ocasionalmente haverá variação na iluminação e no cenário do ambiente de coleta
- Nos vídeos, haverá alternância da distância entre a câmera e o(s) objeto(s), de modo que a rede aprenda a reconhecer objetos de vários tamanhos
- Os cenários com múltiplas amostras servirão justamente para abranger o fator de oclusão dos objetos

### Extração das imagens

- Para cada vídeo, são extraídas __1,5 imagens por segundo__ (para evitar tanta repetição entre os frames)
