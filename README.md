# Sistema de Monitoramento de Nível de Água

Este projeto consiste em um sistema simples de monitoramento de reservatório de água executado via terminal. O programa exibe alertas visuais com cores diferentes utilizando a biblioteca `colorama`, variando de acordo com o nível do reservatório.

## 📋 Funcionalidades

- Exibição de 5 níveis de alerta progressivos (de Crítico a Muito Alto).
- Destaque colorido para cada situação de risco:
  - **Nível 1 (Muito Baixo / Crítico):** Vermelho
  - **Nível 2 (Baixo):** Amarelo
  - **Nível 3 (Médio):** Verde
  - **Nível 4 (Alto):** Ciano
  - **Nível 5 (Muito Alto / Alerta):** Azul
- Restauração automática dos estilos do terminal após a execução.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Colorama** (Biblioteca para estilização de terminal)

## 🚀 Como Executar o Projeto

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale a biblioteca `colorama`:
   ```bash
   python -m pip install colorama
