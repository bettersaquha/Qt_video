from PyQt5.Qt import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication
import sys

from QtVideo.land_ui import Ui_Dialog as Ui_LandDialog
from QtVideo.animal_ui import Ui_Dialog as Ui_AnimalDialog
from QtVideo.plant_ui import Ui_Dialog as Ui_PlantDialog
from QtVideo.Video import Video

# 定义一个继承自 QDialog 的视频对话框类
class Vd_Dialog(QDialog):
    def __init__(self, ui_type):
        super().__init__()

        # 根据 ui_type 加载不同的 UI 和视频文件
        if ui_type == 'land':
            self.ui = Ui_LandDialog()
            self.ui.setupUi(self)
            self.th1 = Video('data/地标视频.mp4')
        elif ui_type == 'animal':
            self.ui = Ui_AnimalDialog()
            self.ui.setupUi(self)
            self.th1 = Video('data/动物视频.mp4')
        elif ui_type == 'plant':
            self.ui = Ui_PlantDialog()
            self.ui.setupUi(self)
            self.th1 = Video('data/植物视频.mp4')
        else:
            raise ValueError("类型应该拼写错误！")

        # 绑定视频线程的信号与槽函数，用于显示视频帧
        self.th1.send.connect(self.showimage)
        self.th1.start()

    # 显示图像的方法
    def showimage(self, h, w, c, b, th_id, result_dict):
        # 创建 QImage 对象用于显示图像
        image = QImage(b, w, h, w * c, QImage.Format_BGR888)
        pix = QPixmap.fromImage(image)

        # 设置 Animal 的 UI 界面
        if th_id == 1:
            width = self.ui.animal_video.width()
            height = self.ui.animal_video.height()
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.ui.animal_video.setPixmap(scale_pix)

            # 设置 UI 界面 label 里的文字
            if result_dict:
                animal_names = list(result_dict.keys())
                probabilities = list(result_dict.values())
                self.ui.animal1.setText(animal_names[0])
                self.ui.probability1.setText(str(probabilities[0]))
                self.ui.animal2.setText(animal_names[1])
                self.ui.probability2.setText(str(probabilities[1]))
                self.ui.animal3.setText(animal_names[2])
                self.ui.probability3.setText(str(probabilities[2]))
                self.ui.animal4.setText(animal_names[3])
                self.ui.probability4.setText(str(probabilities[3]))
                self.ui.animal5.setText(animal_names[4])
                self.ui.probability5.setText(str(probabilities[4]))
                self.ui.animal6.setText(animal_names[5])
                self.ui.probability6.setText(str(probabilities[5]))

        # 设置 Land 的 UI 界面
        elif th_id == 2:
            width = self.ui.land_video.width()
            height = self.ui.land_video.height()
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.ui.land_video.setPixmap(scale_pix)

            # 设置 UI 界面 label 里的文字
            if result_dict:
                name = list(result_dict.values())[0]
                self.ui.land_name.setText(name)

        # 设置 Plant 的 UI 界面
        elif th_id == 3:
            width = self.ui.plant_video.width()
            height = self.ui.plant_video.height()
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.ui.plant_video.setPixmap(scale_pix)

            # 设置 UI 界面 label 里的文字
            if result_dict:
                plant_names = list(result_dict.keys())
                probabilities = list(result_dict.values())
                self.ui.plant1.setText(plant_names[0])
                self.ui.plant_pro1.setText(str(probabilities[0]))
                self.ui.plant2.setText(plant_names[1])
                self.ui.plant_pro2.setText(str(probabilities[1]))
                self.ui.plant3.setText(plant_names[2])
                self.ui.plant_pro3.setText(str(probabilities[2]))
