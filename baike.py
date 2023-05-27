import streamlit as st
import os
from PIL import Image
import random
import datetime
import time
def baike1():
    st.title("病虫害百科:dolphin:病害查询")
    genre = st.selectbox("系统目前支持苹果,玉米,樱桃,马铃薯,葡萄,柑桔,桃,辣椒,番茄与草莓植株病害查询",
        ['苹果植株', '玉米植株', '樱桃植株','马铃薯植株','葡萄植株','柑桔植株', '桃植株', '辣椒植株','番茄植株','草莓植株'],  # 也可以用元组
        index=0
    )
    st.write('你选择查询的是 :white_check_mark:{}.'.format(genre))
    #search = st.text_input('')
    # 将页面分为左中右三部分
    col1, col2 ,col3= st.columns(3)
    if genre == "苹果植株":
        st.balloons()
        with col1:
            imagelist = os.listdir('D:/plants_disease_classify-master/plants_disease_classify_pytorch/baike/apple/')
            print(imagelist)
            rootdir = "D:/plants_disease_classify-master/plants_disease_classify_pytorch/baike/apple/"
            for i in range(len(imagelist)):
                image = Image.open(rootdir + imagelist[i])
    #LABEL_NAMES = ["苹果健康", "苹果黑星病一般"]
                st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        with col2:
            LABEL_NAMES = [":point_right:1.苹果健康", ":point_right:2.苹果黑星病",":point_right:3.苹果黑星病",":point_right:4.苹果灰斑病",":point_right:5.苹果雪松锈",":point_right:6.苹果雪松锈"]
            LABEL_INFOS = ["这是与病虫害植株进行对照的健康组","此植株类别为损伤程度一般组","此植株类别为损伤程度严重组","此植株类别为损伤程度严重组","此植株类别为损伤程度一般组","此植株类别为损伤程度严重组"]
            for i in range(len(LABEL_NAMES)):
                st.title(LABEL_NAMES[i])
                st.title(LABEL_INFOS[i])
                st.title(":star2::star2::star2::star2::star2:")
        with col3:
            moreinfo =["苹果黑星病又称疮痂病。主要为害叶片或果实，还可为害叶柄、果柄、花芽、花器及新梢。从落花期到苹果成熟期均可为害。叶片染病，初现黄绿色圆形或放射状病斑，后变为褐色至黑色，直径3~ 6mm;上生一层黑褐色绒毛状霉，即病菌分生孢子梗及分生孢子。发病后期，多数病斑连在一起，致叶片扭曲变畸。嫩叶染病，表面呈粗糙羽毛状，中间产生黑霉或病斑，周围健全组织变厚，致病斑上凸，背面形成环状凹人。受害严重时叶变小，变厚，呈卷缩或扭曲状。",
                       "苹果灰斑病又名苹果叶斑病，是由梨叶点霉侵染所引起的、发生在苹果上的病害。主要危害叶片，也危害枝条、叶柄、嫩梢及果实。受害叶片一般不变黄脱落，但严重受害的叶片可出现焦枯现象；枝条受害常引起干枯死亡。",
                       "苹果锈病，又名赤星病、苹桧锈病、羊胡子，是由山田胶锈菌侵染所引起的、发生在苹果上的病害。主要为害叶片，也能为害嫩枝、幼果和果柄，还可为害转主寄主桧柏。往往造成早期落叶，弱树量。苹果锈病的流行与早春的气候密切相关，降雨频繁，气温较高易诱发此病流行。相反，春天干燥，虽降雨偏多，气温较低则发病较轻。"]

            #dbaike=st.session_state.date_time.date()
            dbaike=datetime.date.today()
            tbaike=datetime.datetime.now()
            tbaike = f'{tbaike}'.split('.')[0]
           # print(st.session_state.date_time)
            #st.title(f'查询日期为 {dbaike}')

            st.title(f'查询时间为 {tbaike}')
            st.title('以下为苹果病虫害详情信息')
            word = st.empty()
            # 文字占位符
            bar = st.progress(0)

            # 进度条
            for i in range(100):
                word.subheader('查询进度: ' + str(i + 1)+'％')
                bar.progress(i + 1)
                time.sleep(0.002)
            for i in range(len(moreinfo)):
                st.subheader(moreinfo[i])
                #st.subheader(":sparkles::sparkles::sparkles::sparkles::sparkles:")
    elif genre == "玉米植株":
        st.balloons()
        with col1:
            imagelist = os.listdir('D:/plants_disease_classify-master/plants_disease_classify_pytorch/baike/corn/')
            print(imagelist)
            rootdir = "D:/plants_disease_classify-master/plants_disease_classify_pytorch/baike/corn/"
            for i in range(len(imagelist)):
                image = Image.open(rootdir + imagelist[i])
                # LABEL_NAMES = ["苹果健康", "苹果黑星病一般"]
                st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB",
                         output_format="auto")
        with col2:
            LABEL_NAMES = [":point_right:1.玉米健康", ":point_right:2.玉米灰斑病", ":point_right:3.玉米灰斑病",
                           ":point_right:4.玉米锈病", ":point_right:5.玉米锈病", ":point_right:6.玉米叶斑病",":point_right:7.玉米叶斑病",":point_right:8.玉米花叶病"]

            LABEL_INFOS = ["这是与病虫害植株进行对照的健康组", "此植株类别为损伤程度一般组", "此植株类别为损伤程度严重组","此植株类别为损伤程度一般组", "此植株类别为损伤程度严重组", "此植株类别为损伤程度一般组",
                           "此植株类别为损伤程度严重组","此植株类别为损伤程度一般组"]
            for i in range(len(LABEL_NAMES)):
                st.title(LABEL_NAMES[i])
                st.title(LABEL_INFOS[i])
                st.title(":star2::star2::star2::star2::star2:")
        with col3:
            moreinfo = [
                "玉米灰斑病又称尾孢叶斑病、玉米霉斑病，除侵染玉米外，还可侵染高梁、香茅、须芒草等多种禾本科植物。玉米灰斑病是近年上升很快、为害较严重的病害之一。主要为害叶片。初在叶面上形成无明显边缘的椭圆形至矩圆形灰色至浅褐色病斑，后期变为褐色。病斑多限于平行叶脉之间，大小4～20×2～5(mm)。湿度大时，病斑背面生出灰色霉状物，即病菌分生孢子梗和分生孢子。",
                "玉米锈病是由玉米柄锈菌引起、发生在玉米的病害。主要发生在玉米叶片上，也能够侵染叶鞘、茎秆和苞叶。玉米锈病在中国的主要发生区域为北方夏玉米种植区；在华东、华南、西南等南方各省也有发生，但一般对生产影响有限。发病后，叶片被橘黄色的夏孢子堆和夏孢子所覆盖，导致叶片干枯死亡，轻者减产10 - 20 %，重者达30 % 以上，严重地块甚至绝收。玉米柄锈菌喜温暖潮湿的环境，发病温度范围15 - 35℃；最适发病环境温度为20 - 30℃，相对湿度95%以上；最适感病生育期为开花结穗到采收中后期。",
                "玉米叶斑病叶部病斑初为水渍状褪绿半透明小点，后扩大为圆形、椭圆形、梭形或长条形病斑，病斑长2-5毫米、宽1-2毫米，最大的可达7毫米×3毫米。病斑中心灰白色，边缘黄褐色或红褐色，外围有淡黄色晕圈，并具黄褐色相间的断续环纹。主要为害叶片和苞叶。病斑不规则、透光，中央灰白色，边缘褐色，上生黑色小点，即病原菌的子囊座。病菌子囊座生在叶片两面，散生或聚生，初埋生，具圆形孔口露在表皮外。子囊矩圆形，近棒形至囊形，大小35～55×7.5～8.5微米。子囊孢子矩圆形，无色，具隔膜1个，隔膜处稍缢缩。",
                "玉米矮花叶病毒是引起玉米矮花叶病的病原之一，严重危害包括玉米、高粱和甘蔗等作物在内的多种禾本科植物。玉米整个生育期均可感染。幼苗染病心叶基部细胞间出现椭圆形褪绿小点，断续排列成条点花叶状，并发展成黄绿相间的条纹症状，后期病叶叶尖的叶缘变红紫而干枯。发病重的叶片发黄，变脆，易折。病叶鞘、病果穗的苞叶也能现花叶状。发病早的，病株矮化明显。该病发生面积广，为害重。"
                 ]

            # dbaike=st.session_state.date_time.date()
            dbaike = datetime.date.today()
            tbaike = datetime.datetime.now()
            tbaike = f'{tbaike}'.split('.')[0]
            # print(st.session_state.date_time)
            st.title(f'查询日期为 {dbaike}')
            st.title(f'查询时间为 {tbaike}')
            word = st.empty()
            # 文字占位符
            bar = st.progress(0)

            # 进度条
            for i in range(100):
                word.subheader('查询进度: ' + str(i + 1) + '％')
                bar.progress(i + 1)
                time.sleep(0.002)
            for i in range(len(moreinfo)):
                st.subheader(moreinfo[i])
                # st.subheader(":sparkles::sparkles::sparkles::sparkles::sparkles:"
    elif genre == "樱桃植株":
        st.balloons()
        with col1:
            imagelist = os.listdir('D:/plants_disease_classify-master/plants_disease_classify_pytorch/baike/cherry/')
            print(imagelist)
            rootdir = "D:/plants_disease_classify-master/plants_disease_classify_pytorch/baike/cherry/"
            for i in range(len(imagelist)):
                image = Image.open(rootdir + imagelist[i])
    #LABEL_NAMES = ["苹果健康", "苹果黑星病一般"]
                st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        with col2:
            LABEL_NAMES = [":point_right:1.樱桃健康", ":point_right:2.樱桃白粉病",":point_right:3.樱桃白粉病"]
            LABEL_INFOS = ["这是与病虫害植株进行对照的健康组","此植株类别为损伤程度一般组","此植株类别为损伤程度严重组"]
            for i in range(len(LABEL_NAMES)):
                st.title(LABEL_NAMES[i])
                st.title(LABEL_INFOS[i])
                st.title(":star2::star2::star2::star2::star2:")
        with col3:
            moreinfo =["白粉病是一种农作物常见的病害，樱桃也会感染上白粉病，在感染上之后会在叶片出现一些白色状的粉状霉层，在一般的情况下叶片背面的白色粉状霉层比正面的多，然后再慢慢蔓延到果实，从而使果实的果面也出现白色粉状霉层，同时果实会出现表皮枯死、硬化、龟裂等症状，从而使樱桃出生早衰的现象，降低产量。 病害主要危害叶片，影响光合作用，削弱树势汇合成大粉斑，叶片大部分或全叶布满，重病时叶片前部出现白粉斑。病程后期叶片退绿、皱缩。"]
            #dbaike=st.session_state.date_time.date()
            dbaike=datetime.date.today()
            tbaike=datetime.datetime.now()
            tbaike = f'{tbaike}'.split('.')[0]
           # print(st.session_state.date_time)
            st.title(f'查询日期为 {dbaike}')
            st.title(f'查询时间为 {tbaike}')
            word = st.empty()
            # 文字占位符
            bar = st.progress(0)

            # 进度条
            for i in range(100):
                word.subheader('查询进度: ' + str(i + 1)+'％')
                bar.progress(i + 1)
                time.sleep(0.002)
            for i in range(len(moreinfo)):
                st.subheader(moreinfo[i])
                #st.subheader(":sparkles::sparkles::sparkles::sparkles::sparkles:")
    elif genre == "葡萄植株":
        st.balloons()
        with col1:
            imagelist = os.listdir('D:/plants_disease_classify-master/plants_disease_classify_pytorch/baike/grape/')
            print(imagelist)
            rootdir = "D:/plants_disease_classify-master/plants_disease_classify_pytorch/baike/grape/"
            for i in range(len(imagelist)):
                image = Image.open(rootdir + imagelist[i])
                # LABEL_NAMES = ["苹果健康", "苹果黑星病一般"]
                st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB",
                         output_format="auto")
        with col2:
            LABEL_NAMES = [
            ":point_right:1.葡萄健康", ":point_right:2.葡萄黑腐病", ":point_right:3.葡萄黑腐病",
            ":point_right:4.葡萄轮斑病", ":point_right:5.葡萄轮斑病", ":point_right:6.葡萄褐斑病", ":point_right:7.葡萄褐斑病"]
            LABEL_INFOS = ["这是与病虫害植株进行对照的健康组", "此植株类别为损伤程度一般组", "此植株类别为损伤程度严重组","此植株类别为损伤程度一般组", "此植株类别为损伤程度严重组","此植株类别为损伤程度一般组", "此植株类别为损伤程度严重组"]
            #st.title(":star2::star2::star2::star2::star2:")
            for i in range(len(LABEL_NAMES)):
                st.title(LABEL_NAMES[i])

                st.title(LABEL_INFOS[i])
                st.title(":star2::star2::star2::star2::star2:")
        with col3:
            moreinfo = [

                "黑腐病主要发生在果实、叶片、叶柄和新梢上。果实被害后发病初期产生紫褐色小斑点，逐渐扩大后，边缘褐色，中央灰白色，稍凹陷，发病果软烂，而后变为干缩僵果，有明显棱角，不易脱落，病果上生出许多黑色颗粒状小突起，即病菌的分生把子器或子囊壳。叶片发病时，初期产生红褐色小斑点，逐渐扩大成近圆形病斑，直径可达4~7厘米，中央灰白色，外缘褐色，边缘黑褐色，上面生出许多黑色小突起，排入成环状。新梢受害处生褐色椭圆形病斑，中央凹陷，其上生有黑色颗粒状小突起。",
                "葡萄轮斑病主要危害叶片。发病初期在叶面上出现红褐色圆形或不规则形病斑，后扩大为圆形或近圆形，叶面具深浅相间的轮纹，湿度大时叶背面长有浅褐色霉层。该病为真菌性病害，病原菌为葡萄生扁棒壳菌病原菌以子囊壳在落叶上越冬，第2年夏天温度上升、湿度加大时散发出子囊孢子，经气流传播到叶片。病原菌从叶背气孔侵入，发病后产出分生孢子进行再侵染。该病危害美洲种葡萄。因发病期较晚，对当年产量影响较轻，危害严重时引起早期落叶，影响越冬和下一季葡萄长势与结果。",
                "葡萄褐斑病又称葡萄斑点病、褐点病、叶斑病和角斑病等，是由葡萄假尾孢菌和葡萄座束梗尾孢引起、发生在葡萄上的一种病害。主要危害植株中下部叶片。葡萄褐斑病分布于中国各葡萄产区。多雨年份和管理粗放的果园易发生，特别是葡萄采收后忽视防治易引起病害大量发生，造成病叶早落，削弱树势，影响产量。"
             ]
            # dbaike=st.session_state.date_time.date()
            dbaike = datetime.date.today()
            tbaike = datetime.datetime.now()
            tbaike = f'{tbaike}'.split('.')[0]
            # print(st.session_state.date_time)
            st.title(f'查询日期为 {dbaike}')
            st.title(f'查询时间为 {tbaike}')
            word = st.empty()
            # 文字占位符
            bar = st.progress(0)

            # 进度条
            for i in range(100):
                word.subheader('查询进度: ' + str(i + 1) + '％')
                bar.progress(i + 1)
                time.sleep(0.002)
            for i in range(len(moreinfo)):
                st.subheader(moreinfo[i])
                # st.subheader(":sparkles::sparkles::sparkles::sparkles::sparkles:")

    elif genre == "柑桔植株":
        st.balloons()
        with col1:
            imagelist = os.listdir('D:/plants_disease_classify-master/plants_disease_classify_pytorch/baike/orange/')
            print(imagelist)
            rootdir = "D:/plants_disease_classify-master/plants_disease_classify_pytorch/baike/orange/"
            for i in range(len(imagelist)):
                image = Image.open(rootdir + imagelist[i])
    #LABEL_NAMES = ["苹果健康", "苹果黑星病一般"]
                st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        with col2:
            LABEL_NAMES = [":point_right:1.柑桔健康", ":point_right:2.柑桔黄龙病",":point_right:3.柑桔黄龙病"]
            LABEL_INFOS = ["这是与病虫害植株进行对照的健康组","此植株类别为损伤程度一般组","此植株类别为损伤程度严重组"]
            for i in range(len(LABEL_NAMES)):
                st.title(LABEL_NAMES[i])
                st.title(LABEL_INFOS[i])
                st.title(":star2::star2::star2::star2::star2:")
        with col3:
            moreinfo =[
                "柑橘类植物感染黄龙病菌后并不立即显症，存在潜伏期。潜伏期的长短因品种、树龄、健康状况、种植环境等而异但相比其他病原体，黄龙病菌的潜伏期较长。果实的典型症状是着色异常、果小、畸形。染病沙糖橘等宽皮柑橘的果实常表现为果蒂和果肩周围先褪绿转色，其它部位仍然为青绿色，且因蜡质形成受阻而无光泽。果农称之为“红鼻子果”。染病甜橙树的果实常表现为青果，病果的果汁味酸、淡，果实中心柱不正。叶片的典型症状是黄化、变小。据病程长短，叶片黄化有两种主要类型，一种是斑驳型黄化，一种是均匀黄化。"
               ]
            #dbaike=st.session_state.date_time.date()
            dbaike=datetime.date.today()
            tbaike=datetime.datetime.now()
            tbaike = f'{tbaike}'.split('.')[0]
           # print(st.session_state.date_time)
            st.title(f'查询日期为 {dbaike}')
            st.title(f'查询时间为 {tbaike}')
            word = st.empty()
            # 文字占位符
            bar = st.progress(0)

            # 进度条
            for i in range(100):
                word.subheader('查询进度: ' + str(i + 1)+'％')
                bar.progress(i + 1)
                time.sleep(0.002)
            for i in range(len(moreinfo)):
                st.subheader(moreinfo[i])
                #st.subheader(":sparkles::sparkles::sparkles::sparkles::sparkles:")
    elif genre == "柑桔植株":
        st.balloons()
        with col1:
            imagelist = os.listdir('D:/plants_disease_classify-master/plants_disease_classify_pytorch/baike/orange/')
            print(imagelist)
            rootdir = "D:/plants_disease_classify-master/plants_disease_classify_pytorch/baike/orange/"
            for i in range(len(imagelist)):
                image = Image.open(rootdir + imagelist[i])
    #LABEL_NAMES = ["苹果健康", "苹果黑星病一般"]
                st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        with col2:
            LABEL_NAMES = [":point_right:1.柑桔健康", ":point_right:2.柑桔黄龙病",":point_right:3.柑桔黄龙病"]
            LABEL_INFOS = ["这是与病虫害植株进行对照的健康组","此植株类别为损伤程度一般组","此植株类别为损伤程度严重组"]
            for i in range(len(LABEL_NAMES)):
                st.title(LABEL_NAMES[i])
                st.title(LABEL_INFOS[i])
                st.title(":star2::star2::star2::star2::star2:")
        with col3:
            moreinfo =[
                "柑橘类植物感染黄龙病菌后并不立即显症，存在潜伏期。潜伏期的长短因品种、树龄、健康状况、种植环境等而异但相比其他病原体，黄龙病菌的潜伏期较长。果实的典型症状是着色异常、果小、畸形。染病沙糖橘等宽皮柑橘的果实常表现为果蒂和果肩周围先褪绿转色，其它部位仍然为青绿色，且因蜡质形成受阻而无光泽。果农称之为“红鼻子果”。染病甜橙树的果实常表现为青果，病果的果汁味酸、淡，果实中心柱不正。叶片的典型症状是黄化、变小。据病程长短，叶片黄化有两种主要类型，一种是斑驳型黄化，一种是均匀黄化。"
               ]
            #dbaike=st.session_state.date_time.date()
            dbaike=datetime.date.today()
            tbaike=datetime.datetime.now()
            tbaike = f'{tbaike}'.split('.')[0]
           # print(st.session_state.date_time)
            st.title(f'查询日期为 {dbaike}')
            st.title(f'查询时间为 {tbaike}')
            word = st.empty()
            # 文字占位符
            bar = st.progress(0)

            # 进度条
            for i in range(100):
                word.subheader('查询进度: ' + str(i + 1)+'％')
                bar.progress(i + 1)
                time.sleep(0.002)
            for i in range(len(moreinfo)):
                st.subheader(moreinfo[i])
                #st.subheader(":sparkles::sparkles::sparkles::sparkles::sparkles:")
    elif genre == "桃植株":
        st.balloons()
        with col1:
            imagelist = os.listdir('D:/plants_disease_classify-master/plants_disease_classify_pytorch/baike/peach/')
            print(imagelist)
            rootdir = "D:/plants_disease_classify-master/plants_disease_classify_pytorch/baike/peach/"
            for i in range(len(imagelist)):
                image = Image.open(rootdir + imagelist[i])
                # LABEL_NAMES = ["苹果健康", "苹果黑星病一般"]
                st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB",
                         output_format="auto")
        with col2:
            LABEL_NAMES = [":point_right:1.桃健康", ":point_right:2.桃疮痂病病", ":point_right:3.桃疮痂病病"]
            LABEL_INFOS = ["这是与病虫害植株进行对照的健康组", "此植株类别为损伤程度一般组", "此植株类别为损伤程度严重组"]
            for i in range(len(LABEL_NAMES)):
                st.title(LABEL_NAMES[i])
                st.title(LABEL_INFOS[i])
                st.title(":star2::star2::star2::star2::star2:")
        with col3:
            moreinfo = [
                "主要为害果实，其次为害枝梢和叶片。果实发病开始出现褐色小圆斑，以后逐渐扩大为2～3毫米黑色点状，病斑多时汇集成片。由于病菌只为害病果表皮，使果皮停止生长，并木栓化，而果肉生长不受影响，所以，病情严重时经常发生裂果。枝梢发病初期产生褐色圆形病斑，后期病斑隆起，颜色加深，有时出现流胶现象。病菌只为害病枝表层，第2年树液流动时会产生小黑点，即病菌的分生孢子。"

            ]
            # dbaike=st.session_state.date_time.date()
            dbaike = datetime.date.today()
            tbaike = datetime.datetime.now()
            tbaike = f'{tbaike}'.split('.')[0]
            # print(st.session_state.date_time)
            st.title(f'查询日期为 {dbaike}')
            st.title(f'查询时间为 {tbaike}')
            word = st.empty()
            # 文字占位符
            bar = st.progress(0)

            # 进度条
            for i in range(100):
                word.subheader('查询进度: ' + str(i + 1) + '％')
                bar.progress(i + 1)
                time.sleep(0.002)
            for i in range(len(moreinfo)):
                st.subheader(moreinfo[i])
                # st.subheader(":sparkles::sparkles::sparkles::sparkles::sparkles:")

    elif genre == "桃植株":
        st.balloons()
        with col1:
            imagelist = os.listdir('D:/plants_disease_classify-master/plants_disease_classify_pytorch/baike/peach/')
            print(imagelist)
            rootdir = "D:/plants_disease_classify-master/plants_disease_classify_pytorch/baike/peach/"
            for i in range(len(imagelist)):
                image = Image.open(rootdir + imagelist[i])
                # LABEL_NAMES = ["苹果健康", "苹果黑星病一般"]
                st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB",
                         output_format="auto")
        with col2:
            LABEL_NAMES = [":point_right:1.桃健康", ":point_right:2.桃疮痂病", ":point_right:3.桃疮痂病"]
            LABEL_INFOS = ["这是与病虫害植株进行对照的健康组", "此植株类别为损伤程度一般组", "此植株类别为损伤程度严重组"]
            for i in range(len(LABEL_NAMES)):
                st.title(LABEL_NAMES[i])
                st.title(LABEL_INFOS[i])
                st.title(":star2::star2::star2::star2::star2:")
        with col3:
            moreinfo = [
                "主要为害果实，其次为害枝梢和叶片。果实发病开始出现褐色小圆斑，以后逐渐扩大为2～3毫米黑色点状，病斑多时汇集成片。由于病菌只为害病果表皮，使果皮停止生长，并木栓化，而果肉生长不受影响，所以，病情严重时经常发生裂果。枝梢发病初期产生褐色圆形病斑，后期病斑隆起，颜色加深，有时出现流胶现象。病菌只为害病枝表层，第2年树液流动时会产生小黑点，即病菌的分生孢子。"

            ]
            # dbaike=st.session_state.date_time.date()
            dbaike = datetime.date.today()
            tbaike = datetime.datetime.now()
            tbaike = f'{tbaike}'.split('.')[0]
            # print(st.session_state.date_time)
            st.title(f'查询日期为 {dbaike}')
            st.title(f'查询时间为 {tbaike}')
            word = st.empty()
            # 文字占位符
            bar = st.progress(0)

            # 进度条
            for i in range(100):
                word.subheader('查询进度: ' + str(i + 1) + '％')
                bar.progress(i + 1)
                time.sleep(0.002)
            for i in range(len(moreinfo)):
                st.subheader(moreinfo[i])
                # st.subheader(":sparkles::sparkles::sparkles::sparkles::sparkles:")
    elif genre == "辣椒植株":
        st.balloons()
        with col1:
            imagelist = os.listdir('D:/plants_disease_classify-master/plants_disease_classify_pytorch/baike/lajiao/')
            print(imagelist)
            rootdir = "D:/plants_disease_classify-master/plants_disease_classify_pytorch/baike/lajiao/"
            for i in range(len(imagelist)):
                image = Image.open(rootdir + imagelist[i])
                # LABEL_NAMES = ["苹果健康", "苹果黑星病一般"]
                st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB",
                         output_format="auto")
        with col2:
            LABEL_NAMES = [":point_right:1.辣椒健康", ":point_right:2.辣椒疮痂病", ":point_right:3.辣椒疮痂病"]
            LABEL_INFOS = ["这是与病虫害植株进行对照的健康组", "此植株类别为损伤程度一般组", "此植株类别为损伤程度严重组"]
            for i in range(len(LABEL_NAMES)):
                st.title(LABEL_NAMES[i])
                st.title(LABEL_INFOS[i])
                st.title(":star2::star2::star2::star2::star2:")
        with col3:
            moreinfo = [
                "主要为害叶片、茎蔓、果实，尤以叶片上发生普遍。苗期发病，子叶上产生银白死小斑点，水渍状，后变为暗色凹陷病斑。如防治不及时，常引起全部落叶，植株死亡。成株期一般在开花盛期开始发病。叶片发病，初期形成水渍状、黄绿色的小斑点，扩大后变成圆形或不规则形，暗褐色，边缘隆起，中央凹陷的病斑，粗糙呈疮痂状。严重时叶片变黄、干枯、破裂，早期脱落。茎部和果梗发病，初期形成水渍状斑点，渐发展成褐色短条斑。病斑木栓化隆起，纵裂呈溃疡状疮痂斑。果实发病，形成圆形或长圆形的黑色疮痂斑。潮湿时病斑上有菌脓溢出。"
            ]
            # dbaike=st.session_state.date_time.date()
            dbaike = datetime.date.today()
            tbaike = datetime.datetime.now()
            tbaike = f'{tbaike}'.split('.')[0]
            # print(st.session_state.date_time)
            st.title(f'查询日期为 {dbaike}')
            st.title(f'查询时间为 {tbaike}')
            word = st.empty()
            # 文字占位符
            bar = st.progress(0)

            # 进度条
            for i in range(100):
                word.subheader('查询进度: ' + str(i + 1) + '％')
                bar.progress(i + 1)
                time.sleep(0.002)
            for i in range(len(moreinfo)):
                st.subheader(moreinfo[i])
                # st.subheader(":sparkles::sparkles::sparkles::sparkles::sparkles:")
    elif genre == "马铃薯植株":
        st.balloons()
        with col1:
            imagelist = os.listdir('D:/plants_disease_classify-master/plants_disease_classify_pytorch/baike/potato/')
            print(imagelist)
            rootdir = "D:/plants_disease_classify-master/plants_disease_classify_pytorch/baike/potato/"
            for i in range(len(imagelist)):
                image = Image.open(rootdir + imagelist[i])
                # LABEL_NAMES = ["苹果健康", "苹果黑星病一般"]
                st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB",
                         output_format="auto")
        with col2:
            LABEL_NAMES = [":point_right:1.马铃薯健康", ":point_right:2.马铃薯早疫", ":point_right:3.马铃薯早疫",":point_right:4.马铃薯晚疫", ":point_right:5.马铃薯晚疫"]
            LABEL_INFOS = ["这是与病虫害植株进行对照的健康组", "此植株类别为损伤程度一般组", "此植株类别为损伤程度严重组","此植株类别为损伤程度一般组", "此植株类别为损伤程度严重组"]
            for i in range(len(LABEL_NAMES)):
                st.title(LABEL_NAMES[i])
                st.title(LABEL_INFOS[i])
                st.title(":star2::star2::star2::star2::star2:")
        with col3:
            moreinfo = [
                "马铃薯早疫病俗称夏疫病、轮纹病或干斑病，是由茄链格孢引起、发生于马铃薯的一种病害。此病主要危害马铃薯叶片，也可侵染块茎。 此病主要为害叶片，也能侵害叶柄、茎和薯块。在叶上病斑最初为褐色圆形斑点，以后逐渐扩大成圆至近圆形，褐色至暗褐色，病斑边缘明显，有清晰的同心轮纹，有时病斑外缘有较窄的黄色晕圈。病斑上可产生少许黑色霉状物。发病多时病斑可连接成不规则大形枯斑，使叶片局部枯死，严重时叶片全部枯死。但仍能看出有轮纹的病斑轮廓，因而易于与其他病害辨认。",
                "马铃薯晚疫病是由致病疫霉引起、发生于马铃薯的一种病害。此病主要危害马铃薯茎、叶和块茎。也能够侵染花蕾、浆果。 马铃薯晚疫病是马铃薯的主要病害之一。晚疫病发生在马铃薯的叶、茎和薯块上。叶片发病，起初造成形状不规则的黄褐色斑点，没有整齐的界限。气候潮湿时，病斑迅速扩大，其边缘呈水渍状，有一圈白色霉状物，在叶的背面，长有茂密的白霉，形成霉轮，这是马铃薯晚疫病的特征。在干燥时，病斑停止扩展，病部变褐变脆，病斑边缘亦不产生白霉。"

            ]
            # dbaike=st.session_state.date_time.date()
            dbaike = datetime.date.today()
            tbaike = datetime.datetime.now()
            tbaike = f'{tbaike}'.split('.')[0]
            # print(st.session_state.date_time)
            st.title(f'查询日期为 {dbaike}')
            st.title(f'查询时间为 {tbaike}')
            word = st.empty()
            # 文字占位符
            bar = st.progress(0)

            # 进度条
            for i in range(100):
                word.subheader('查询进度: ' + str(i + 1) + '％')
                bar.progress(i + 1)
                time.sleep(0.002)
            for i in range(len(moreinfo)):
                st.subheader(moreinfo[i])
                # st.subheader(":sparkles::sparkles::sparkles::sparkles::sparkles:")
    elif genre == "草莓植株":
        st.balloons()
        with col1:
            imagelist = os.listdir('D:/plants_disease_classify-master/plants_disease_classify_pytorch/baike/strawberry/')
            print(imagelist)
            rootdir = "D:/plants_disease_classify-master/plants_disease_classify_pytorch/baike/strawberry/"
            for i in range(len(imagelist)):
                image = Image.open(rootdir + imagelist[i])
                # LABEL_NAMES = ["苹果健康", "苹果黑星病一般"]
                st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB",
                         output_format="auto")
        with col2:
            LABEL_NAMES = [":point_right:1.草莓健康", ":point_right:2.草莓叶枯病", ":point_right:3.草莓叶枯病"]
            LABEL_INFOS = ["这是与病虫害植株进行对照的健康组", "此植株类别为损伤程度一般组", "此植株类别为损伤程度严重组"]
            for i in range(len(LABEL_NAMES)):
                st.title(LABEL_NAMES[i])
                st.title(LABEL_INFOS[i])
                st.title(":star2::star2::star2::star2::star2:")
        with col3:
            moreinfo = [
                "果梗也可染病。叶枯病属低温、高湿性病害，多在春秋季发病，初发病时，叶面上产生紫褐色无光泽小斑点，以后逐渐扩大成不规则形病斑。病斑多沿主侧叶脉分布，发病重时整个叶面布满病斑，发病后期全叶黄褐色至暗褐色，直至枯死。叶柄或果柄发病后，病斑呈黑褐色，微凹陷，脆而易折。叶枯病病源为风梨草莓褐斑病菌，以子囊壳或分生孢子在病组织上越冬，春季释放出子囊壳或分生孢子，借风力传播。秋季和早春雨露较多的天气有利于浸染发病，一般健壮苗发病轻，弱苗发病重。"
            ]
            # dbaike=st.session_state.date_time.date()
            dbaike = datetime.date.today()
            tbaike = datetime.datetime.now()
            tbaike = f'{tbaike}'.split('.')[0]
            # print(st.session_state.date_time)
            st.title(f'查询日期为 {dbaike}')
            st.title(f'查询时间为 {tbaike}')
            word = st.empty()
            # 文字占位符
            bar = st.progress(0)

            # 进度条
            for i in range(100):
                word.subheader('查询进度: ' + str(i + 1) + '％')
                bar.progress(i + 1)
                time.sleep(0.002)
            for i in range(len(moreinfo)):
                st.subheader(moreinfo[i])
                # st.subheader(":sparkles::sparkles::sparkles::sparkles::sparkles:")