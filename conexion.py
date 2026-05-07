import mysql.connector
from mysql.connector import Error

class Conexion:
    def __init__(self):
        self.config = {
            "host":'localhost',
            "user":'root',
            "password":"",
            "db":"prueba_python"
        }
        self.conexion = None
        self.cursor = None
    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(**self.config)
            if self.conexion.is_connected():
                print("Conexión exitosa")   
                self.cursor = self.conexion.cursor()
        except Error as e:
            print(f"ERROR: {e}")         
    #SIRIVE PARA INSERTAR, MODIFICAR O ELIMINAR
    def insertar(self, sql, valores):
        self.cursor.execute(sql, valores)
        self.conexion.commit()
        #sirve para seleccionar bonito
    def seleccionar (self,sql):
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
        