import mysql.connector
import mysql.connector.connection


def deletar():
  connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="97113632",      #####------faz a conexão
    database="usuario"
  )

  cursor = connection.cursor()

  data = int(input("digite id:", ))
  sql = "DELETE FROM cadastro WHERE id = {}".format(data)


  cursor.execute(sql)
  connection.commit()

  recordsaffected = cursor.rowcount

  print(recordsaffected, " registros excluídos")

  cursor.close()
  connection.close()

