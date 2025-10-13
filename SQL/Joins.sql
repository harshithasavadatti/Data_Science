--left,right,leftouter,rightout, inner, full outer, symmetrics difference for these two tables

--Customer Table
CREATE TABLE Customers (
    CustomerID NUMBER PRIMARY KEY,
    CustomerName VARCHAR2(100) NOT NULL,
    Email VARCHAR2(100),
    City VARCHAR2(50),
    Country VARCHAR2(50)
);

INSERT INTO Customers (CustomerID, CustomerName, Email, City, Country) VALUES
(1, 'John Smith', 'john.smith@gmail.com', 'New York', 'USA');

INSERT INTO Customers (CustomerID, CustomerName, Email, City, Country) VALUES
(2, 'Priya Sharma', 'priya.sharma@gmail.com', 'Delhi', 'India');

INSERT INTO Customers (CustomerID, CustomerName, Email, City, Country) VALUES
(3, 'Carlos Mendez', NULL, 'Madrid', 'Spain');

INSERT INTO Customers (CustomerID, CustomerName, Email, City, Country) VALUES
(4, 'Aisha Khan', 'aisha.khan@gmail.com', NULL, 'UAE');

INSERT INTO Customers (CustomerID, CustomerName, Email, City, Country) VALUES
(5, 'Liam Brown', 'liam.brown@gmail.com', 'London', NULL);


-- Product Table
CREATE TABLE Products (
    ProductID NUMBER PRIMARY KEY,
    ProductName VARCHAR2(100) NOT NULL,
    Category VARCHAR2(50),
    Price NUMBER,
    CustomerID NUMBER,
    CONSTRAINT fk_customers
        FOREIGN KEY (CustomerID)
        REFERENCES Customers(CustomerID)
);

INSERT INTO Products (ProductID, ProductName, Category, Price, CustomerID) VALUES
(101, 'Laptop', 'Electronics', 850, 1);

INSERT INTO Products (ProductID, ProductName, Category, Price, CustomerID) VALUES
(102, 'Smartphone', 'Electronics', 500, 1);

INSERT INTO Products (ProductID, ProductName, Category, Price, CustomerID) VALUES
(103, 'Tablet', 'Electronics', 300, 2);

INSERT INTO Products (ProductID, ProductName, Category, Price, CustomerID) VALUES
(104, 'Headphones', 'Accessories', 100, NULL);

INSERT INTO Products (ProductID, ProductName, Category, Price, CustomerID) VALUES
(105, 'Watch', 'Accessories', 150, 3);

INSERT INTO Products (ProductID, ProductName, Category, Price, CustomerID) VALUES
(106, 'Camera', 'Electronics', 700, 2);

INSERT INTO Products (ProductID, ProductName, Category, Price, CustomerID) VALUES
(107, 'Shoes', 'Fashion', 80, 4);

INSERT INTO Products (ProductID, ProductName, Category, Price, CustomerID) VALUES
(108, 'Backpack', 'Fashion', NULL, 4);

select * from Customers

select * from Products


--1. left join
select c.CustomerID, c.CustomerName, c.Email, c.City, c.Country 
from Customers c
left join Products p
on c.CustomerID = p.CustomerID
order by c.CustomerID;

--2. right join
select p.CustomerID, p.ProductID, p.ProductName, p.Category, p.Price
from Products p
right join Customers c
on p.CustomerID = c.CustomerID
order by p.CustomerID;

--3.leftouter join
select c.CustomerID, c.CustomerName, c.Email, c.City, c.Country 
from Customers c
left outer join Products p
on c.CustomerID = p.CustomerID
order by c.CustomerID;

--4.Right outer join
select p.CustomerID, p.ProductID, p.ProductName, p.Category, p.Price
from Products p
right outer join Customers c
on p.CustomerID = c.CustomerID
order by p.CustomerID;

--5. inner join
select c.CustomerID, c.CustomerName, p.ProductID, p.ProductName
from Customers c
inner join Products p on c.CustomerID = p.CustomerID
order by c.CustomerID;


--6. full outer join
select c.CustomerID, c.CustomerName, p.ProductID, p.ProductName
from Customers c
full outer join Products p on c.CustomerID = p.CustomerID
order by c.CustomerID;


--7. Symmetric Difference
SELECT 
    c.CustomerID AS Customer_ID,
    c.CustomerName,
    c.Email,
    c.City,
    c.Country,
    p.ProductID,
    p.ProductName,
    p.Category,
    p.Price
FROM Customers c
FULL OUTER JOIN Products p
ON c.CustomerID = p.CustomerID
WHERE c.CustomerID IS NULL OR p.CustomerID IS NULL
ORDER BY c.CustomerID;
