from PyQt5.QtCore import  *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from cv2 import *
import time;
#面向对象的方法来开发
class VideoBox(QWidget):
    #初始化界面
    def __init__(self):
        #把父类界面继承过来
        QWidget.__init__(self)
        #设置一个播放和暂停的状态值
        self.status=True
        self.pictureLabel=QLabel()
        init_image=QPixmap("resources/sssss.jpg")
        self.pictureLabel.setPixmap(init_image)
        #把按钮加到桌面上
        self.playButton=QPushButton()
        #设置按钮有效
        self.playButton.setEnabled(True)
        #设置图标
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        #把点击动作发生在按钮上,clicked点击,connect表示点击后执行哪一个函数
        self.playButton.clicked.connect(self.switch_video)

        #做布局,指明布局方向，有的布局横向QHBoxLayout 纵向布局 QVBoxLayout
        layout1=QVBoxLayout()
        layout1.addWidget(self.pictureLabel)
        layout1.addWidget(self.playButton)
        self.setLayout(layout1)
        #定义全局视频
        self.playCapture = VideoCapture("resources/test.mp4")
        #定义定时器
        self.timer=VideoTimer()
        self.timer.timeSignal.signal[str].connect(self.show_video)
    def show_video(self):
        if self.playCapture.isOpened():
            # cv2读取视频时会显示出成功或失败，后跟视频图像的ndarray
            success, frame = self.playCapture.read()
            print(success)
            if success:
                height, width = frame.shape[:2]
                print(width, height)
                # 格式的问题
                if frame.ndim == 3:
                    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                elif frame.ndim == 2:
                    rgb = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
                image = QImage(rgb.flatten(), width, height, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(image)
                self.pictureLabel.setPixmap(pixmap)
    def switch_video(self):
        if self.status:
            self.timer.start()
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.timer.stop()
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        #状态值的互联交替取反
        self.status= not self.status
#封装pyqtSignal信号
class Communicate(QObject):
    signal=pyqtSignal(str)
class VideoTimer(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.timeSignal=Communicate()
        self.mutex=QMutex()
    def run(self):
        with QMutexLocker(self.mutex):
            self.stopped=False
        while True:

            if self.stopped==True:
                return
            #发送信号给视频要求更新,emit发送信号
            self.timeSignal.signal.emit("1")
            #时间延迟
            time.sleep(1/10)
    def stop(self):
        with QMutexLocker(self.mutex):
            self.stopped=True

if __name__=="__main__":
    #定义app
    app=QApplication(sys.argv)
    #定义的界面类实例化
    mv=VideoBox()
    mv.show()
    sys.exit(app.exec_())



