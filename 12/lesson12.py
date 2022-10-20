create database if not exists test1;
show databases;
use test1;
create table users(
	id int primary key auto_increment,
    name varchar(10),
    age int(11),
    gender varchar(10),
    nationality varchar(10)
    );

show tables;
drop table users;

delete from users where id=5;


insert users(name, age, gender, nationality) values (
	'Liam', 40, 'male', 'USA'
    );
insert users(name, age, gender, nationality) values (
	'Emma', 28, 'female', 'BR'
    );
insert users(name, age, gender, nationality) values (
	'Mia', 31, 'female', 'BEL'
    );
insert users(name, age, gender, nationality) values (
	'Oliver', 53, 'male', 'BEL'
    );

select * from users;
select name, age from users;

create table posts (
	id int primary key auto_increment,
    user_id int,
    title varchar(100),
    description varchar(100),
    foreign key (user_id) references users (id)
    );

select * from posts;

insert posts(user_id, title, description) values(
  3, 'Чего хорошего в этом?', 'да так, ничего особенного'
);
insert posts(user_id, title, description) values(
  4, 'как сделать?', 'не получается'
);

create table comments (
	id int primary key auto_increment,
    text varchar(100),
    user_id int,
    foreign key (user_id) references users (id),
    post_id int,
    foreign key (post_id) references posts (id)
    );

select * from comments;
drop table comments;

insert comments(text, user_id, post_id) values(
  'все хорошо, правильно', 1, 3
);


create table likes (
	id int primary key auto_increment,
    user_id int,
    foreign key (user_id) references users (id),
    post_id int,
    foreign key (post_id) references posts (id)

    );

select * from likes;
drop table likes;

insert likes(user_id, post_id) values(
  4, 1
  );