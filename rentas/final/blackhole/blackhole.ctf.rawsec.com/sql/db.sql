
create table `contacts` (
    id int not null auto_increment,
    name text not null,
    email text not null,
    docs varchar(255) default null,
    primary key (id)
);