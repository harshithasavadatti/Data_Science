--📊 B. Analytical / Window Functions (30 Questions)

--1.Assign row numbers to customers ordered by credit limit descending.
-- select cust_id,cust_first_name, cust_last_name , cust_credit_limit,
-- row_number() over (order by cust_credit_limit desc) as row_num
-- from sh.customers

--2.Rank customers within each state by credit limit.
-- select cust_id, cust_first_name,cust_last_name, cust_credit_limit, 
-- rank() over (partition by cust_state_province
--              order by cust_credit_limit desc ) as state_rank
-- from sh.customers
-- order by cust_state_province,state_rank

--3.Use DENSE_RANK() to find the top 5 credit holders per country.
-- select * from (
--     select
--     h.country_name,c.cust_first_name, c.cust_last_name,c.cust_credit_limit,
--     dense_rank() over(partition by h.country_name order by c.cust_credit_limit desc)
--     as rank_in_country
-- from sh.customers c
-- join sh.countries h on c.country_id = h.country_id )
-- where rank_in_country <= 5
-- order by country_name, rank_in_country, cust_credit_limit DESC;

--4.Divide customers into 4 quartiles based on their credit limit using NTILE(4).
-- SELECT 
--     cust_first_name,
--     cust_last_name,
--     cust_credit_limit,
--     NTILE(4) OVER (ORDER BY cust_credit_limit DESC) AS credit_quartile
-- FROM sh.customers
-- ORDER BY credit_quartile, cust_credit_limit DESC

--5.Calculate a running total of credit limits ordered by customer_id.
-- select cust_id, cust_first_name , cust_last_name , cust_credit_limit,
-- sum(cust_credit_limit)over (order by cust_id) as running_total
-- from sh.customers
-- order by cust_id

--6.Show cumulative average credit limit by country.
-- SELECT 
--     h.country_name,
--     c.cust_id,
--     c.cust_credit_limit,
--     AVG(c.cust_credit_limit) OVER (
--         PARTITION BY h.country_name 
--         ORDER BY c.cust_id
--     ) AS cumulative_avg
-- FROM sh.customers c
-- JOIN sh.countries h 
--     ON c.country_id = h.country_id
-- ORDER BY h.country_name, c.cust_id;

--7.Compare each customer’s credit limit to the previous one using LAG().
-- select cust_id, cust_first_name, cust_last_name , cust_credit_limit,
-- lag(cust_credit_limit) over (order by cust_id) as prev_credit_limit,
-- (cust_credit_limit - lag(cust_credit_limit)over (order by cust_id)) as difference
-- from sh.customers

--8.Show next customer’s credit limit using LEAD().
-- select cust_id, cust_first_name, cust_last_name, cust_credit_limit, 
-- lead(cust_credit_limit) over (order by cust_id) as next_credit_limit
-- from sh.customers

--9.Display the difference between each customer’s credit limit and the previous one.
-- SELECT cust_id,cust_first_name,cust_last_name, cust_credit_limit,
-- cust_credit_limit - LAG(cust_credit_limit) OVER (ORDER BY cust_id) AS diff_from_previous
-- FROM sh.customers
-- ORDER BY cust_id;

--10.For each country, display the first and last credit limit using FIRST_VALUE() and LAST_VALUE().
-- select h.country_name,c.cust_id , c.cust_credit_limit,
-- first_value(c.cust_credit_limit) over (partition by h.country_name order by c.cust_credit_limit) as first_limit,
-- last_value(c.cust_credit_limit) over (partition by h.country_name order by c.cust_credit_limit ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as last_limit
-- from sh.customers c , sh.countries h
-- where c.country_id = h.country_id
-- order by h.country_name , c.cust_credit_limit  

--11.Compute percentage rank (PERCENT_RANK()) of customers based on credit limit.
-- select cust_id, cust_first_name, cust_last_name, cust_credit_limit,
-- round(percent_rank()over (order by cust_credit_limit),3) as rank_percent
-- from sh.customers

----PERCENT_RANK()	((Rank - 1) / (n - 1) )Lowest = 0, Highest = 1
-- --CUME_DIST()	(Number of rows ≤ current / total rows)	Always > 0 and ≤ 1

--12.Show each customer’s position in percentile (CUME_DIST() function).
-- select cust_id, cust_first_name, cust_last_name , cust_credit_limit, 
-- round(cume_dist() over(order by cust_credit_limit), 3) as percentile_position
-- from sh.customers

--13.Display the difference between the maximum and current credit limit for each customer.
-- select cust_id, cust_first_name, cust_last_name , cust_credit_limit, 
-- max(cust_credit_limit) over () - cust_credit_limit as difference_from_max
-- from sh.CUSTOMERS
-- order by difference_from_max

--14.Rank income levels by their average credit limit.
-- select cust_income_level,round(avg(cust_credit_limit), 2) as avg_credit_limit,
-- rank() over (order by avg(cust_credit_limit) desc) as income_rank
-- from sh.customers
-- group by cust_income_level
-- order by income_rank;

--15.Calculate the average credit limit over the last 10 customers (sliding window).
-- select cust_id, cust_first_name,cust_last_name,cust_credit_limit,
-- round(avg(cust_credit_limit) over (order by cust_id rows between 9 preceding and current row ), 2) as avg_last_10
-- from sh.customers

--16.For each state, calculate the cumulative total of credit limits ordered by city.
-- select cust_state_province,cust_city,
-- sum(cust_credit_limit) over (partition by cust_state_province order by cust_city) as cumulative_credit_limit
-- from sh.customers

--17.Find customers whose credit limit equals the median credit limit (use PERCENTILE_CONT(0.5)).
-- select cust_id,cust_first_name,cust_last_name,cust_credit_limit
-- from sh.customers
-- where cust_credit_limit = (
-- select percentile_cont(0.5) within group (order by cust_credit_limit)
-- from sh.customers
-- )

--18.Display the highest 3 credit holders per state using ROW_NUMBER() and PARTITION BY.
-- SELECT  cust_state_province, cust_id, cust_first_name, cust_last_name, cust_credit_limit
-- FROM (
-- SELECT cust_state_province,cust_id, cust_first_name, cust_last_name, cust_credit_limit,
-- ROW_NUMBER()OVER (PARTITION BY cust_state_province ORDER BY cust_credit_limit DESC ) AS rnk
-- FROM sh.customers
-- )
-- WHERE rnk <= 3

--19.Identify customers whose credit limit increased compared to previous row (using LAG).
-- select cust_id, cust_first_name, cust_last_name, cust_credit_limit, prev_credit_limit
-- from (
-- select cust_id, cust_first_name, cust_last_name, cust_credit_limit,
-- lag(cust_credit_limit) over (order by cust_id) as prev_credit_limit
-- from sh.customers
-- )
-- where cust_credit_limit > prev_credit_limit

--20.Calculate moving average of credit limits with a window of 3.
-- select cust_id , cust_first_name, cust_last_name , cust_credit_limit, 
-- round(avg(cust_credit_limit) over (order by cust_id rows between 2 preceding  and current row),2) as moving_avg
-- from sh.customers

--21.Show cumulative percentage of total credit limit per country.
-- select h.country_name ,round( 
-- (sum(c.cust_credit_limit) over (partition by h.country_name order by c.cust_credit_limit) /
--  sum(c.cust_credit_limit) over (partition by h.country_name ) *100),2) as total_credit_percentage
-- from sh.customers c , sh.countries h
-- where c.country_id = h.country_id

--22.Rank customers by age (derived from CUST_YEAR_OF_BIRTH).
-- select cust_id, cust_first_name, cust_last_name, cust_year_of_birth,
-- (2025 - cust_year_of_birth) as age,
-- rank()over (order by (2025 - cust_year_of_birth) desc) as age_rank
-- from sh.customers

--23.Calculate difference in age between current and previous customer in the same state.
-- select cust_state_province, cust_id, cust_first_name, cust_last_name, cust_year_of_birth,
-- (2025 - cust_year_of_birth) as age,
-- lag(2025 - cust_year_of_birth) over(partition by cust_state_province order by cust_id) as age_difference
-- from sh.customers

--24.Use RANK() and DENSE_RANK() to show how ties are treated differently.
-- select 
--     cust_id,
--     cust_first_name,
--     cust_last_name,
--     cust_credit_limit,
--     rank() over (order by cust_credit_limit desc) as rank_no,
--     dense_rank() over (order by cust_credit_limit desc) as dense_rank_no
-- from sh.customers

--25.Compare each state’s average credit limit with country average using window partition.
-- select 
--     h.country_name,
--     c.cust_state_province,
--     round(avg(c.cust_credit_limit) over (partition by c.cust_state_province),2) as state_avg,
--     round(avg(c.cust_credit_limit) over (partition by h.country_name),2) as country_avg,
--     round(avg(c.cust_credit_limit) over (partition by c.cust_state_province) -
--     avg(c.cust_credit_limit) over (partition by h.country_name),2) as diff_from_country
-- from sh.customers c, sh.countries h
-- where c.country_id = h.country_id
-- order by h.country_name, c.cust_state_province

--26.Show total credit per state and also its rank within each country.
-- select 
--     h.country_name,
--     c.cust_state_province,
--     sum(c.cust_credit_limit) as total_credit,
--     rank() over (
--         partition by h.country_name
--         order by sum(c.cust_credit_limit) desc
--     ) as state_rank
-- from sh.customers c, sh.countries h
-- where c.country_id = h.country_id
-- group by h.country_name, c.cust_state_province
-- order by h.country_name, state_rank

--27.Find customers whose credit limit is above the 90th percentile of their income level.
-- select 
--     cust_id,
--     cust_first_name,
--     cust_last_name,
--     cust_income_level,
--     cust_credit_limit
-- from (
--     select 
--         cust_id,
--         cust_first_name,
--         cust_last_name,
--         cust_income_level,
--         cust_credit_limit,
--         percentile_cont(0.9) within group (order by cust_credit_limit)
--             over (partition by cust_income_level) as p90_limit
--     from sh.customers
-- )
-- where cust_credit_limit > p90_limit
-- order by cust_income_level, cust_credit_limit desc;

--28.Display top 3 and bottom 3 customers per country by credit limit.
-- select 
--     country_name,
--     cust_id,
--     cust_first_name,
--     cust_last_name,
--     cust_credit_limit,
--     top_rank,
--     bottom_rank
-- from (
--     select 
--         h.country_name,
--         c.cust_id,
--         c.cust_first_name,
--         c.cust_last_name,
--         c.cust_credit_limit,
--         rank() over (
--             partition by h.country_name 
--             order by c.cust_credit_limit desc
--         ) as top_rank,
--         rank() over (
--             partition by h.country_name 
--             order by c.cust_credit_limit asc
--         ) as bottom_rank
--     from sh.customers c, sh.countries h
--     where c.country_id = h.country_id
-- )
-- where top_rank <= 3 or bottom_rank <= 3
-- order by country_name, cust_credit_limit desc;

--29.Calculate rolling sum of 5 customers’ credit limit within each country.
-- select 
--     h.country_name,
--     c.cust_id,
--     c.cust_first_name,
--     c.cust_last_name,
--     c.cust_credit_limit,
--     sum(c.cust_credit_limit) over (
--         partition by h.country_name
--         order by c.cust_id
--         rows between 4 preceding and current row
--     ) as rolling_sum_5
-- from sh.customers c, sh.countries h
-- where c.country_id = h.country_id

--30.For each marital status, display the most and least wealthy customers using analytical functions.
select 
    cust_marital_status,
    cust_id,
    cust_first_name,
    cust_last_name,
    cust_credit_limit,
    wealth_rank_high,
    wealth_rank_low
from (
    select 
        cust_marital_status,
        cust_id,
        cust_first_name,
        cust_last_name,
        cust_credit_limit,
        rank() over (
            partition by cust_marital_status 
            order by cust_credit_limit desc
        ) as wealth_rank_high,
        rank() over (
            partition by cust_marital_status 
            order by cust_credit_limit asc
        ) as wealth_rank_low
    from sh.customers
)
where wealth_rank_high = 1 or wealth_rank_low = 1
order by cust_marital_status, cust_credit_limit desc;
