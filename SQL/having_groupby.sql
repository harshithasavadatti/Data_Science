-- Questions on GROUP BY and HAVING --

--26. Count the number of customers in each city.
-- select cust_city, count(*) as customer_count
-- from sh.customers 
-- group by cust_city

-- 27. Find cities with more than 100 customers.
-- select cust_city, count(*) as customer_count
-- from sh.customers 
-- group by cust_city 
-- having customer_count > 100

--28. Count the number of customers in each state.
-- select cust_state_province, count(*) as customer_count
-- from sh.customers 
-- group by cust_state_province

--29. Find states with fewer than 50 customers.
-- select cust_state_province, count(*) as customer_count
-- from sh.customers 
-- group by cust_state_province 
-- having customer_count < 50

--30. Calculate the average credit limit of customers in each city.
-- select cust_city, avg(cust_credit_limit) as average_credit_limit
-- from sh.customers 
-- group by cust_city

--31. Find cities with average credit limit greater than 8,000.
-- select cust_city, avg(cust_credit_limit) as average_credit_limit
-- from sh.customers 
-- group by cust_city
-- having average_credit_limit > 8000

--32. Count customers by marital status.
-- select cust_marital_status, count(*) as customer_count
-- from sh.customers 
-- group by cust_marital_status

--33. Find marital statuses with more than 200 customers.
-- select cust_marital_status, count(*) as customer_count
-- from sh.customers 
-- group by cust_marital_status
-- having customer_count > 200

--34. Calculate the average year of birth grouped by gender.
-- select cust_gender, avg(cust_year_of_birth) as average_YOB
-- from sh.customers
-- group by cust_gender

--35. Find genders with average year of birth after 1990.
-- select cust_gender, avg(cust_year_of_birth) as average_YOB
-- from sh.customers
-- group by cust_gender
-- having average_YOB > 1990

--36. Count the number of customers in each country.
-- select c.country_name , count(*) as customer_count
-- from sh.customers cu
-- join sh.countries c
--   on cu.country_id = c.country_id 
-- group by c.country_name 

--37. Find countries with more than 1,000 customers.
-- select c.country_name , count(*) as customer_count
-- from sh.customers cu
-- join sh.countries c
--   on cu.country_id = c.country_id 
-- group by c.country_name 
-- having customer_count > 1000
 
--38. Calculate the total credit limit per state.
-- select cust_state_province,sum(cust_credit_limit) as total_credit_limit
-- from sh.customers 
-- group by cust_state_province 

--39. Find states where the total credit limit exceeds 100,000.
-- select cust_state_province,sum(cust_credit_limit) as total_credit_limit
-- from sh.customers 
-- group by cust_state_province
-- having total_credit_limit > 100000

--40. Find the maximum credit limit for each income level.
-- select cust_income_level , max(cust_credit_limit) as max_credit_limit
-- from sh.customers 
-- group by cust_income_level
-- order by max_credit_limit desc

--41. Find income levels where the maximum credit limit is greater than 15,000.
-- select cust_income_level , max(cust_credit_limit) as max_credit_limit
-- from sh.customers 
-- group by cust_income_level
-- having max_credit_limit > 15000

--42. Count customers by year of birth.
-- select cust_year_of_birth, count(*) as customer_count
-- from sh.customers 
-- group by cust_year_of_birth

--43. Find years of birth with more than 50 customers.
-- select cust_year_of_birth, count(*) as customer_count
-- from sh.customers 
-- group by cust_year_of_birth
-- having customer_count > 50

--44. Calculate the average credit limit per marital status.
-- select cust_marital_status, avg(cust_credit_limit) as average_credit_limit
-- from sh.customers 
-- group by cust_marital_status

--45. Find marital statuses with average credit limit less than 5,000.
-- select cust_marital_status, avg(cust_credit_limit) as average_credit_limit
-- from sh.customers 
-- group by cust_marital_status
-- having average_credit_limit < 5000

--46. Count the number of customers by email domain (e.g., `company.example.com`).
-- SELECT SUBSTR(cust_email, INSTR(cust_email, '@') + 1) AS domain,
--        COUNT(*) AS customer_count
-- FROM sh.customers
-- GROUP BY domain

--47. Find email domains with more than 300 customers.
-- select substr(cust_email,instr(cust_email,'@')+1) as domain,
--    count(*) as customer_count
-- from sh.customers 
-- group by domain
-- having customer_count > 300

--48. Calculate the average credit limit by validity (`CUST_VALID`).
-- select cust_valid, avg(cust_credit_limit) as average_credit_limit
-- from sh.customers 
-- group by cust_valid

--49. Find validity groups where the average credit limit is greater than 7,000.
-- select cust_valid, avg(cust_credit_limit) as average_credit_limit
-- from sh.customers 
-- group by cust_valid
-- having average_credit_limit > 7000

--50. Count the number of customers per state and city combination where there are more than 50 customers.
-- select cust_state_province, cust_city, count(*) as customer_count
-- from sh.customers 
-- group by cust_state_province, cust_city 
-- having customer_count > 50