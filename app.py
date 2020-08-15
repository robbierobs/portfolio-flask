from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(128))
#     #posts = db.relationship('Post', backref='author', lazy='dynamic')
#     about_me = db.Column(db.String(140))
#     last_seen = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<User {}>'.format(self.username)

# class Locomotive(db.Model):
#     unit_number = db.Column(db.Integer, primary_key=True)
#     model = db.Column(db.String(120))
#     cs = db.Column(db.Boolean, unique=True, default=True)
#     lsl = db.Column(db.Boolean, unique=True, default=True)
#     fra_date = db.Column(db.String(120))
#     epa_date = db.Column(db.String(120))
#     lube_due = db.Column(db.String(120))
#     cs_due = db.Column(db.String(120))
#     afm_due = db.Column(db.String(120))
#     fuel_capacity = db.Column(db.Integer, default=0)
#     incoming_fuel = db.Column(db.Integer, default=0)
#     currrent_fuel = db.Column(db.Integer, default=0)
#     ptc_status = db.Column(db.Integer, default=0)
#     direction  = db.Column(db.String(10))
#     updated = db.Column(db.String(120))
#     home_shop = db.Column(db.String(120))
#     alt_shop = db.Column(db.String(120))

#     def __repr__(self):
#         return '<Locomotive %r' % self.id

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/tasks', methods=['POST', 'GET'])
def tasks():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/tasks')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('tasks.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/tasks')
    except:
        return "There was an error deleting that task."

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/tasks')
        except:
            return 'There was an issue updating your task.'
    else:
        return render_template('update.html', task=task)

@app.route('/portfolio')
def portfolio():
    return render_template('index.html')

@app.route('/about_me')
def about_me():
    return render_template('about_me.html')

@app.route('/boro')
def boro():
    return render_template('boro.html')
    
@app.route('/photo_gallery')
def photo_gallery():
    return render_template('photo_gallery.html')

@app.route('/landing2')
def landing2():
    return render_template('projects/landing2.html')

@app.route('/coming_soon')
def coming_soon():
    return render_template('/projects/coming_soon.html')

@app.route('/rotating_text')
def rotating_text():
    return render_template('/projects/rotate_circular.html')
@app.route('/resume')
def resume():
    return render_template('/resume.html')
@app.route('/new_home')
def new_home():
    return render_template('/new_home.html')

if __name__ == "__main__":
    app.run(debug=True)