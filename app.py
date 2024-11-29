import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from qfluentwidgets import (FluentWindow, FluentIcon as FIF, NavigationItemPosition)
from widgets.todo import TodoWidget


class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        # 设置标题和图标
        self.setWindowIcon(QIcon('./resources/icon.png'))
        self.setWindowTitle("Maple Apps")
        
        # 创建子界面实例
        self.todoWidget = TodoWidget(self)
        
        # 添加子界面
        self.addSubInterface(self.todoWidget, FIF.QUICK_NOTE, 'Todo', NavigationItemPosition.SCROLL)


def main():
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()