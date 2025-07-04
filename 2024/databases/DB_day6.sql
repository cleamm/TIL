/* 
서브쿼리(Subquery): SQL 내부에서 사용되는 select문
사용법은 괄호 안에 기술하도록 되어 있음. 복잡한 데이터를 추출함
서브쿼리가 먼저 실행된 후 메인 쿼리가 실행됨
select * from 테이블명
where 컬럼 = (select 컬럼 from 테이블명);
간단하게는 (select ...) 이런 구조면 서브쿼리임
*/
use 한빛무역;
select 고객번호, 담당자명, 마일리지 from 고객
where 마일리지 = (select max(마일리지) from 고객);


-- 고객 테이블에서 주문번호가 'H0250'인 고객에 대해
-- 고객회사명, 담당자명을 추출하시오.
select 고객회사명, 담당자명 from 고객
left outer join 주문
on 고객.고객번호 = 주문.고객번호
where 주문번호 = (select 주문번호 from 주문 where 주문번호 = 'H0250');

SELECT 고객회사명, 담당자명 FROM 고객
INNER JOIN 주문
ON 고객.고객번호 = 주문.고객번호
WHERE 주문번호='H0250';

select 고객회사명, 담당자명 from 고객
where 고객번호 = (select 고객번호 from 주문 where 주문번호 = 'H0250');

-- 부산광역시 고객의 최소마일리지보다 더 큰 마일리지를 가진 모든 고객 정보를 추출
select * from 고객
where 마일리지 > (select min(마일리지) from 고객 where 도시='부산광역시');

select * from 주문;
-- 부산광역시 고객 전체 주문건수를 출력
select count(*) as 주문건수 from 주문
where 고객번호 in (select 고객번호 from 고객 where  도시='부산광역시');

-- 부산광역시 전체 고객의 마일리지를 추출하시오: 2819 806 7795 1177 7329
-- 부산광역시 전체 고객의 마일리지를 추출 -> 최소 1명 이상의 부산광역시 고객 마일리지보다 더 큰 고객 정보 조회
-- ANY : 서브쿼리의 각 결과에 대해 비교했을 때 최소 1건 이상 조건이 만족되는 자료 조회
select 마일리지 from 고객
where 도시 in(select 도시 from 고객 where 도시='부산광역시');

select * from 고객
where 마일리지 > any (select 마일리지 from 고객 where 도시='부산광역시');


select 마일리지 from 고객
where 도시 = '부산광역시';

-- 고객 테이블에서 지역별로 마일리지 평균 조회
select 지역, avg(마일리지) from 고객
group by 지역;

-- 각 지역의 어느 평균 마일리지보다도 더 큰 마일리지를 갖고있는 고객정보를 조회
-- any : 여러 개 중에 저거어도 1개 이상 조건에 해당하면 조회
-- all : 여러 개 모두에 대해 조건에 부합하면 조회

select * from 고객
where 마일리지 > all (select avg(마일리지)
from 고객 group by 지역);

select avg(마일리지) from 고객 group by 지역;

-- 고객 중 최소 1번 이상 주문한 적이 있다면 해당 고객의 정보를 조회
select * from 고객
where 고객번호 in (select 고객번호 from 주문);

-- select * from 주문 where 고객번호=고객.고객번호;
-- 위 코드는 당연히 안됨=고객테이블이 없는 상태임

select * from 고객
where exists 
(select 고객번호 from 주문 where 고객번호=고객.고객번호);

-- join을 사용한 문제풀이
select * from 고객
inner join 주문
on 고객.고객번호 = 주문.고객번호;

SELECT DISTINCT 고객회사명
FROM 고객
INNER JOIN 주문
ON 고객.고객번호 = 주문.고객번호;

-- 고객 테이블 전체의 평균마일리지보다 큰 도시에 대해 
-- 도시명, 도시 평균마일리지 조회
select 도시 as 도시명, avg(마일리지) as 도시평균마일리지 from 고객
where 마일리지 > (select avg(마일리지) from 고객)
group by 도시;
-- 위는 내가 작성한 코드인데 where절에 avg를 이용할 수가 없으므로 having절로 변경하여 사용해야 될듯함
-- 위에서 아래와 같이 변경해야됨
select 도시, avg(마일리지) as 평균마일리지
from 고객
group by 도시
having avg(마일리지) > (select avg(마일리지) from 고객);

-- 결과 필터링에 사용되는 것이 where절이며(열단위)
-- 그룹 단위의 필터링이 필요할 때 having절을 사용해야됨

-- DML: 데이터 조작어
-- 부서번호 : A5, 부서명 : 마케팅부 추가
select * from 부서;
insert into 부서 values('A5', '마케팅부');

insert into 제품 values(999,'맛동산',1500,10); -- 포장단위 누락 에러
insert into 제품 values(999,'맛동산',null,1500,10);
select * from 제품;

insert into 제품(제품번호, 제품명, 단가, 재고)
values(888, '새우깡', 2000, 50); -- 컬럼이 지정되었으므로 에러가 없음

insert into 제품(제품명, 단가, 재고)
values('새우깡', 1000, 30); -- 에러 발생 : 제품번호(NN)값이 입력이 안됨
-- 위 에러는 primary key, 즉 고유번호가 있어야 하는데 입력되지 않았음

/*
학번 수강과목 이름...
1    	DB    
1
1
PK(학번, 수강과목)
*/

select * from 사원;

insert into 사원(사원번호, 이름, 직위, 성별, 입사일)
values('E20', '홍길동', '수습사원', '남', curdate());
-- 위 코드를 두번 실행하면 사원번호(PK)가 중복되므로 에러를 출력

insert into 사원(사원번호, 이름, 직위, 성별, 입사일)
values('E21', '임꺽정', '수습사원', '남', curdate()),
('E22', '신사임당', '수습사원', '여', curdate());
-- 위와 같이 연속으로 여러 데이터를 삽입하는 방법이 있음

select * from 사원;

/* 
update : 데이터를 변경
update 테이블명
set 컬럼 = 값, 컬럼 = 값
where 조건
보통 열 전체를 바꾸지 않으므로 where를 붙여서 사용함
*/
-- E01 자료 검색 => 이름 : 김소미 변경
update 사원 
set 이름 = '김소미' 
where 사원번호 = 'E01';

select * from 사원;

select * from 제품;

/*
고래밥, 제품번호:111, 단가:2500, 재고: 40 추가
고래밥 -> 상어밥으로 변경
새우깡의 단가를 10% 인상
맛동산의 재고를 10 증가
*/
insert into 제품(제품번호, 제품명, 단가, 재고) 
values(111, '고래밥', 2500, 40);
update 제품 set 제품명 = '상어밥' where 제품명 = '고래밥'; 
update 제품 set 단가 = 단가*1.1 where 제품명 = '새우깡';
update 제품 set 재고 = 재고 + 10 where 제품명 = '맛동산';

-- delete 테이블명 where 조건;
select * from 제품;
delete from 제품 where 제품번호 = 999;
-- 위 코드로 제품번호 999에 해당하는 행을 삭제

select * from 사원 order by 입사일 desc;

delete from 사원 order by 입사일 desc limit 3;
-- 위 코드로 사원 테이블의 입사일 내림차순 상위 3개를 삭제함

select * from 부서;

-- A1, 부서명: 총무부 추가
insert into 부서(부서번호, 부서명)
values('A1', '총무부'); -- 에러 발생(PK 중복)

insert into 부서(부서번호, 부서명)
values('A1', '총무부')
on duplicate key update -- 위코드를 실행하고 안되면 뒷 내용을 업데이트
부서명 = '총무부';

/*
삭제를 하면 취소도 할 수 있어야 하는 법
commit, rollback 명령어가 있음(단 데이터 관리자가 하는 일임)
autocommit : 설정(1)
commit(작업저장=>복원X), rollback(복원)
물론 이게 끝이 아니라 로그를 통해서 복원을 할 수도 있기는 하나,
우리의 영역이 아님
*/

-- select 문 수행 결과를 다른 테이블에 추가
/*
insert into 테이블명(컬럼1, 컬럼2,..)
select 컬럼1, 컬럼2,...
from 테이블명
where 조건
*/

/* 예시 쿼리
insert into 고객(고객번호, 담당자명, 주소, 마일리지)
select 고객번호, 담당자명, 주소, 마일리지 from 고객2
where 주소 = '서울특별시';
고객2테이블에서 주소가 서울특별시인 고객의 고객번호, 담당자명, 주소, 마일리지를
각각 추출하여 고객 테이블의 고객번호, 담당자명, 주소, 마일리지 열에 추가
*/

/* 테이블 생성 방법
create table 고객2(
고객번호 char(5) primary key,
담당자명 varchar(20),
주소 varchar(50),
마일리지 int 고객2);
*/

select * from 고객2;

SELECT * FROM 고객2;

INSERT INTO 고객2(고객번호, 담당자명, 주소, 마일리지)
VALUES('AAAAA', '홍길동', '서울특별시', 50000);

INSERT INTO 고객(고객번호, 담당자명, 주소, 마일리지)
SELECT 고객번호, 담당자명, 주소, 마일리지
FROM 고객2;

SELECT * FROM 고객;

-- 고객2에 (BBBBB, 임꺽정, '광주광역시', 10000) 레코드를 추가
-- 고객테이블에 고객테이블 데이터를 추가
select * from 고객2;

insert into 고객2 values('BBBBB', '임꺽정', '광주광역시', 10000);
delete from 고객 where 고객번호='AAAAA';
insert into 고객(고객번호, 담당자명, 주소, 마일리지)
select 고객번호, 담당자명, 주소, 마일리지
from 고객2;


-- 문제풀이
-- 1 배재용 사원의 부서명 조회
select 부서명 from 부서
where 부서번호 = (select 부서번호 from 사원 where 이름 = '배재용');

-- 2 한번도 주문한 적이 없는 제품의 정보를 조회
select *, 단가*재고 as 재고금액 from 제품
where 제품번호 not in (select 제품번호 from 주문세부);

-- 3 담당자명, 고객회사명, 주문건수, 최초주문일과 최종주문일 조회
select * from 고객;

select 담당자명, 고객회사명, count(주문.고객번호), min(주문일), max(주문일) from 주문
right outer join 고객
on 주문.고객번호 = 고객.고객번호 
group by 고객.고객번호;

-- 4 제품 테이블에 레코드를 추가하시오.
insert into 제품(제품번호, 제품명, 포장단위, 단가, 재고)
values(95, '망고베리 아이스크림', '400g', 800, 30);

-- 5 제품 테이블에 레코드 추가
insert into 제품(제품번호, 제품명, 단가)
values(96, '눈꽃빙수맛 아이스크림', 2000);

-- 6 96번 제품의 재고를 30으로 변경
update 제품 set 재고 = 30 where 제품번호 = 96;

-- 7 사원이 한명도 존재하지 않는 부서를 부서 테이블에서 삭제
delete from 부서
where 부서번호 not in (select 부서번호 from 사원);