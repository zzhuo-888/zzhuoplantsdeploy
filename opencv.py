import cv2
import streamlit as st
import numpy as np
from PIL import Image
from test2 import *
import shutil

def brighten_image(image, amount):
    img_bright = cv2.convertScaleAbs(image, beta=amount)
    return img_bright


def blur_image(image, amount):
    blur_img = cv2.GaussianBlur(image, (11, 11), amount)
    return blur_img


def enhance_details(img):
    #shutil.rmtree('./data/twotest')
    #os.mkdir('./data/twotest')
    #os.mkdir('./data/twotest', 0o777)
    #img = Image.open(img)  # 读取图片
    save_path = './data/twotest/test.jpg'
    #img.save(save_path)  # 保存图片
    im = Image.fromarray(img)
    #im = Image.open(save_path)
    im.save(save_path)
    hdr=pridect(loadmodel("./checkpoints/best_model/resnet50/0/model_best.pth.tar"))
   # hdr=pridect("testimage.jpg", "./checkpoints/best_model/resnet50/0/model_best.pth.tar")
    #hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
    print("eee",hdr)
    return hdr


def main_loop():
    st.title("欢迎进入农作物健康识别系统")
    st.subheader("Welcome to the Crop Health Identification System!")
    st.text("本系统支持10种农作物50余种病虫害检测，欢迎您的使用")

    blur_rate = st.sidebar.slider("Blurring", min_value=0.5, max_value=3.5)
    brightness_amount = st.sidebar.slider("Brightness", min_value=-50, max_value=50, value=0)
    apply_enhancement_filter = st.sidebar.checkbox('Enhance Details')

    image_file = st.file_uploader("请上传植物叶片图像", type=['jpg', 'png', 'jpeg'])
    if not image_file:
        return None

    original_image = Image.open(image_file)
    original_image = np.array(original_image)

    processed_image = blur_image(original_image, blur_rate)
    processed_image = brighten_image(processed_image, brightness_amount)
    processed_image = enhance_details(processed_image)
    if apply_enhancement_filter:

        processed_image = enhance_details(processed_image)

    st.text("Original Image vs Processed Image")
    #st.image([original_image, processed_image])
    st.image(original_image)
    st.success(processed_image["test.jpg"])
    return processed_image["test.jpg"]
if __name__ == '__main__':
    main_loop()
