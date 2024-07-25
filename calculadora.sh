#!/bin/bash
#Aqui saberemos o nome do usuário

echo "digite seu primeiro nome"
read primeiro_nome
echo "bem vindx, $primeiro_nome"

#Aqui se inicia a calculadora
echo -e "\niniciando a calculadora"
python3 script_calculadora.py

echo -e "\nparabéns, $primeiro_nome, você usou a calculadora"
