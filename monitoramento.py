from colorama import Fore, Style, init

# Inicializa o colorama para garantir compatibilidade no terminal
init(autoreset=True)


def definir_cor_nivel(nivel):
  """Função responsável por retornar a cor correspondente ao nível do reservatório."""
  if nivel == 1:
    return Fore.RED
  elif nivel == 2:
    return Fore.YELLOW
  elif nivel == 3:
    return Fore.GREEN
  elif nivel == 4:
    return Fore.CYAN
  elif nivel == 5:
    return Fore.BLUE
  else:
    return Style.RESET_ALL


def simular_reservatorio():
  # Lista contendo as informações dos níveis e suas respectivas mensagens
  status_reservatorio = [
      (1, "Nível 1: Muito baixo (crítico)"),
      (2, "Nível 2: Baixo"),
      (3, "Nível 3: Médio"),
      (4, "Nível 4: Alto"),
      (5, "Nível 5: Muito alto (alerta)"),
  ]

  print("=== SISTEMA DE MONITORAMENTO DE NÍVEL DE ÁGUA ===")
  print("Simulando o painel de controle do reservatório:\n")

  # Exibindo cada situação do reservatório
  for nivel, mensagem in status_reservatorio:
    cor = definir_cor_nivel(nivel)
    print(f"{cor}[ALERTA] {mensagem}{Style.RESET_ALL}")


if __name__ == "__main__":
  simular_reservatorio()