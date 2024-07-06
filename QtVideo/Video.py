from PyQt5.QtCore import QThread, pyqtSignal
import cv2 as cv
from AI.AI_total import ai_plant, ai_animal, ai_landmark

# 定义一个继承自 QThread 的视频处理线程类
class Video(QThread):
    # 定义一个信号，用于发送处理后的视频帧和结果
    send = pyqtSignal(int, int, int, bytes, int, object)

    def __init__(self, video_name):
        super().__init__()
        # 初始化视频处理线程
        self.th_id = 0  # 初始化线程 ID

        # 根据视频文件名设置线程 ID
        if video_name == 'data/动物视频.mp4':
            self.th_id = 1
        elif video_name == 'data/地标视频.mp4':
            self.th_id = 2
        elif video_name == 'data/植物视频.mp4':
            self.th_id = 3
        else:
            self.th_id = -1

        # 打开视频文件
        self.dev = cv.VideoCapture(video_name)
        if not self.dev.isOpened():
            print(f"Failed to open video: {video_name}")
            return

    def run(self):
        # 处理视频帧
        while True:
            # 获取视频帧
            ret, frame = self.dev.read()
            if not ret:
                print('no')
                break  # 结束循环

            # 根据线程 ID 处理视频帧并获取结果字典
            if self.th_id == 1:
                result_dict = ai_animal(frame)
            elif self.th_id == 2:
                result_dict = ai_landmark(frame)
            elif self.th_id == 3:
                result_dict = ai_plant(frame)
            else:
                result_dict = {}

            # 获取帧的高、宽和通道数
            h, w, c = frame.shape
            img_bytes = frame.tobytes()  # 将帧转换为字节数组
            # 发射信号，将处理后的帧和结果发送给主线程
            self.send.emit(h, w, c, img_bytes, self.th_id, result_dict)
            QThread.usleep(10000)  # 模拟帧间延迟，单位为微秒（这里是10毫秒）

# 示例调用方式（放在另一个模块中）
# video_thread = Video('data/动物视频.mp4')
# video_thread.send.connect(handle_frame)  # 连接信号与槽函数
# video_thread.start()  # 开始线程
