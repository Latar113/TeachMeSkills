from peewee import *
from datetime import *

db = MySQLDatabase(database='test2', user='root', password='password', host='127.0.0.1', port=3306)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    id = PrimaryKeyField()
    name = CharField(max_length=20, unique=True)
    age = IntegerField(constraints=[Check('age>0 and age<120')])
    gender = CharField(max_length=20)
    nationality = CharField(max_length=20)
    email = CharField(max_length=20, unique=True)


class Posts(BaseModel):
    id = PrimaryKeyField()
    user_id = ForeignKeyField(User, on_delete='set null', null=True)
    title = CharField(max_length=200)
    description = CharField(max_length=200)
    created = DateTimeField(null=False, default=datetime.now())
    likes = ManyToManyField(User, on_delete='cascade')


Likes = Posts.likes.get_through_model()


class Comments(BaseModel):
    id = PrimaryKeyField()
    text = TextField()
    user_id = ForeignKeyField(User, on_delete='set null', null=True)
    post_id = ForeignKeyField(Posts, on_delete='set null', null=True)


# class Likes(BaseModel):
#     id = PrimaryKeyField()
#     user_id = ForeignKeyField(User, on_delete='set null', null=True)
#     post_id = ForeignKeyField(Posts, on_delete='set null', null=True)

# Likes.drop_table()
# Comments.drop_table()
# Posts.drop_table()
# User.drop_table()


User.create_table()
Posts.create_table()
Comments.create_table()
Likes.create_table()

# user1 = User(name='Francisco', age=18, gender='M', nationality='USA', email='1@mail')
# user1.save()
#
# User.create(name='Kate', age=35, gender='F', nationality='USA', email='2@mail)
# User.create(name='Tom', age=19, gender='F', nationality='USA', email='3@mail)
# #
# # users = User.select().execute()
# #
# # for x in users:
# #     print(x.name)
#
# data = [{'name': 'Kolya', 'age':13, 'gender':'f', 'nationality':'rus', 'email': 4@mail'},
#         {'name':'Petya', 'age':61, 'gender':'f', 'nationality':'rus', 'email': 5@mail'},
#         {'name':'Genry', 'age':25, 'gender':'f', 'nationality':'bel', 'email': 6@mail'},
#         {'name':'Rik', 'age':29, 'gender':'f', 'nationality':'bel', 'email': 7@mail'}]
#
# # User.insert_many(data, fields=[User.name, User.age, User.gender, User.nationality, User.email]).execute()
#
# user1 = User(**data[0]).save()
# Posts.create(
#     user_id=user1,
#     title="OHHHHHH",
#     description='adbgadgf;'
# )
