# streamlit_app.pimport streamlit as st
import streamlit as st
# mysqlclient==2.1.1
# SQLAlchemy==2.0.1
# Initialize connection.
from sqlalchemy.sql import text

# Perform query.

# Print results.
# on = pymysql.connect(host="39.103.="root", password="zhaozhuo2001.", database="plants_disease", charset="utf8")
conn = st.experimental_connection('mysql', type='sql')


# Perform query.


def add_userdata(username, password, flag, number, mail):

    users = {'username': username, 'password': password, 'flag': flag, 'number': number, 'mail': mail}
    st.write(username)
    # c.execute(text('SELECT username FROM userstable WHERE username =`username`;'))
    # df = conn.query('SELECT * FROM userstable WHERE username ="{users[username]}";')
    # st.write(df)
    c = conn.session
    c.execute(text("SELECT * FROM usertable WHERE username = %s;"), username=username)
    c.commit()
    return c

    # user = execute.first()
    #     df=conn.query('select * from usertable where username = ? and password > ?;',['admin','123'])

    #     st.write(len(df))
    #     st.write(conn.query('SELECT password FROM userstable WHERE username =?;'))
    #     connect.query('select * from test where name = ? and id > ?',['testname','2'],(err,rows)=>{});
    #     if len(conn.query('SELECT username FROM userstable WHERE username =`username`;'))==1:
    #         data=conn.query('SELECT username FROM userstable WHERE username =`username`;')
    #         print(data)
    #         st.write(data)
    #         st.warning("用户名已存在，请更换一个新的用户名。")
    # def add(username, password, flag, number, mail):
    #     users={'username':username,'password':password,'flag':flag,'number':number,'mail':mail}
    #     #pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
    #     c=conn.session
    #     c.execute(text('INSERT INTO userstable(username,password,flag,number,mail) VALUES(:username1,:password1,:flag1,:number1,:mail1);'),params=dict(username1=users['username'],password1=users['password'],flag1=users['flag'],number1=users['number'],mail1=users['mail']))
    #     c.commit()
    #     st.success("恭喜，您已成功注册。")
    #     st.info("请在左侧选择“登录”选项进行登录。")
    # def show_search():##所有浏览记录
    #     data=conn.query('SELECT * FROM search;')
    #     return data
    # st.write(show_search().columns = ['编号','日期','识别者','识别结果'])
    # df = conn.query('SELECT * from userstable;', ttl=6000)
    # st.write(type(df))
    # # Print results.
    # for row in df.itertuples():
    #     st.write(f"{row.username} has a ")
add_userdata('admin', 'password', 1, 1, 1)
# add('admin1', 'password', 1, 1,1)
# with conn.session as s:
#    pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
#    for k in pet_owners:
#        s.execute(
#           text('INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet);'),
#            params=dict(owner=k, pet=pet_owners[k])
#        )
#    s.commit()