-- 다음 조건에 따라 고객 테이블에서 고객회사명과 전화번호를 다른 형태로 보이도록 함수를 사용해봅시다.
-- 고객회사명2와 전화번호2를 만드는 조건은 다음과 같습니다.alter
-- 조건
-- 고객회사명2: 기존 고객회사명 중 앞의 두자리를 *로 변환한다.
-- 전화번호2: 기존 전화번호의 (xxx)xxx-xxxx형식을 xxx-xxx-xxxx로 변환
use 한빛무역;

select 고객회사명, 
	replace(고객회사명,left(고객회사명,2), '**') as 고객회사명2, 
    전화번호, 
    replace(replace(전화번호, left(전화번호,1),''), ')', '-') as 전화번호2 
from 고객;

-- 2
select * from 주문세부;
select *,
truncate(주문수량 * 단가, -1) as 주문금액, 
truncate(주문수량 * 단가 * 할인율, -1) as 할인금액, 
truncate((주문수량 * 단가) - (주문수량 * 단가 * 할인율),-1) as 실주문금액 
from 주문세부;

-- 3
select * from 사원;
select 이름, 생일, 
timestampdiff(year, 생일, now()) as 만나이, 
입사일, 
timestampdiff(day, 입사일, now()) as 입사일수, 
adddate(입사일, 500) as 500일후 
from 사원;

-- 4 고객 테이블에서 도시 컬럼의 데이터를 다음 조건에 따라 대도시와 도시로 구분, 마일리지 점수에 따라 vvip, vip, 일반 고객으로 구분하라.
select 담당자명, 고객회사명, 도시, 
case when 도시 like '%광역시' or 도시 like '%특별시' then '대도시' else '일반도시' end as 도시구분, 
마일리지, 
마일리지 as 마일리지구분 
from 고객;

-- 5
select 주문번호, 고객번호, 주문일, 
year(주문일) as 주문년도, 
quarter(주문일) as 주문분기, 
month(주문일) as 주문월, 
day(주문일) as 주문일,
weekday(주문일) as 주문요일,
case when weekday(주문일) = 0 then '월요일' 
when weekday(주문일) = 1 then '화요일' 
when weekday(주문일) = 2 then '수요일'
when weekday(주문일) = 3 then '목요일'
when weekday(주문일) = 4 then '금요일'
when weekday(주문일) = 5 then '토요일'
else '일요일' end as 한글요일
from 주문;

-- 6
select *, timestampdiff(day, 요청일, 발송일) as 지연일수 from 주문
having 지연일수 > 6;