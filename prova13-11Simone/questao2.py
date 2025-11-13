#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simulador de Caixa Eletrônico
Programa que simula um caixa eletrônico com saque de notas de 10, 20 e 50 reais.
"""

def validar_valor(valor):
    """
    Valida se o valor é um múltiplo de 10.
    
    Args:
        valor (int): valor a ser validado
        
    Returns:
        bool: True se válido, False caso contrário
    """
    return valor > 0 and valor % 10 == 0


def calcular_notas(valor):
    """
    Calcula a quantidade de notas necessárias para sacar o valor.
    Prioriza notas maiores (50, depois 20, depois 10).
    
    Args:
        valor (int): valor a sacar (deve ser múltiplo de 10)
        
    Returns:
        dict: dicionário com as quantidades de cada nota
    """
    notas = {
        50: 0,
        20: 0,
        10: 0
    }
    
    # Priorizar notas de 50
    notas[50] = valor // 50
    valor %= 50
    
    # Depois notas de 20
    notas[20] = valor // 20
    valor %= 20
    
    # Finalmente notas de 10
    notas[10] = valor // 10
    
    return notas


def exibir_resultado(valor_original, notas):
    """
    Exibe o resultado do saque de forma formatada.
    
    Args:
        valor_original (int): valor original solicitado
        notas (dict): dicionário com as quantidades de cada nota
    """
    print("\n" + "="*50)
    print(f"{'SAQUE APROVADO':^50}")
    print("="*50)
    print(f"Valor solicitado: R$ {valor_original:.2f}")
    print("\nNotas entregues:")
    
    if notas[50] > 0:
        print(f"  • {notas[50]} nota(s) de R$ 50,00 = R$ {notas[50] * 50:.2f}")
    if notas[20] > 0:
        print(f"  • {notas[20]} nota(s) de R$ 20,00 = R$ {notas[20] * 20:.2f}")
    if notas[10] > 0:
        print(f"  • {notas[10]} nota(s) de R$ 10,00 = R$ {notas[10] * 10:.2f}")
    
    total = (notas[50] * 50) + (notas[20] * 20) + (notas[10] * 10)
    total_notas = notas[50] + notas[20] + notas[10]
    
    print(f"\nTotal de notas: {total_notas}")
    print(f"Total em dinheiro: R$ {total:.2f}")
    print("="*50 + "\n")


def main():
    """Função principal que executa o simulador de caixa eletrônico."""
    print("\n" + "="*50)
    print(f"{'BEM-VINDO AO CAIXA ELETRÔNICO':^50}")
    print("="*50)
    print("\nNotas disponíveis: R$ 10, R$ 20 e R$ 50")
    print("O valor deve ser múltiplo de 10.\n")
    
    while True:
        try:
            # Ler o valor desejado
            entrada = input("Digite o valor que deseja sacar (ou 'sair' para encerrar): ").strip()
            
            # Opção para sair
            if entrada.lower() in ['sair', 'exit', 'q']:
                print("\nObrigado por usar nosso caixa eletrônico. Até logo!\n")
                break
            
            # Converter para inteiro
            valor = int(entrada)
            
            # Validar o valor
            if not validar_valor(valor):
                print("\n" + "!"*50)
                print(f"{'ERRO: VALOR INVÁLIDO':^50}")
                print("!"*50)
                print("O valor deve ser múltiplo de 10 e maior que zero.")
                print("Notas disponíveis: R$ 10, R$ 20 e R$ 50")
                print("!"*50 + "\n")
                continue
            
            # Calcular as notas
            notas = calcular_notas(valor)
            
            # Exibir resultado
            exibir_resultado(valor, notas)
        
        except ValueError:
            print("\n" + "!"*50)
            print(f"{'ERRO: ENTRADA INVÁLIDA':^50}")
            print("!"*50)
            print("Por favor, digite um número inteiro válido.")
            print("!"*50 + "\n")
        except KeyboardInterrupt:
            print("\n\nOperação cancelada pelo usuário. Até logo!\n")
            break
        except Exception as e:
            print(f"\nErro inesperado: {e}\n")


if __name__ == "__main__":
    main()
