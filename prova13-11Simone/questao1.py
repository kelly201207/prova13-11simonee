#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Login com Tentativas Limitadas
Programa que simula um sistema de login com bloqueio após 3 tentativas incorretas.
"""

import time
from datetime import datetime


# Credenciais pré-definidas
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "1234"
MAX_TENTATIVAS = 3


def exibir_cabecalho():
    """Exibe o cabeçalho do sistema."""
    print("\n" + "="*60)
    print(f"{'SISTEMA DE LOGIN':^60}")
    print("="*60 + "\n")


def exibir_tabela_referencia():
    """Exibe as credenciais de teste (para fins demonstrativos)."""
    print("-"*60)
    print("CREDENCIAIS PARA TESTE:")
    print("-"*60)
    print(f"Usuário: {USUARIO_CORRETO}")
    print(f"Senha: {SENHA_CORRETA}")
    print("-"*60 + "\n")


def validar_login(usuario, senha):
    """
    Valida as credenciais de login.
    
    Args:
        usuario (str): usuário inserido
        senha (str): senha inserida
        
    Returns:
        bool: True se credenciais estão corretas, False caso contrário
    """
    return usuario == USUARIO_CORRETO and senha == SENHA_CORRETA


def exibir_tentativa_restante(tentativas_restantes):
    """
    Exibe mensagem sobre tentativas restantes.
    
    Args:
        tentativas_restantes (int): número de tentativas restantes
    """
    if tentativas_restantes > 0:
        if tentativas_restantes == 1:
            print(f"\n⚠️  AVISO: Você tem apenas {tentativas_restantes} tentativa restante!")
        else:
            print(f"\n⚠️  Tentativas restantes: {tentativas_restantes}")
    else:
        print("\n❌ ERRO: Tentativas esgotadas!")


def exibir_sucesso():
    """Exibe mensagem de login bem-sucedido."""
    print("\n" + "="*60)
    print(f"{'✅ LOGIN REALIZADO COM SUCESSO!':^60}")
    print("="*60)
    print(f"Bem-vindo, {USUARIO_CORRETO}!")
    print(f"Data e hora do acesso: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("="*60 + "\n")


def exibir_bloqueio():
    """Exibe mensagem de conta bloqueada."""
    print("\n" + "="*60)
    print(f"{'❌ CONTA BLOQUEADA':^60}")
    print("="*60)
    print("Você excedeu o número máximo de tentativas.")
    print("A conta foi temporariamente bloqueada por segurança.")
    print(f"Data e hora do bloqueio: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("="*60 + "\n")


def ler_credenciais():
    """
    Lê as credenciais do usuário.
    
    Returns:
        tuple: (usuário, senha) inseridos
    """
    usuario = input("Usuário: ").strip()
    senha = input("Senha: ").strip()
    return usuario, senha


def main():
    """Função principal que executa o sistema de login."""
    exibir_cabecalho()
    exibir_tabela_referencia()
    
    tentativas_restantes = MAX_TENTATIVAS
    bloqueado = False
    
    while tentativas_restantes > 0:
        print(f"Tentativa {MAX_TENTATIVAS - tentativas_restantes + 1}/{MAX_TENTATIVAS}\n")
        
        try:
            # Ler credenciais
            usuario, senha = ler_credenciais()
            
            # Validar credenciais
            if validar_login(usuario, senha):
                exibir_sucesso()
                # Opção de fazer novo login
                opcao = input("Deseja fazer logout e sair? (s/n): ").strip().lower()
                if opcao in ['s', 'sim', 'y', 'yes']:
                    print("Desconectando... Até logo!\n")
                    break
                else:
                    tentativas_restantes = MAX_TENTATIVAS
                    print("Retornando ao login...\n")
            else:
                # Credenciais incorretas
                tentativas_restantes -= 1
                print("\n❌ Usuário ou senha incorretos!")
                exibir_tentativa_restante(tentativas_restantes)
                
                if tentativas_restantes > 0:
                    time.sleep(1)  # Pequeno delay para segurança
                    print()
        
        except KeyboardInterrupt:
            print("\n\nOperação cancelada pelo usuário. Até logo!\n")
            break
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}\n")
    
    # Se esgotou as tentativas
    if tentativas_restantes == 0:
        bloqueado = True
        exibir_bloqueio()
        
        # Opção para tentar desbloquear (simulação)
        print("Opções:")
        print("1. Tentar novamente (simula reset de segurança)")
        print("2. Sair")
        
        opcao = input("\nDigite sua escolha (1 ou 2): ").strip()
        if opcao == '1':
            print("\nSolicitação de reset enviada para administrador.")
            print("Redirecionando para a tela de login...\n")
            tentativas_restantes = MAX_TENTATIVAS
            bloqueado = False
            main()  # Reinicia o login
        else:
            print("\nPrograma encerrado. Até logo!\n")


if __name__ == "__main__":
    main()
