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

### :page_facing_up: Planejamento

1. Capacitação
    1. Deep Learning
    2. Redes Neurais Convolucionais (CNN)
    3. Object Detection
    4. Object Tracking
2. Definição da biblioteca de Deep Learning a ser usada
3. Definição do algoritmo de Object Detection a ser usado
4. Definição da(s) tarefa(s) a ser(em) usada(s) como base para o programa
5. Coleta de imagens/vídeos registrando as etapas da(s) tarefa(s)
6. Rotulagem das imagens obtidas
7. Construção da rede neural
8. Treinamento/ajuste e teste da rede neural
9. Codificação do algoritmo identificador de tarefas
10. Integração do detector com o algoritmo
11. Testes finais com vídeos em tempo real


[form]: documentos/Formulario%20Unico%20de%20Proposta.pdf
