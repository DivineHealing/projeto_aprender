from PyQt6 import QtCore, QtGui, QtWidgets
from login import somar_valores  # Importa a função de soma do arquivo login.py


class Ui_telaCadastro(object):
    def setupUi(self, telaCadastro):
        telaCadastro.setObjectName("telaCadastro")
        telaCadastro.resize(321, 298)
        telaCadastro.setStyleSheet(60, 60, 60)
        self.label = QtWidgets.QLabel(parent=telaCadastro)
        self.label.setGeometry(QtCore.QRect(10, 10, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=telaCadastro)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.login = QtWidgets.QLineEdit(parent=telaCadastro)
        self.login.setGeometry(QtCore.QRect(60, 10, 113, 20))
        self.login.setObjectName("login")
        self.senha = QtWidgets.QLineEdit(parent=telaCadastro)
        self.senha.setGeometry(QtCore.QRect(60, 40, 113, 20))
        self.senha.setObjectName("senha")
        self.btnCadastrar = QtWidgets.QPushButton(parent=telaCadastro)
        self.btnCadastrar.setGeometry(QtCore.QRect(90, 100, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btnCadastrar.setFont(font)
        self.btnCadastrar.setObjectName("btnCadastrar")
        
        # Conectar o botão à função de somar
        self.btnCadastrar.clicked.connect(self.func_login)

        self.retranslateUi(telaCadastro)
        QtCore.QMetaObject.connectSlotsByName(telaCadastro)

    def retranslateUi(self, telaCadastro):
        _translate = QtCore.QCoreApplication.translate
        telaCadastro.setWindowTitle(_translate("telaCadastro", "Tela de Cadastro"))
        self.label.setText(_translate("telaCadastro", "Login"))
        self.label_2.setText(_translate("telaCadastro", "Senha"))
        self.btnCadastrar.setText(_translate("telaCadastro", "Cadastrar"))
        
        
        
        
    def func_login(self):
        # Pega os valores inseridos nos campos de login e senha
        login_text = self.login.text()
        senha_text = self.senha.text()
        
        # Chama a função para realizar o cadastro do arquivo login.py
        cadastrar = somar_valores(login_text, senha_text)
        
        # Exibe a confirmação de cadastro no terminal
        if isinstance(cadastrar, str):
            print(f"A usuario {login_text} e a senha {senha_text} registrado com sucesso!")
            self.login.setText("")
            self.senha.setText("")
            telaCadastro.close()
        else:
            print(cadastrar)  # Se for uma mensagem de erro, exibe no terminal
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    telaCadastro = QtWidgets.QWidget()
    ui = Ui_telaCadastro()
    ui.setupUi(telaCadastro)
    telaCadastro.show()
    sys.exit(app.exec())

