import streamlit as st

from firstpage import *
from opencv import *
import streamlit as st
st.set_page_config(page_title="YSU-农作物健康识别系统",layout="wide")

# Initialize connection.
# Uses st.cache_resource to only run once.
userlist = [] # 存放所有的用户名
pwdlist = [] # 存放所有的用户密码
blacklist = [] # 存放所有的黑名单用户
plantlist=[]#病虫害名
plantinfolist=[]#病虫害详细信息
solvelist=[] #病虫害解决措施

# 2.读取所有的注册信息 使用a+模式打开文件，在调整指针位置，防止文件不存在时报错
with open('./user.txt','a+',encoding='utf-8') as fp:
    fp.seek(0) # 调整当前的的指针位置到文件头部
    res = fp.readlines()  # 按照每一行读取所有的用户数据
    for i in res:  # 循环读取的每一行数据
        r = i.strip()  # 处理每一个换行 admin:123\n ==> admin:123
        arr = r.split(':')  # admin:123 ==> ['admin','123']
        userlist.append(arr[0]) # 把用户名追加到 用户名列表中
        pwdlist.append(arr[1])  # 把用户对应的密码 追加到 用户密码 列表中

    # 获取黑名单数据
    with open('./black.txt','a+',encoding='utf-8') as fp:
        fp.seek(0)
        res = fp.readlines()
        for i in res:
            blacklist.append(i.strip())
def show_slove(dname1):
    with open('./plants.txt','a+',encoding='utf-8') as fp:
        fp.seek(0)  # 调整当前的的指针位置到文件头部
        res = fp.readlines()  # 按照每一行读取所有的用户数据
        for i in res:
            r = i.strip()  # 处理每一个换行 admin:123\n ==> admin:123
            arr = r.split('#')  # admin:123 ==> ['admin','123']
            if len(arr)==3:
                plantlist.append(arr[0])  # 病虫害名称
                plantinfolist.append(arr[1])
                solvelist.append(arr[2])  # 解决措施
         
    plantinx=plantlist.index(dname1)
    #print("标号",plantinx)
    plants=[]
    plants.append(plantinfolist[plantinx])
    plants.append(solvelist[plantinx])
    return plants
#def create_usertable():
#    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')
def add_userdata(username, password):
        if(username in userlist):
            st.warning("用户名已存在，请更换一个新的用户名。")
        else:
            with open('./user.txt','a+',encoding='utf-8') as fp:
                fp.write(f'{username}:{password}\n')
                st.success("恭喜，您已成功注册。")
                st.info("请在左侧选择“登录”选项进行登录。")

#def add_userdata(username, password):
#    if c.execute('SELECT username FROM userstable WHERE username = %s',(username)):
#        st.warning("用户名已存在，请更换一个新的用户名。")
#    else:
#        c.execute('INSERT INTO userstable(username,password) VALUES(%s,%s)',(username,password))
#        con.commit()
#        st.success("恭喜，您已成功注册。")
#        st.info("请在左侧选择“登录”选项进行登录。")
def login_user(username,password):
    errornum=3
    if username in userlist:
        if username in blacklist:
            st.warning("当前用户属于锁定状态，不可登录。")
        else:
            inx = userlist.index(username)
            if password == pwdlist[inx]:
                return True;
            else:
                errornum-=1
            if errornum == 0:
                st.warning("您的账户已被锁定！")
                with open('./black.txt','a+',encoding='utf-8') as fp:
                    fp.write(username+'\n')
                    return False;
            else:
                st.warning("密码输入错误，请重新输入密码。")
    else:
        st.warning("用户名不存在，请先选择注册按钮完成注册。")


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
    menu = ["首页","登录","注册", "注销"]

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

    elif choice =="登录":
        backimage = Image.open('glod.jpg')
        st.image(backimage, caption='Sunrise by the mountains',use_column_width = True)
        st.sidebar.subheader("登录区域")
        username = st.sidebar.text_input("用户名")
        password = st.sidebar.text_input("密码",type = "password")
        if st.sidebar.checkbox("开始登录"):
            logged_user = login_user(username,password)
            if logged_user:
                st.session_state.count += 1

                if st.session_state.count >= 1:
                    st.sidebar.success("您已登录成功，您的用户名是 {}".format(username))
                    #st.title("成功登录后可以看到的内容")
                    st.balloons()
                    #main_loop()
                    dname1 = str(main_loop())
                    print(dname1)
                    if dname1!='None':

                    # dname=main_loop()
                        slove_data = show_slove(dname1)
                    # print(type(slove_data))
                    # for row in slove_data:
                    #   print("ee12e")
                    # print("%d--%d" % (cloumn[0], cloumn[1]))
                        st.success(slove_data[0])
                        st.success(slove_data[1])


                else:

                    st.sidebar.warning("用户名或者密码不正确，请检查后重试。")
    elif choice =="注册":
        #st.subheader("注册")
        backimage = Image.open('sunrise.jpg')
        st.image(backimage, caption='Sunrise by the mountains',use_column_width = True)
        new_user = st.sidebar.text_input("用户名")
        new_password = st.sidebar.text_input("密码",type = "password")
        new_password1 = st.sidebar.text_input("确认密码",type = "password")
        if st.sidebar.button("注册"):
            if(new_password==new_password1):
                add_userdata(new_user,new_password)
            else:
                st.sidebar.warning("两次密码不正确，请检查后重试。")
    elif choice =="注销":
        st.session_state.count = 0
        if st.session_state.count == 0:
            st.info("您已成功注销，如果需要，请选择左侧的登录按钮继续登录。")
if __name__=="__main__":
    main()
