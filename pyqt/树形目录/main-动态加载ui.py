from PyQt5 import  QtWidgets
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import  QFileSystemModel,QMenu,QAction
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5.QtCore import Qt




class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        loadUi('form1.ui', self)


        # 将按钮点击事件和槽函数绑定
        #显示文件系统
        self.pushButton.clicked.connect(self.file)
        #显示自定义树
        self.pushButton_2.clicked.connect(self.my_tree)
        self.treeView.clicked.connect(self.tree_cilcked)

        #创建右键菜单
        self.createContextMenu()



    # 定义槽函数
    def file(self):
        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.treeView.setModel(self.model)



    

    def my_tree(self):
        items={'父节点1':None,'父节点2':{"子节点1":None,"子节点2":None},'父节点3':None}

        #构造tree模型
        def CreatTreeModel(items):
            #创建空模型
            model1 = QStandardItemModel()
            # 获取模型顶级节点的地址
            root_node = model1.invisibleRootItem()
            #采用递归函数构造tree模型
            def recursion(items=items, model=model1, node=root_node):
                for (x, y) in items.items():
                    # 设置子节点
                    model.branch = QStandardItem(x)
                    # 子节点不可修改
                    model.branch.setEditable(False)
                    # 添加子节点
                    node.appendRow(model.branch)
                    # 如果有孙节点，继续添加孙节点
                    if y != None:
                        recursion(y, model.branch, model.branch)
            recursion(items)
            return model1

        model2=CreatTreeModel(items)
        #绑定模型到控件
        self.treeView.setModel(model2)


    def tree_cilcked(self, Qmodelidx):
        print(Qmodelidx.internalPointer)


    #在treeview内创建右键菜单
    def createContextMenu(self):
        # 必须将对象的ContextMenuPolicy属性设置为Qt.CustomContextMenu， 否则无法使用customContextMenuRequested信号
        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)

        # 将右键点击事件和槽函数绑定
        self.treeView.customContextMenuRequested.connect(self.showContextMenu)

        # 创建QMenu
        self.treeView.contextMenu = QMenu(self)
        # 将动作与处理函数相关联
        # 这里为了简单，将所有action与同一个处理函数相关联，
        # 当然也可以将他们分别与不同函数关联，实现不同的功能
        self.treeView.contextMenu.addAction(QAction(u"动作A", self, triggered=self.actionHandler))
        self.treeView.contextMenu.addAction(QAction(u"动作B", self, triggered=self.actionHandler))
        self.treeView.contextMenu.addAction(QAction(u"动作C", self, triggered=self.actionHandler))



    #右键点击时调用的函数
    def showContextMenu(self, pos):
        # 菜单显示前，将它移动到鼠标点击的位置
        self.treeView.contextMenu.move(self.pos() + pos)
        self.treeView.contextMenu.show()

 
    #菜单中的具体action调用的函数
    def actionHandler(self):
        print('action handler')

	

if __name__ == "__main__":
    # 创建了一个PyQt封装的QApplication对象,创建的时候,把系统参数传进去了.顾名思义,这一句创建了一个应用程序对象
    app = QtWidgets.QApplication(sys.argv)
    # #创建一个我们生成的那个窗口，注意把类名修改为MainWindow
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
