-- SQL Questions on WHERE

--1. Find customers born after the year 1990.
-- select * from sh.customers 
-- where cust_year_of_birth >1990

--2. List all male customers (`CUST_GENDER = 'M'`).
-- select * from sh.customers
-- where cust_gender = 'M'

--3. Retrieve all female customers (`CUST_GENDER = 'F'`) living in Sydney.
-- select * from sh.customers
-- where cust_gender ='F' and cust_city = 'Sydney'

--4. Find customers with income level `"G: 130,000 - 149,999"`.
-- select * from sh.customers 
-- where cust_income_level = 'G: 130,000 - 149,999'

--5. Get all customers with a credit limit above 10,000.
-- select * from sh.customers 
-- where cust_credit_limit > 10000

--6. Retrieve customers from the state "California".
-- select * from sh.customers 
-- where cust_state_province = 'California'

-- 7. Find customers who have provided an email address.
-- select * from sh.customers 
-- where cust_email is not null 

--8. List customers with missing marital status.
-- select * from sh.customers 
-- where CUST_MARITAL_STATUS is null 

--9. Find customers whose postal code starts with "53".
-- select * from sh.customers 
-- where cust_postal_code like '53%'

--10. Get customers born before 1980 with a credit limit above 5,000.
-- select * from sh.customers 
-- where cust_year_of_birth < 1980 and cust_credit_limit > 5000

--11. Retrieve customers from Almere or Amersfoort.
-- select * from sh.customers 
-- where cust_city = 'Almere' or cust_city = 'Amersfoort'

--12. Find customers who do not have a credit limit.
-- select * from sh.customers 
-- where CUST_CREDIT_LIMIT is null 

--13. List customers whose phone number starts with "487".
-- select * from sh.customers 
-- where CUST_MAIN_PHONE_NUMBER like '487%'

--14. Find married customers with income level `"Medium"`.
-- select * from sh.customers 
-- where CUST_MARITAL_STATUS = 'married' and 
-- (CUST_INCOME_LEVEL like 'G%' or CUST_INCOME_LEVEL like 'H%' or CUST_INCOME_LEVEL like  'I%' )

--15. Get customers whose last name starts with "G".
-- select * from sh.customers 
-- where CUST_LAST_NAME like 'G%'

--16. Find customers with city_id = 51057.
-- select * from sh.customers 
-- where CUST_CITY_ID = '51057'

--17. Retrieve all customers who are valid (`CUST_VALID = 'A'`).
-- select * from sh.customers 
-- where CUST_VALID = 'A'

--18. Find customers whose effective start date (`CUST_EFF_FROM`) is after 2020.
-- select * from sh.customers 
-- where CUST_EFF_FROM > DATE '2020-12-31'

--19. Retrieve customers whose effective end date (`CUST_EFF_TO`) is before 2021.
-- select * from sh.customers 
-- where CUST_EFF_TO < '2021-12-31'

--20. Find customers with credit limit between 5,000 and 9,000.
-- select * from sh.customers 
-- where CUST_CREDIT_LIMIT between 5000 and 9000

--21. Get all customers from country_id = 101.
-- select * from sh.customers 
-- where COUNTRY_ID = 101

--22. Find customers whose email ends with `"@company.example.com"`.
-- select * from sh.customers 
-- where CUST_EMAIL like '%@company.example.com'

--23. List customers with `CUST_TOTAL_ID = 52772`.
-- select * from sh.customers 
-- where CUST_TOTAL_ID = 52772

--24. Find customers with `CUST_SRC_ID` in (10, 20, 30).
-- select * from sh.customers 
-- where CUST_SRC_ID in (10, 20, 30)

--25. Retrieve customers who either do not have email or do not have a credit limit.
-- select * from sh.customers 
-- where CUST_EMAIL is null or CUST_CREDIT_LIMIT is null 
