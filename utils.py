import os
import sqlite3
import shutil
import csv
from datetime import datetime
from pathlib import Path

def backup_database():
    """Cria um backup do banco de dados antes de alterações."""
    src = Path("data/livraria.db")
    dst = Path(f"backups/backup_livraria_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.db")
    shutil.copy(src, dst)

def export_to_csv():
    """Exporta os dados do banco para um arquivo CSV."""
    conn = sqlite3.connect("data/livraria.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()

    with open("exports/livros_exportados.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Título", "Autor", "Ano Publicação", "Preço"])
        writer.writerows(livros)
    
    print("Dados exportados para CSV com sucesso.")

def import_from_csv():
    """Importa dados de um arquivo CSV para o banco de dados."""
    conn = sqlite3.connect("data/livraria.db")
    cursor = conn.cursor()

    with open("exports/livros_exportados.csv", mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cursor.execute("INSERT INTO livros (titulo, autor, ano_publicacao, preco) VALUES (?, ?, ?, ?)", 
                            (row[1], row[2], int(row[3]), float(row[4])))
        conn.commit()

    print("Dados importados do CSV com sucesso.")

def clean_old_backups():
    """Mantém apenas os 5 backups mais recentes."""
    backups = sorted(Path("backups").glob("*.db"), key=os.path.getmtime, reverse=True)
    for backup in backups[5:]:
        os.remove(backup)
        print(f"Backup {backup} removido.")
