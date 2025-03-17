from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'cdac'
app.config['MYSQL_DB'] = 'mydb'  # Replace 'your_database_name' with your actual database name

# Initialize Flask-MySQLdb
mysql = MySQL(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        email = request.form['email']
        psw = request.form['psw']
        psw_repeat = request.form['psw-repeat']
        if psw==psw_repeat:
            try:
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, psw))
                mysql.connection.commit()
                cur.close()
                return redirect("/sign_in")  
            except Exception as e:
                print(f"ERROR: {e}")
                return f"ERROR: {e}"
        else:
            message = "password does not match"
            return render_template("register.html", tasks=message) 
    else:
        return render_template('register.html')

@app.route("/adminsign_in", methods=["POST","GET"] )
def adminsign_in():
    if request.method == "POST":
        email = request.form['email']
        psw = request.form['psw']
        try:
            cur = mysql.connection.cursor()
            query = "SELECT * FROM admin WHERE email = %s"
            cur.execute(query, (email,))
            temp = cur.fetchall()
            if len(temp) !=0:
                if temp[0][2] == psw:
                    return redirect('/adminhome')
                else:
                    return render_template('index.html')
            else:
                return redirect("/adminsign_in")
        except Exception as e:
            print(f"ERROR: {e}")
            return f"ERROR: {e}"
    else:
        return render_template('adminsign_in.html')
    
@app.route("/sign_in", methods=["POST","GET"] )
def sign_in():
    if request.method == "POST":
        email = request.form['email']
        psw = request.form['psw']
        try:
            cur = mysql.connection.cursor()
            query = "SELECT * FROM users WHERE email = %s"
            cur.execute(query, (email,))
            temp = cur.fetchall()
            if len(temp) !=0:
                if temp[0][2] == psw:
                    return redirect('/home')
                else:
                    return render_template('sign_in.html')
            else:
                return redirect("/sign_in")
        except Exception as e:
            print(f"ERROR: {e}")
            return f"ERROR: {e}"
    else:
        return render_template('sign_in.html')

@app.route("/adminhome", methods=["POST", "GET"])
def adminhome():
    if request.method == "POST":
        current_task = request.form['content']
        seat_val = request.form['seat']
        price = request.form['price']
        try:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO vehicle (vehicle_name, seat,price,name,age,licence_no) VALUES (%s, %s, %s, 'none',0,0)", (current_task, seat_val,price))
            mysql.connection.commit()
            cur.close()
            return redirect("/adminhome")
        except Exception as e:
            print(f"ERROR: {e}")
            return f"ERROR: {e}"
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM vehicle ORDER BY seat")
        tasks = cur.fetchall()
        cur.close()
        return render_template('adminhome.html', tasks=tasks)

@app.route("/home", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        current_task = request.form['content']
        seat_val = request.form['seat']
        try:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO vehicle (vehicle_name, seat) VALUES (%s, %s)", (current_task, seat_val))
            mysql.connection.commit()
            cur.close()
            return redirect("/home")
        except Exception as e:
            print(f"ERROR: {e}")
            return f"ERROR: {e}"
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM vehicle ORDER BY seat")
        tasks = cur.fetchall()
        cur.close()
        return render_template('home.html', tasks=tasks)

@app.route("/bookingDetails/<int:id>", methods=("POST","GET"))
def bookingDetails(id:int):
    if request.method == "POST":
        my_id = id
        days= request.form['daycount']
        name = request.form['name']
        age = request.form['age']
        licence = request.form['li_no']
        phone_no= request.form['number']
        try:
            cur = mysql.connection.cursor()
            cur.execute("UPDATE vehicle SET name =%s,age=%s,licence_no=%s where id = %s",(name,age,licence,my_id))
            mysql.connection.commit()
            cur.close()
            a = "/delete/"+str(my_id)
            return redirect(a)
        except Exception as e:
            print(f"ERROR: {e}")
            return f"ERROR: {e}"
    else:
        return render_template('getDate.html', id=id)

@app.route("/delete/<int:id>")
def delete(id:int):
    cur = mysql.connection.cursor()
    try:
        #cur.execute("DELETE FROM vehicle WHERE id = %s", (id,))
        #mysql.connection.commit()
        #cur.close()
        a = "/confirm/"+str(id)
        return redirect(a)
    except Exception as e:
        return f"ERROR: {e}"

@app.route("/confirm/<int:id>")
def confirm(id:int):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM vehicle where id =%s",(id,))
    tasks = cur.fetchone()
    cur.execute("DELETE FROM vehicle WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return render_template('res.html', tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
