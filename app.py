from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from need.imgsr import preprocess, postprocess
import coremltools as ct
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 读取ui文件
        loader = QUiLoader()
        file = QFile("need/main.ui")
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file)
        file.close()
        self.ui.show()

        self.model_path = 'models/flexible.mlmodel'
        self.out = '/Users/ls/Desktop/output.jpg'

        # 绑定按钮事件
        self.ui.pb_init.clicked.connect(self.init_model)
        self.ui.pb_predict.clicked.connect(self.predict)
        self.ui.pb_choice.clicked.connect(self.choice)

        self.ui.pb_predict.setEnabled(False)
        self.ui.pb_choice.setEnabled(False)
    
    def init_model(self):
        self.model = ct.models.MLModel(self.model_path)
        # 设置按钮状态
        self.ui.pb_init.setEnabled(False)
        self.ui.pb_predict.setEnabled(True)
        self.ui.pb_choice.setEnabled(True)
    
    def predict(self):
        out = self.model.predict({'x': self.img})
        postprocess(out, self.out, self.source_shape)

    def choice(self):
        self.img_path, _ = QFileDialog.getOpenFileName(self, '选择图像', os.getcwd(), '图像文件(*.jpg *.png)')
        self.img, self.source_shape = preprocess(self.img_path)
        print(self.source_shape)        
        

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()