from PyQt5 import QtWidgets, QtGui, QtCore
from QtVideo.main_ui import Ui_Dialog
from QtVideo.vd_dialog import Vd_Dialog

# 定义一个继承自 QMainWindow 的主对话框类
class MainDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()  # 实例化 UI 对象
        self.ui.setupUi(self)  # 设置 UI

        # 获取 QLabel 对象，Qt Designer 中设置了一个 QLabel 用于显示背景图
        self.label = self.ui.label

        # 监听窗口大小变化事件，绑定到 on_resize 方法
        self.resizeEvent = self.on_resize

    # 定义窗口大小变化事件处理方法
    def on_resize(self, event):
        # 调整 QLabel 的大小为窗口的大小
        self.label.resize(self.width(), self.height())
        # 设置 QLabel 的样式，包括字体、颜色、背景图片等
        self.label.setStyleSheet("""
                    font-family: "Arial";
                    font-size: 24px;
                    font-weight: bold;
                    color: white;
                    background-color: green;  /* 绿色背景 */
                    border: 2px solid white;
                    border-radius: 10px;
                    padding: 10px;
                    text-align: center;
                    background-image: url("D:/大三下/企业实训/第一周_图像识别api调用/project1/data/背景0.JPG");
                    background-position: center;
                    background-repeat: no-repeat;
                    background-size: cover;  /* 调整背景图片的大小，使其覆盖标签 */
                """)

    # 定义进入“land”模式的槽函数
    def landgoin(self):
        self.vd_dialog = Vd_Dialog('land')  # 创建 Vd_Dialog 对象，模式为 'land'
        self.vd_dialog.show()  # 显示对话框
        self.close()  # 关闭当前窗口

    # 定义进入“animal”模式的槽函数
    def animalgoin(self):
        self.vd_dialog = Vd_Dialog('animal')  # 创建 Vd_Dialog 对象，模式为 'animal'
        self.vd_dialog.show()  # 显示对话框
        self.close()  # 关闭当前窗口

    # 定义进入“plant”模式的槽函数
    def plantgoin(self):
        self.vd_dialog = Vd_Dialog('plant')  # 创建 Vd_Dialog 对象，模式为 'plant'
        self.vd_dialog.show()  # 显示对话框
        self.close()  # 关闭当前窗口