# Desenvolvimento de um assistente virtual para segurança e saúde no trabalho, apoiado por Inteligência Artificial

Projeto de Iniciação Científica do curso de [Ciência da Computação](http://cc.uffs.edu.br/)
da [UFFS campus Chapecó](https://www.uffs.edu.br/campi/chapeco).

### :scroll: Especificação

- [Formulário Único de Proposta][form]

### :man_teacher: Orientador

- Claunir Pavan
  - [GitHub](https://github.com/cleopavan)
  - [Lattes](http://lattes.cnpq.br/7362574930328474)

### :man_student: Acadêmicos

- Paulo Gabriel Sena Comasetto (bolsista)
  - [GitHub](https://github.com/paulogsc)
  - [Lattes](http://lattes.cnpq.br/1331812120349303)

- Richard Henrique Herrera Silva (voluntário)
  - [GitHub](https://github.com/henriqueherrera)
  - [LinkedIn](http://linkedin.com/in/richard-herrera-b096a8187)

### :pen: Descrição

O objetivo descrito no [formulário][form] do projeto é elaborar um programa que auxilie em tempo real um eletricista nas tarefas a serem realizadas (e.g., instalação de um sistema de aterramento temporário).
Para tal, o eletricista estará equipado com uma câmera que registrará as atividades do profissional. Tendo em mente a sequência de passos a serem efetuados para completar a tarefa, o algoritmo deverá identificar, por meio das imagens obtidas, a etapa em que o eletricista encontra-se no momento. A partir daí, o programa auxiliará o profissional, indicando o próximo passo a ser executado ou sinalizando caso alguma etapa seja cumprida na ordem errada.

Todavia, em virtude da alta complexidade em implementar o sistema descrito acima, ficou acertado que, em um primeiro momento, o objetivo do projeto seria apenas desenvolver um programa que acompanharia (de modo visual) a execução de uma dada tarefa, informando a próxima etapa a ser feita até o cumprimento do processo. O ambiente que servirá de base para a coleta de imagens, a definição das tarefas e a construção do algoritmo será um alheio ao do setor elétrico, uma vez que o objetivo é somente implementar um "programa simples de acompanhamento visual de tarefas".

### :balance_scale: Licenciamento

Os códigos do projeto estão licenciados da seguinte forma:

- O modelo (rede neural) presente na pasta `projeto` foi baseado no repositório da empresa Ultralytics, presente [neste link](https://www.github.com/ultralytics/yolov3). Esse repositório está sob a licença GPL 3.0; portanto, o código modificado do presente repositório também encontra-se sob a mesma licença ([cópia][gpl])
- Os _scripts shell_ que foram usados no decorrer do projeto - contidos na pasta `scripts` - são originais e escritos pelo autor deste repositório, e recebem a licença MIT ([cópia][mit])
- Os arquivos `.odg` e `.png` do diretório `.assets` são originais e desenvolvidos pelo autor deste repositório, e estão sob a licença MIT ([cópia][mit])

O dataset presente neste repositório está licenciado do seguinte modo:

- As imagens recebem as seguintes licenças:

| Imagens | Copyright | Licença | Referência | Link |
|:-------:|:---------:|:-------:|:----------:|:----:|
| carro-000-\*.jpg - carro-096-*.jpg\ | © 2020 Paulo Gabriel Sena Comasetto | [CC BY-NC-SA 4.0][cc by-nc-sa 4.0] |||
| carro-097-*.jpg |||| [Link](http://www.vision.caltech.edu/pmoreels/Datasets/Giuseppe_Toys_03/) |
| carro-100-*.jpg || [Pixabay License](https://pixabay.com/service/license/) |||
| carro-101-*.jpg || [Unsplash License](https://unsplash.com/license) |||
| xicara-000-\*.jpg - xicara-099-\*.jpg | © 2020 Paulo Gabriel Sena Comasetto | [CC BY-NC-SA 4.0][cc by-nc-sa 4.0] |||
| xicara-101-*.jpg ||| Sapp, Benjamin & Saxena, Ashutosh & Ng, Andrew. (2008). A Fast Data Collection and Augmentation Procedure for Object Recognition.. 1402-1408. | [Link](http://ai.stanford.edu/~asaxena/robotdatacollection/dataset.html) |
| xicara-103-*.jpg ||| A Large-Scale Hierarchical Multi-View RGB-D Object Dataset; Kevin Lai, Liefeng Bo, Xiaofeng Ren, and Dieter Fox; IEEE International Conference on Robotics and Automation (ICRA), May 2011 | [Link](http://rgbd-dataset.cs.washington.edu/dataset/rgbd-dataset_full/) |
| xicara-104-*.jpg || [Pixabay License](https://pixabay.com/service/license/) |||

- As labels/anotações das imagens são copyright dos autores (© 2020 Paulo Gabriel Sena Comasetto and Richard Henrique Herrera Silva) e estão sob a licença [CC BY-NC-SA 4.0][cc by-nc-sa 4.0]


[form]: documentos/Formulario%20Unico%20de%20Proposta.pdf
[kaggle]: https://www.kaggle.com

[gpl]: GPL.txt
[mit]: MIT.txt

[cc by-nc-sa 4.0]: https://creativecommons.org/licenses/by-nc-sa/4.0/
