import torch
import torchvision
import torch.nn.functional as F
from torch import nn
from config import config
import torchvision.transforms as transforms
from PIL import Image
from model import *
from tqdm import tqdm
from torch.autograd import Variable
from collections import OrderedDict
from dataloader import *
from torch.utils.data import DataLoader
import streamlit as st
@st.cache
def loadmodel(modelPath):
    pmodel = get_net()
    # model = torch.nn.DataParallel(model)
    #pmodel.cuda()
    pmodel.eval()
    #best_model = torch.load(modelPath)
    best_model = torch.load(modelPath, map_location=lambda storage, loc: storage)
    pmodel.load_state_dict(best_model["state_dict"])
    return pmodel
def pridect( pmodel):
    '''
    预测函数
    :param imagePath: 图片路径
    :param modelPath: 模型路径
    :return:
    '''
    # 1. 读取图片
    image = Image.open(imagePath)
    # 2. 进行缩放
  #  image = image.resize(config.img_height,config.img_weight)
    #image.show()
    # 3. 加载模型
    #model = torch.load(modelPath)
    #model=model.load_state_dict(model)

    #model = model.to(Common.device)
   # model= model.to(torch.device("cuda:0" if torch.cuda.is_available() else "cpu"))


#######
    csv_map = OrderedDict({"filename": [], "probability": []})
    test_files = get_files(config.test_two_data, "test")

    test_loader = DataLoader(ChaojieDataset(test_files, test=True), batch_size=1, shuffle=False, pin_memory=False)
    pred_dict={}
    with open("./submit/baseline.json", "w", encoding="utf-8") as f:
        submit_results = []
        for i, (input, filepath) in enumerate(tqdm(test_loader)):
            # 3.2 change everything to cuda and get only basename
            filepath = [os.path.basename(x) for x in filepath]
            with torch.no_grad():
                image_var = Variable(input)
                # 3.3.output
                # print(filepath)
                # print(input,input.shape)
                y_pred = pmodel(image_var)
                # print(y_pred.shape)
                smax = nn.Softmax(1)
                smax_out = smax(y_pred)
            # 3.4 save probability to csv files
            csv_map["filename"].extend(filepath)
            for output in smax_out:
                prob = ";".join([str(i) for i in output.data.tolist()])
                csv_map["probability"].append(prob)
        result = pd.DataFrame(csv_map)

        result["probability"] = result["probability"].map(lambda x: [float(i) for i in x.split(";")])
        for index, row in result.iterrows():
            pred_label = np.argmax(row['probability'])
            pred_acc = row['probability'][pred_label]
            if pred_label > 43:
                pred_label = pred_label + 2
            print( row['filename'], config.LABEL_NAMES[pred_label])
            pred_dict.update({row['filename']: config.LABEL_NAMES[pred_label]})
    return pred_dict



if __name__ == '__main__':
    #loadmodel("./checkpoints/best_model/resnet50/0/model_best.pth.tar")
    pridect(loadmodel("./checkpoints/best_model/resnet50/0/model_best.pth.tar"))
