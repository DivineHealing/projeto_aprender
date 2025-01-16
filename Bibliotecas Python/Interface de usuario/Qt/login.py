import sqlite3 as sq

def somar_valores(valor1, valor2):
    try:       
        banco = sq.connect('Usuario.db')
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXIST user (user text,senha text)")
        cursor.execute("INSERT INTO User VALUES ('"+valor1+"', '"+valor2+"')")
        banco.commit()
        banco.close()
        
    
    except sq.Error as erro:
        # Retorna None ou uma mensagem de erro se não for possível converter
        return f"Erro ao inserir os dados: {erro}"