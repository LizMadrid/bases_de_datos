import sys
from PyQt6 import QtWidgets, uic
from conexion import Conexion

class MainController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.conexion = Conexion()
        self.conexion.conectar()
        self.btn_insert.clicked.connect(self.add_user)

    def add_user(self):
        name = self.txt_name.text()
        last = self.txt_last.text()
        email = self.txt_email.text()
        passw = self.txt_pass.text()
        passw_confirm = self.txt_pass_confirm.text()

        if name.strip() == "" or last.strip == "" or email.strip() == "" or passw.strip() == "" or passw_confirm.strip() == "":
            QtWidgets.QMessageBox.warning(self, "Favor de llenar todos los campos")
        elif passw != passw_confirm:
            QtWidgets.QMessageBox.warning(self, "Las contraseñas no coinciden")   
        else:
            sql = "INSERT INTO users values (%s,%s,%s,%s,%s,%s)"
            valores = (0,name,last,email,passw,'default.jpg') 
            self.conexion.insertar(sql,valores)
            QtWidgets.QMessageBox.information(self,"Registro insertado correctamente", None)