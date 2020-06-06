## Coleta do dataset

### Acompanhamento da coleta

| Objeto    | Total | Coletados |
|:---------:|:-----:|:---------:|
| Carros    |   100 |       100 |
| Garrafas  |       |           |
| Xícaras   |   100 |       100 |
| Múltiplos |    40 |        20 |

### Versionamento

- No repositório, será mantida somente a versão mais recente e atualizada do dataset
- As versões anteriores ou obsoletas serão retiradas do repositório e armazenadas no [Kaggle](https://www.kaggle.com)

### Visão geral

- Serão coletadas imagens de objetos de 3 classes (carrinhos de brinquedo, garrafas e xícaras)
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

### Datasets externos

Além da coleta manual das imagens, também serão emprestadas imagens de outros datasets de terceiros. Os créditos para essas imagens externas estará presente no [arquivo de créditos](creditos.md).
