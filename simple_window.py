import sys

from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    #创建QApplication类的实例
    app = QApplication(sys.argv)
    #创建一个窗口
    w = QWidget()
    #设置窗口属性
    #设置窗口尺寸
    w.resize(500,500)
    #设置窗口可移动
    w.move(300,300)
    #设置窗口的标题
    w.setWindowTitle("简单的基于PyQt5的桌面应用")
    #显示窗口
    w.show()
    #进入程序主循环，并通过exit函数确保安全结束
    sys.exit(app.exec_())