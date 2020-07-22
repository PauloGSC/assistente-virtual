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

- Raphael Borges dos Santos Filho (voluntário)
  - [GitHub](http://github.com/oraphaborges)
  - [LinkedIn](https://br.linkedin.com/in/raphael-borges-63a04591)

### :pen: Descrição

O objetivo descrito no [formulário][form] do projeto é elaborar um programa que auxilie em tempo real um eletricista nas tarefas a serem realizadas (e.g., instalação de um sistema de aterramento temporário).
Para tal, o eletricista estará equipado com uma câmera que registrará as atividades do profissional. Tendo em mente a sequência de passos a serem efetuados para completar a tarefa, o algoritmo deverá identificar, por meio das imagens obtidas, a etapa em que o eletricista encontra-se no momento. A partir daí, o programa auxiliará o profissional, indicando o próximo passo a ser executado ou sinalizando caso alguma etapa seja cumprida na ordem errada.

Todavia, em virtude da alta complexidade em implementar o sistema descrito acima, ficou acertado que, em um primeiro momento, o objetivo do projeto seria apenas desenvolver um programa que acompanharia (de modo visual) a execução de uma dada tarefa, informando a próxima etapa a ser feita até o cumprimento do processo. O ambiente que servirá de base para a coleta de imagens, a definição das tarefas e a construção do algoritmo será um alheio ao do setor elétrico, uma vez que o objetivo é somente implementar um "programa simples de acompanhamento visual de tarefas".

### :balance_scale: Licenciamento

Os códigos do projeto estão atualmente licenciados da seguinte forma:

- O modelo (rede neural) presente na pasta `projeto/projeto` foi baseado no repositório da empresa Ultralytics, presente [neste link](https://www.github.com/ultralytics/yolov3). Esse repositório está sob a licença GPL 3.0; portanto, o código modificado do presente repositório também encontra-se sob a mesma licença ([cópia][gpl])
- Os _scripts shell_ que foram usados no decorrer do projeto - contidos na pasta `projeto/outros/scripts` - são originais e escritos pelos autores deste repositório, e recebem a licença MIT ([cópia][mit])
- Os arquivos `.odg` e `.png` (com exceção de `.assets/modelo.png`) são originais e desenvolvidos pelos autores deste repositório, e estão sob a licença MIT ([cópia][mit]

As imagens e vídeos coletados para o projeto estão atualmente licenciados do seguinte modo:

- Os datasets antigos e que já foram usados/não foram usados no projeto estão hospedados no [Kaggle][kaggle] e listados no arquivo [datasets.md](projeto/outros/markdowns/datasets.md); em geral, recebem a licença CC BY-NC-SA (para maiores detalhes, visitar o dataset)
- Os datasets presentes neste repositório ainda estão sendo usados para o treinamento do modelo; assim que forem utilizados, serão retirados do repositório, armazenadas no [Kaggle][kaggle] e licenciadas sob uma licença Creative Commons


[form]: documentos/Formulario%20Unico%20de%20Proposta.pdf
[kaggle]: https://www.kaggle.com

[gpl]: GPL.txt
[mit]: MIT.txt
