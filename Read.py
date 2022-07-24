import mysql.connector
import mysql.connector.connection

def listar():
  connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="97113632",          #####_____________faz a conexão
    database="usuario"
  )

  cursor = connection.cursor()
  cursor.execute("SELECT * FROM cadastro")
  results = cursor.fetchall() ##-----pega os dados da tabela e adiciona na variavel results


    ####--------laço para imprimir as linhas
  print(results)

  cursor.close()
  connection.close()