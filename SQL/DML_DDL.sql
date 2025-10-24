-- ======================================================
-- Drop tables if they already exist (for re-run)
-- ======================================================
DROP TABLE IF EXISTS BookingDetails;
DROP TABLE IF EXISTS Bookings;
DROP TABLE IF EXISTS Flights;
DROP TABLE IF EXISTS Passengers;
DROP TABLE IF EXISTS Airports;

-- ======================================================
-- Airports Table
-- ======================================================
CREATE TABLE Airports (
    AirportID INT IDENTITY(1,1) PRIMARY KEY,
    AirportName VARCHAR(100),
    City VARCHAR(50),
    Country VARCHAR(50)
);

-- ======================================================
-- Flights Table
-- ======================================================
CREATE TABLE Flights (
    FlightID INT IDENTITY(1001,1) PRIMARY KEY,
    FlightNumber VARCHAR(10),
    AirlineName VARCHAR(100),
    OriginAirportID INT,
    DestinationAirportID INT,
    DepartureTime DATETIME,
    ArrivalTime DATETIME,
    BaseFare DECIMAL(10,2),
    FOREIGN KEY (OriginAirportID) REFERENCES Airports(AirportID),
    FOREIGN KEY (DestinationAirportID) REFERENCES Airports(AirportID)
);

-- ======================================================
-- Passengers Table
-- ======================================================
CREATE TABLE Passengers (
    PassengerID INT IDENTITY(501,1) PRIMARY KEY,
    FullName VARCHAR(100),
    Gender CHAR(1),
    Age INT,
    Email VARCHAR(100)
);

-- ======================================================
-- Bookings Table
-- ======================================================
CREATE TABLE Bookings (
    BookingID INT IDENTITY(2001,1) PRIMARY KEY,
    PassengerID INT,
    BookingDate DATETIME DEFAULT GETDATE(),
    TotalAmount DECIMAL(10,2),
    PaymentStatus VARCHAR(20),
    FOREIGN KEY (PassengerID) REFERENCES Passengers(PassengerID)
);

-- ======================================================
-- BookingDetails Table
-- ======================================================
CREATE TABLE BookingDetails (
    BookingDetailID INT IDENTITY(3001,1) PRIMARY KEY,
    BookingID INT,
    FlightID INT,
    SeatNumber VARCHAR(10),
    Class VARCHAR(20),
    Fare DECIMAL(10,2),
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID),
    FOREIGN KEY (FlightID) REFERENCES Flights(FlightID)
);




-- Airports
INSERT INTO Airports (AirportName, City, Country) VALUES
('Kempegowda International Airport', 'Bangalore', 'India'),
('Chhatrapati Shivaji Airport', 'Mumbai', 'India'),
('Indira Gandhi International Airport', 'Delhi', 'India'),
('Heathrow Airport', 'London', 'UK'),
('John F. Kennedy Airport', 'New York', 'USA');

-- Flights
INSERT INTO Flights (FlightNumber, AirlineName, OriginAirportID, DestinationAirportID, DepartureTime, ArrivalTime, BaseFare)
VALUES
('AI101', 'Air India', 1, 3, '2023-10-15 08:00', '2023-10-15 10:30', 7500),
('6E220', 'IndiGo', 2, 1, '2023-10-16 09:30', '2023-10-16 11:00', 5500),
('BA150', 'British Airways', 3, 4, '2023-10-17 22:00', '2023-10-18 05:00', 45000),
('AI222', 'Air India', 4, 5, '2023-10-18 10:00', '2023-10-18 18:30', 52000),
('DL560', 'Delta Airlines', 5, 3, '2023-10-19 14:00', '2023-10-20 02:00', 48000);

-- Passengers
INSERT INTO Passengers (FullName, Gender, Age, Email)
VALUES
('Ravi Kumar', 'M', 34, 'ravi.kumar@gmail.com'),
('Sneha Patel', 'F', 28, 'sneha.patel@yahoo.com'),
('John Smith', 'M', 45, 'john.smith@gmail.com'),
('Priya Sharma', 'F', 31, 'priya.sharma@outlook.com'),
('David Johnson', 'M', 50, 'david.johnson@gmail.com');

-- Bookings
INSERT INTO Bookings (PassengerID, BookingDate, TotalAmount, PaymentStatus)
VALUES
(501, '2023-10-10', 8000, 'Paid'),
(502, '2023-10-12', 5500, 'Paid'),
(503, '2023-10-13', 46000, 'Paid'),
(504, '2023-10-14', 52000, 'Pending'),
(505, '2023-10-15', 48000, 'Paid');

-- Booking Details
INSERT INTO BookingDetails (BookingID, FlightID, SeatNumber, Class, Fare)
VALUES
(2001, 1001, '12A', 'Economy', 8000),
(2002, 1002, '14B', 'Economy', 5500),
(2003, 1003, '2C', 'Business', 46000),
(2004, 1004, '3D', 'Business', 52000),
(2005, 1005, '5A', 'Premium', 48000);

1)flights from Air India
select * from Flights where Flightname = 'Air India'

2)add new column to flights table called duration number
ALTER TABLE Flights
ADD duration NUMBER;

3)Modify the data type of base fare column in flights name to decimal (12,2)
ALTER TABLE Flights
AlTER COLUMN BaseFare DECIMAL(12,2);

4)update the fare of all flights where class equal to economy by 50% increase (100% + 50% = 150% = *1.5)
UPDATE BookingDetails
SET Fare = Fare * 1.5
WHERE Class = 'Economy';

5)Change ravi's email id to ravi.kumar@yahoo.com in passenger's table
Update Passengers
set email = 'ravi.kumar@yahoo.com'
where fullname = 'Ravi Kumar'

6)Delete all passengers whose age is greater than 50
delete from  passengers  
where age > 50