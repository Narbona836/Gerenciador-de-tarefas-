-----

# 📝 Gerenciador de Tarefas em Python

Um simples e intuitivo gerenciador de tarefas por linha de comando (CLI) construído em Python. Este projeto permite adicionar, visualizar e remover tarefas rapidamente, ajudando você a manter sua rotina organizada.

## ✨ Funcionalidades

  * **Adicionar Tarefa:** Insira novas tarefas na sua lista.
  * **Visualizar Tarefas:** Veja todas as tarefas numeradas para fácil referência.
  * **Remover Tarefa:** Exclua tarefas da lista pelo seu número de índice.
  * **Interface Simples:** Utiliza o terminal para uma experiência de usuário leve e direta.

## 🚀 Como Executar o Projeto

Estas instruções ajudarão você a ter uma cópia do projeto em execução em sua máquina local.

### Pré-requisitos

Você só precisa ter o **Python** instalado em seu sistema.

```bash
# Você pode verificar se o Python está instalado
python --version 
# ou
python3 --version
```

### Instalação e Execução

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/Narbona836/Gerenciador-de-tarefas-
    cd gerenciador-de-tarefas-python
    ```
2.  **Execute o Programa:**
    ```bash
    python gerenciar_tarefas.py
    ```

### Utilização

Ao executar o programa, você verá o menu principal:

```
    Ｇｅｒｅｎｃｉａｄｏｒ ｄｅ ｔａｒｅｆａｓ
    
1. Adicionar uma tarefa
2. Visualizar lista de tarefas
3. Remover uma tarefa da lista
4. Sair do programa

Digite a opção desejada: 
```

Basta digitar o número da opção desejada e pressionar `Enter`.

## 💻 Código Fonte (Estrutura Principal)

O projeto é estruturado em torno de funções que manipulam uma lista global de tarefas (`tarefas = []`).

```python

tarefas = []

def adicionar_tarefa():
    # ... lógica para adicionar ...

def visualizar_tarefas():
    # ... lógica para exibir a lista ...

def remover_tarefa():
    # ... lógica para remover uma tarefa ...

def gerenciador_de_tarefas():
    # ... loop principal para interagir com o usuário ...

if __name__ == "__main__":
    # Inicia o programa
    # ...
```

## 🤝 Contribuições

Sinta-se à vontade para sugerir melhorias ou adicionar novas funcionalidades\!

1.  Faça um `fork` do projeto.
2.  Crie uma `branch` para sua funcionalidade (`git checkout -b feature/AmazingFeature`).
3.  Comite suas mudanças (`git commit -m 'Add some AmazingFeature'`).
4.  Faça o `push` para a branch (`git push origin feature/AmazingFeature`).
5.  Abra um `Pull Request`.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT.

-----

**Desenvolvido por:** [Willian Narbona Aquino /https://github.com/Narbona836]

-----
