# calculadora-simples
 Projeto de calculadora simples em python criado no modulo "Lógica de Programação com Python" do curso "Porfissão: Analista de Dados" da EBAC. É necessário ter o pacote de Python3 instalado, caso necessario, segue instrução de como instalá-lo no Windows: https://python.org.br/instalacao-windows/

Existem dois arquivos: 
  1) <<calculadora.sh>> trata-se de um shell script para ser executado em bash. Ele recebe nome do usuário como input e instrui o python a executar a calculadora. Ao final de uma utilização da calculadora, parabeniza o usuário.

    * Uma vez que o arquivo <<calculadora.sh>> tenha sido baixado, use o terminal para navegar até o diretório onde este se encontra e digite a linha de comando <<bash calculadora.sh>>. 

    * Caso haja erro, é possível executar o comando  <<chmod  u+rwx calculadora.sh>>, para conceder permissão de executar ao usuário.
     
  3) <<script_calculadora.py>> trata-se da calculadora. O programa tem tais passos:
      * Pede primeiro input numerico, transforma-o em float (numero Real).
           * Caso input não seja numérico, avisa e pede novo input
      * Informa as possibilidades de operações: + | - | * | / 
      * Pede input de operador.
           * Caso input não seja uma das 4 possibilidades, pede novamente 
      * Pede segundo input numerico, transforma-o em float (numero Real).
           * Caso input não seja numérico, avisa e pede novo input
      * Um conjunto de ifs vai gerar resultado diferentes das operações a depender do operador escolhido.
           * Resultado revela também nome da operação realizada. 
