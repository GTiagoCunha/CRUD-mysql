import Create as cr
import Update as up
import Read as rd
import Delete as dl


print("************************")
print("     REGISTROS DE USUARIOS     ")
print("************************")


opcao = int(input(" 1 Cadastrar\n 2 Alterar\n 3 Listar\n 4 Deletar\n Digite sua opção:"))



if opcao == 1:
    cr.create()
elif opcao ==2:
    up.alterar()
elif opcao == 3:
    rd.listar()
elif opcao == 4:
    dl.deletar()
else:
    print("opção invalida digite novamente")

