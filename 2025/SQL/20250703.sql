-- --각 사원에 대해서 사번, 이름, 부서명, 직속상관이름, 부서장이름을 조회하세요.
-- --// 105명 employees e, departments d, employees m, employees dm
-- SELECT e.EMPLOYEE_ID "사번",
--        e.FIRST_NAME "이름",
--        d.DEPARTMENT_NAME "부서명",
--        m.FIRST_NAME "직속상관",
--        dm.FIRST_NAME "부서장"
-- FROM employees e, departments d, employees m, employees dm
-- WHERE e.DEPARTMENT_ID = d.DEPARTMENT_ID
-- AND  e.MANAGER_ID = m.EMPLOYEE_ID
-- AND  d.MANAGER_ID = dm.EMPLOYEE_ID;


-- CREATE TABLE author(
--     author_id     number(10),
--     author_name   varchar2(100) NOT null,
--     author_desc   varchar2(500),
--     PRIMARY key(author_id)
-- );
-- SELECT * FROM author;

-- CREATE TABLE book (
--   book_id     NUMBER(10),
--   title     VARCHAR2(100) NOT NULL,
--   pubs     VARCHAR2(100),
--   pub_date     DATE,
--   author_id NUMBER(10),
--   PRIMARY     KEY(book_id),
--   CONSTRAINT c_book_fk FOREIGN KEY (author_id)
--   REFERENCES author(author_id)
-- );
-- SELECT * FROM book;

-- INSERT INTO author VALUES (1, '박경리', '토지 작가');
-- INSERT INTO author(author_id, author_name) VALUES (2, '이문열');

-- UPDATE AUTHOR SET AUTHOR_NAME = '기안84', AUTHOR_DESC = '웹툰작가' WHERE AUTHOR_ID = 1;

-- SELECT * FROM AUTHOR;

-- DELETE FROM AUTHOR WHERE AUTHOR_ID = 1;
-- SELECT * FROM AUTHOR;


-- DROP SEQUENCE SEQ_AUTHOR_ID;
-- CREATE SEQUENCE SEQ_AUTHOR_ID INCREMENT BY 1 START WITH 1;

-- INSERT INTO AUTHOR VALUES (SEQ_AUTHOR_ID.NEXTVAL, '박경리', '토지 작가 ');
-- INSERT INTO AUTHOR VALUES (SEQ_AUTHOR_ID.NEXTVAL, '이문열', '삼국지 작가');


-- DROP TABLE BOOK;
-- DROP TABLE AUTHOR;
-- -- 테이블 BOOK, AUTHOR 순 드랍 및 생성 진행 후 아래 코드
-- DELETE FROM AUTHOR WHERE AUTHOR_ID > 0;
-- CREATE SEQUENCE SEQ_AUTHOR_ID INCREMENT BY 1 START WITH 1;

-- INSERT INTO AUTHOR VALUES (SEQ_AUTHOR_ID.NEXTVAL, '이문열', '경북 영양');
-- INSERT INTO AUTHOR VALUES (SEQ_AUTHOR_ID.NEXTVAL, '박경리', '경상남도 통영');
-- INSERT INTO AUTHOR VALUES (SEQ_AUTHOR_ID.NEXTVAL, '유시민', '17대 국회의원');
-- INSERT INTO AUTHOR VALUES (SEQ_AUTHOR_ID.NEXTVAL, '기안84', '기안동에서 산 84년생');
-- INSERT INTO AUTHOR VALUES (SEQ_AUTHOR_ID.NEXTVAL, '강풀', '온라인 만화가 1세대');
-- INSERT INTO AUTHOR VALUES (SEQ_AUTHOR_ID.NEXTVAL, '김영하', '알쓸신잡');

-- SELECT * FROM AUTHOR;


-- SELECT * FROM BOOK;
-- CREATE SEQUENCE SEQ_BOOK_ID INCREMENT BY 1 START WITH 1;
-- INSERT INTO BOOK VALUES (SEQ_BOOK_ID.NEXTVAL, '우리들의 일그러진 영웅', '다림', TO_DATE('1998-02-22', 'YYYY-MM-DD'), 81);
-- INSERT INTO BOOK VALUES (SEQ_BOOK_ID.NEXTVAL, '삼국지', '민음사', TO_DATE('2002-03-01', 'YYYY-MM-DD'), 81);
-- INSERT INTO BOOK VALUES (SEQ_BOOK_ID.NEXTVAL, '토지', '마로니에북스', TO_DATE('2012-08-15', 'YYYY-MM-DD'), 82);
-- INSERT INTO BOOK VALUES (SEQ_BOOK_ID.NEXTVAL, '유시민의 글쓰기 특강', '생각의길', TO_DATE('2015-04-01', 'YYYY-MM-DD'), 83);
-- INSERT INTO BOOK VALUES (SEQ_BOOK_ID.NEXTVAL, '패션왕', '중앙북스(books)', TO_DATE('2012-02-22', 'YYYY-MM-DD'), 84);
-- INSERT INTO BOOK VALUES (SEQ_BOOK_ID.NEXTVAL, '순정만화', '재미주의', TO_DATE('2011-08-03', 'YYYY-MM-DD'), 85);
-- INSERT INTO BOOK VALUES (SEQ_BOOK_ID.NEXTVAL, '오직두사람', '문학동네', TO_DATE('2017-05-04', 'YYYY-MM-DD'), 86);
-- INSERT INTO BOOK VALUES (SEQ_BOOK_ID.NEXTVAL, '26년', '재미주의', TO_DATE('2012-02-04', 'YYYY-MM-DD'), 85);

-- SELECT B.BOOK_ID, TITLE, PUBS, TO_CHAR(PUB_DATE, 'YYYY-MM-DD') "PUB_DATE", A.AUTHOR_ID, AUTHOR_NAME, AUTHOR_DESC 
-- FROM BOOK B, AUTHOR A WHERE B.AUTHOR_ID = A.AUTHOR_ID;