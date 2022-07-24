import mysql.connector
import mysql.connector.connection


def create():

  connection = mysql.connector.connect(
    host="localhost",
    database="usuario",
    user="root",
    password="97113632",
  )

  cursor = connection.cursor()

  nome = input("Digite o nome:")
  email = input("DIgite o email:")
  sql = "INSERT INTO cadastro (usuario, email) VALUES ('{}', '{}');".format(nome,email)

  cursor.execute(sql)
  connection.commit()

  userid = cursor.lastrowid

  cursor.close()
  connection.close()

  print("Foi cadastrado o novo usuário de ID:", userid)