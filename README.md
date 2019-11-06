# blog_demo
# 需要下载的包和库
# alembic==1.3.0
# Click==7.0
# Flask==1.1.1
# Flask-Migrate==2.5.2
# Flask-MySQLdb==0.2.0
# Flask-Script==2.0.6
# Flask-SQLAlchemy==2.4.1
# itsdangerous==1.1.0
# Jinja2==2.10.3
# Mako==1.1.0
# MarkupSafe==1.1.1
# mysqlclient==1.4.4
# PyMySQL==0.9.3
# python-dateutil==2.8.1
# python-editor==1.0.4
# six==1.12.0
# SQLAlchemy==1.3.10
# Werkzeug==0.16.0
# 想要运行首先得环境一致了

# 这个包和库在 install.txt文件中
# 下载方法 pip install -r install.txt 就行了

# 还有就是要先通过命令来运行 manage.py 这个文件 操作方法
# 先进入pycharm 把这个项目导进pycharm中
# 然后点击 Terminal 在里面 先运行 pip install -r install.txt
# 在运行 python manage.py db init
# 后就会多出一个 migrations 这个文件夹
# 然后 在运行 python manage.py db migrate
# 最后 在运行 python manage.py db upgrade
# 运行完成后 数据库就会有 user和question 这两个数据表
