/*
insert into Person(id, name, Birthday) -- id는 고유값
values (1, "홍길동", "1999-01-01");

insert into Person values(10, "임꺽정", "1999-01-02"); -- 이런식으로 작성해도 되긴 함;;

/*
위와 같이 '작은 따옴표 안도', "큰 따옴표 안에 작성해도" 실행에 문제 없어 보임
속성이름을 소문자 대문자의 구분이 없어도 인지함
*/
/*
DELETE FROM Person; -- data 삭제, 데이터 구조는 남아있음
UPDATE Person SET name="세종";
select * from Person;
*/
--DROP TABLE Person;
--select * from Person;

INSERT INTO Ppap(Name, Birthday) VALUES ("박길동","1985-01-02"), ("최길동","1999-11-11"); -- help me!!
