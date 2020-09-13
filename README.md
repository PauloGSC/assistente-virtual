# Desenvolvimento de um assistente virtual para segurança e saúde no trabalho, apoiado por Inteligência Artificial

Projeto de Iniciação Científica do curso de [Ciência da Computação](http://cc.uffs.edu.br/)
da [UFFS campus Chapecó](https://www.uffs.edu.br/campi/chapeco).

### :scroll: Especificação

- [Formulário Único de Proposta][form]

### :man_teacher: Orientador

- Claunir Pavan
  - [GitHub](https://github.com/cleopavan)
  - [Lattes](http://lattes.cnpq.br/7362574930328474)

### :man_student: Acadêmico

- Paulo Gabriel Sena Comasetto
  - [GitHub](https://github.com/paulogsc)
  - [Lattes](http://lattes.cnpq.br/1331812120349303)

### :pen: Descrição

O objetivo formal do projeto consistiu em elaborar um algoritmo, utilizando técnicas de Deep Learning, para auxiliar um trabalhador do setor elétrico nas suas tarefas. O programa atuaria como um “assistente virtual”, monitorando e orientando as atividades realizadas pelo profissional. A fim de possibilitar esse acompanhamento, o eletricista estaria equipado com uma câmera de vídeo para o registro das ações do profissional em tempo real. O software receberia a entrada visual captada pela câmera, identificaria a etapa em que o trabalhador se encontra e indicaria o próximo passo a ser executado; caso alguma etapa fosse cumprida na ordem incorreta, o programa também sinalizaria ao profissional. Esse ciclo repetir-se-ia até o cumprimento total da tarefa.

Todavia, em virtude da alta complexidade em desenvolver o algoritmo descrito acima, o objetivo de implementar um software completo para assistente virtual precisou ser revisto e relaxado. Neste contexto, buscamos verificar a viabilidade do objetivo original, elaborando um programa que execute a principal função do assistente virtual: reconhecer e detectar determinados objetos em imagens recebidas por uma câmera.    

### :balance_scale: Licenciamento

Os códigos do projeto estão licenciados da seguinte forma:

- O modelo (rede neural) presente na pasta `projeto` foi baseado no repositório da empresa Ultralytics, presente [neste link](https://www.github.com/ultralytics/yolov3). Esse repositório está sob a licença GPL 3.0; portanto, o código modificado do presente repositório também encontra-se sob a mesma licença ([cópia][gpl])
- Os _scripts shell_ que foram usados no decorrer do projeto - contidos na pasta `scripts` - são originais e escritos pelo autor deste repositório, e recebem a licença MIT ([cópia][mit])

O dataset (`projeto/data/train` e `projeto/data/test`) está licenciado do seguinte modo:

- As imagens recebem as seguintes licenças:

| Imagens | Copyright | Licença | Referência | Link |
|:-------:|:---------:|:-------:|:----------:|:----:|
| carro-000-\*.jpg - carro-096-*.jpg\ | © 2020 Paulo Gabriel Sena Comasetto | [CC BY-NC-SA 4.0][cc by-nc-sa 4.0] |||
| carro-097-*.jpg |||| [Link](http://www.vision.caltech.edu/pmoreels/Datasets/Giuseppe_Toys_03/) |
| carro-100-*.jpg || [Pixabay License](https://pixabay.com/service/license/) |||
| carro-101-*.jpg || [Unsplash License](https://unsplash.com/license) |||
| dtc-* | © 2020 Claunir Pavan | [CC BY-NC-SA 4.0][cc by-nc-sa 4.0] |||
| xicara-000-\*.jpg - xicara-099-\*.jpg | © 2020 Paulo Gabriel Sena Comasetto | [CC BY-NC-SA 4.0][cc by-nc-sa 4.0] |||
| xicara-101-*.jpg ||| Sapp, Benjamin & Saxena, Ashutosh & Ng, Andrew. (2008). A Fast Data Collection and Augmentation Procedure for Object Recognition.. 1402-1408. | [Link](http://ai.stanford.edu/~asaxena/robotdatacollection/dataset.html) |
| xicara-103-*.jpg ||| A Large-Scale Hierarchical Multi-View RGB-D Object Dataset; Kevin Lai, Liefeng Bo, Xiaofeng Ren, and Dieter Fox; IEEE International Conference on Robotics and Automation (ICRA), May 2011 | [Link](http://rgbd-dataset.cs.washington.edu/dataset/rgbd-dataset_full/) |
| xicara-104-*.jpg || [Pixabay License](https://pixabay.com/service/license/) |||

- As labels/anotações das imagens são copyright de  2020 Paulo Gabriel Sena Comasetto and Richard Henrique Herrera Silva, e estão sob a licença [CC BY-NC-SA 4.0][cc by-nc-sa 4.0]


[form]: documentos/Formulario%20Unico%20de%20Proposta.pdf
[kaggle]: https://www.kaggle.com

[gpl]: GPL.txt
[mit]: MIT.txt

[cc by-nc-sa 4.0]: https://creativecommons.org/licenses/by-nc-sa/4.0/
