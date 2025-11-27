#!/usr/bin/env python3
"""
ATIVIDADE: Desenvolvimento de App COnversor de Unidades Baseado em Componentes
NOME DO APP: iConvert
POR: Esthefison Souza

COMPONENTES:
- Componente 1 (UnitManager): Reutilizaando a biblioteca 'Pint'.
- Componente 2 (ConverterService): Desenvolvimento de lógica de negócios do zero.
"""

import click
from pint import UnitRegistry, errors
import sys

# SEÇÃO 1: COMPONENTE REUTILIZADO
# Biblioteca Base: Pint (https://pint.readthedocs.io/)

class UnitManager:
    """
    [COMPONENTE 1 - Reutilização]
    Responsável por gerenciar a instância única do registro de unidades (Sngleton).
    
    MOTIVO DA REUTILIZAÇÃO:
    Reutilizando aqui a biblioteca Pint que já possui milhares de definições físicas 
    ao invés de escrever as fórmulas fsicas de conversão do zero.
    
    PARA REUTILIZAR ESTE COMPONENTE:
    1. Copiar esta classe para um novo projeto.
    2. Chame `UnitManager.get_registry()` para obter o objeto central do Pint.
    3. Isso garante que o app compartilhe as mesmas configurações de unidades.
    """
    _registry = None

    @classmethod
    def get_registry(cls):
        """
        Retorna a instância única do UnitRegistry (Padrão Singleton).
        Configura a formatação padrão para 2 casas decimais evitando warnings (avisos).
        """
        if cls._registry is None:
            # Instancia da biblioteca externa Pint
            cls._registry = UnitRegistry()
            # Configuração para evitar DeprecationWarning e padronizar saída
            cls._registry.formatter.default_format = ".2f"
        return cls._registry


# SEÇÃO 2: COMPONENTE DESENVOLVIDO (LÓGICA DE NEGÓCIO)
# Desenvolvimento: Lógica própria


class ConverterService:
    """
    [COMPONENTE 2 - Desenvolvimento Próprio]
    Serviço que empacota a lógica de conversão, isolando a complexidade
    da biblioteca Pint e fornecendo tratamento de erros para ficar fácil de compreender.
    
        FUNCIONALIDADES:
        - Realiza conversões de float + unidade origem -> unidade destino.
        - Trata erros de dimensão (ex: quando tentamos converter metros em quilos).
        - Trata erros de unidades inexistentes.
    
        COMO REUTILIZAR ESTE COMPONENTE:
        Este componente não usa print() nem input().
        Pode ser importado em:
        - APIs Web
        - Apps Desktop
        - Scripts de automação de dados.
    """
    
    def __init__(self):
        # Acoplamento fraco: Usa o UnitManager para obter as definições
        self.ureg = UnitManager.get_registry()

    def convert(self, amount: float, from_unit: str, to_unit: str) -> str:
        """
        Método principal de conversão.
        Retorna uma string formatada com o sucesso ou a mensagem de erro.
        """
        try:
            # Cria a quantidade usando a definição do Pint
            quantity = amount * self.ureg(from_unit)
            
            # Realiza a conversão matmatica
            result = quantity.to(to_unit)
            
            return f"{amount} {from_unit} equivale a {result}"
        
        except errors.UndefinedUnitError:
            return f"Erro: Padrão de Unidade desconhecida ou com erro de digitação."
        except errors.DimensionalityError as e:
            return f"Erro de Dimensão: Impossível converter {e.units1} (Origem) para {e.units2} (Destino)."
        except ValueError:
            return "Erro: O valor inserido não é um número válido."
        except Exception as e:
            return f"Erro inesperado no sistema: {e}"


# SEÇÃO 3: INTERFACE DE LINHA DE COMANDO (CLI)
# Biblioteca Base: Click (https://click.palletsprojects.com/)


@click.group()
def cli():
    """
    App 'iConvert': Conversor de Unidades Modulável.
    Utiliza a biblioteca Click para gerenciar comandos e argumentos.
    """
    pass

@cli.command()
@click.argument('amount', type=float)
@click.argument('from_unit', type=str)
@click.argument('to_unit', type=str)
def converter(amount, from_unit, to_unit):
    """
    Comando para conversão direta (One-shot).
    Uso: python iConvert.py converter [VALOR] [ORIGEM] [DESTINO]
    """
    # Instancia do Componente de Serviço
    service = ConverterService()
    
    # Execução da lógica
    resultado = service.convert(amount, from_unit, to_unit)
    
    # Exibição (Camada de Apresentação)
    color = 'red' if "Erro" in resultado else 'green'
    click.secho(resultado, fg=color, bold=True)

@cli.command()
def interativo():
    """
    Inicia o modo interativo.
    Permite múltiplas conversões sem precisarmos reiniciar o programa.
    Uso: python iConvert.py interativo
    """
    service = ConverterService()
    
    click.clear() 
    click.secho("=== Conversor Interativo iConvert ===", fg='cyan', bold=True)
    click.secho("Digite 'quit', 'sair' ou 'exit' para encerrar.", fg='cyan')
    click.secho("Exemplo: converter 10 km m", fg='white', dim=True)
    click.secho("Ou direto: 10 km m\n", fg='white', dim=True)

    while True:
        try:
            command_text = input(click.style("iConvert> ", fg='yellow', bold=True))
            parts = command_text.strip().split()
            
            if not parts:
                continue

            # Critério de saída
            if parts[0].lower() in ['quit', 'sair', 'exit']:
                click.secho("Encerrando App iConvert. Até logo!", fg='cyan')
                break
            
            # Lógica de Parsing (Interpretação do comando)
            if parts[0] == 'converter':
                if len(parts) != 4:
                    click.secho("Erro: Use: converter [VALOR] [ORIGEM] [DESTINO]", fg='red')
                    continue
                amount, from_unit, to_unit = float(parts[1]), parts[2], parts[3]
                resultado = service.convert(amount, from_unit, to_unit)
                
            # Lógica Inteligente (Atalho: valor unidade unidade)
            elif len(parts) == 3 and parts[0].replace('.', '', 1).isdigit():
                amount, from_unit, to_unit = float(parts[0]), parts[1], parts[2]
                resultado = service.convert(amount, from_unit, to_unit)

            else:
                click.secho(f"Comando não reconhecido.", fg='red')
                continue

            # Feedback Visual
            color = 'red' if "Erro" in resultado else 'green'
            click.secho(f"Result: {resultado}", fg=color)

        except ValueError:
            click.secho("Erro: Certifique-se de que o valor é um número.", fg='red')
        except KeyboardInterrupt:
            print("\nSaindo forçadamente...")
            break

# Ponto de Entrada do Script
if __name__ == '__main__':
    cli()