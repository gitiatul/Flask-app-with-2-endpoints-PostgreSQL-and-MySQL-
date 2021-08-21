from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

SQLALCHEMY_DATABASE_URI = 'postgres://db_user:db_pw@localhost:5432/db_name'
SQLALCHEMY_BINDS = {
    'db1': SQLALCHEMY_DATABASE_URI,
    'db2': 'mysql://db_user:db_pw@localhost:3306/db_name'
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)    

class Todo(db.Model):

    sno=db.Column(db.Integer ,primary_key=True)
    title=db.Column(db.String(200) ,nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route('/',methods=['GET','POST'])
def fun():
    
    if request.method=="POST":
        newtask=(request.form['task'])
        todo=Todo(title=newtask)
        db.session.add(todo)
        db.session.commit()
    alldata=Todo.query.all()
    return render_template('index.html',alldata=alldata)

    

@app.route('/data')
def data():
    alldata=Todo.query.all()
    print(alldata)
    return "data page"

if __name__=="__main__":
    app.run(debug=True)