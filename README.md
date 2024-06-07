# Põe na Lista!

Põe na Lista! é um aplicativo de lista de tarefas simples, criado usando a biblioteca Tkinter em Python. Este aplicativo permite que você adicione, edite e exclua tarefas facilmente.

## Funcionalidades

- **Adicionar Tarefa**: Adicione novas tarefas à sua lista.
- **Editar Tarefa**: Edite tarefas existentes.
- **Excluir Tarefa**: Exclua tarefas quando concluídas.
- **Rolagem**: Suporte a listas de tarefas longas com barra de rolagem.

## Como Usar

### Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. Este projeto foi desenvolvido usando Python 3.

### Passos para Rodar o Código

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/poe-na-lista.git
   ```
2. Navegue até o diretório do projeto:
   ```sh
   cd poe-na-lista
   ```
3. Certifique-se de ter a biblioteca Tkinter instalada. A Tkinter geralmente já vem instalada com o Python, mas se você encontrar problemas, instale-a usando:
   ```sh
   sudo apt-get install python3-tk
   ```
4. Execute o script Python:
   ```sh
   python app.py
   ```

### Estrutura do Código

- `app.py`: Contém a lógica principal do aplicativo.
- `edit.png` e `delete.png`: Ícones usados para editar e excluir tarefas.

### Funcionalidades do Código

- **Adicionar Tarefa**: A função `add_task` permite adicionar uma nova tarefa. Se a entrada estiver vazia ou for igual a "Item a ser adicionado", uma mensagem de aviso será exibida.
- **Editar Tarefa**: A função `prepare_edit` prepara uma tarefa para edição, preenchendo a entrada de texto com o texto da tarefa.
- **Atualizar Tarefa**: A função `update_task` atualiza o texto de uma tarefa existente.
- **Excluir Tarefa**: A função `delete_task` exclui uma tarefa da lista.

Espero que este README forneça todas as informações necessárias para começar a usar e personalizar o "Põe na Lista!". Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato.
