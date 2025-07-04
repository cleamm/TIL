-- join 테이블을 합치는 작업( 주로 내부 조인(inner join)이 많이 쓰임 ) 교집합의 성향이 있음(양쪽 테이블에 같은 컬럼이 있어야 조인이 됨)
-- 외부 조인은 한쪽 테이블만 있어도 조인이 됨

-- varchar는 가변적 길이를 가지며 검색시 다소 느릴 수 있음. 공간 효율에서는 통상적으로 char보다 훨씬 좋음
-- char는 고정적 길이를 가지며 검색시 varchar보다 구조적으로 빠르며 공간 활용면에서는 사용되는 길이가 고정적일 경우 효율이 좋음. 

-- ANSI SQL 사용법을 익힐 것. non-ansi는 호환성 오류가 있을 수 있다는 듯함

-- 내부 조인
-- 각 테이블에서 조인 조건에 일치되는 데이터만 조인
-- equi, non-equi 조인으로 나뉨
-- 이퀴 조인은 조인 조건에 =연산자를 사용
-- 비이퀴 조인은 = 연산자 이외의 비교 연산자를 사용

-- 외부조인
-- 외부조인을 통해 조건에 맞지 않아도 함께 출력 가능
-- 데이터가 있는 것과 없는 것이 있으면 있는 것을 기준으로 데이터 출력

-- left or right 조인
-- from 테이블a left join 테이블b
-- 위와 같은 경우에는 left이므로 테이블a를 중심으로 데이터 출력함

-- self join
-- 테이블에서 자신을 참조함.(테이블 내 한 컬럼이 다른 컬럼을 참조)

/*
ANSI SQL : 미국 표준 SQL
'<>' == '!='

DBMS : SQL
미국 : 영어
호주 : 영어
영국 : 영어
대한민국 : 한국어
중국 : 중국어
세계 공통어로 영어가 꼽히는 것처럼
SQL은 ANSI SQL이 공용 SQL 용어를 사용할 수 있음
*/


use 한빛무역;
select * from 주문;
select * from 부서; -- 4건
select * from 사원; -- 10건

select * from 부서 cross join 사원; -- 1:n의 형식으로 모두 연결됨(4건 * 10건 = 총 40건)
select * from 부서 cross join 사원
where 이름 = '이소미';
-- ANSI SQL(공용이므로 가급적 이 사용법을 선호하는 것이 좋음)
select 부서.부서번호, 부서명, 이름, 사원.부서번호 as 사원부서번호 from 부서 
cross join 사원
where 이름 = '이소미';

-- NON ANSI SQL(mysql에서는 작동함)
select 부서.부서번호, 부서명, 이름, 사원.부서번호 as 사원부서번호 
from 부서, 사원
where 이름 = '이소미';

select * from 사원; -- 10건
select * from 부서;

-- ANSI SQL
select * from 사원 
inner join 부서 on 사원.부서번호 = 부서.부서번호
where 성별='여';

-- NON ANSI SQL
select * from 사원, 부서 
where 사원.부서번호 = 부서.부서번호 and 성별='여';

select * from 고객;
select * from 주문;

-- ANSI 표준으로 작성
select 고객.고객번호, 담당자명, 고객회사명, count(*) as 주문건수
from 고객
inner join 주문 -- non으로 작성할 때 join절과 on이 없어야 함. 이 조건은 전부 where로 이동하여 충족하면 됨
on 고객.고객번호 = 주문.고객번호
group by 고객.고객번호, 담당자명, 고객회사명
order by count(*) desc;

-- NON ANSI SQL
select 고객.고객번호, 담당자명, 고객회사명, count(*) as 주문건수
from 고객, 주문
where 고객.고객번호 = 주문.고객번호
group by 고객.고객번호, 담당자명, 고객회사명
order by count(*) desc;

select 고객번호, 고객회사명, 담당자명
from 고객;

select *
from 주문;

/*고객별  주문금액의 합계(SUM(주문수량 * 단가))를 출력(내림차순) */
select 고객.고객번호, 고객회사명, 담당자명, sum(주문수량 * 단가) as 주문금액합계
from 고객
inner join 주문
on 고객.고객번호 = 주문.고객번호
inner join 주문세부
on 주문.주문번호 = 주문세부.주문번호
group by 고객.고객번호, 고객회사명, 담당자명;

select * from 고객, 마일리지등급;

-- 테이블명.컬럼명 이렇게 select 하지 않더라도 중복되는 컬럼명이 아니라면 컬럼명만으로 조회도 됨
-- 테이블명.* 이라고 하면 당연히 테이블명의 모든 컬럼 조회가 가능함.
select 고객번호, 담당자명, 마일리지, 마일리지등급.*
from 고객
cross join 마일리지등급
where 담당자명 = '이은광';

-- 고객 테이블에서 담당자명이 '이은광'인 경우의 
-- 고객번호, 고객회사명, 담당자명, 마일리지, 마일리지등급을 출력
/* 고객 테이블에서 담당자명이 '이은광'인 경우의 고객번호, 고객회사명, 담당자명,
마일리지, 마일리지등급을 출력 */
/*고객 테이블의 마일리지 값을 마일리지등급 테이블의 하한, 상한마일리지 값의
범위에 따라 내부 조인 */

-- 아래는 join없이 사용한 나의 쿼리
select 고객번호, 고객회사명, 담당자명, 마일리지,
case when 마일리지 >= 100000 then 'S'
when 마일리지 >= 10000 then 'A'
when 마일리지 >= 1000 then 'B'
when 마일리지 >= 100 then 'C'
else 'D' end as 마일리지등급
from 고객
where 담당자명 = '이은광';

-- 아래는 inner join 사용한 쿼리 = 훨씬 간결하고 쉬워짐
select 고객번호, 고객회사명, 담당자명, 마일리지, 등급명
from 고객
inner join 마일리지등급
on 마일리지 >= 하한마일리지 and 마일리지 <= 상한마일리지
where 담당자명 = '이은광';

-- between을 사용한 방법
select 고객번호, 고객회사명, 담당자명, 마일리지, 등급명
from 고객
inner join 마일리지등급
on 마일리지 between 하한마일리지 and 상한마일리지
where 담당자명 = '이은광';


select * from 사원
left outer join 부서 -- left, right, full(mysql 지원x -> union으로 대체해야됨)
-- left면 from이 기준, right면 join 오른쪽의 테이블을 기준으로 삼음
on 사원.부서번호 = 부서.부서번호
where 성별 = '여';

-- 기준이 되는 테이블은 기본적으로 모든 데이터가 조회됨(타 테이블에 정보가 없어도 조회가 됨)
select * from 사원
right outer join 부서
on 사원.부서번호 = 부서.부서번호;
-- where 성별 = '여';

-- 사원테이블(기준)과 부서테이블을 외부 조인(부서번호)
-- => 사원테이블의 부서번호가 NULL인 부서명을 출력하시오.
-- 정답) 홍보부
select 부서명 from 사원
right outer join 부서
on 부서.부서번호 = 사원.부서번호
where 사원.부서번호 is null;

-- 소속 부서가 없는 사원의 이름과 부서번호, 부서명을 출력하시오
-- 정수진 null null

select * from 사원;

-- 소속 부서가 없는 사원의 이름과, 부서번호, 부서명을 출력하시오.
-- 정수진 null null
select 이름, 사원.부서번호, 부서명 from 사원
left outer join 부서
on 부서.부서번호 = 사원.부서번호
where 부서명 is null;

-- self join(빈도가 낮은 join 방식임;;)
-- 사원의 상사번호로 상사를 찾아야하는 상황이라면 self join을 사용하기 용이함
select 사원.상사번호, 상사.사원번호 as 상사번호, 사원.이름 as 후임, 상사.이름 as 상사 from 사원
left outer join 사원 as 상사
on 사원.상사번호 = 상사.사원번호
where 상사.이름 is not null;

-- 위같은 경우는 self join일까??
-- 셀프조인 - 사원번호, 사원이름, 상사의사원번호, 상사의 이름 출력
select 사원.사원번호, 사원.이름, 상사.사원번호, 상사.이름 from 사원
inner join 사원 as 상사
on 사원.상사번호 = 상사.사원번호;

-- 사원이름, 직위, 상사이름을 상사이름 순으로 정렬해서 출력
-- 상사가 없는 사원의 이름도 함께 출력
-- 셀프 조인으로 상사와 사원정보를 확인, 외부 조인으로 상사가 없는 사원 정보를 확인
select 사원.이름 as 후임이름, 사원.직위, 상사.이름 as 상사이름 from 사원
left outer join 사원 as 상사
on 사원.상사번호 = 상사.사원번호
order by 상사.이름;

-- 강사님 풀이
SELECT 사원.이름 AS 이름, 사원.직위, 상사.이름 AS 상사이름
FROM 사원 AS 상사
RIGHT OUTER JOIN 사원
ON 사원.상사번호 = 상사.사원번호
ORDER BY 상사이름;



-- sql 연습문제 3개
-- 한빛무역 DB의 제품 테이블과 주문세부 테이블을 조인하여 
-- 제품명별로 주문수량합과 주문금액합을 보이시오.
select * from 제품; -- 제품번호, 제품명, 포장단위, 단가, 재고
select * from 주문세부; -- 주문번호, 제품번호, 단가, 주문수량, 할인율

select 제품명, 
sum(주문수량) as 주문수량, 
sum(ceil((제품.단가 * 주문수량)*(1-할인율))) as 총주문금액
from 제품
left outer join 주문세부 on 제품.제품번호 = 주문세부.제품번호
group by 제품명;


-- 주문, 주문세부, 제품 테이블을 활용해 '아이스크림' 제품에 대해 (주문년도 제품명)별로 주문수량합을 조회
select * from 주문; -- 주문번호, 고객번호, 사원번호, 주문일, 요청일, 발송일 
select * from 주문세부; -- 주문번호, 제품번호, 단가, 주문수량, 할인율
select * from 제품; -- 제품번호, 제품명, 포장단위, 단가, 재고

select year(주문.주문일) as 주문년도, 제품.제품명, sum(주문세부.주문수량) as 주문수량합 from 제품
left outer join 주문세부
on 제품.제품번호 = 주문세부.제품번호
left outer join 주문
on 주문.주문번호 = 주문세부.주문번호
where 제품명 like '%아이스크림'
group by year(주문일), 제품명;

-- 제품, 주문세부 테이블을 활용해 제품명별로 주문수량합을 조회,
-- 이때 주문이 한번도 안된 제품에 대한 정보도 함께 조회할 것.
select * from 제품; -- 제품번호, 제품명, 포장단위, 단가, 재고
select * from 주문세부; -- 주문번호, 제품번호, 단가, 주문수량, 할인율

select 제품명, sum(주문세부.주문수량) as 주문수량합 from 제품
left outer join 주문세부
on 제품.제품번호 = 주문세부.제품번호
group by 제품명;