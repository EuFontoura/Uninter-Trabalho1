## QUESTÃO 1 de 4 – Conteúdos até Aula 3
<b>Enunciado:</b> Imagina-se que você é um dos programadores responsáveis pela construção de um app de vendas para uma determinada empresa X que vende em atacado. Uma das estratégias de vendas dessa empresa X é dar desconto maior conforme o valor da compra, conforme a <b>listagem abaixo:</b>

Se valor for <b>menor</b> que 2500 o desconto será de 0%;
Se valor for <b>igual ou maior</b> que 2500 e <b>menor</b>que 6000 o desconto será de 4%;
Se valor for <b>igual ou maior</b> que 6000 e <b>menor </b>que 10000 o desconto será de 7%;
Se valor for <b>igual ou maior</b> que 10000 o desconto será de 11%;

<b>Elabore um programa em Python que:</b>

1 - Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu <b>nome e sobrenome</b><i> [EXIGÊNCIA DE CÓDIGO 1 de 6];</i>

2 - Deve-se implementar o input do <b>valor unitário</b> e <b>da quantidade do produto</b> <i>[EXIGÊNCIA DE CÓDIGO 2 de 6];</i>

Deve-se implementar o desconto <b>conforme a enunciado acima </b>(obs.: atente-se as condições de menor, igual e maior) <i>[EXIGÊNCIA DE CÓDIGO 3 de 6];</i>

3 - Deve-se implementar o <b>valor total sem desconto</b> e o <b>valor total com desconto</b> <i>[EXIGÊNCIA DE CÓDIGO 4 de 6];</i>

4 - Deve-se implementar as estruturas <b>if, elif e else (todas elas)</b> <i>[EXIGÊNCIA DE CÓDIGO 5 de 6];  </i>

5 - Deve-se inserir comentários <u>relevantes</u> no código <i>[EXIGÊNCIA DE CÓDIGO 6 de 6];</i>

6 - Deve-se apresentar na saída de console uma mensagem de boas-vindas com seu nome <i>[EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 2];</i>

7 - Deve-se apresentar na saída de console um pedido recebendo desconto (<b>valor total sem desconto</b> maior ou igual a 2500) <i>[EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 2];  </i>

___

## QUESTÃO 2 de 4 - Conteúdo até aula 04
<b>Enunciado:</b> Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma loja que vende Açaí e Cupuaçu. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.
A Loja possui seguinte relação:

- Tamanho <b>P</b> de Cupuaçu <b>(CP)</b> custa 9 reais e o Açaí <b>(AC)</b> custa 11 reais;
- Tamanho <b>M</b> de Cupuaçu <b>(CP)</b> custa 14 reais e o Açaí <b>(AC)</b> custa 16 reais;
- Tamanho <b>G</b> de Cupuaçu <b>(CP)</b> custa 18 reais e o Açaí <b>(AC)</b> custa 20 reais;

<b>Elabore um programa em Python que: </b>

1 - Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu <b>nome e sobrenome</b> <i>[EXIGÊNCIA DE CÓDIGO 1 de 8];</i> 

2 - Deve-se implementar o input do <b>sabor</b> (CP/AC) e o print “Sabor inválido. Tente novamente" se o usuário entra com valor diferente de CP e AC <i>[EXIGÊNCIA DE CÓDIGO 2 de 8];</i> 

3 - Deve-se implementar o input do <b>tamanho</b> (P/M/G) e o print “Tamanho inválido. Tente novamente" se o usuário com entra valor diferente de P, M ou G <i>[EXIGÊNCIA DE CÓDIGO 3 de 8];</i> 

4 - Deve-se implementar if, elif e/ou else, utilizando o modelo <b>aninhado</b> (aula 3 – Tema 4) com cada uma das combinações de <b>sabor</b> e <b>tamanho</b> <i>[EXIGÊNCIA DE CÓDIGO 4 de 8];</i> 

5 - Deve-se implementar um <b>acumulador</b> para somar os valores dos pedidos <i>[EXIGÊNCIA DE CÓDIGO 5 de 8];</i> 

6 - Deve-se implementar o input com a pergunta: “Deseja pedir mais alguma coisa?”. Se sim <b>repetir a partir do item B</b>, senão encerrar o programa executar o print do acumulador <i>[EXIGÊNCIA DE CÓDIGO 6 de 8];</i> 

7 - Deve-se implementar as estruturas de <b>while, break, continue (todas elas)</b> <i>[EXIGÊNCIA DE CÓDIGO 7 de 8];</i> 

8 - Deve-se inserir comentários <u>relevantes</u> no código <i>[EXIGÊNCIA DE CÓDIGO 8 de 8];</i> 

9 - Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome <i>[EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];</i> 

10 - Deve-se apresentar na saída de console um pedido em que o usuário errou o <b>sabor</b> <i>[EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4]; </i> 

11 - Deve-se apresentar na saída de console um pedido em que o usuário errou o <b>tamanho</b> <i>[EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];</i> 

12 - Deve-se apresentar na saída de console um pedido com duas opções sabores diferentes e com tamanhos diferentes <i>[EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4]; </i> 

___

## QUESTÃO 3 de 4 - Conteúdo até aula 05
<b>Enunciado:</b> Você foi contratado para desenvolver um sistema de cobrança de serviços de uma copiadora. Você ficou com a parte de desenvolver a interface com o funcionário.
A copiadora opera da seguinte maneira:

- Serviço de Digitalização (DIG) o custo por página é de um real e dez centavos;
- Serviço de Impressão Colorida (ICO) o custo por página é de um real; 
- Serviço de Impressão Preto e Branco (IPB) o custo por página é de quarenta centavos; 
- Serviço de Fotocópia (FOT) o custo por página é de vinte centavos; 
- Se número de páginas for <b>menor</b> que 20 retornar o número de página sem desconto;
- Se número de páginas for <b>igual ou maior</b> que 20 e <b>menor</b> que 200 retornar o número de páginas com o desconto é de 15%;
- Se número de páginas for <b>igual ou maior</b> que 200 e <b>menor</b> que 2000 retornar o número de páginas com o desconto é de 20%;
- Se número de páginas for <b>igual ou maior</b> que 2000 e <b>menor</b> que 20000 retornar o número de páginas com o desconto é de 25%;
- Se número de páginas for <b>maior ou igual</b> à 20000 não é aceito pedidos nessa quantidade de páginas;

- Para o <b>adicional</b> de encadernação simples (1) é cobrado um valor <b>extra</b> de 15 reais;
- Para o <b>adicional</b> de encadernação de capa dura (2) é cobrado um valor <b>extra</b> de 40 reais;
- Para o <b>adicional</b> de não querer mais nada (0) é cobrado um valor <b>extra</b> de 0 reais;

O valor final da conta é calculado da seguinte maneira:

<center>total = <b>(servico * num_pagina) + extra</b></center><br>

<b>Elabore um programa em Python que: </b>

- Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome *[EXIGÊNCIA DE CÓDIGO 1 de 7];*

- Deve-se implementar a função `escolha_servico()` em que: *[EXIGÊNCIA DE CÓDIGO 2 de 7];*
  - Pergunta o **serviço** desejado;
  - Retorna o valor **serviço** com base na escolha do usuário;
  - Repete a pergunta do item **B.a** se digitar uma opção diferente de: dig/ico/ipb/fot;
<br>
- Deve-se implementar a função `num_pagina()` em que: *[EXIGÊNCIA DE CÓDIGO 3 de 7];*
  - Pergunta o **número de páginas;**
  - Retorna o **número de páginas** com desconto seguindo a regra do enunciado (desconto calculado em cima do número de páginas);
  -  Repete a pergunta do item **C.a** se digitar um valor acima de 20000 ou valor não numérico (use try/except para não numérico)
<br>
- Deve-se implementar a função `servico_extra()` em que: *[EXIGÊNCIA DE CÓDIGO 4 de 7];*
  - Pergunta pelo serviço **adicional;**
  - Retornar o valor de apenas uma das **opções** de **adicional**
  - Repetir a pergunta item **D.a** se digitar uma opção diferente de: 1/2/0;
<br>
- Deve-se implementar o total a pagar no código principal (**main**), ou seja, não pode estar dentro de função, conforme o enunciado *[EXIGÊNCIA DE CÓDIGO 5 de 7];*

Deve-se implementar **try/except** *[EXIGÊNCIA DE CÓDIGO 6 de 7];*

Deve-se inserir comentários <u>relevantes</u> no código *[EXIGÊNCIA DE CÓDIGO 7 de 7];*

Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome *[EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];*

Deve-se apresentar na saída de console um pedido no qual o usuário errou a opção de serviço *[EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4];*

Deve-se apresentar na saída de console um pedido no qual o usuário digitou ultrapassou no número de páginas *[EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];*

Deve-se apresentar na saída de console um pedido com opção de serviço, número de páginas e serviço extra válidos *[EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];*

___

## QUESTÃO 4 de 4 - Conteúdo até aula 06

**Enunciado:** Você e sua equipe de programadores foram contratados por pequena empresa para desenvolver o software de gerenciamento de livros. Este software deve ter o seguinte menu e opções:
- Cadastrar Livro
- Consultar Livro
  - Consultar Todos 
  - Consultar por Id
  - Consultar por Autor
- Retornar ao menu
- Remover Livro
- Encerrar Programa

**Elabore um programa em Python que:**

- Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome *[EXIGÊNCIA DE CÓDIGO 1 de 8];*
<br>
- Deve-se implementar uma lista vazia com o nome de **lista_livro** e a variável id_global com valor inicial igual a 0 *[EXIGÊNCIA DE CÓDIGO 2 de 8];*
<br>
- Deve-se implementar uma função chamada `cadastrar_livro(id)` em que: *[EXIGÊNCIA DE CÓDIGO 3 de 8];*
  - Pergunta **nome, autor, editora** do livro;
  - Armazena o **id** (este é fornecido via parâmetro da função), **nome, autor, editora** dentro de um dicionário;
  - **Copiar** o dicionário para dentro da **lista_livro**;
<br>
- Deve-se implementar uma função chamada `consultar_livro()` em que: *[EXIGÊNCIA DE CÓDIGO 4 de 8];*
  - Deve-se perguntar qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Autor / 4. Retornar ao menu):
    - Se Consultar Todos, apresentar todos os livros com todos os seus dados cadastrados;
    - Se Consultar por Id, apresentar o livro específico com todos os seus dados cadastrados;
    - Se Consultar por Autor, apresentar o(s) livro(s) do autor com todos os seus dados cadastrados;
    - Se Retornar ao menu, deve-se retornar ao menu principal;
    - Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta **D.a.**
    - Enquanto o usuário não escolher a opção 4, o menu consultar livros deve se repetir.
<br>
- Deve-se implementar uma função chamada `remover_livro()` em que: *[EXIGÊNCIA DE CÓDIGO 5 de 8];*
  - Deve-se pergunta pelo **id** do livro a ser removido;
  - Remover o livro da **lista_livro**;
  - Se o id fornecido não for de um livro da lista, printar “Id inválido” e repetir a pergunta **E.a.**
<br>
- Deve-se implementar uma estrutura de menu no código principal (**main**), ou seja, não pode estar dentro de função, em que: *[EXIGÊNCIA DE CÓDIGO 6 de 8];*
  -  Deve-se pergunta qual opção deseja (1. Cadastrar Livro / 2. Consultar Livro / 3. Remover Livro / 4. Encerrar Programa):
<br>
- Se Cadastrar Livro, acrescentar em um **id_ global** e chamar a função `cadastrar_livro(id_ global)`;
  - Se Consultar Livro, chamar função **`consultar_livro();`**
  - Se Remover Livro, chamar função **`remover_livro();`**
  - Se Encerrar Programa, sair do menu (e com isso acabar a execução do código);
  - Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta **F.a.**
  - Enquanto o usuário não escolher a opção 4, o menu deve se repetir.
<br>
- Deve-se implementar uma **lista de dicionários** (uma lista contento dicionários dentro) *[EXIGÊNCIA DE CÓDIGO 7 de 8];*
<br>
- Deve-se inserir comentários <u>relevantes</u> no código *[EXIGÊNCIA DE CÓDIGO 8 de 8];*
<br>
- Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome *[EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 6];*
<br>
- Deve-se apresentar na saída de console um cadastro de 3 livros (sendo 2 deles no mesmo autor) *[EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 6];*
<br>
- Deve-se apresentar na saída de console uma consulta de todos os livros *[EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 6];*
<br>
- Deve-se apresentar na saída de console uma consulta por código (id) de um dos livros *[EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 6];*
<br>
- Deve-se apresentar na saída de console uma consulta por autor em que 2 livros sejam do mesmo autor *[EXIGÊNCIA DE SAÍDA DE CONSOLE 5 de 6];*
<br>
- Deve-se apresentar na saída de console uma remoção de um dos livros seguida de uma consulta de todos os livros *[EXIGÊNCIA DE SAÍDA DE CONSOLE 6 de 6];*
