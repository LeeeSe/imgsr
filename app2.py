from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import QThread
from need.imgsr import preprocess, postprocess
from need.ui_main import Ui_MainWindow
import coremltools as ct
import os
import sys

class init_model_thread(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        self.parent.load_model()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # # 读取ui文件
        # loader = QUiLoader()
        # file = QFile("need/main.ui")
        # file.open(QFile.ReadOnly)
        # self.ui = loader.load(file)
        # file.close()
        self.setupUi(self)
        self.show()

        self.init_model_thread = init_model_thread(parent=self)

        self.current_path = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.user_path = os.path.expanduser('~')
        self.model_path = os.path.join(self.current_path, 'models/flexible.mlmodel')
        self.out = os.path.join(self.user_path, 'Desktop/out.jpg')

        # 绑定按钮事件
        self.pb_init.clicked.connect(self.init_model)
        self.pb_predict.clicked.connect(self.predict)
        self.pb_choice.clicked.connect(self.choice)

        self.pb_predict.setEnabled(False)
        self.pb_choice.setEnabled(False)
    
    def init_model(self):
        # 设置按钮状态
        self.pb_init.setEnabled(False)
        # 设置标签
        self.label_now.setText('加载中')
        # 加载模型
        self.init_model_thread.start()

    def load_model(self):
        try:
            self.model = ct.models.MLModel(self.model_path)
            # 设置按钮状态
            self.pb_predict.setEnabled(True)
            self.pb_choice.setEnabled(True)
            # 设置标签
            self.label_now.setText('请选择图片')
        except:
            self.pb_init.setEnabled(True)
            self.pb_predict.setEnabled(False)
            self.pb_choice.setEnabled(False)
            self.label_now.setText('加载失败')

    def predict(self):
        out = self.model.predict({'x': self.img})
        postprocess(out, self.out, self.source_shape)
        # 设置标签
        self.label_now.setText('完成')

    def choice(self):
        self.img_path, _ = QFileDialog.getOpenFileName(self, '选择图像', os.getcwd(), '图像文件(*.jpg *.png *.jpeg)')
        self.img, self.source_shape = preprocess(self.img_path)
        # 设置标签
        self.label_now.setText('请开始优化')
        print(self.source_shape)        
        

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()