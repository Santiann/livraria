import sqlite3
from utils import backup_database, export_to_csv, import_from_csv, clean_old_backups
from pathlib import Path

Path("data").mkdir(parents=True, exist_ok=True)
Path("backups").mkdir(parents=True, exist_ok=True)
Path("exports").mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect("data/livraria.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS livros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    ano_publicacao INTEGER NOT NULL,
                    preco REAL NOT NULL)''')
conn.commit()

def adicionar_livro():
    titulo = input("Título do livro: ")
    autor = input("Autor: ")
    ano = int(input("Ano de publicação: "))
    preco = float(input("Preço: "))

    cursor.execute("INSERT INTO livros (titulo, autor, ano_publicacao, preco) VALUES (?, ?, ?, ?)", 
                    (titulo, autor, ano, preco))
    conn.commit()
    
    backup_database()
    print("Livro adicionado e backup criado.")

def exibir_livros():
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    for livro in livros:
        print(livro)

def atualizar_preco():
    livro_id = int(input("ID do livro a ser atualizado: "))
    novo_preco = float(input("Novo preço: "))
    
    cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (novo_preco, livro_id))
    conn.commit()
    
    backup_database()
    print("Preço atualizado e backup criado.")

def remover_livro():
    livro_id = int(input("ID do livro a ser removido: "))
    
    cursor.execute("DELETE FROM livros WHERE id = ?", (livro_id,))
    conn.commit()
    
    backup_database()
    print("Livro removido e backup criado.")

def buscar_por_autor():
    autor = input("Nome do autor: ")
    cursor.execute("SELECT * FROM livros WHERE autor LIKE ?", ('%' + autor + '%',))
    livros = cursor.fetchall()
    for livro in livros:
        print(livro)

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar novo livro")
        print("2. Exibir todos os livros")
        print("3. Atualizar preço de um livro")
        print("4. Remover um livro")
        print("5. Buscar livros por autor")
        print("6. Exportar dados para CSV")
        print("7. Importar dados de CSV")
        print("8. Fazer backup do banco de dados")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_livro()
        elif opcao == '2':
            exibir_livros()
        elif opcao == '3':
            atualizar_preco()
        elif opcao == '4':
            remover_livro()
        elif opcao == '5':
            buscar_por_autor()
        elif opcao == '6':
            export_to_csv()
        elif opcao == '7':
            import_from_csv()
        elif opcao == '8':
            backup_database()
        elif opcao == '9':
            clean_old_backups()
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
