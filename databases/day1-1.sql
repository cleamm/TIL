/*
delete from Ppap;
insert into Ppap
values (1, '홍길동', '1988-08-28');

insert into Ppap(id, name, birthday) values (2, '이순신', '1000-10-10');

insert into Ppap(name, birthday) values('김길동','1988-08-28'), ('박길동', '1988-08-28');
*/
delete from practice0402;
insert into practice0402(id, name, addr, tel) 
values (1, '이명박', '서울시', '010-1234-5678'), (2, '박근혜', '인천시','010-1111-2222');

select * from practice0402;

update practice0402 set name='문재인'; -- where = 1 이라고 하면 id값이 지정됨

select * from practice0402 where addr='서울시';