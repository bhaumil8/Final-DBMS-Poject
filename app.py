from flask import Flask,render_template,request,session,redirect,flash
import smtplib
import numpy as np
import mysql.connector

app = Flask(__name__)
app.secret_key = 'nisarg'

@app.route('/',methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        otp = np.random.randint(100000,999999)
        global gotp
        gotp = otp
        message= f'Your otp is {otp}.'
        email = request.form.get('email')
        name = request.form.get('name')
        add = request.form.get('add')
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login('21ceh052@nirmauni.ac.in','changeme123')
        server.sendmail("21ceh052@nirmauni.ac.in",email,message)

        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "innpro"
        )

        mycursor = mydb.cursor()

        q1 = f"select email from login"

        mycursor.execute(q1)

        myemail = mycursor.fetchall()
        if(myemail != []):
            if email in myemail[0]:
                # flash('Your account has already been created.')
                return render_template('otp.html',email="")

        q2 = f"insert into login (email , name, address) values('{email}','{name}','{add}')"

        mycursor.execute(q2)

        q3 = f"select uid from login where email = '{email}'"
        mycursor.execute(q3)

        mr = mycursor.fetchall()

        uid = mr[0][0]
        print(uid) 
        session['uid'] = uid
        session['name'] = name
        print(name)
        mydb.commit()

        mycursor.close()
        mydb.close()

        # flash(f'Check your email and verify otp.')
        return render_template('otp.html',email=email)
    return render_template('signup.html')

@app.route('/otp',methods = ['GET','POST'])
def otp():
    if request.method == 'POST':
        if(int(request.form.get('otp')) == gotp):
            flash("Welcome to our website")
            return render_template('index.html')
        return render_template('signup.html')
    return render_template('otp.html')

# @app.route('/menu')
# def menu():
#     mydb = mysql.connector.connect(
#             host = "localhost",
#             user = "root",
#             password = "",
#             database = "bandhan"
#         )
    
#     mycursor = mydb.cursor()

#     q1 = f"select * from food"

#     mycursor.execute(q1)

#     myresult = mycursor.fetchall()

#     return render_template('menu.html',mydata = myresult)
    

@app.route('/signup')
def login():
    return render_template('signup.html')

# if __name__ == '__main' :
#     app.run(debug=True)

# from flask import Flask,render_template,redirect,request,session,jsonify
# import mysql.connector


# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')
    # return render_template('checking.html')

@app.route('/menu')
def menu():
    mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "innpro"
        )
    
    mycursor = mydb.cursor()

    q1 = f"select * from menu"

    mycursor.execute(q1)

    myresult = mycursor.fetchall()


    return render_template('menu.html',mydata = myresult)

@app.route('/cart',methods = ['GET','POST'])
def cart():
    if(request.method == 'POST'):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "innpro"
        )

    foodid = (request.form.get('foodid'))
    print(foodid)
    
    mycursor = mydb.cursor()

    q1 = f"SELECT * FROM menu WHERE fid = '{foodid}'"
    mycursor.execute(q1)
    
    dt = mycursor.fetchall()
    # print(dt[0][1])
    uid = session['uid']
    q2 = f"INSERT INTO cart VALUES ({dt[0][0]}, '{dt[0][1]}', '{dt[0][2]}', '{dt[0][3]}', {dt[0][4]},1,{uid},{dt[0][4]});"
    mycursor.execute(q2)

    mydb.commit()

    mycursor.close()
    mydb.close()

    return redirect('/menu')
    # myresult = mycursor.fetchall()


@app.route('/order')
def order():
    mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "innpro"
        )
    
    mycursor = mydb.cursor()

    q1 = f"select * from cart"

    mycursor.execute(q1)

    myresult = mycursor.fetchall()

    sum = 0

    for i in myresult:
        sum = sum + i[7]

    print(sum)

    return render_template('order.html',myorder = myresult,sum=sum)

@app.route('/logout')
def logout():
    return render_template('signup.html')


# @app.route('/')
# def chek():
#     return render_template('checking.html')

@app.route('/dec',methods=['GET','POST'])
def decr():
    if request.method == 'POST':
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "innpro"
        )
        mycursor = mydb.cursor()

        value = request.form.get('dec')

        q1 = f"update cart set fquant = fquant - 1 where fid = {value} and fquant > 0"

        mycursor.execute(q1)

        q1 = f"update cart set tprice = fprice*fquant where fid = {value}"

        mycursor.execute(q1)

        q1 = f"delete from cart where fquant = 0"

        mycursor.execute(q1)

        mydb.commit()

        mydb.close()
        mycursor.close()

        return redirect('/order')
    return redirect('/order')

@app.route('/inc',methods=['GET','POST'])
def incr():
    if request.method == 'POST':
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "innpro"
        )
        mycursor = mydb.cursor()

        value = request.form.get('inc')

        print(value)

        q1 = f"update cart set fquant = fquant + 1 where fid = {request.form.get('inc')}"

        mycursor.execute(q1)

        q1 = f"update cart set tprice = fprice*fquant where fid = {value}"
        # q2 = f"select fprice*fquant from cart where fid = {value}"

        mycursor.execute(q1)

        # myresult = mycursor.fetchall()

        mydb.commit()

        mydb.close()
        mycursor.close()

        return redirect('/order')
    return redirect('/order')


@app.route('/checkout',methods=['GET','POST'])
def checkout():
    if request.method == 'POST':
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "innpro"
        )
        mycursor = mydb.cursor()

        q1 = f"SELECT DISTINCT(fid) FROM cart"

        mycursor.execute(q1)

        myfid = mycursor.fetchall()

        q1 = f"SELECT fquant FROM cart"
        mycursor.execute(q1)

        myq = mycursor.fetchall()

        uid = session['uid']

        for i in range(len(myfid)):
            q2 = f"insert into orders values({myfid[i][0]},{uid},{myq[i][0]})"
            mycursor.execute(q2)

        q1 = f"delete from cart"

        mycursor.execute(q1)

        mydb.commit()

        mydb.close()
        mycursor.close()

        return redirect('/order')
    return redirect('/order')
    

@app.route('/preorder')
def preorders():
    mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "innpro"
        )
    
    mycursor = mydb.cursor()
    uid = session['uid']

    q1 = f"select * from menu where fid in (select fid from orders where uid = {uid})"

    mycursor.execute(q1)

    myresult = mycursor.fetchall()


    return render_template('preorder.html',mydata = myresult)


if(__name__ == "__main__"):
    app.run(debug=True)
    