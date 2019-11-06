from flask import Flask, render_template, request, redirect, url_for, session
import config
from models import User, Question
from exts import db
from decorators import login_required
from sqlalchemy import or_
from datetime import datetime

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    context = {
        'questions': Question.query.order_by('create_time').all()
    }
    return render_template('index.html', **context)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            # 如果想在31天都不需要登录
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return '手机号或者密码错误,请确认后在登录!'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # 　手机号码验证
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return '该手机号码已被注册,请更换手机号码!'
        else:
            # password1 与 password2 是否相等
            if password1 != password2:
                return '两次密码输入的不一致,请确认后在输入!'
            else:
                user = User(telephone=telephone, username=username, password=password1)
                db.session.add(user)
                db.session.commit()
                # 如果注册成功,就让它跳到登录页面
                return redirect(url_for('login'))


@app.route('/logout')
def logout():
    # session.pop('user_id')
    # del session['user_id']
    session.clear()
    return redirect(url_for('login'))


@app.route('/question', methods=['GET', 'POST'])
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title, content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        question.author = user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/detail/<question_id>')
def detail(question_id):
    question_model = Question.query.filter(Question.id == question_id).first()
    return render_template('detail.html', question=question_model)


@app.route('/search')
def search():
    q = request.args.get('q')
    # title content  或
    questions = Question.query.filter(or_(Question.title.contains(q),
                                          Question.content.contains(q))).order_by('create_time')
    return render_template('index.html', questions=questions)


@app.route('/del_question/<question_id>')
@login_required
def del_question(question_id):
    question_model = Question.query.filter(Question.id == question_id).first()
    db.session.delete(question_model)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/change/<question_id>', methods=['GET', 'POST'])
@login_required
def change(question_id):
    question_model = Question.query.filter(Question.id == question_id).first()

    if request.method == 'GET':
        return render_template('change.html', question=question_model)
    else:
        question_model.content = request.form.get('content')
        # question_model.crete_time = datetime.now()
        # print(question_model.crete_time)
        db.session.commit()
        # title = request.form.get('title')
        # content = request.form.get('content')
        # question = Question(content=content)
        # user_id = session.get('user_id')
        # user = User.query.filter(User.id == user_id).first()
        # question.author = user
        # db.session.add(question)
        # db.session.commit()
        return redirect(url_for('index'))


@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}


if __name__ == '__main__':
    app.run()
