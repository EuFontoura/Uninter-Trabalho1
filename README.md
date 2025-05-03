<h2>QUESTÃO 1 de 4 – Conteúdos até Aula 3</h2>
<b>Enunciado:</b> Imagina-se que você é um dos programadores responsáveis pela construção de um app de vendas para uma determinada empresa X que vende em atacado. Uma das estratégias de vendas dessa empresa X é dar desconto maior conforme o valor da compra, conforme a <b>listagem abaixo:</b>

Se valor for <b>menor</b> que 2500 o desconto será de 0%;<br>
Se valor for <b>igual ou maior</b> que 2500 e <b>menor</b>que 6000 o desconto será de 4%;<br>
Se valor for <b>igual ou maior</b> que 6000 e <b>menor </b>que 10000 o desconto será de 7%;<br>
Se valor for <b>igual ou maior</b> que 10000 o desconto será de 11%;<br>

<b>Elabore um programa em Python que:</b><br><br>

1 - Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu <b>nome e sobrenome</b><i> [EXIGÊNCIA DE CÓDIGO 1 de 6];</i><br><br>

2 - Deve-se implementar o input do <b>valor unitário</b> e <b>da quantidade do produto</b> <i>[EXIGÊNCIA DE CÓDIGO 2 de 6];</i><br><br>

Deve-se implementar o desconto <b>conforme a enunciado acima </b>(obs.: atente-se as condições de menor, igual e maior) <i>[EXIGÊNCIA DE CÓDIGO 3 de 6];</i><br><br>

3 - Deve-se implementar o <b>valor total sem desconto</b> e o <b>valor total com desconto</b> <i>[EXIGÊNCIA DE CÓDIGO 4 de 6];</i><br><br>

4 - Deve-se implementar as estruturas <b>if, elif e else (todas elas)</b> <i>[EXIGÊNCIA DE CÓDIGO 5 de 6];  </i><br><br>

5 - Deve-se inserir comentários <u>relevantes</u> no código <i>[EXIGÊNCIA DE CÓDIGO 6 de 6];</i><br><br>

6 - Deve-se apresentar na saída de console uma mensagem de boas-vindas com seu nome <i>[EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 2];</i><br><br>

7 - Deve-se apresentar na saída de console um pedido recebendo desconto (<b>valor total sem desconto</b> maior ou igual a 2500) <i>[EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 2];  </i><br>

<hr>

<h2>QUESTÃO 2 de 4 - Conteúdo até aula 04</h2>
<b>Enunciado:</b> Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma loja que vende Açaí e Cupuaçu. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.<br>
A Loja possui seguinte relação:<br><br>

<ul>
<li>Tamanho <b>P</b> de Cupuaçu <b>(CP)</b> custa 9 reais e o Açaí <b>(AC)</b> custa 11 reais;</li>
<li>Tamanho <b>M</b> de Cupuaçu <b>(CP)</b> custa 14 reais e o Açaí <b>(AC)</b> custa 16 reais;</li>
<li>Tamanho <b>G</b> de Cupuaçu <b>(CP)</b> custa 18 reais e o Açaí <b>(AC)</b> custa 20 reais;</li>
</ul>

<b>Elabore um programa em Python que: </b><br><br>

1 - Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu <b>nome e sobrenome</b> <i>[EXIGÊNCIA DE CÓDIGO 1 de 8];</i><br><br>

2 - Deve-se implementar o input do <b>sabor</b> (CP/AC) e o print “Sabor inválido. Tente novamente" se o usuário entra com valor diferente de CP e AC <i>[EXIGÊNCIA DE CÓDIGO 2 de 8];</i><br><br>

3 - Deve-se implementar o input do <b>tamanho</b> (P/M/G) e o print “Tamanho inválido. Tente novamente" se o usuário com entra valor diferente de P, M ou G <i>[EXIGÊNCIA DE CÓDIGO 3 de 8];</i><br><br>

4 - Deve-se implementar if, elif e/ou else, utilizando o modelo <b>aninhado</b> (aula 3 – Tema 4) com cada uma das combinações de <b>sabor</b> e <b>tamanho</b> <i>[EXIGÊNCIA DE CÓDIGO 4 de 8];</i><br><br>

5 - Deve-se implementar um <b>acumulador</b> para somar os valores dos pedidos <i>[EXIGÊNCIA DE CÓDIGO 5 de 8];</i><br><br>

6 - Deve-se implementar o input com a pergunta: “Deseja pedir mais alguma coisa?”. Se sim <b>repetir a partir do item B</b>, senão encerrar o programa executar o print do acumulador <i>[EXIGÊNCIA DE CÓDIGO 6 de 8];</i><br><br>

7 - Deve-se implementar as estruturas de <b>while, break, continue (todas elas)</b> <i>[EXIGÊNCIA DE CÓDIGO 7 de 8];</i><br><br>

8 - Deve-se inserir comentários <u>relevantes</u> no código <i>[EXIGÊNCIA DE CÓDIGO 8 de 8];</i><br><br>

9 - Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome <i>[EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];</i><br><br>

10 - Deve-se apresentar na saída de console um pedido em que o usuário errou o <b>sabor</b> <i>[EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4]; </i><br><br>

11 - Deve-se apresentar na saída de console um pedido em que o usuário errou o <b>tamanho</b> <i>[EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];</i><br><br>

12 - Deve-se apresentar na saída de console um pedido com duas opções sabores diferentes e com tamanhos diferentes <i>[EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4]; </i><br>

<hr>

<h2>QUESTÃO 3 de 4 - Conteúdo até aula 05</h2>
<b>Enunciado:</b> Você foi contratado para desenvolver um sistema de cobrança de serviços de uma copiadora. Você ficou com a parte de desenvolver a interface com o funcionário.<br>
A copiadora opera da seguinte maneira:<br><br>

<ul>
<li>Serviço de Digitalização (DIG) o custo por página é de um real e dez centavos;</li>
<li>Serviço de Impressão Colorida (ICO) o custo por página é de um real;</li>
<li>Serviço de Impressão Preto e Branco (IPB) o custo por página é de quarenta centavos;</li>
<li>Serviço de Fotocópia (FOT) o custo por página é de vinte centavos;</li>
</ul>

<ul>
<li>Se número de páginas for <b>menor</b> que 20 retornar o número de página sem desconto;</li>
<li>Se número de páginas for <b>igual ou maior</b> que 20 e <b>menor</b> que 200 retornar o número de páginas com o desconto é de 15%;</li>
<li>Se número de páginas for <b>igual ou maior</b> que 200 e <b>menor</b> que 2000 retornar o número de páginas com o desconto é de 20%;</li>
<li>Se número de páginas for <b>igual ou maior</b> que 2000 e <b>menor</b> que 20000 retornar o número de páginas com o desconto é de 25%;</li>
<li>Se número de páginas for <b>maior ou igual</b> à 20000 não é aceito pedidos nessa quantidade de páginas;</li>
</ul>

<ul>
<li>Para o <b>adicional</b> de encadernação simples (1) é cobrado um valor <b>extra</b> de 15 reais;</li>
<li>Para o <b>adicional</b> de encadernação de capa dura (2) é cobrado um valor <b>extra</b> de 40 reais;</li>
<li>Para o <b>adicional</b> de não querer mais nada (0) é cobrado um valor <b>extra</b> de 0 reais;</li>
</ul>

<p>O valor final da conta é calculado da seguinte maneira:</p>

<center>total = <b>(servico * num_pagina) + extra</b></center><br>

<b>Elabore um programa em Python que: </b><br><br>

<ul>
<li>Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome <i>[EXIGÊNCIA DE CÓDIGO 1 de 7];</i></li>
<li>Deve-se implementar a função <code>escolha_servico()</code> em que: <i>[EXIGÊNCIA DE CÓDIGO 2 de 7];</i><br>
  - Pergunta o <b>serviço</b> desejado;<br>
  - Retorna o valor <b>serviço</b> com base na escolha do usuário;<br>
  - Repete a pergunta do item <b>B.a</b> se digitar uma opção diferente de: dig/ico/ipb/fot;<br>
</li>
<li>Deve-se implementar a função <code>num_pagina()</code> em que: <i>[EXIGÊNCIA DE CÓDIGO 3 de 7];</i><br>
  - Pergunta o <b>número de páginas;</b><br>
  - Retorna o <b>número de páginas</b> com desconto seguindo a regra do enunciado (desconto calculado em cima do número de páginas);<br>
  - Repete a pergunta do item <b>C.a</b> se digitar um valor acima de 20000 ou valor não numérico (use try/except para não numérico)<br>
</li>
<li>Deve-se implementar a função <code>servico_extra()</code> em que: <i>[EXIGÊNCIA DE CÓDIGO 4 de 7];</i><br>
  - Pergunta pelo serviço <b>adicional;</b><br>
  - Retornar o valor de apenas uma das <b>opções</b> de <b>adicional</b><br>
  - Repetir a pergunta item <b>D.a</b> se digitar uma opção diferente de: 1/2/0;<br>
</li>
<li>Deve-se implementar o total a pagar no código principal (<b>main</b>), ou seja, não pode estar dentro de função, conforme o enunciado <i>[EXIGÊNCIA DE CÓDIGO 5 de 7];</i></li>
<li>Deve-se implementar <b>try/except</b> <i>[EXIGÊNCIA DE CÓDIGO 6 de 7];</i></li>
<li>Deve-se inserir comentários <u>relevantes</u> no código <i>[EXIGÊNCIA DE CÓDIGO 7 de 7];</i></li>
</ul>

<ul>
<li>Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome <i>[EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];</i></li>
<li>Deve-se apresentar na saída de console um pedido no qual o usuário errou a opção de serviço <i>[EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4];</i></li>
<li>Deve-se apresentar na saída de console um pedido no qual o usuário digitou ultrapassou no número de páginas <i>[EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];</i></li>
<li>Deve-se apresentar na saída de console um pedido com opção de serviço, número de páginas e serviço extra válidos <i>[EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];</i></li>
</ul>

<hr>

<h2>QUESTÃO 4 de 4 - Conteúdo até aula 06</h2>

<p><strong>Enunciado:</strong> Você e sua equipe de programadores foram contratados por pequena empresa para desenvolver o software de gerenciamento de livros. Este software deve ter o seguinte menu e opções:</p>
<ul>
  <li>Cadastrar Livro</li>
  <li>Consultar Livro
    <ul>
      <li>Consultar Todos</li>
      <li>Consultar por Id</li>
      <li>Consultar por Autor</li>
    </ul>
  </li>
  <li>Retornar ao menu</li>
  <li>Remover Livro</li>
  <li>Encerrar Programa</li>
</ul>

<p><strong>Elabore um programa em Python que:</strong></p>

<ul>
  <li>Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome <em>[EXIGÊNCIA DE CÓDIGO 1 de 8];</em></li>
  <li>Deve-se implementar uma lista vazia com o nome de <strong>lista_livro</strong> e a variável id_global com valor inicial igual a 0 <em>[EXIGÊNCIA DE CÓDIGO 2 de 8];</em></li>
  <li>Deve-se implementar uma função chamada <code>cadastrar_livro(id)</code> em que: <em>[EXIGÊNCIA DE CÓDIGO 3 de 8];</em>
    <ul>
      <li>Pergunta <strong>nome, autor, editora</strong> do livro;</li>
      <li>Armazena o <strong>id</strong> (este é fornecido via parâmetro da função), <strong>nome, autor, editora</strong> dentro de um dicionário;</li>
      <li><strong>Copiar</strong> o dicionário para dentro da <strong>lista_livro</strong>;</li>
    </ul>
  </li>
  <li>Deve-se implementar uma função chamada <code>consultar_livro()</code> em que: <em>[EXIGÊNCIA DE CÓDIGO 4 de 8];</em>
    <ul>
      <li>Deve-se perguntar qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Autor / 4. Retornar ao menu):</li>
      <li>Se Consultar Todos, apresentar todos os livros com todos os seus dados cadastrados;</li>
      <li>Se Consultar por Id, apresentar o livro específico com todos os seus dados cadastrados;</li>
      <li>Se Consultar por Autor, apresentar o(s) livro(s) do autor com todos os seus dados cadastrados;</li>
      <li>Se Retornar ao menu, deve-se retornar ao menu principal;</li>
      <li>Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta <strong>D.a.</strong></li>
      <li>Enquanto o usuário não escolher a opção 4, o menu consultar livros deve se repetir.</li>
    </ul>
  </li>
  <li>Deve-se implementar uma função chamada <code>remover_livro()</code> em que: <em>[EXIGÊNCIA DE CÓDIGO 5 de 8];</em>
    <ul>
      <li>Deve-se pergunta pelo <strong>id</strong> do livro a ser removido;</li>
      <li>Remover o livro da <strong>lista_livro</strong>;</li>
      <li>Se o id fornecido não for de um livro da lista, printar “Id inválido” e repetir a pergunta <strong>E.a.</strong></li>
    </ul>
  </li>
  <li>Deve-se implementar uma estrutura de menu no código principal (<strong>main</strong>), ou seja, não pode estar dentro de função, em que: <em>[EXIGÊNCIA DE CÓDIGO 6 de 8];</em>
    <ul>
      <li>Deve-se pergunta qual opção deseja (1. Cadastrar Livro / 2. Consultar Livro / 3. Remover Livro / 4. Encerrar Programa):</li>
      <li>Se Cadastrar Livro, acrescentar em um <strong>id_ global</strong> e chamar a função <code>cadastrar_livro(id_ global)</code>;</li>
      <li>Se Consultar Livro, chamar função <strong><code>consultar_livro();</code></strong></li>
      <li>Se Remover Livro, chamar função <strong><code>remover_livro();</code></strong></li>
      <li>Se Encerrar Programa, sair do menu (e com isso acabar a execução do código);</li>
      <li>Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta <strong>F.a.</strong></li>
      <li>Enquanto o usuário não escolher a opção 4, o menu deve se repetir.</li>
    </ul>
  </li>
  <li>Deve-se implementar uma <strong>lista de dicionários</strong> (uma lista contento dicionários dentro) <em>[EXIGÊNCIA DE CÓDIGO 7 de 8];</em></li>
  <li>Deve-se inserir comentários <u>relevantes</u> no código <em>[EXIGÊNCIA DE CÓDIGO 8 de 8];</em></li>
  <li>Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome <em>[EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 6];</em></li>
  <li>Deve-se apresentar na saída de console um cadastro de 3 livros (sendo 2 deles no mesmo autor) <em>[EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 6];</em></li>
  <li>Deve-se apresentar na saída de console uma consulta de todos os livros <em>[EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 6];</em></li>
  <li>Deve-se apresentar na saída de console uma consulta por código (id) de um dos livros <em>[EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 6];</em></li>
  <li>Deve-se apresentar na saída de console uma consulta por autor em que 2 livros sejam do mesmo autor <em>[EXIGÊNCIA DE SAÍDA DE CONSOLE 5 de 6];</em></li>
  <li>Deve-se apresentar na saída de console uma remoção de um dos livros seguida de uma consulta de todos os livros <em>[EXIGÊNCIA DE SAÍDA DE CONSOLE 6 de 6];</em></li>
</ul>

