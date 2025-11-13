#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora de Índice de Massa Corporal (IMC)
Programa que calcula o IMC e classifica o resultado conforme tabela da OMS.
"""

def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC).
    
    Args:
        peso (float): peso em quilogramas
        altura (float): altura em metros
        
    Returns:
        float: valor do IMC calculado
    """
    if altura <= 0 or peso <= 0:
        return None
    return peso / (altura * altura)


def classificar_imc(imc):
    """
    Classifica o IMC conforme tabela da OMS.
    
    Args:
        imc (float): valor do IMC
        
    Returns:
        str: classificação do IMC
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25.0:
        return "Peso normal"
    elif imc < 30.0:
        return "Sobrepeso"
    else:
        return "Obesidade"


def obter_cor_classificacao(classificacao):
    """
    Retorna uma cor/ícone para visual na classificação.
    
    Args:
        classificacao (str): classificação do IMC
        
    Returns:
        str: símbolo ou descrição de cor
    """
    cores = {
        "Abaixo do peso": "🔵",
        "Peso normal": "🟢",
        "Sobrepeso": "🟡",
        "Obesidade": "🔴"
    }
    return cores.get(classificacao, "⚪")


def exibir_resultado(peso, altura, imc, classificacao):
    """
    Exibe o resultado do cálculo de IMC de forma formatada.
    
    Args:
        peso (float): peso em kg
        altura (float): altura em metros
        imc (float): valor do IMC
        classificacao (str): classificação do IMC
    """
    cor = obter_cor_classificacao(classificacao)
    
    print("\n" + "="*60)
    print(f"{'RESULTADO DO CÁLCULO DE IMC':^60}")
    print("="*60)
    print(f"Peso: {peso:.2f} kg")
    print(f"Altura: {altura:.2f} m")
    print(f"\nIMC: {imc:.2f}")
    print(f"\nClassificação: {cor} {classificacao}")
    print("="*60 + "\n")


def exibir_tabela_referencia():
    """Exibe a tabela de referência de classificação do IMC."""
    print("\n" + "-"*60)
    print(f"{'TABELA DE REFERÊNCIA DE IMC':^60}")
    print("-"*60)
    print("Classificação          | IMC (kg/m²)")
    print("-"*60)
    print("Abaixo do peso         | Menor que 18,5")
    print("Peso normal            | 18,5 a 24,9")
    print("Sobrepeso              | 25,0 a 29,9")
    print("Obesidade              | 30,0 ou mais")
    print("-"*60 + "\n")


def main():
    """Função principal que executa a calculadora de IMC."""
    print("\n" + "="*60)
    print(f"{'CALCULADORA DE ÍNDICE DE MASSA CORPORAL (IMC)':^60}")
    print("="*60)
    
    exibir_tabela_referencia()
    
    while True:
        try:
            # Ler altura
            entrada_altura = input("Digite sua altura em metros (ou 'sair' para encerrar): ").strip()
            
            # Opção para sair
            if entrada_altura.lower() in ['sair', 'exit', 'q']:
                print("\nObrigado por usar a calculadora de IMC. Até logo!\n")
                break
            
            # Converter altura para float
            altura = float(entrada_altura)
            
            # Validar altura
            if altura <= 0 or altura > 3:
                print("\n" + "!"*60)
                print("ERRO: Altura inválida!")
                print("Por favor, digite uma altura válida em metros (ex: 1.75)")
                print("!"*60 + "\n")
                continue
            
            # Ler peso
            entrada_peso = input("Digite seu peso em quilogramas: ").strip()
            
            # Converter peso para float
            peso = float(entrada_peso)
            
            # Validar peso
            if peso <= 0 or peso > 500:
                print("\n" + "!"*60)
                print("ERRO: Peso inválido!")
                print("Por favor, digite um peso válido em kg (ex: 70.5)")
                print("!"*60 + "\n")
                continue
            
            # Calcular IMC
            imc = calcular_imc(peso, altura)
            
            # Classificar IMC
            classificacao = classificar_imc(imc)
            
            # Exibir resultado
            exibir_resultado(peso, altura, imc, classificacao)
            
            # Perguntar se deseja calcular novamente
            continuar = input("Deseja calcular o IMC de outra pessoa? (s/n): ").strip().lower()
            if continuar not in ['s', 'sim', 'y', 'yes']:
                print("\nObrigado por usar a calculadora de IMC. Até logo!\n")
                break
        
        except ValueError:
            print("\n" + "!"*60)
            print("ERRO: Entrada inválida!")
            print("Por favor, digite números válidos (use ponto ou vírgula para decimais).")
            print("Exemplo: altura 1.75, peso 70.5")
            print("!"*60 + "\n")
        except KeyboardInterrupt:
            print("\n\nOperação cancelada pelo usuário. Até logo!\n")
            break
        except Exception as e:
            print(f"\nErro inesperado: {e}\n")


if __name__ == "__main__":
    main()
