from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QVBoxLayout,QPushButton,QStyle
from PyQt5.QtGui import QPixmap
import sys
#面向对象的方法来开发
class VideoBox(QWidget):
    #初始化界面
    def __init__(self):
        #把父类界面继承过来
        QWidget.__init__(self)
        #定义一个图片标签类QLabel
        self.pictureLabel=QLabel()
        #定义一个像素图片类QPixmap
        init_image=QPixmap("resources/sssss.jpg")
        #将实例化的图片标签类加载实例化的像素图片类内容
        self.pictureLabel.setPixmap(init_image)
        # 把按钮加到桌面上
        self.playButton = QPushButton()
        # 设置按钮有效
        self.playButton.setEnabled(True)
        # 设置图标
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        # 把点击动作发生在按钮上,clicked点击,connect表示点击后执行哪一个函数
        self.playButton.clicked.connect(self.switch_image)
        # 做布局,指明布局方向，有的布局横向QHBoxLayout 纵向布局 QVBoxLayout
        layout1=QVBoxLayout()
        #将实例化的图片标签类添加到纵向布局中
        layout1.addWidget(self.pictureLabel)
        # 将实例化的按钮类添加到纵向布局中
        layout1.addWidget(self.playButton)
        #添加布局layout1到QWidget的桌面窗口上
        self.setLayout(layout1)
    def switch_image(self):
        other_image = QPixmap("resources/kkkkk.jpg")
        self.pictureLabel.setPixmap(other_image)

if __name__=="__main__":
    #定义app
    app=QApplication(sys.argv)
    #定义的界面类实例化
    mv=VideoBox()
    #显示窗口
    mv.show()
    #安全退出
    sys.exit(app.exec_())