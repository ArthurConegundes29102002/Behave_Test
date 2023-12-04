from flask import Flask, url_for, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

# ------------------------------------------------- configurando conexão com BD

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///List.db'

db = SQLAlchemy(app)

class TaskDB(db.Model):

    id = db.Column(db.Integer,primary_key=True)

    content = db.Column(db.String(200),nullable=False)
    
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' %self.id

# ------------------------------------------------- rota para a página principal:

@app.route('/', methods=['POST','GET'])
def HomePage():

    if request.method == 'POST':
        task_content = request.form['content'] #variável assume o valor do forms da página html, que tem o método post

        NewTask = TaskDB(content = task_content)

        try:
            db.session.add(NewTask)
            db.session.commit()
            return redirect('/')
        
        except:
            return 'Issue Found'

    else:
        tasks = TaskDB.query.order_by(TaskDB.date_created).all()
        return render_template('homepage.html',tasks=tasks)
    
# ------------------------------------------------- rota de deletar elementos:

@app.route('/delete/<int:id>')
def DeleteTask(id):
    deleted_task = TaskDB.query.get_or_404(id)

    try:
        db.session.delete(deleted_task)
        db.session.commit()
        return redirect('/')
    
    except:
        return "something went wrong"
    
# -------------------------------------------------rota de fazer update nos elementos








# -------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)