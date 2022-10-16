# 测试mlmodel
import coremltools as ct
import cv2
import numpy as np


# 初始化模型
def init_model(model_path):
    model = ct.models.MLModel(model_path)
    return model

# 预处理
def preprocess(img_path):
    # 以三通道读取图片
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    source_shape = img.shape
    img = cv2.resize(img, (256, 256))
    img = img.transpose(2, 0, 1)
    img = img[np.newaxis, :, :, :]
    img = img / 255.0
    return img, source_shape

# 后处理
def postprocess(out, save_path, source_shape):
    out_img = out['var_4053'][0]
    out_img = out_img.transpose(1, 2, 0)
    out_img = out_img * 255.0
    # 归一化到0-255
    out_img = (out_img - np.min(out_img)) / (np.max(out_img) - np.min(out_img)) * 255
    out_img = out_img.astype(np.uint8)
    out_img = cv2.resize(out_img, (source_shape[1], source_shape[0]))
    cv2.imwrite(save_path, out_img)

# 获取cmd参数
def get_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, default='models/flexible.mlmodel', help='model path')
    parser.add_argument('--img', type=str, default='test.jpg', help='image path')
    parser.add_argument('--out', type=str, default='/Users/ls/Desktop/output.jpg', help='output path')
    args = parser.parse_args()
    return args

# 主函数
def main():
    args = get_args()
    model = init_model(args.model)
    img, source_shape = preprocess(args.img)
    out = model.predict({'x': img})
    postprocess(out, args.out, source_shape)


if __name__ == '__main__':
    main()


