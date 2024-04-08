use 한빛무역;
select * from 고객;
select char_length('hello');
select char_length("반갑습니다"),
length("hello"),
length("반갑습니다");

select concat("반갑습니다","안녕하세요", "잘가세요"),
concat_ws("-","반갑습니다","안녕하세요", "잘가세요");

select left('ai 서비스 개발', 5),
right('ai 서비스 개발',5),
substr('ai서비스개발',3,4), -- substr('글자', 시작할 인덱스, 글자개수)
substr('ai 서비스 개발',2);

select substring_index('서울특별시 강남구 역삼동', ' ', 2); -- 2번째 띄어쓰기부터 뒷내용 제거
select substring_index('강북구강남구영등포구', '구', 2); -- 2번째 '구'부터 뒷내용 제거
select substring_index('서울특별시 강남구 역삼동', ' ', -2);  -- 2번째 띄어쓰기 포함, 이전 내용 제거

-- distinct 뒤에 두개 이상의 컬럼이 들어오면 열의 조합이 중복될 때 제거함
select distinct 지역, 도시 from 고객;

-- 특정 문자로 채우기 --
select lpad('sql', 5, '#');
select rpad('sql', 5, '#');

-- 공백 제거 -- 
select ltrim('   sql   ');
select rtrim('   sql   ');
select trim('    sql   ');

-- 1.양쪽  2.왼쪽  3.오른쪽) 동일 문자열 제거 --
select trim(both 'ab' from 'abacbcdab');
select trim(leading 'ab' from 'ababcdab');
select trim(trailing 'ab' from 'ababcdab'); 

-- field(찾으려는 문자열, 문자열1, 문자열2,...) = 인덱스 반환
select field('java', 'sql', 'java', 'c');
select find_in_set('java', 'sql,java,c'); -- 띄어쓰기가 있으면 탐색이 안되는듯;;

-- instr(문자열, 찾을 문자열) = 첫글자 인덱스 반환
-- locate(찾을 문자열, 문자열) 위와 같은 결과
select instr('네 인생을 살아라', '인생');
select locate('인생', '네 인생을 살아라');

-- elt(인덱스 번호, '문자열1, 문자열2,...) = 인덱스값에 해당하는 데이터 반환(파이썬 인덱싱임)
select elt(3, 'hello', 'hi', 'hiihi');

-- repeat(문자열, 횟수) = 문자열 반복(자바스크립트 repeat와 동일)
select repeat('ㅋ',10);

-- replace('전체 문자열', '변경전 문자열', '변경후 문자열') = 문자열 치환 함수 
select replace('010.1234.5678', '.', '-'); -- .이 -로 바뀜

-- reverse('문자열') 문자열 뒤집기
select reverse('abcd');

-- 자릿수 지정 함수
select ceiling(123.56); -- 올림
select floor(123.56); -- 내림
select round('123.4'); -- 반올림 and 따옴표로 묶어도 계산됨
select round('123.36', 1); -- 첫째자리까지 반올림
select truncate(123.56, 1); -- 첫째자리까지 남기고 버림

select abs(-3); -- 절대값
select abs(3);
select sign(1); -- 부호 판별 (양, 음, 0) 중 하나
select sign(3);

 -- 나머지값
select mod(10, 4);
select 10%4;
select 10 mod 4;

select power(2,4); -- 제곱
select power(2,1/2); -- 제곱근1
select sqrt(49); -- 제곱근2
select rand(); -- 랜덤값(소수)
select rand(20240405); -- 괄호에 입력한 시드값으로 출력됨 = 지정된 값이 있음

select round(rand()*2); -- 0 <= rand() < 1

select now(); -- 날짜+시간
select curdate(); -- 날짜
select curtime(); -- 시간

select year(now()), month(now());
select quarter(now());
select hour(now());
select minute(now());
select day(now());
select day(curdate()); -- 이것되 되네;;
select datediff('2024-01-19', '2024-04-05'); -- datediff(종료일자, 시작일자)
select timestampdiff(day, now(), '2024-04-30'); -- 단위, 시작, 끝
select timestampdiff(month, now(), '2024-12-30');
select timestampdiff(year, now(), '2025-12-30');

select adddate(now(), 28); -- 당일부터 +한 날짜 혹은 시간
select adddate(now(), interval 20 day);
select adddate(now(), interval 20 month);
select adddate(now(), interval 20 hour);

select subdate(now(), interval 20 hour); -- 당일부터 -한 날짜 혹은 시간
select last_day(now()); -- 현재 월의 마지막 일자
select dayofyear(now()); -- 올해 며칠 경과했는가
select weekday(now()); -- 요일 0: 월요일

-- 데이터 형 변환 : cast(값 as 타입), convert()
select cast(45 as unsigned); -- unsigned: 부호가 없는 형태
select cast(45 as signed);
/* signed
1byte = 8bit => 1bit:부호(0 또는 1), 7bit: 숫자
7bit = -128... 0,~127
unsigned
1byte = 8bit => 1bit:부호(0 또는 1), 8bit: 숫자
부호가 없으므로 범위가 2배로 커짐
8bit = 0~255
*/

select cast(1 as char(1)); -- 숫자 1 => 문자 1
select convert(1, char(1)); -- 숫자 1 => 문자 1

-- if(조건식, 참, 거짓)
select if(1+2>0, '양수', '음수');

select ifnull(5, 10);
select ifnull(null, 10);
-- ifnull함수의 1번째 인수가 null이 아니면 1번째 인수를 반환,
-- null이면 2번째 인수 반환;

select nullif(3, 5); -- 두 값이 같으면 null 다르면 1번째 인수 반환

-- when 조건1 then 값1 when 조건2 then 값2
select case when 100*2 > 300 then '합격!'
when 100*2 > 200 then '불합격'
else '재시험' end;

select sum(마일리지) from 고객 where 도시 = '대전광역시';
-- select 집계함수 from 테이블명 ...(where 등)

select count(지역) from 고객; -- count함수는 null을 탐색하지 않음
select count(*), count(도시), count(고객번호), count(지역) from 고객;
-- 위와 같은 방법으로 여러 열들에 대해서 null값이 있는지 확인할 수 있음.

select sum(마일리지), avg(마일리지), min(마일리지), max(마일리지) from 고객;

/* 고객 테이블에서 '서울특별시' 고객에 대한 마일리지를 각(합, 최대, 최소, 평균)을 출력*/
select sum(마일리지), max(마일리지), min(마일리지), avg(마일리지) from 고객
where 도시 = '서울특별시';

-- group by절 : 그룹별로 묶어서 요약
/*
select 그룹으로 묶을 열, 집계함수
from 테이블명
where 조건
group by 그룹으로 묶을 열(번호)
*/

select 도시, count(도시) as 소속인원, sum(마일리지) as 마일리지합계, avg(마일리지) as 마일리지평균 
from 고객 group by 도시;

/* 도시 단위로 그룹화 -> 그룹별 마일리지의 합계*/
select 도시, count(*) as 고객수, sum(마일리지) as 마일리지합계, avg(마일리지) as 마일리지평균
from 고객
group by 1;
/*각 도시별 '고객수' 열을 추가 */
select 도시, count(도시) as 고객수 from 고객 group by 도시;

select 담당자직위, count(담당자직위) from 고객 group by 담당자직위;
select 도시, count(도시) from 고객 group by 도시;

-- 담당자직위별로 그룹화, 같은 담당자직위에 대해서 도시별로 그룹화 -> 집계
select 담당자직위, 도시, avg(마일리지) as 평균마일리지, count(*) as 고객수 
from 고객 group by 담당자직위, 도시;

-- having 절 : group by에 대한 조건
/*
select 그룹으로 묶을 열, 집계함수
from 테이블명
where 조건
group by 그룹을 묶을 열(번호)
having
*/

-- 도시별로 그룹화, 고객수, 평균마일리지 조회 후 고객수 3명이상인 레코드 조회
select 도시, count(*) as 고객수, avg(마일리지) as 평균마일리지 
from 고객 group by 도시
having 고객수 >= 3;

-- 고객테이블에서 고객번호가 T로 시작하는 고객을 검색
-- T로 시작하는 고객을 도시별로 묶어서 고객의 마일리지 합계 조회
select 도시, sum(마일리지) from 고객
where 고객번호 like 'T%'
group by 도시
having sum(마일리지) >= 500;

-- 광역시 고객에 대해 담당자직위별로 최대마일리지 조회, 최대마일리지가 5000점 이상인 레코드만 조회
select 담당자직위, max(마일리지) as 최대마일리지 from 고객
where 도시 like '%광역시'
group by 담당자직위
having 최대마일리지 >= 5000;

-- with rollup : 그룹별 소계, 전체 총계 구할 때 사용 group by 다음에 사용
select 도시, count(*) as 고객수,  avg(마일리지) as 평균마일리지 from 고객 
where 지역 is null
group by 도시
with rollup; -- 각 컬럼의 합계를 연산하여 조회

-- 담당자직위에 '마케팅'이라는 단어가 들어간
-- 고객(담당자직위, 도시)별 고객수를 출력
-- 출력 : 담당자직위 도시 고객수
select 담당자직위, 도시, count(*) as 고객수 from 고객
where 담당자직위 like '%마케팅%'
group by 담당자직위, 도시;
-- with rollup;
