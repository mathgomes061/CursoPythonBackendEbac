# Aprovado, reprovado ou recuperação:
# Receba média de um aluno e diga se ele foi aprovado (média >= 7)
# em recuperação (5 <= média < 7)
# reprovado (média < 5).

nota_aluno = float(input())

# if nota_aluno >= 7:
#     print("Aprovado")
# elif nota_aluno >= 5 and nota_aluno < 7:
#     print("Em recuperação")
# else:
#     print("Reprovado")


if nota_aluno >= 7:
    print("Aprovado")
elif nota_aluno < 5:
    print("Reprovado")
else:
    print("Em recuperação")
