from flask import Flask,render_template,request
from forms import fillup
import mysql.connector


mydb = mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="123vittal",
    database='project'
)
 
mycurser = mydb.cursor()

app = Flask(__name__)
app.config['SECRET_KEY'] = '123vittal'
sqlformula = "INSERT INTO crime(Location,Police_stn,Date,criminalname,criminal_adhr,victimname,victim_adhr,crimetype) VALUES( %s, %s, %s, %s, %s,%s, %s, %s)"

@app.route('/')
def home():
    return render_template('layout.html')

@app.route('/add',methods = ['GET', 'POST'])
def fillupp():
    form = fillup()
    if form.is_submitted():
        result = request.form
        val_list=[]
        key_list=[]
        for i,j in result.items():
            val_list.append(j)
            key_list.append(i)
        mycurser.execute(sqlformula,val_list[:-1])
        mydb.commit()
        return render_template('see.html',val = val_list,keys=key_list,result=result)

    return render_template('index.html',form = form)

@app.route('/view')
def view():
    mycurser.execute("select * from crime")
    dbs = mycurser.fetchall()
    return render_template('view.html',res=dbs)


@app.route('/mostwant')
def indd():
    mycurser.execute("select count(criminal_adhr),criminalname from crime group by criminal_adhr order by count(criminal_adhr) desc limit 1")
    db1 = mycurser.fetchall()
    return render_template('mostwant.html',res=db1)





if __name__ == '__main__':
    app.run(debug=True)