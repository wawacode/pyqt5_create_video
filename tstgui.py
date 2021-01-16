from PyQt5.QtCore import  *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
#面向对象的方法来开发
class VideoBox(QWidget):
    #初始化界面
    def __init__(self):
        #把父类界面继承过来
        QWidget.__init__(self)
        #设置一个交换图片的标识位
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
    def switch_video(self):
        if self.status:
            other_image=QPixmap("resources/kkkkk.jpg")
            self.pictureLabel.setPixmap(other_image)
        else:
            other_image = QPixmap("resources/sssss.jpg")
            self.pictureLabel.setPixmap(other_image)
        self.status=not self.status
if __name__=="__main__":
    #定义app
    app=QApplication(sys.argv)
    #定义的界面类实例化
    mv=VideoBox()
    mv.show()
    sys.exit(app.exec_())



