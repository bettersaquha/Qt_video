import sys
from PyQt5.QtWidgets import QApplication
from QtVideo.dialog_app import App

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())