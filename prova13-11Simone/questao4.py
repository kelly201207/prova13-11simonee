#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Tabuada com Intervalo
Programa que lê um número inteiro e um intervalo, exibindo a tabuada do número nesse intervalo.
"""

def ler_numero():
    """
    Lê um número inteiro do usuário.
    
    Returns:
        int: número inteiro inserido pelo usuário
    """
    while True:
        try:
            numero = int(input("Digite um número inteiro para a tabuada: ").strip())
            return numero
        except ValueError:
            print("❌ ERRO: Por favor, digite um número inteiro válido.\n")


def ler_intervalo():
    """
    Lê o intervalo (início e fim) do usuário.
    
    Returns:
        tuple: (início, fim) do intervalo
    """
    while True:
        try:
            inicio = int(input("Digite o início do intervalo: ").strip())
            fim = int(input("Digite o fim do intervalo: ").strip())
            
            if inicio > fim:
                print("❌ ERRO: O início deve ser menor ou igual ao fim!\n")
                continue
            
            return inicio, fim
        except ValueError:
            print("❌ ERRO: Por favor, digite números inteiros válidos.\n")


def exibir_tabuada(numero, inicio, fim):
    """
    Exibe a tabuada do número dentro do intervalo especificado.
    
    Args:
        numero (int): número para o qual calcular a tabuada
        inicio (int): início do intervalo
        fim (int): fim do intervalo
    """
    print("\n" + "="*60)
    print(f"{'TABUADA DO ' + str(numero):^60}")
    print(f"{'(de ' + str(inicio) + ' a ' + str(fim) + ')':^60}")
    print("="*60 + "\n")
    
    for i in range(inicio, fim + 1):
        resultado = numero * i
        print(f"{numero:4d} × {i:4d} = {resultado:6d}")
    
    print("\n" + "="*60 + "\n")


def formatar_tabuada_tabela(numero, inicio, fim):
    """
    Exibe a tabuada em formato de tabela.
    
    Args:
        numero (int): número para o qual calcular a tabuada
        inicio (int): início do intervalo
        fim (int): fim do intervalo
    """
    print("\n" + "="*60)
    print(f"{'TABUADA DO ' + str(numero) + ' (Formato Tabela)':^60}")
    print("="*60)
    
    # Cabeçalho
    print(f"{'Multiplicador':<15} {'×':<3} {'Número':<15} {'=':<3} {'Resultado':<15}")
    print("-"*60)
    
    # Dados
    for i in range(inicio, fim + 1):
        resultado = numero * i
        print(f"{i:<15} {'×':<3} {numero:<15} {'=':<3} {resultado:<15}")
    
    print("="*60 + "\n")


def menu_opcoes():
    """
    Exibe um menu com opções de formatação.
    
    Returns:
        str: opção escolhida pelo usuário
    """
    print("\nEscolha o formato de exibição:")
    print("1. Formato padrão (um resultado por linha)")
    print("2. Formato tabela")
    print("3. Ambos")
    
    while True:
        opcao = input("\nDigite sua escolha (1, 2 ou 3): ").strip()
        if opcao in ['1', '2', '3']:
            return opcao
        print("❌ ERRO: Opção inválida! Digite 1, 2 ou 3.\n")


def main():
    """Função principal que executa o gerador de tabuada."""
    print("\n" + "="*60)
    print(f"{'GERADOR DE TABUADA COM INTERVALO':^60}")
    print("="*60 + "\n")
    
    while True:
        # Ler número
        numero = ler_numero()
        
        # Ler intervalo
        inicio, fim = ler_intervalo()
        
        # Menu de opções
        opcao = menu_opcoes()
        
        # Exibir tabuada conforme opção
        if opcao == '1':
            exibir_tabuada(numero, inicio, fim)
        elif opcao == '2':
            formatar_tabuada_tabela(numero, inicio, fim)
        elif opcao == '3':
            exibir_tabuada(numero, inicio, fim)
            formatar_tabuada_tabela(numero, inicio, fim)
        
        # Pergunta se deseja continuar
        continuar = input("Deseja calcular a tabuada de outro número? (s/n): ").strip().lower()
        if continuar not in ['s', 'sim', 'y', 'yes']:
            print("\nObrigado por usar o gerador de tabuada. Até logo!\n")
            break


if __name__ == "__main__":
    main()
