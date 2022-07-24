import mysql.connector
import datetime

def alterar():
  connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="97113632",
    database="usuario"
  )

  cursor = connection.cursor()

  usuario = input("digite o nome:")
  email = input("digite o email: ")
  id = int(input("Digite o ID:"))
  sql = "UPDATE cadastro SET usuario = '{}', email = '{}' WHERE id = {}".format(usuario, email, id)

  cursor.execute(sql)
  connection.commit()

  recordsaffected = cursor.rowcount

  cursor.close()
  connection.close()

  print(recordsaffected, " registros alterados")