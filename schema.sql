drop table if exists registrants;
create table registrants (
    name TEXT NOT NULL, 
    email TEXT NOT NULL,
    subject TEXT NOT NULL,
    message TEXT NOT NULL
);