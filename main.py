import sys
from PyQt6 import QtWidgets
from main_controller import MainController
#pip freeze > requirements.txt
#pip install mysql-connector-python==9.7.0

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainController()
    window.show()
    sys.exit(app.exec())

if __name__ =="__main__":
    main()
