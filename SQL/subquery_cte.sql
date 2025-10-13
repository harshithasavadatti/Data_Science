--1)for each city display top 2 customers by credit limit using subquery 
--and CTE in sh.customers


--subquery
-- select * from (
--     select cust_id,cust_first_name, cust_last_name, cust_city,cust_credit_limit,
--     row_number() over(partition by cust_city order by cust_credit_limit desc)
--     as rn from sh.customers
-- )
-- where rn <=2

--CTE
-- with ranked_customers as (
--     select cust_id, cust_first_name,cust_last_name,cust_credit_limit,
--     row_number() over(partition by cust_city order  by cust_credit_limit desc) as rn
--     from sh.customers
-- )
-- select * from ranked_customers
-- where rn <=2


--2)sh.customers, cust_id, cust_credit_limit classify them as premium 
--or standard,  top 5 should be premium and rest should be standard
with ranked_customers as(
    select cust_id, cust_first_name, cust_last_name, cust_credit_limit,
    ROW_NUMBER() over (order by cust_credit_limit desc)as rn
    from sh.customers
)

Select cust_id, cust_first_name, cust_last_name, cust_credit_limit,
    case 
        when rn <= 5 then 'Premium Tier'
        else 'Standard Tier'
    end as Tier
from ranked_customers
order by cust_credit_limit desc