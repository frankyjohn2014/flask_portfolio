Сайт написанный на flask, технологии с которыми я работаю

install mysql
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
create database sql_test character set utf8 collate utf8_unicode_ci;

python3 manage.py db migrate
db stamp head
db migrate
db upgrade

from app import db
from app import user_datastore
>>> user_datastore.create_user(email='frankyjohn2014@gmail.com', password='admin')
db.session.commit()
from models import User
user = User.query.first()
user.id
user.email
>>> 'frankyjohn2014@gmail.com'

add role 


from app import db

>>> from app import user_datastore
>>> from models import User
>>> user = User.query.first()
>>> user
<User 1>
>>> user_datastore.create_role(name='admin', description='administrator')
<Role (transient 140186340422320)>
>>> db.session.commit()
>>> from models import Role
>>> role = Role.query.first()
>>> user_datastore.add_role_to_user(user,role)
True
>>> db.session.commit()
