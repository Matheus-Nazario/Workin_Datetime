from datetime import date, datetime

from pytz import timezone

# data atual EUA
data_atual = date.today()
print(data_atual)

# ---------------------------------------------

# Formado sem o "0" fia 14/5/2021
data_em_texto = "{}/{}/{}".format(
    data_atual.day, data_atual.month, data_atual.year
)
print(data_em_texto)

# ----------------------------------

# corretocom "0" 14/05/2021
data_em_texto = data_atual.strftime("%d/%m/%Y")
print("data_em_texto:  ", data_em_texto)

# --------------------------------------
# Datas e horas juntos
data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y")

print("Data_e_hora_em_texto:  ", data_e_hora_em_texto)

# --------------------------------------------

# strftime() para mostrar a data e horário

data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")

print(data_e_hora_em_texto)

"""
Perfeito! Até agora aprendemos a pegar a data atual com a classe date
,datetime e até aprendemos a formatar datas, transformando-as em strings.
Mas e se precisássemos fazer o caminho contrário?
"""
# --------------------------------------

# Convertendo uma string em datetime

data_em_texto = "01/03/2018 12:30"
data_e_hora = datetime.strptime(data_em_texto, "%d/%m/%Y %H:%M")


# ----------------------------


data_e_hora_atuais = datetime.now()
fuso_horario = timezone("America/Sao_Paulo")
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime(
    "%d/%m/%Y %H:%M"
)

print(data_e_hora_sao_paulo_em_texto)
