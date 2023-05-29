import streamlit as st
import pytz
from firstpage import *
from mail import *
from opencv import *
import streamlit as st
from  baike import *
from sqlalchemy.sql import text
from st_aggrid import AgGrid
import sys
import requests
st.set_page_config(page_title="YSU-农作物健康识别系统",layout="wide")
conn = st.experimental_connection('mysql', type='sql')
c=conn.session

#def add_userdata(username, password):
def add_userdata(username, password, flag, number, mail):
    users = {'username': username, 'password': password,'flag':flag,'number':number,'mail':mail}
    if len(conn.query('SELECT username FROM userstable WHERE username =:username1;', params=dict(username1=users['username'])))==1:

        st.warning("用户名已存在，请更换一个新的用户名。")
    else:
       # users = {'username': username, 'password': password, 'flag': flag, 'number': number, 'mail': mail}
        # pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
        c = conn.session
        c.execute(text(
            'INSERT INTO userstable(username,password,flag,number,mail) VALUES(:username1,:password1,:flag1,:number1,:mail1);'),
                  params=dict(username1=users['username'], password1=users['password'], flag1=users['flag'],
                              number1=users['number'], mail1=users['mail']))
        c.commit()
        st.success("恭喜，您已成功注册。")
        st.info("请在左侧选择“登录”选项进行登录。")



def login_user(username,password):
    users={'username':username,'password':password}
    data=conn.query('SELECT flag FROM userstable WHERE username =:username1;',params=dict(username1=users['username']))
    fdata = [tuple(x) for x in data.values]
    #if fdata!='':
    if(len(fdata)!=0):
        if fdata[0][0]!='2':
            data=conn.query('SELECT * FROM userstable WHERE username =:username1 AND password= :password1;',params=dict(username1=users['username'],password1=users['password']))
            #data=c.commit()

            if len(data)==1:
                data = [tuple(x) for x in data.values]
                return data
            else:
                st.warning("账号密码输入错误，请重新登录。")
        else:
           st.warning("用户已进入黑名单，限制登录，详情请咨询管理员。")
    else:
        st.warning("没有该用户，请您先注册。")

def view_all_users():
    data = conn.query('SELECT * from userstable;', ttl=600)
    data = [tuple(x) for x in data.values]
    return data
def view_one_users(username):
    users = {'username': username}
    data = conn.query('SELECT * FROM userstable WHERE username =:username1;',
                      params=dict(username1=users['username']))

    data = [tuple(x) for x in data.values]
    return data

def show_slove(dname1):##病虫害信息及防治措施
    dname = {'dname': dname1}
    data=conn.query('SELECT * FROM information WHERE dname=:dname1;',params=dict(dname1=dname['dname']))
    data = [tuple(x) for x in data.values]
    #st.write(data)
    return data
def show_search():##所有浏览记录
    data=conn.query('SELECT * FROM search;')
    data = [tuple(x) for x in data.values]
    #data=c.fetchall()
    #print("数据是",data)
    return data

def change_users(users,pd,fg):

   #print("数据111222是",password,username)
    if fg=="管理员用户":
        fg=0
    elif fg=="普通用户":
        fg=1
    else:
        fg=2
    changes = {'username': users, 'password': pd, 'flag': fg}
    #st.write(changes)
    # print(changes['username'],changes['password'],changes['flag'])
    c = conn.session
    c.execute(text('UPDATE userstable SET password =:pd   WHERE username = :users ;'),
                  params=dict(pd=changes['password'],users=changes['username']))
    data = c.execute(text('UPDATE userstable SET flag =:fg   WHERE username = :users ;'),
                  params=dict(fg=changes['flag'], users=changes['username']))
    c.commit()
    #df=conn.query('UPDATE userstable SET password =:pd and flag= :fg  WHERE username = :users ;',params=dict(pd=changes['password'],fg=changes['flag'],users=changes['username']))
    #c.commit()
    return data

def change_mail(users,number,mail):
    changemail={'username':users,'number':number,'mail':mail}
    #df=conn.query('UPDATE userstable SET number =:number,mail=:mail  WHERE username = :users;',params=dict(number=changemail['number'],mail=changemail['mail'],users=changemail['username']))
    c = conn.session
    c.execute(text('UPDATE userstable SET number =:number  WHERE username = :users;'),
                  params=dict(number=changemail['number'],users=changemail['username']))
    data=c.execute(text('UPDATE userstable SET mail=:mail  WHERE username = :users;'),
                  params=dict(mail=changemail['mail'],users=changemail['username']))
    c.commit()

    return data
def add_searchdata(username, datetimenow, plantname):
    searchs = {'username': username, 'datetime': datetimenow, 'plantname': plantname}
    data=c.execute(text('INSERT INTO search(user,datetime,plantdname) VALUES(:username1,:datetime1,:plantdname1);'),
                  params=dict(username1=searchs['username'], datetime1=searchs['datetime'], plantdname1=searchs['plantname']))
    c.commit()
    return data
# Initialize connection.
# Uses st.cache_resource to only run once.
# userlist = [] # 存放所有的用户名
# pwdlist = [] # 存放所有的用户密码
# blacklist = [] # 存放所有的黑名单用户
# plantlist=[]#病虫害名
# plantinfolist=[]#病虫害详细信息
# solvelist=[] #病虫害解决措施
#
# # 2.读取所有的注册信息 使用a+模式打开文件，在调整指针位置，防止文件不存在时报错
# with open('./user.txt','a+',encoding='utf-8') as fp:
#     fp.seek(0) # 调整当前的的指针位置到文件头部
#     res = fp.readlines()  # 按照每一行读取所有的用户数据
#     for i in res:  # 循环读取的每一行数据
#         r = i.strip()  # 处理每一个换行 admin:123\n ==> admin:123
#         arr = r.split(':')  # admin:123 ==> ['admin','123']
#         userlist.append(arr[0]) # 把用户名追加到 用户名列表中
#         pwdlist.append(arr[1])  # 把用户对应的密码 追加到 用户密码 列表中
#
#     # 获取黑名单数据
#     with open('./black.txt','a+',encoding='utf-8') as fp:
#         fp.seek(0)
#         res = fp.readlines()
#         for i in res:
#             blacklist.append(i.strip())
# def show_slove(dname1):
#     with open('./plants.txt','a+',encoding='utf-8') as fp:
#         fp.seek(0)  # 调整当前的的指针位置到文件头部
#         res = fp.readlines()  # 按照每一行读取所有的用户数据
#         for i in res:
#             r = i.strip()  # 处理每一个换行 admin:123\n ==> admin:123
#             arr = r.split('#')  # admin:123 ==> ['admin','123']
#             if len(arr)==3:
#                 plantlist.append(arr[0])  # 病虫害名称
#                 plantinfolist.append(arr[1])
#                 solvelist.append(arr[2])  # 解决措施
#
#     plantinx=plantlist.index(dname1)
#     #print("标号",plantinx)
#     plants=[]
#     plants.append(plantinfolist[plantinx])
#     plants.append(solvelist[plantinx])
#     return plants
# #def create_usertable():
# #    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')
# def add_userdata(username, password, flag, telnumber, mailnumber):
#         if(username in userlist):
#             st.warning("用户名已存在，请更换一个新的用户名。")
#         else:
#             with open('./user.txt','a+',encoding='utf-8') as fp:
#                 fp.write(f'{username}:{password}:{flag}:{telnumber}:{mailnumber}\n')
#                 st.success("恭喜，您已成功注册。")
#                 st.info("请在左侧选择“登录”选项进行登录。")
#
# #def add_userdata(username, password):
# #    if c.execute('SELECT username FROM userstable WHERE username = %s',(username)):
# #        st.warning("用户名已存在，请更换一个新的用户名。")
# #    else:
# #        c.execute('INSERT INTO userstable(username,password) VALUES(%s,%s)',(username,password))
# #        con.commit()
# #        st.success("恭喜，您已成功注册。")
# #        st.info("请在左侧选择“登录”选项进行登录。")
# def login_user(username,password):
#     errornum=3
#     if username in userlist:
#         if username in blacklist:
#             st.warning("当前用户属于锁定状态，不可登录。")
#         else:
#             inx = userlist.index(username)
#             if password == pwdlist[inx]:
#                 return True;
#             else:
#                 errornum-=1
#             if errornum == 0:
#                 st.warning("您的账户已被锁定！")
#                 with open('./black.txt','a+',encoding='utf-8') as fp:
#                     fp.write(username+'\n')
#                     return False;
#             else:
#                 st.warning("密码输入错误，请重新输入密码。")
#     else:
#         st.warning("用户名不存在，请先选择注册按钮完成注册。")


#def login_user(username,password):
#     if c.execute('SELECT username FROM userstable WHERE username = %s',(username)):
#        c.execute('SELECT * FROM userstable WHERE username = %s AND password = %s',(username,password))
#        data=c.fetchall()
       # print("数据是",data)
#        return data
#    else:
#        st.warning("用户名不存在，请先选择注册按钮完成注册。")
#st.warning("用户名不存在，请先选择注册按钮完成注册。")

#def view_all_users():
#    c.execute('SELECT * FROM userstable')
#    data = c.fetchall()
#    return data
#def show_slove(dname1):
#    c.execute('SELECT * FROM information WHERE dname= %s ',(dname1))
#    data=c.fetchall()
#    print("数据是",data)
#    return data

def main():
    menu = ["首页","登录","注册", "病虫害百科","注销"]

    if 'count' not in st.session_state:
        st.session_state.count = 0
    choice = st.sidebar.selectbox("选项",menu)
    st.sidebar.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 250px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 250px;
        margin-left: -250px;
    }
     </style>
     """,
    unsafe_allow_html=True,)

    if choice =="首页":
        #st.subheader("YSU农作物健康识别系统")
        #st.markdown('''Streamlit文档的地址是：https://docs.streamlit.io/''')
        show();

       # c1, c2 = st.columns(2)
       # with c1:
       #     st.success("首页1")
       #     st.image("testimage.jpg")
       # with c2:
       #     st.success("首页2")
        #    st.image("testimage.jpg")
    elif choice =="登录":
        backimage = Image.open('glod.jpg')
        st.image(backimage, caption='If your location is in the wheat fields, do not go to the streets of Paris',use_column_width = True)
        st.sidebar.subheader("登录区域")
        username = st.sidebar.text_input("用户名")
        password = st.sidebar.text_input("密码",type = "password")
        shenfen=st.sidebar.radio('请选择您的登录身份：',  ('管理员登录', '普通用户登录'))
        if st.sidebar.checkbox("开始登录"):
            logged_user = login_user(username,password)
            if logged_user:
                st.session_state.count += 1

                if st.session_state.count >= 1:
                    st.sidebar.success("您已登录成功，您的用户名是 {}".format(username))
                    if(logged_user[0][2]=='0' and shenfen=='管理员登录'):#管理员登录

                        menu1 = ["病虫害识别","权限管理", "用户提问栏","识别记录查询"]
                        if 'count' not in st.session_state:
                            st.session_state.count = 0
                        choice1 = st.sidebar.selectbox("管理员功能", menu1)
                        st.sidebar.markdown(
                            """
                            <style>
                            [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
                            width: 250px;
                            }
                            [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
                            width: 250px;
                            margin-left: -250px;
                            }
                            </style>
                            """,
                            unsafe_allow_html=True, )
                        if choice1=="用户提问栏":
                            # 其他用法和radio基本一致



                            def personmanage():

                                data_frame = pd.DataFrame({
                                    '个人信息': [logged_user[0][0],logged_user[0][1] , logged_user[0][3], logged_user[0][4]]

                                }, index=['用户名', '密码', '手机号', '电子邮箱'])
                                return data_frame

                            df = personmanage()
                            #st.dataframe(df)

                            col1, col2= st.columns(2)
                            with col1:
                                with st.form("my_form"):

                                    st.write("Inside the form")
                                    slider_val =  st.dataframe(df)
                                    checkbox_val = st.checkbox("Form checkbox")

                                # Every form must have a submit button.
                                    submitted = st.form_submit_button("提交")
                                    if submitted:
                                        st.write("slider", slider_val, "checkbox", checkbox_val)

                                st.write("Outside the form")
                        elif choice1 == "病虫害识别":
                            st.balloons()
                            dname1 = str(main_loop())
                            # print("名称是",dname1)
                            # dname=main_loop()

                            slove_data = show_slove(dname1)
                            # print(type(slove_data))
                            # for row in slove_data:
                            #   print("ee12e")
                            # print("%d--%d" % (cloumn[0], cloumn[1]))
                            datetimenow = datetime.datetime.now(pytz.timezone("Asia/Shanghai"))
                            datetimenow = f'{datetimenow}'.split('.')[0]
                            if dname1 !='None':
                                add_searchdata(username, datetimenow, dname1)
                            #
                            for i in slove_data:
                                st.warning(":sunny::sunny::sunny:已同步将您的农作物识别结果发送至您的邮箱，请注意查收。:sunny::sunny::sunny:")

                                # print(i)
                                dinfo = i[2]
                                dsolve = i[3]
                                st.success(dinfo)
                                st.success(dsolve)

                                datapess = {
                                    'sender': "2577982484@qq.com",  # 发送者邮箱，自己用可写死
                                    'password': "regdayyboktpeacc",  # 在开启SMTP服务后，可以生成授权码，此处为授权码
                                    'subject': "农作物健康识别系统",  # 邮件主题名，没有违规文字都行
                                }
                                # st.write("slider", slider_val, "checkbox", checkbox_val)
                                # load_message(data, receiver, mailusername, diseasename, diseaseinfo, diseasesolve)
                                load_message(datapess, logged_user[0][4], logged_user[0][0], dname1, dinfo, dsolve)
                        elif choice1=="识别记录查询":
                            # 其他用法和radio基本一致
                            allmanagedata1 = list(show_search())

                            for i in range(len(allmanagedata1)):  ###获取为元组类型，需转换为列表
                                allmanagedata1[i] = list(allmanagedata1[i])
                            print(allmanagedata1)
                            allmanagedatanum = []  ##所有编号数据
                            for i in range(len(allmanagedata1)):
                                allmanagedatanum.append(allmanagedata1[i][0])
                            allmanagedatatime = []  ##所有储存时间
                            for i in range(len(allmanagedata1)):
                                allmanagedatatime.append(allmanagedata1[i][1])
                            allmanagedatauserser = []  ##所有使用者数据
                            for i in range(len(allmanagedata1)):
                                allmanagedatauserser.append(allmanagedata1[i][2])
                            allmanagedataplantser = []  ##所有植株病虫害数据
                            for i in range(len(allmanagedata1)):
                                allmanagedataplantser.append(allmanagedata1[i][3])

                            def showallmanageser(allmanagedatanum, allmanagedatatime, allmanagedatauserser,
                                              allmanagedataplantser):
                                AgGrid(
                                    pd.DataFrame({

                                        '识别编号': allmanagedatanum,
                                        '识别时间': allmanagedatatime,
                                        '识别者': allmanagedatauserser,
                                        '植株叶片识别结果': allmanagedataplantser,

                                    }),
                                    fit_columns_on_grid_load=True,
                                    editable=True,
                                    enable_enterprise_modules=True,
                                    height=500, )

                            showallmanageser(allmanagedatanum, allmanagedatatime, allmanagedatauserser,
                                             allmanagedataplantser)



                        elif choice1=="权限管理":
                            # 其他用法和radio基本一致
                            allmanagedata=list(view_all_users())
                            print(allmanagedata)
                            for i in range(len(allmanagedata)):###获取为元组类型，需转换为列表
                                allmanagedata[i]=list(allmanagedata[i])
                            print(allmanagedata)
                            for i in range(len(view_all_users())):
                                print(type(allmanagedata[i][2]))
                                if allmanagedata[i][2]=='0':
                                    print("属于",i)
                                    allmanagedata[i][2]='管理员用户'
                                    print(allmanagedata[i])
                                elif allmanagedata[i][2]=='1':
                                    allmanagedata[i][2]="普通用户"
                                else:
                                    allmanagedata[i][2]='黑名单用户限制登录'
                            print("总共有", allmanagedata)
                            allmanagedatauser=[]  ##所有用户名数据
                            for i in range(len(allmanagedata)):
                                allmanagedatauser.append(allmanagedata[i][0])
                            allmanagedatapd=[]     ##所有用户密码数据
                            for i in range(len(allmanagedata)):
                                allmanagedatapd.append(allmanagedata[i][1])
                            allmanagedatanum=[]     ##所有用户手机号数据
                            for i in range(len(allmanagedata)):
                                allmanagedatanum.append(allmanagedata[i][3])
                            allmanagedatamail = []  ##所有用户邮箱数据
                            for i in range(len(allmanagedata)):
                                allmanagedatamail.append(allmanagedata[i][4])
                            allmanagedataflag = []  ##所有用户身份数据
                            for i in range(len(allmanagedata)):
                                allmanagedataflag.append(allmanagedata[i][2])
                            # def testSelectBox():
                            #
                            #     data_frame = pd.DataFrame({
                            #
                            #         '用户账号':allmanagedatauser,
                            #         '用户密码':allmanagedatapd,
                            #         '用户手机号码':allmanagedatanum,
                            #         '用户邮箱':allmanagedatamail,
                            #         '用户身份':allmanagedataflag,
                            #
                            #     })
                            #     return data_frame
                            #
                            # df = testSelectBox()
                            #
                            # col1, col2= st.columns([2,1])
                            # with col1:
                            #     with st.form("my_form"):
                            #
                            #         st.write("Inside the form")
                            #         slider_val =  st.dataframe(df)
                            #         checkbox_val = st.checkbox("Form checkbox")
                            #
                            #     # Every form must have a submit button.
                            #         submitted = st.form_submit_button("提交")
                            #         if submitted:
                            #             st.write("slider", slider_val, "checkbox", checkbox_val)
                            #
                            #     st.write("Outside the form")
                            col1, col2= st.columns([7,3])

                            with col1:

                                def showallmanage(allmanagedatauser,allmanagedatapd,allmanagedatanum,allmanagedatamail,allmanagedataflag):
                                    AgGrid(
                                        pd.DataFrame({

                                            '用户账号': allmanagedatauser,
                                            '用户密码': allmanagedatapd,
                                            '用户手机号码': allmanagedatanum,
                                            '用户邮箱': allmanagedatamail,
                                            '用户身份': allmanagedataflag,

                                        }),
                                        fit_columns_on_grid_load=True,
                                        editable=True,
                                        enable_enterprise_modules=True,
                                        height=500, )

                                showallmanage(allmanagedatauser,allmanagedatapd,allmanagedatanum,allmanagedatamail,allmanagedataflag)
                               # def showall(allmanagedatauser,allmanagedatapd,allmanagedatanum,allmanagedatamail,allmanagedataflag):
                            with col2:
                                with st.form("my_forms"):
                                    st.write("修改用户信息")
                                    # slider_val =  st.dataframe(df)
                                    userchange = st.selectbox("选择要修改的用户名",
                                                              allmanagedatauser,
                                                              index=1)

                                    pdchange = st.text_input('密码', type="password")
                                    pd2change = st.text_input('确认密码', type="password")
                                    shenfenchange = st.selectbox("选择要变更的身份",
                                                                 ['普通用户', '管理员用户', '黑名单用户限制登录'],
                                                                 index=0)

                                    # checkbox_val = st.checkbox("Form checkbox")

                                    # Every form must have a submit button.
                                    submitted = st.form_submit_button("提交")
                                    if submitted:
                                        if pdchange != pd2change:
                                            st.write(":exclamation::exclamation::exclamation:两次输入的密码不一致")
                                        else:  ##若一致则修改密码
                                            for i in range(len(allmanagedatauser)):
                                                if (allmanagedatauser[i] == userchange):
                                                    allmanagedatapd[i] = pdchange
                                                    allmanagedataflag[i] = shenfenchange
                                                    print(pdchange, shenfenchange)
                                                    print("密码", allmanagedatapd[i], "身份", allmanagedataflag[i])
                                                    change_users(userchange, pdchange, shenfenchange)
                                                    break
                            #change_users(userchange,pdchange,shenfenchange)



                    elif(logged_user[0][2]=='1' and shenfen=='普通用户登录'):#普通用户登录

                        menu1 = ["病虫害识别","信息修改", "用户提问"]
                        if 'count' not in st.session_state:
                            st.session_state.count = 0
                        choice2 = st.sidebar.selectbox("用户功能", menu1)
                        st.sidebar.markdown(
                            """
                            <style>
                            [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
                            width: 250px;
                            }
                            [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
                            width: 250px;
                            margin-left: -250px;
                            }
                            </style>
                            """,
                            unsafe_allow_html=True, )
                        if choice2 == "病虫害识别":
                            st.balloons()
                            dname1 = str(main_loop())
                            # print("名称是",dname1)
                            # dname=main_loop()

                            slove_data = show_slove(dname1)
                            # print(type(slove_data))
                            # for row in slove_data:
                            #   print("ee12e")
                            # print("%d--%d" % (cloumn[0], cloumn[1]))
                            datetimenow = datetime.datetime.now(pytz.timezone("Asia/Shanghai"))


                            datetimenow = f'{datetimenow}'.split('.')[0]
                            # datetimenow=list(datetimenow)
                            # for i in range(len(datetimenow)):
                            #     flag=0
                            #     if(flag==0 and datetimenow[i]==':'):
                            #         datetimenow[i]='时'
                            #         flag=1
                            #     elif(flag==1 and datetimenow[i]==':'):
                            #         datetimenow[i]='分'
                            # datetimenow.append('秒')
                            # datetimenow= ''.join(datetimenow)
                            #
                            if dname1 !='None':
                                add_searchdata(username, datetimenow, dname1)


                            for i in slove_data:
                                st.warning(":sunny::sunny::sunny:已同步将您的农作物识别结果发送至您的邮箱，请注意查收。:sunny::sunny::sunny:")

                                # print(i)
                                dinfo = i[2]
                                dsolve = i[3]
                                st.success(dinfo)
                                st.success(dsolve)

                                datapess = {
                                    'sender': "2577982484@qq.com",  # 发送者邮箱，自己用可写死
                                    'password': "regdayyboktpeacc",  # 在开启SMTP服务后，可以生成授权码，此处为授权码
                                    'subject': "农作物健康识别系统",  # 邮件主题名，没有违规文字都行
                                }
                                # st.write("slider", slider_val, "checkbox", checkbox_val)
                                # load_message(data, receiver, mailusername, diseasename, diseaseinfo, diseasesolve)
                                load_message(datapess, logged_user[0][4], logged_user[0][0], dname1, dinfo, dsolve)
                        if choice2 == "信息修改":
                            # 其他用法和radio基本一致
                            #logged_user1=list(logged_user)
                            def personmanage():

                                pd.set_option('max_colwidth', 200)
                                timenow=datetime.datetime.now(pytz.timezone("Asia/Shanghai"))
                                timenow = f'{timenow}'.split('.')[0]
                                time=[]
                                time.append(timenow)
                                # logged_user1=view_one_users(username)
                                # st.write(logged_user1)
                                data_frame = pd.DataFrame({
                                    '个人信息': [time[0], logged_user[0][0],  logged_user[0][1], logged_user[0][3],  logged_user[0][4],"普通用户"]

                                }, index=['查询时间','用户名', '密码', '手机号', '电子邮箱','登录身份'])


                                return data_frame

                            df = personmanage()
                            # st.dataframe(df)

                            col1, col2,col3 = st.columns([30,33,37])
                            with col1:
                                #df.set_column_width(columns=["个人信息"], width=100)
                                with st.form("my_forms"):
                                    st.subheader(":boom:当前用户信息:boom:")
                                    st.dataframe(df)
                                    submitted = st.form_submit_button("刷新")

                            with col2:
                                with st.form("my_forms1"):
                                    #st.write(":boom:修改用户密码:boom:")
                                    st.subheader(":boom:修改用户密码:boom:")
                                    # slider_val =  st.dataframe(df)
                                    pdnow = st.text_input('原密码', logged_user[0][1])
                                    pdchange = st.text_input('输入新密码', type="password")
                                    pd2change = st.text_input('确认密码', type="password")

                                    # checkbox_val = st.checkbox("Form checkbox")

                                    # Every form must have a submit button.
                                    submitted_mm = st.form_submit_button("提交")
                                    if submitted_mm:
                                        if pdchange != pd2change:
                                            st.write(":exclamation::exclamation::exclamation:两次输入的密码不一致")
                                        else:  ##若一致则修改密码

                                            change_users(logged_user[0][0], pdchange, "普通用户")
                                            logged_user = list(logged_user)
                                            logged_user[0][1] = pdchange
                                            logged_user = tuple(logged_user)
                            with col3:
                                with st.form("my_forms2"):
                                    st.subheader(":boom:更新手机号及电子邮箱:boom:")
                                    # slider_val =  st.dataframe(df)
                                    numnow = st.text_input('更改手机号')
                                    mailnow = st.text_input('更改邮箱号')
                                    mailnowyzm = st.text_input('邮箱验证码',type="password")


                                    submitted_mail = st.form_submit_button("更新")
                                    print(mailnow)
                                    print("111",isValid(mailnow))
                                    if isValid(mailnow):
                                        st.info("即将向邮箱{}发送验证码,请注意查收".format(mailnow))
                                        verification_now = SendEmail(data=data, receiver=mailnow).send_email()
                                        mailnowyzm1 = verification_now
                                      # print(verification)
                                      # print(yanzhengma, yanzhengma1)
                                    if submitted_mail:
                                        if (mailnowyzm == mailnowyzm1):

                                            change_mail(logged_user[0][0], numnow, mailnow)
                                            logged_user=list(logged_user)
                                            logged_user[0][3] = numnow
                                            logged_user[0][4] = mailnow
                                            logged_user=tuple(logged_user)
                                        else:
                                            st.sidebar.warning("邮箱验证码错误，请检查后重试。")



                                # st.dataframe(df)

                    elif(logged_user[0][2]=='1' and shenfen=='管理员登录' or logged_user[0][2]=='0' and shenfen=='普通用户登录'):

                        st.warning(":exclamation::exclamation::exclamation:您的身份选择有误，请退出后重新选择身份查看！")
                    else:
                        st.warning(":exclamation::exclamation::exclamation:您已被限制登录，详情请联系管理员。")

                    # st.balloons()
                    # dname1 = str(main_loop())
                    # # print("名称是",dname1)
                    # # dname=main_loop()
                    #
                    # slove_data = show_slove(dname1)
                    # # print(type(slove_data))
                    # # for row in slove_data:
                    # #   print("ee12e")
                    # # print("%d--%d" % (cloumn[0], cloumn[1]))
                    # datetimenow = datetime.datetime.now()
                    # datetimenow = f'{datetimenow}'.split('.')[0]
                    # add_searchdata(username, datetimenow, dname1)
                    #
                    #
                    #
                    # for i in slove_data:
                    #     st.warning(":sunny::sunny::sunny:已同步将您的农作物识别结果发送至您的邮箱，请注意查收。:sunny::sunny::sunny:")
                    #
                    #     # print(i)
                    #     dinfo = i[2]
                    #     dsolve = i[3]
                    #     st.success(dinfo)
                    #     st.success(dsolve)
                    #
                    #
                    #     datapess = {
                    #             'sender': "2577982484@qq.com",  # 发送者邮箱，自己用可写死
                    #             'password': "regdayyboktpeacc",  # 在开启SMTP服务后，可以生成授权码，此处为授权码
                    #             'subject': "农作物健康识别系统",  # 邮件主题名，没有违规文字都行
                    #         }
                    #         # st.write("slider", slider_val, "checkbox", checkbox_val)
                    #         # load_message(data, receiver, mailusername, diseasename, diseaseinfo, diseasesolve)
                    #     load_message(datapess, logged_user[0][4], logged_user[0][0], dname1, dinfo, dsolve)


                    #              c1, c2 = st.columns(2)
                    #             with c1:
                    #                st.success()
                    #               st.image()
                    #          with c2:
                    #             st.success()
                    #            st.image()

                    #st.title("成功登录后可以看到的内容")


            else:
                st.sidebar.warning("用户登录失败，请检查后重试。")
    elif choice =="注册":
        #st.subheader("注册")
        backimage = Image.open('zhuce.jpg')
        st.image(backimage, caption='Sunrise by the mountains',use_column_width = True)
        new_user = st.sidebar.text_input("用户名")
        new_password = st.sidebar.text_input("密码",type = "password")
        new_password1 = st.sidebar.text_input("确认密码",type = "password")
        telnumber=st.sidebar.text_input("用户手机号")
        mailnumber = st.sidebar.text_input("用户邮箱")
        new_flag=1 ###注册用户均为普通用户
        yanzhengma=st.sidebar.text_input("邮箱验证码",type = "password")
        #print("是不是",isValid(mailnumber))
        if isValid(mailnumber):
            st.info("即将向邮箱{}发送验证码,请注意查收".format(mailnumber))
            verification = SendEmail(data=data, receiver=mailnumber).send_email()
            yanzhengma1=verification
        #print(verification)
        #print(yanzhengma, yanzhengma1)
        if st.sidebar.button("注册"):
            print(yanzhengma,yanzhengma1)
            if(new_password==new_password1  and yanzhengma==yanzhengma1):
                #create_usertable()
                add_userdata(new_user,new_password,new_flag,telnumber,mailnumber)
            else:
                print(yanzhengma, yanzhengma1)
                st.sidebar.warning("两次密码不正确或验证码错误，请检查后重试。")
    elif choice =="注销":
        st.session_state.count = 0
        if st.session_state.count == 0:
            st.info("您已成功注销，如果需要，请选择左侧的登录按钮继续登录。")


    elif choice =="病虫害百科":
        # res = socket.gethostbyname(socket.gethostname())
        # res='121.22.29.122'
        # reader = geoip2.database.Reader('./GeoLite2-City.mmdb')
        # cityip = reader.city(res)
        # print(reader.city(res))
        # # if reader.city(res)!=None:
        # #     cityip = reader.city(res)
        # #     #cityip = reader.city(res)
        # # else:
        # #     cityip=[39.906497, 119.539445]
        #print(cityip)
        # list1=[]
        # list1.append(np.random.randn(10, 2) +[39.906497, 119.539445])
        # print(list1)

        map_data = pd.DataFrame([[39.906497,119.539445]],##随机np.random.randn(10, 2) +[39.906497, 119.539445],
            columns=['lat', 'lon'])
        st.sidebar.map(map_data)

        baike1()
if __name__=="__main__":
    main()
