from PySide6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QAbstractItemView
from qfluentwidgets import (PushButton, LineEdit, ListWidget)


class TodoWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        self.setObjectName("todo-widget")
        self.setStyleSheet("background-color: #f3f4f6;")
        
        # 布局
        self.layout = QVBoxLayout(self)
        self.inputLayout = QHBoxLayout()
        
        # 输入控件
        self.taskInput = LineEdit(self)
        self.taskInput.setPlaceholderText("输入任务...")
        self.inputLayout.addWidget(self.taskInput, 1)
        
        # 添加按钮
        self.addButton = PushButton("添加", self)
        self.addButton.clicked.connect(self.addTask)
        self.inputLayout.addWidget(self.addButton)
        
        # 列表
        self.taskList = ListWidget(self)
        self.taskList.setSelectionMode(QAbstractItemView.MultiSelection)
        
        # 删除按钮
        self.deleteButton = PushButton("删除任务", self)
        self.deleteButton.setEnabled(False)  # 默认禁用
        self.deleteButton.clicked.connect(self.deleteTask)
        
        # 设置布局
        self.layout.addLayout(self.inputLayout)
        self.layout.addWidget(self.taskList)
        self.layout.addWidget(self.deleteButton)
        
        # 更新删除按钮状态
        self.taskList.itemSelectionChanged.connect(self.updateDeleteButton)


    # 添加任务
    def addTask(self):
        taskText = self.taskInput.text().strip()
        if taskText:
            self.taskList.addItem(taskText)
            self.taskInput.clear()


    # 删除任务
    def deleteTask(self):
        selectedItems = self.taskList.selectedItems()
        for item in selectedItems:
            self.taskList.takeItem(self.taskList.row(item))


    # 更新删除按钮状态
    def updateDeleteButton(self):
        if self.taskList.selectedItems():
            self.deleteButton.setEnabled(True)
        else:
            self.deleteButton.setEnabled(False)