## Dataset

### Acompanhamento da coleta/rotulagem

| Categoria | Meta     | Coletados | Rotulados |
|:---------:|:--------:|:---------:|:---------:|
| Carros    | 3000     | 3011      | 3011      |
| Garrafas  |          | 1719      | 1296      |
| Xícaras   | 3000     | 3020      | 3020      |
| Múltiplos |          | 425       | 425       |
|           |          | __8175__  | __7752__  |

### Versionamento

- No repositório, será mantida somente a versão mais recente e atualizada do dataset
- As versões anteriores ou obsoletas serão retiradas do repositório e armazenadas no [Kaggle](https://www.kaggle.com)

### Visão geral

- Serão coletadas imagens de objetos de 3 classes (carrinhos de brinquedo, garrafas e xícaras)
- Adicionalmente, cenários contendo múltiplos (2 ou 3) objetos também serão registrados

### Forma de coleta

- Para cada objeto, um único vídeo com cerca de __20s__ mostrando o objeto de vários ângulos (o mesmo vale para os cenários com múltiplos objetos)

### Abrangência de situações distintas

- Para garantir mais variedade às imagens coletadas, ocasionalmente haverá variação na iluminação e no cenário do ambiente de coleta
- Nos vídeos, haverá alternância da distância entre a câmera e o(s) objeto(s), de modo que a rede aprenda a reconhecer objetos de vários tamanhos
- Os cenários com múltiplas amostras servirão justamente para abranger o fator de oclusão dos objetos

### Extração das imagens

- Para cada vídeo, são extraídas __1,5 imagens por segundo__ (para evitar tanta repetição entre os frames)
- Cada imagem é analisada cuidadosamente; imagens muito borradas, sem foco ou com qualidade ruim são descartadas

### Datasets externos

Além da coleta manual das imagens, também serão emprestadas imagens de outros datasets de terceiros. Os créditos para essas imagens externas estarão presente no [arquivo de créditos](creditos.md).
