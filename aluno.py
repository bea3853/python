print("Sistema de média do Aluno")
aluno = input("Digite o nome do Aluno")
nota1 = float(input("Digite a nota 1 do aluno"))
nota2 = float(input("Digite a nota 2 do aluno"))
nota3 = float(input("Digite a nota 3 do aluno"))
nota4 = float(input("Digite a nota 4 do aluno"))
media = (nota1+nota2+nota3+nota4+nota4) / 4
if media < 7:
    print("Recuperação")
if media < 5:
    print("Não ")
else:
    print("Passou!")
    print("O aluno %s, possui a media %f", aluno, media)
