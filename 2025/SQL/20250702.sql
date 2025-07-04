-- 마지막으로 신입사원이 들어온 날은 언제 입니까? 다음 형식으로 출력해주세요.
-- 예) 2014년 07월 10일
-- SELECT TO_CHAR(max(hire_date), 'YYYY"년" MM"월" DD"일"' )  
-- FROM employees;

-- 문제3 부서별로 평균임금, 최고임금, 최저임금을 부서(department_id)와 함께 출력하고 정렬 순서는 부서번호의 내림차순
-- select DEPARTMENT_ID, avg(salary), max(salary), min(salary) from EMPLOYEES 
-- GROUP BY DEPARTMENT_ID ORDER BY DEPARTMENT_ID desc;

-- 문제4. 업무(JOB_ID)별로 평균임금, 최고임금, 최저임금을 업무와 함께 출력하고 정렬순서는 업무 내림차순
-- SELECT JOB_ID, AVG(SALARY), MAX(SALARY), MIN(SALARY) FROM EMPLOYEES GROUP BY JOB_ID ORDER BY JOB_ID DESC;

-- 문제5. 가장 오래 근속한 직원의 입사일은 언제인가요? 다음 형식으로 출력해주세요.
-- 2014년 07월 10일
-- SELECT TO_CHAR(MIN(HIRE_DATE), 'YYYY"년" MM"월" DD"일"') FROM EMPLOYEES;

-- HAVING절
-- SELECT DEPARTMENT_ID, COUNT(*), SUM(SALARY) 
-- FROM EMPLOYEES 
-- GROUP BY DEPARTMENT_ID 
-- HAVING SUM(SALARY) > 20000;


-- 문제6. 평균임금과 최저임금의 차이가 2000미만인 부서(DEPARTMENT_ID), 평균임금, 최저임금, 
-- 그리고 (평균-최저)임금을 (평균-최저)임금의 내림차순으로 정렬
-- SELECT DEPARTMENT_ID, AVG(SALARY), MIN(SALARY) AVG(SALARY)-MIN(SALARY) FROM EMPLOYEES 
-- GROUP BY DEPARTMENT_ID
-- HAVING AVG(SALARY)-MIN(SALARY) < 2000
-- ORDER BY AVG(SALARY)-MIN(SALARY) DESC;

-- 평균임금과 최저임금의 차이가 2000 미만인 
-- 부서(department_id), 평균임금, 최저임금, (평균임금 – 최저임금) 
-- (평균임금 – 최저임금)의 내림차순으로 정렬해서 출력하세요.
-- SELECT e.department_id, 
--        avg(e.salary) d_avg,
--        min(e.SALARY) d_min,
--        avg(e.salary) - min(e.SALARY) d_diff
-- FROM employees e
-- GROUP BY e.department_id
-- HAVING avg(e.salary) - min(e.SALARY) < 2000
-- ORDER BY 4 desc;

-- 문제7. 업무(JOB_ID)별로 최고임금과 최저임금의 차이를 출력. 차이를 확인할 수 있도록 내림차순 정렬
-- SELECT JOB_ID, MAX(SALARY)-MIN(SALARY) "최고-최저" FROM EMPLOYEES GROUP BY JOB_ID ORDER BY MAX(SALARY)-MIN(SALARY) DESC;


-- SELECT EMPLOYEE_ID, SALARY, 
--     CASE WHEN JOB_ID = 'AC_ACCOUNT' THEN SALARY + SALARY * 0.1
--          WHEN JOB_ID = 'AC_MGR' THEN SALARY + SALARY * 0.2
--          ELSE SALARY
--     END JOB_ID
-- FROM EMPLOYEES;

-- 직원의 이름, 부서, 팀을 출력하세요
-- 팀은 부서코드로 결정하며 
-- 부서코드가10~50 이면'A-TEAM', 60~100이면 'B-TEAM', 110~150이면 'C-TEAM' 나머지는 '팀없음' 으로 출력하세요
-- SELECT FIRST_NAME, JOB_ID, DEPARTMENT_ID,
--     CASE WHEN DEPARTMENT_ID >= 10 AND DEPARTMENT_ID <=50 THEN 'A-TEAM' 
--          WHEN DEPARTMENT_ID >= 60 AND DEPARTMENT_ID <=100 THEN 'B-TEAM' 
--          WHEN DEPARTMENT_ID >= 110 AND DEPARTMENT_ID <=150 THEN 'C-TEAM' 
--          ELSE '팀없음'
--     END "TEAM"
-- FROM EMPLOYEES;

-- 직원의 이름, 부서코드, 팀
-- 10~50   A-TEAM
-- 60~100  B-TEAM
-- 110~150 C-TEAM
-- 나머지    팀없음
-- SELECT e.FIRST_NAME,
--        e.DEPARTMENT_ID,
--        CASE WHEN e.DEPARTMENT_ID BETWEEN 10  AND  50 THEN 'A-TEAM'
--             WHEN e.DEPARTMENT_ID BETWEEN 50  AND 100 THEN 'B-TEAM'
--             WHEN e.DEPARTMENT_ID BETWEEN 110 AND 150 THEN 'C-TEAM'
--             ELSE '팀없음'
--        END "팀"
-- FROM EMPLOYEES e ;


-- SELECT FIRST_NAME, DEPARTMENT_NAME FROM EMPLOYEES, DEPARTMENTS;

-- SELECT em.first_name, em.department_id, de.department_name, de.department_id 
-- FROM employees em, departments de
-- where em.department_id = de.department_id;

-- 직원의 이름, 직급 아이디, 직급 명칭을 출력
-- join할 테이블 (employees, jobs)
-- SELECT * FROM EMPLOYEES EM, JOBS J;
-- SELECT EM.FIRST_NAME, J.JOB_ID, J.JOB_TITLE FROM EMPLOYEES EM, JOBS J WHERE J.JOB_ID = EM.JOB_ID;

-- 직원의 이름, 직급아이디, 직급명칭을 출력
-- SELECT e.FIRST_NAME ,
--        e.JOB_ID,
--        j.JOB_TITLE 
-- FROM EMPLOYEES e,
--      JOBS j 
-- WHERE e.JOB_ID = j.JOB_ID;


-- 모든 직원이름, 부서이름, 업무명을 출력
-- SELECT e.FIRST_NAME, d.DEPARTMENT_NAME, j.JOB_TITLE 
-- FROM EMPLOYEES e, DEPARTMENTS d, JOBS j 
-- WHERE e.DEPARTMENT_ID = d.DEPARTMENT_ID AND e.JOB_ID = j.JOB_ID;


-- 모든 직원이름, 부서이름, 업무명
-- SELECT e.FIRST_NAME ,
--        d.DEPARTMENT_NAME,
--        j.JOB_TITLE
-- FROM EMPLOYEES e ,
--      DEPARTMENTS d ,
--      JOBS j
-- WHERE e.JOB_ID = j.JOB_ID
-- AND e.DEPARTMENT_ID = d.DEPARTMENT_ID;

-- -- 1. LEFT OUTER JOIN
-- SELECT E.FIRST_NAME, M.FIRST_NAME 
-- FROM EMPLOYEES E, EMPLOYEES M 
-- WHERE E.MANAGER_ID = M.EMPLOYEE_ID(+); -- 이는 오라클 방식의 LEFT OUTER JOIN

-- -- ORACL SQL
-- SELECT E.FIRST_NAME, D.DEPARTMENT_ID 
-- FROM EMPLOYEES E, DEPARTMENTS D 
-- WHERE E.DEPARTMENT_ID = D.DEPARTMENT_ID(+);

-- -- ANSI SQL(표준)
-- SELECT E.DEPARTMENT_ID, E.FIRST_NAME, D.DEPARTMENT_ID 
-- FROM EMPLOYEES E LEFT OUTER JOIN DEPARTMENTS D
-- ON E.DEPARTMENT_ID = D.DEPARTMENT_ID;

-- -- 2. RIGHT OUTER JOIN
-- -- ORACLE SQL
-- SELECT E.DEPARTMENT_ID, E.FIRST_NAME, D.DEPARTMENT_ID 
-- FROM EMPLOYEES E, DEPARTMENTS D WHERE E.DEPARTMENT_ID(+) = D.DEPARTMENT_ID;

-- -- ANSI SQL
-- SELECT E.DEPARTMENT_ID, E.FIRST_NAME, D.DEPARTMENT_ID
-- FROM EMPLOYEES E RIGHT OUTER JOIN DEPARTMENTS D ON E.DEPARTMENT_ID = D.DEPARTMENT_ID;

-- -- FULL OUTER SQL
-- -- ORACLE SQL (못함. ANSI 방법으로 사용해야 됨)
-- SELECT E.DEPARTMENT_ID, E.FIRST_NAME, D.DEPARTMENT_ID 
-- FROM EMPLOYEES E, DEPARTMENTS D WHERE E.DEPARTMENT_ID(+) = D.DEPARTMENT_ID(+); 

-- -- ANSI SQL
-- SELECT E.DEPARTMENT_ID, E.FIRST_NAME, D.DEPARTMENT_ID
-- FROM EMPLOYEES E FULL OUTER JOIN DEPARTMENTS D ON E.DEPARTMENT_ID = D.DEPARTMENT_ID;

-- SELF JOIN = ALIAS를 사용하는 방법 밖에 없음(DEPARTMENTS "D" 같은 거)

-- 문제1. 각 사원(EMPLOYEE)에 대해서 
-- 사번(EMPLOYEE_ID), 이름(FIRST_NAME), 부서명(DEPARTMENT_NAME), 매니저(MANAGER)의 이름(FIRST_NAME)을 조회 -- 105개
-- SELECT E.EMPLOYEE_ID "사번", E.FIRST_NAME "이름", D.DEPARTMENT_NAME "부서명", M.FIRST_NAME "매니저 이름" 
-- FROM EMPLOYEES E, DEPARTMENTS D, EMPLOYEES M
-- WHERE E.DEPARTMENT_ID = D.DEPARTMENT_ID AND M.EMPLOYEE_ID = E.MANAGER_ID;

-- 문제2. 지역(REGIONS)에 속한 나라들을 지역이름(REGION_NAME), 나라이름(COUNTRY_NAME)으로 출력하되, 
-- 지역이름, 나라이름 순서대로 내림차순 정렬
-- SELECT R.REGION_NAME "지역이름", C.COUNTRY_NAME "나라이름" 
-- FROM COUNTRIES C, REGIONS R WHERE R.REGION_ID = C.REGION_ID ORDER BY R.REGION_NAME DESC, C.COUNTRY_NAME DESC;
-- -- 지역(regions)에 속한 나라들을 
-- -- 지역이름(region_name), 나라이름(country_name)으로 출력하되 
-- -- 지역이름, 나라이름 순서대로 내림차순으로 정렬하세요
-- select r.region_name, c.country_name
-- from hr.regions r, hr.countries c
-- where r.region_id = c.region_id 
-- order by 1 desc, 2 desc;


-- 문제3. 각 부서(department)에 대해서 
-- 부서번호(department_id), 부서이름(department_name), 
-- 매니저(manager)의 이름(first_name), 
-- 위치(locations)한 도시(city)
-- 나라(countries)

-- SELECT D.DEPARTMENT_ID, D.DEPARTMENT_NAME, E.FIRST_NAME, L.CITY 
-- FROM DEPARTMENTS D, EMPLOYEES E, LOCATIONS L, COUNTRIES C
-- WHERE E.DEPARTMENT_ID = D.DEPARTMENT_ID AND C.COUNTRY_ID = L.COUNTRY_ID AND D.LOCATION_ID = L.LOCATION_ID;

-- ??3번 패스함

-- 문제4. 'Public Accountant'의 직책(job_title) 으로 과거에 근무한 적이 있는 모든 사원의 사번과 이름을 출력하세요
-- (현재 Public Accountant의 직책으로 근무하는 사원은 고려하지 않습니다.)
-- FIRST_NAME과 LAST_NAME을 합쳐 출력합니다.  2명 나옴(101, 200)

-- SELECT E.EMPLOYEE_ID, E.FIRST_NAME || ' ' || E.LAST_NAME "FULLNAME" 
-- FROM JOBS J, EMPLOYEES E, JOB_HISTORY JH 
-- WHERE J.JOB_TITLE = 'Public Accountant'
-- AND J.JOB_ID = JH.JOB_ID
-- AND E.EMPLOYEE_ID = JH.EMPLOYEE_ID ;

-- SELECT e.EMPLOYEE_ID ,
--        e.FIRST_NAME || ' ' || e.LAST_NAME name
-- FROM hr.JOB_HISTORY jh, 
--      hr.EMPLOYEES e , 
--      hr.JOBS j 
-- WHERE jh.EMPLOYEE_ID = e.EMPLOYEE_ID 
-- AND   jh.JOB_ID = j.JOB_ID 
-- AND   j.JOB_TITLE = 'Public Accountant';


-- -- 계정 생성
-- CREATE USER webdb IDENTIFIED BY 1234;
-- -- 접속, 리소스 사용 권한부여
-- GRANT resource, CONNECT TO webdb;

-- CREATE TABLE book(
--     book_id number(5),
--     job_title varchar2(50),
--     author varchar2(10),
--     pub_date date
-- );

-- DROP TABLE author; -- 테이블 삭제
-- CREATE TABLE author(
--     author_id number(10),
--     author_name varchar2(100),
--     author_desc varchar2(500)
-- )

-- drop table book;
-- CREATE TABLE book (
--     book_id NUMBER(10),
--     title VARCHAR2(100) NOT NULL,
--     pubs VARCHAR2(100),
--     pub_date DATE,
--     author_id NUMBER(10),
--     PRIMARY KEY(book_id),
--     CONSTRAINT c_book_fk FOREIGN KEY (author_id)
--     REFERENCES author(author_id)
-- );
-- select * from book;
-- select * from author;

-- DROP TABLE author;
-- CREATE TABLE author(
--     author_id     number(10),
--     author_name   varchar2(100) NOT null,
--     author_desc   varchar2(500),
--     PRIMARY key(author_id)
-- );
-- SELECT * FROM author;

-- DROP TABLE book;
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

-- UPDATE AUTHOR SET author_name = '기안84', author_desc = '웹툰작가' WHERE author_id=1;

-- select * from author;

-- 문제1-1. 각 사원에 대해서 사번, 이름, 부서명, 직속상관 이름과 부서장(DEPARTMENTS 테이블의 매니저ID) 이름을 조회하세요
-- 105명 employees e, departments d, employees m, employees dm
-- 125, Julia, Shipping, Matthew, Adam
-- 127, James, Shipping, Matthew, Adam
-- 204, Hermann, Public Relations, Neena, Hermann
-- 126, Irene, Shipping, Matthew, Adam
-- 128, Steven, Shipping, Matthew, Adam
-- 180, Winston, Shipping, Matthew, Adam
-- 181, Jean, Shipping, Matthew, Adam
-- 182, Martha, Shipping, Matthew, Adam
-- 183, Girard, Shipping, Matthew, Adam
-- 137, Renske, Shipping, Shanta, Adam
-- 138, Stephen, Shipping, Shanta, Adam
-- SELECT E.EMPLOYEE_ID "사번", E.FIRST_NAME "이름", D.DEPARTMENT_NAME "부서명", M.FIRST_NAME "직속상관", DM.FIRST_NAME "부서장" 
-- FROM EMPLOYEES E, EMPLOYEES M, EMPLOYEES DM, DEPARTMENTS D
-- WHERE E.MANAGER_ID = M.EMPLOYEE_ID 
-- AND D.MANAGER_ID = DM.EMPLOYEE_ID 
-- AND D.DEPARTMENT_ID = E.DEPARTMENT_ID;

