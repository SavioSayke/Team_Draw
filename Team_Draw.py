import random
from PyQt5 import uic,QtWidgets

app = QtWidgets.QApplication([])
tela = uic.loadUi("Team_Draw.ui")

jogadores = ["Jogador_1","Jogador_2","Jogador_3","Jogador_4","Jogador_5","Jogador_6","Jogador_7","Jogador_8","Jogador_9",
"Jogador_10","Jogador_11","Jogador_12","Jogador_13","Jogador_14"]

jogadores_m = ["Jogador_15","Jogador_16","Jogador_17"]

def all_random():
    sortear_j = (random.choice(jogadores))
    tela.label_4.setText(str(sortear_j))
    jogadores.remove(sortear_j)
    sortear_j = (random.choice(jogadores_m))
    tela.label_5.setText(str(sortear_j))
    jogadores_m.remove(sortear_j)
    sortear_j = (random.choice(jogadores))
    tela.label_6.setText(str(sortear_j))
    jogadores.remove(sortear_j)
    sortear_j = (random.choice(jogadores))
    tela.label_7.setText(str(sortear_j))
    jogadores.remove(sortear_j)
    sortear_j = (random.choice(jogadores))
    tela.label_8.setText(str(sortear_j))
    jogadores.remove(sortear_j)
    sortear_j = (random.choice(jogadores))
    tela.label_9.setText(str(sortear_j))
    jogadores.remove(sortear_j)
    sortear_j = (random.choice(jogadores))
    tela.label_10.setText(str(sortear_j))
    jogadores.remove(sortear_j)
    sortear_j = (random.choice(jogadores_m))
    tela.label_11.setText(str(sortear_j))
    jogadores_m.remove(sortear_j)
    sortear_j = (random.choice(jogadores))
    tela.label_12.setText(str(sortear_j))
    jogadores.remove(sortear_j)
    sortear_j = (random.choice(jogadores))
    tela.label_13.setText(str(sortear_j))
    jogadores.remove(sortear_j)
    sortear_j = (random.choice(jogadores))
    tela.label_14.setText(str(sortear_j))
    jogadores.remove(sortear_j)
    sortear_j = (random.choice(jogadores))
    tela.label_15.setText(str(sortear_j))
    jogadores.remove(sortear_j)
    sortear_j = (random.choice(jogadores))
    tela.label_16.setText(str(sortear_j))
    jogadores.remove(sortear_j)
    sortear_j = (random.choice(jogadores))
    tela.label_17.setText(str(sortear_j))
    jogadores.remove(sortear_j)
    sortear_j = (random.choice(jogadores))
    tela.label_18.setText(str(sortear_j))
    jogadores.remove(sortear_j)
    sortear_j = (random.choice(jogadores))
    tela.label_19.setText(str(sortear_j))
    jogadores.remove(sortear_j)
    sortear_j = (random.choice(jogadores_m))
    tela.label_20.setText(str(sortear_j))
    jogadores_m.remove(sortear_j)

def sorteio_time1_j1():
    sortear_j = (random.choice(jogadores))
    tela.label_4.setText(str(sortear_j))
    jogadores.remove(sortear_j)

def sorteio_time1_j2():
    sortear_j = (random.choice(jogadores_m))
    tela.label_5.setText(str(sortear_j))
    jogadores_m.remove(sortear_j)

def sorteio_time1_j3():
    sortear_j = (random.choice(jogadores))
    tela.label_6.setText(str(sortear_j))
    jogadores.remove(sortear_j)

def sorteio_time1_j4():
    sortear_j = (random.choice(jogadores))
    tela.label_7.setText(str(sortear_j))
    jogadores.remove(sortear_j)

def sorteio_time1_j5():
    sortear_j = (random.choice(jogadores))
    tela.label_8.setText(str(sortear_j))
    jogadores.remove(sortear_j)

def sorteio_time2_j1():
    sortear_j = (random.choice(jogadores))
    tela.label_9.setText(str(sortear_j))
    jogadores.remove(sortear_j)

def sorteio_time2_j2():
    sortear_j = (random.choice(jogadores))
    tela.label_10.setText(str(sortear_j))
    jogadores.remove(sortear_j)

def sorteio_time2_j3():
    sortear_j = (random.choice(jogadores_m))
    tela.label_11.setText(str(sortear_j))
    jogadores_m.remove(sortear_j)

def sorteio_time2_j4():
    sortear_j = (random.choice(jogadores))
    tela.label_12.setText(str(sortear_j))
    jogadores.remove(sortear_j)

def sorteio_time2_j5():
    sortear_j = (random.choice(jogadores))
    tela.label_13.setText(str(sortear_j))
    jogadores.remove(sortear_j)

def sorteio_time3_j1():
    sortear_j = (random.choice(jogadores_m))
    tela.label_14.setText(str(sortear_j))
    jogadores_m.remove(sortear_j)

def sorteio_time3_j2():
    sortear_j = (random.choice(jogadores))
    tela.label_15.setText(str(sortear_j))
    jogadores.remove(sortear_j)

def sorteio_time3_j3():
    sortear_j = (random.choice(jogadores))
    tela.label_16.setText(str(sortear_j))
    jogadores.remove(sortear_j)

def sorteio_time3_j4():
    sortear_j = (random.choice(jogadores))
    tela.label_17.setText(str(sortear_j))
    jogadores.remove(sortear_j)

def sorteio_time3_j5():
    sortear_j = (random.choice(jogadores))
    tela.label_18.setText(str(sortear_j))
    jogadores.remove(sortear_j)

def sorteio_fora_1():
    sortear_j = (random.choice(jogadores))
    tela.label_19.setText(str(sortear_j))
    jogadores.remove(sortear_j)

def sorteio_fora_2():
    sortear_j = (random.choice(jogadores))
    tela.label_20.setText(str(sortear_j))
    jogadores.remove(sortear_j)

tela.pushButton_2.clicked.connect(sorteio_time1_j1)
tela.pushButton_3.clicked.connect(sorteio_time1_j2)
tela.pushButton_4.clicked.connect(sorteio_time1_j3)
tela.pushButton_5.clicked.connect(sorteio_time1_j4)
tela.pushButton_6.clicked.connect(sorteio_time1_j5)
tela.pushButton_7.clicked.connect(sorteio_time2_j1)
tela.pushButton_8.clicked.connect(sorteio_time2_j2)
tela.pushButton_9.clicked.connect(sorteio_time2_j3)
tela.pushButton_10.clicked.connect(sorteio_time2_j4)
tela.pushButton_11.clicked.connect(sorteio_time2_j5)
tela.pushButton_12.clicked.connect(sorteio_time3_j1)
tela.pushButton_13.clicked.connect(sorteio_time3_j2)
tela.pushButton_14.clicked.connect(sorteio_time3_j3)
tela.pushButton_15.clicked.connect(sorteio_time3_j4)
tela.pushButton_16.clicked.connect(sorteio_time3_j5)
tela.pushButton_18.clicked.connect(sorteio_fora_1)
tela.pushButton_19.clicked.connect(sorteio_fora_2)

tela.pushButton_17.clicked.connect(all_random)

tela.show()
app.exec()