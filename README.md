# Sistema de Gerenciamento de Livraria

Este projeto é um **Sistema de Gerenciamento de Livraria** que combina vários conceitos de manipulação de arquivos, banco de dados SQLite, e operações com arquivos CSV. O sistema permite realizar operações CRUD com um banco de dados de livros, exportar/importar dados, e gerenciar backups de forma automatizada.

## 📂 Funcionalidades do Sistema

### 1. Manipulação de Arquivos
- Utiliza as bibliotecas **os** e **pathlib** para organizar e manter:
  - Arquivos de backup da base de dados.
  - Cópias dos dados em arquivos CSV.
  - Diretórios organizados de maneira eficiente.

### 2. SQLite (CRUD)
- O banco de dados principal é gerido em **SQLite**, incluindo:
  - **Livros**: ID, título, autor, ano de publicação e preço.
  - Suporte completo para operações CRUD:
    - **Criar**: Adicionar novos livros ao banco.
    - **Ler**: Exibir todos os livros cadastrados.
    - **Atualizar**: Modificar o preço de livros existentes.
    - **Deletar**: Remover livros do banco.
    - **Buscar**: Encontrar livros por autor.

### 3. CSV
- **Exportação** de dados do banco de dados para arquivos CSV.
- **Importação** de dados de arquivos CSV para o banco de dados.

### 4. Backup e Limpeza de Arquivos
- Geração automática de **backups** sempre que livros forem adicionados, atualizados ou removidos.
- **Limpeza de backups antigos**: Mantém apenas os 5 backups mais recentes no diretório.

---

## 📋 Requisitos do Sistema

### Banco de Dados (livraria.db)
- Deve armazenar as seguintes informações:
  - **id**: Chave primária, gerada automaticamente.
  - **titulo**: Texto.
  - **autor**: Texto.
  - **ano_publicacao**: Inteiro.
  - **preco**: Número flutuante.

### Operações CRUD
- **Adicionar um novo livro.**
- **Exibir todos os livros cadastrados.**
- **Atualizar o preço de um livro.**
- **Remover um livro.**
- **Buscar livros por autor.**

### Manipulação de Arquivos
- **Exportar** dados do banco de dados em formato CSV para um diretório específico.
- **Importar** dados de um arquivo CSV para o banco de dados.
- Realizar **backup automático** do banco de dados antes de qualquer modificação (inserção, atualização ou remoção).
- Usar a biblioteca **pathlib** para gerenciar diretórios de backup.

---

## 🛠️ Estrutura de Arquivos e Diretórios

A estrutura de diretórios do sistema será organizada da seguinte forma:

```bash
/meu_sistema_livraria/
    ├── /backups/
    │   ├── backup_livraria_2024-01-01.db
    │   ├── backup_livraria_2024-01-02.db
    │   └── ...
    ├── /data/
    │   └── livraria.db
    └── /exports/
        └── livros_exportados.csv
```

---

## 🎮 Exemplo de Execução do Sistema

Ao executar o sistema, será exibido o seguinte menu interativo:

```bash
1. Adicionar novo livro
2. Exibir todos os livros
3. Atualizar preço de um livro
4. Remover um livro
5. Buscar livros por autor
6. Exportar dados para CSV
7. Importar dados de CSV
8. Fazer backup do banco de dados
9. Sair
```

O usuário pode selecionar qualquer uma das opções para realizar a operação correspondente.

---

## 📌 Desafios Extras

### 1. Validação de Entradas
- Adicione validação para garantir que os campos, como o ano e o preço, recebam valores válidos.

### 2. Relatórios
- Gere relatórios a partir dos dados exportados, nos formatos **PDF** ou **HTML**, para uma visualização organizada.

---

## 🚀 Como Rodar o Sistema

### 1. Clone o repositório:
```bash
git clone https://github.com/usuario/livraria.git
cd livraria
```

### 2. Crie o ambiente virtual (opcional, mas recomendado):
```bash
python -m venv env
```

### 3. Ative o ambiente virtual:
- No **Windows**:
```bash
.\env\Scripts\activate
```
- No **Linux/Mac**:
```bash
source env/bin/activate
```

### 4. Execute o sistema:
```bash
python main.py
```

