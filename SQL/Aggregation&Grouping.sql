----🧮 SQL Scenario-Based Questions on SH.CUSTOMERS
----🧱 A. Aggregation & Grouping (20 Questions)

--1.Find the total, average, minimum, and maximum credit limit of all customers.
-- select 
--     sum(cust_credit_limit) as Total_Credit_Limit,
--     avg(cust_credit_limit) as Average_Credit_Limit,
--     min(cust_credit_limit) as Minimum_Credit_Limit,
--     max(cust_credit_limit) as Maximum_Credit_Limit
-- from sh.customers

--2.Count the number of customers in each income level.
-- select cust_income_level,count(*) as customer_count
-- from sh.customers 
-- group by cust_income_level
-- order by customer_count desc

--3.Show total credit limit by state and country.
-- select h.country_name , c.cust_state_province, sum(cust_credit_limit) as Total_Credit_Limit
-- from  sh.COUNTRIES h, sh.customers c
-- where h.country_id = c.country_id
-- group by c.cust_state_province, h.country_name
-- order by h.country_name, Total_Credit_Limit desc

--4.Display average credit limit for each marital status and gender combination.
-- select avg(cust_credit_limit) as Average_Credit_Limit, cust_marital_status, cust_gender
-- from sh.customers
-- group by  cust_marital_status, cust_gender

--5.Find the top 3 states with the highest average credit limit.
-- select avg(cust_credit_limit) as Average_Credit_Limit, cust_state_province
-- from sh.customers 
-- GROUP BY cust_state_province
-- ORDER BY Average_Credit_Limit DESC
-- FETCH FIRST 3 ROWS ONLY;

--using dense_rank
-- select *
-- from (
--     select cust_state_province,
--     avg(cust_credit_limit) as Average_Credit_Limit,
--     dense_rank() over (order by avg(cust_credit_limit) desc) as rank
--   from sh.customers
--   group by cust_state_province
-- )
-- where rank <=3

--6.Find the country with the maximum total customer credit limit
-- select h.country_name, sum(cust_credit_limit) as Total_Credit_Limit
-- from sh.countries h, sh.customers c
-- where h.country_id = c.country_id 
-- group by h.country_name 
-- order by Total_Credit_Limit desc
-- fetch first 1 row only

--using dense rank
-- select *
-- from (
--     select 
--         h.country_name,
--         sum(c.cust_credit_limit) as total_credit_limit,
--         dense_rank() over (order by sum(c.cust_credit_limit) desc) as rank
--     from sh.countries h , sh.customers c
--     where h.country_id = c.country_id
--     group by h.country_name
-- )
-- where rank = 1;

--7.Show the number of customers whose credit limit exceeds their state average.
-- SELECT 
--     COUNT(*) AS customers_above_state_avg
-- FROM sh.customers c
-- WHERE c.cust_credit_limit > (
--     SELECT AVG(c2.cust_credit_limit)
--     FROM sh.customers c2
--     WHERE c2.cust_state_province = c.cust_state_province
-- );

--8.Calculate total and average credit limit for customers born after 1980.
-- select sum(cust_credit_limit) as total_credit_limit, avg(cust_credit_limit)as average_credit_limit
-- from sh.customers 
-- where cust_year_of_birth > 1980

--9.Find states having more than 50 customers.
-- SELECT 
--     cust_state_province,
--     COUNT(*) AS customer_count
-- FROM sh.customers
-- GROUP BY cust_state_province
-- HAVING COUNT(*) > 50
-- ORDER BY customer_count DESC;

-- 10. List countries where the average credit limit is higher than the global average
-- SELECT 
--     h.country_name,
--     AVG(c.cust_credit_limit) AS avg_credit_limit
-- FROM sh.countries h, sh.customers c 
-- where h.country_id = c.country_id
-- GROUP BY h.country_name
-- HAVING AVG(c.cust_credit_limit) > (
--     SELECT AVG(cust_credit_limit)
--     FROM sh.customers
-- )

-- 11. Calculate the variance and standard deviation of customer credit limits by country
-- SELECT 
--     h.country_name,
--     VARIANCE(c.cust_credit_limit) AS variance_credit,
--     STDDEV(c.cust_credit_limit) AS standard_deviation
-- FROM sh.customers c
-- JOIN sh.countries h 
--     ON h.country_id = c.country_id
-- GROUP BY h.country_name
-- ORDER BY h.country_name

--12.Find the state with the smallest range (max–min) in credit limits.
-- SELECT *
-- FROM (
--     SELECT 
--         cust_state_province,
--         MIN(cust_credit_limit) AS minimum_credit_limit,
--         MAX(cust_credit_limit) AS maximum_credit_limit,
--         (MAX(cust_credit_limit) - MIN(cust_credit_limit)) AS credit_limit_range,
--         DENSE_RANK() OVER (ORDER BY (MAX(cust_credit_limit) - MIN(cust_credit_limit)) ASC) AS rank
--     FROM sh.customers
--     GROUP BY cust_state_province
-- )
-- WHERE rank = 1;

--13.Show the total number of customers per income level and the percentage contribution of each.
-- SELECT 
--     cust_income_level,
--     COUNT(*) AS total_customers,
--     ROUND(
--         (COUNT(*) * 100) / (SELECT COUNT(*) FROM sh.customers),
--         2
--     ) AS percentage_contribution
-- FROM sh.customers
-- GROUP BY cust_income_level
-- ORDER BY total_customers DESC

--14.For each income level, find how many customers have NULL credit limits.
-- SELECT 
--     cust_income_level,
--     COUNT(*) AS null_credit_customers
-- FROM sh.customers
-- WHERE cust_credit_limit IS NULL
-- GROUP BY cust_income_level
-- ORDER BY null_credit_customers DESC


-- 15.Display countries where the sum of credit limits exceeds 10 million.
-- select COUNTRY_ID,
-- sum(cust_credit_limit)as total_credit_limit
-- from sh.CUSTOMERS
-- group by COUNTRY_ID
-- having sum(cust_credit_limit) >1000000

-- 16.Find the state that contributes the highest total credit limit to its country.
-- SELECT country_id, cust_state_province, total_credit
-- FROM (
--     SELECT 
--         country_id,
--         cust_state_province,
--         SUM(cust_credit_limit) AS total_credit,
--         ROW_NUMBER() OVER (
--             PARTITION BY country_id 
--             ORDER BY SUM(cust_credit_limit) DESC
--         ) AS rn
--     FROM sh.customers
--     GROUP BY country_id, cust_state_province
-- )
-- WHERE rn = 1
-- ORDER BY country_id;

-- 17.Show total credit limit per year of birth, sorted by total descending.
-- select cust_year_of_birth,
-- sum(cust_credit_limit)as total_credit_limit 
-- from sh.CUSTOMERS
-- group by CUST_YEAR_OF_BIRTH
-- order by total_credit_limit desc

-- 18.Identify customers who hold the maximum credit limit in their respective country.
-- SELECT 
--     country_id,
--     cust_id,
--     cust_first_name,
--     cust_last_name,
--     cust_credit_limit
-- FROM (
--     SELECT 
--         country_id,
--         cust_id,
--         cust_first_name,
--         cust_last_name,
--         cust_credit_limit,
--         MAX(cust_credit_limit) OVER (PARTITION BY country_id) AS max_credit_in_country
--     FROM sh.customers
-- )
-- WHERE cust_credit_limit = max_credit_in_country
-- ORDER BY country_id, cust_id;


-- 19.Show the difference between maximum and average credit limit per country.
-- SELECT COUNTRY_ID,
--        MAX(CUST_CREDIT_LIMIT) AS max_credit_limit,
--        AVG(CUST_CREDIT_LIMIT) AS avg_credit_limit,
--        (MAX(CUST_CREDIT_LIMIT) - AVG(CUST_CREDIT_LIMIT)) AS diff_credit_limit
-- FROM sh.CUSTOMERS
-- GROUP BY COUNTRY_ID;

-- 20.Display the overall rank of each state based on its total credit limit (using GROUP BY + analytic rank).
-- SELECT CUST_STATE_PROVINCE,
--        SUM(CUST_CREDIT_LIMIT) AS total_credit_limit,
--        RANK() OVER (ORDER BY SUM(CUST_CREDIT_LIMIT) DESC) AS overall_rank
-- FROM sh.CUSTOMERS
-- GROUP BY CUST_STATE_PROVINCE;




