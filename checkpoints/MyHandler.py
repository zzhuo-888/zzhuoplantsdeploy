"""
Module for image classification default handler
"""
import logging
import torch
import torch.nn.functional as F
import io
from PIL import Image
from torchvision import transforms
from ts.torch_handler.base_handler import BaseHandler

class MyHandler(BaseHandler):
    """
    ImageClassifier handler class. This handler takes an image
    and returns the name of object in that image.
    """
    def __init__(self, *args, **kwargs):
        super().__init__()   
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
        ])

    def preprocess_one_image(self, req):
        #对输入图片进行预处理操作（这表示单个图像）
        image = req.get("data")
        if image is None:
            image = req.get("body")
        image = Image.open(io.BytesIO(image))
        image = self.transform(image) #这个就是预处理操作
        image =image.unsqueeze(0)
        return image

    def preprocess(self, requests):
        #为应对同时处理多个图片，我们设计成多图片的预处理
        images = [self.preprocess_one_image(req) for req in requests]
        images = torch.cat(images)
        return images

    def inference(self, images):
        #推理，调用模型对输入进行预测，预测之后得到判断结果
        outs = self.model(images)
        probs = F.softmax(outs, dim=1)
        preds = torch.argmax(probs, dim=1)
        return preds

    def postprocess(self, preds):
       #输出，定义输出展示方式
        preds = preds.cpu().tolist()
        return preds