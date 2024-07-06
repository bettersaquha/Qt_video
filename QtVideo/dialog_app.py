import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QGridLayout, QVBoxLayout, QStackedWidget
from PyQt5 import QtWidgets, QtCore, QtGui
from QtVideo.login_ui import Ui_Dialog as LoginUi_Dialog
from QtVideo.main_dialog import MainDialog
import re

# 定义一个继承自 QApplication 的应用程序类
class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.login_window = Login()  # 创建登录窗口实例
        self.login_window.show()  # 显示登录窗口

# 定义一个继承自 QWidget 的登录窗口类
class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = LoginUi_Dialog()  # 实例化登录 UI 对象
        self.ui.setupUi(self)  # 设置 UI

        # 创建 QLabel 对象用于显示背景图片
        self.label = QtWidgets.QLabel(self)
        self.pixmap = QtGui.QPixmap("data/背景0.jpg")
        self.label.resize(self.width(), self.height())  # 设置 QLabel 尺寸
        self.label.setScaledContents(True)  # 设置 QLabel 内容按比例缩放
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))
        self.label.lower()  # 将 QLabel 置于所有控件的底层

        # 监听窗口大小变化事件，绑定到 on_resize 方法
        self.resizeEvent = self.on_resize

        # 预定义用户账户和密码
        self.users = [
            {"account": "01111111111", "password": "01password"},
            {"account": "12222222222", "password": "02password"},
            {"account": "23333333333", "password": "03password"},
            {"account": "34444444444", "password": "04password"}
        ]
        # 连接登录按钮的点击事件到 validate_login 方法
        self.ui.login_commit.clicked.connect(self.validate_login)

    # 定义窗口大小变化事件处理方法
    def on_resize(self, event):
        self.label.resize(self.width(), self.height())
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))

    # 验证登录信息
    def validate_login(self):
        account = self.ui.cin_account.text()
        password = self.ui.cin_password.text()
        print(f"1....Trying to login with account: {account}, password: {password}")

        # 验证账号是否为11位的数字，且密码至少6位并包含字母和数字
        if len(account) == 11 and (len(password) >= 6 and re.fullmatch(r'(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}', password)):
            print(f"2....Trying to login with account: {account}, password: {password}")
            user_found = False
            for user in self.users:
                if user["account"] == account:
                    user_found = True
                    if user["password"] == password:
                        QMessageBox.information(self, 'OK了哦', '登录成功')
                        self.maingoin()  # 登录成功后调用 maingoin
                        print(f"3....Trying to login with account: {account}, password: {password}")
                        break
                    else:
                        QMessageBox.warning(self, 'Warning', '密码错误，请重新输入')
                        self.ui.cin_password.clear()  # 清除密码框内容，让用户重新输入
                        break
            if not user_found:
                self.users.append({"account": account, "password": password})
                QMessageBox.information(self, 'OK了哦', '注册成功，您已登录')
                self.maingoin()  # 注册成功后调用 maingoin
                print(f"4....Trying to login with account: {account}, password: {password}")
        else:
            # 提示账号或密码格式错误
            if len(account) != 11:
                QtWidgets.QMessageBox.warning(self, 'Warning', '账号必须是11位数字')
                self.ui.cin_account.clear()  # 清除账号框内容，让用户重新输入
            elif not (len(password) >= 6 and re.fullmatch(r'(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}', password)):
                QtWidgets.QMessageBox.warning(self, 'Warning', '密码必须是字母和数字组合，且至少长度为6')
                self.ui.cin_password.clear()  # 清除密码框内容，让用户重新输入
        return

    # 进入主对话框界面
    def maingoin(self):
        self.main_window = MainDialog()  # 创建主对话框实例
        self.main_window.show()  # 显示主对话框
        self.close()  # 关闭当前登录窗口

# 主函数入口
if __name__ == "__main__":
    app = App(sys.argv)  # 创建应用程序实例
    sys.exit(app.exec_())  # 运行应用程序
