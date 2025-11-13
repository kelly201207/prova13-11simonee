#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analisador de Números
Programa que lê 8 números inteiros e analisa suas propriedades (pares, ímpares, positivos, negativos, maior, menor).
"""


def ler_numeros(quantidade=8):
    """
    Lê uma quantidade específica de números inteiros do usuário.
    
    Args:
        quantidade (int): quantidade de números a ler (padrão: 8)
        
    Returns:
        list: lista com os números inteiros lidos
    """
    numeros = []
    print(f"Digite {quantidade} números inteiros:\n")
    
    for i in range(1, quantidade + 1):
        while True:
            try:
                numero = int(input(f"Número {i}: ").strip())
                numeros.append(numero)
                break
            except ValueError:
                print("❌ ERRO: Por favor, digite um número inteiro válido.\n")
    
    return numeros


def analisar_numeros(numeros):
    """
    Analisa os números e calcula estatísticas.
    
    Args:
        numeros (list): lista de números inteiros
        
    Returns:
        dict: dicionário com as estatísticas calculadas
    """
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0
    
    for numero in numeros:
        # Contar pares e ímpares
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        
        # Contar positivos e negativos
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
    
    # Encontrar maior e menor
    maior = max(numeros)
    menor = min(numeros)
    
    return {
        'pares': pares,
        'impares': impares,
        'positivos': positivos,
        'negativos': negativos,
        'maior': maior,
        'menor': menor,
        'quantidade': len(numeros)
    }


def exibir_resultado(numeros, analise):
    """
    Exibe o resultado da análise de forma formatada.
    
    Args:
        numeros (list): lista de números analisados
        analise (dict): dicionário com as estatísticas
    """
    print("\n" + "="*70)
    print(f"{'ANÁLISE DOS NÚMEROS DIGITADOS':^70}")
    print("="*70)
    
    # Números digitados
    print("\n📊 NÚMEROS DIGITADOS:")
    print("-" * 70)
    numeros_formatados = " | ".join(str(n) for n in numeros)
    print(f"{numeros_formatados}")
    
    # Análise
    print("\n📈 ANÁLISE:")
    print("-" * 70)
    print(f"Quantidade de números:        {analise['quantidade']}")
    print(f"\n📍 CLASSIFICAÇÃO POR TIPO:")
    print(f"  • Números pares:            {analise['pares']:>3} ({'🟢' if analise['pares'] > 0 else '⚪'})")
    print(f"  • Números ímpares:          {analise['impares']:>3} ({'🟢' if analise['impares'] > 0 else '⚪'})")
    
    print(f"\n📍 CLASSIFICAÇÃO POR SINAL:")
    print(f"  • Números positivos:        {analise['positivos']:>3} ({'🟢' if analise['positivos'] > 0 else '⚪'})")
    print(f"  • Números negativos:        {analise['negativos']:>3} ({'🟢' if analise['negativos'] > 0 else '⚪'})")
    
    print(f"\n📍 EXTREMOS:")
    print(f"  • Maior número:             {analise['maior']:>3} 📈")
    print(f"  • Menor número:             {analise['menor']:>3} 📉")
    
    print("\n" + "="*70 + "\n")


def exibir_graficos(analise):
    """
    Exibe gráficos de barras simples com as estatísticas.
    
    Args:
        analise (dict): dicionário com as estatísticas
    """
    print("\n" + "="*70)
    print(f"{'GRÁFICOS':^70}")
    print("="*70)
    
    # Gráfico pares vs ímpares
    print("\n📊 Pares vs Ímpares:")
    max_val = max(analise['pares'], analise['impares'])
    escala = 30
    
    if max_val > 0:
        pares_barra = int((analise['pares'] / max_val) * escala)
        impares_barra = int((analise['impares'] / max_val) * escala)
    else:
        pares_barra = impares_barra = 0
    
    print(f"Pares    {'█' * pares_barra} {analise['pares']}")
    print(f"Ímpares  {'█' * impares_barra} {analise['impares']}")
    
    # Gráfico positivos vs negativos
    print("\n📊 Positivos vs Negativos:")
    max_val = max(analise['positivos'], analise['negativos'])
    
    if max_val > 0:
        positivos_barra = int((analise['positivos'] / max_val) * escala)
        negativos_barra = int((analise['negativos'] / max_val) * escala)
    else:
        positivos_barra = negativos_barra = 0
    
    print(f"Positivos {'█' * positivos_barra} {analise['positivos']}")
    print(f"Negativos {'█' * negativos_barra} {analise['negativos']}")
    
    print("\n" + "="*70 + "\n")


def main():
    """Função principal que executa o analisador de números."""
    print("\n" + "="*70)
    print(f"{'ANALISADOR DE NÚMEROS':^70}")
    print("="*70 + "\n")
    
    while True:
        try:
            # Ler 8 números
            numeros = ler_numeros(8)
            
            # Analisar números
            analise = analisar_numeros(numeros)
            
            # Exibir resultado
            exibir_resultado(numeros, analise)
            
            # Exibir gráficos
            exibir_graficos(analise)
            
            # Pergunta se deseja continuar
            continuar = input("Deseja analisar mais 8 números? (s/n): ").strip().lower()
            if continuar not in ['s', 'sim', 'y', 'yes']:
                print("\nObrigado por usar o analisador de números. Até logo!\n")
                break
            
            print()
        
        except KeyboardInterrupt:
            print("\n\nOperação cancelada pelo usuário. Até logo!\n")
            break
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}\n")


if __name__ == "__main__":
    main()
