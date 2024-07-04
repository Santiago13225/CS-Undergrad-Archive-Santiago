create table SUPPLIERS(
SupplierID			INT			NOT NULL,
CompanyName		VARCHAR(32),
ContactLastName		VARCHAR(15),
ContactFirstName		VARCHAR(15),
Phone				VARCHAR(13),
PRIMARY KEY (SupplierID));
#UNIQUE(CompanyName));

create table BOOKS(
BookID			INT			NOT NULL,
Title				VARCHAR(32),
Unit_Price			DECIMAL(10,2),
Author				VARCHAR(15),
Unit_in_Stock			INT,
SupplierID			INT,
SubjectID			INT,
PRIMARY KEY (BookID));

create table SUBJECTS(
SubjectID			INT			NOT NULL,
CategoryName		VARCHAR(15),
PRIMARY KEY (SubjectID));
#UNIQUE(CategoryName));

create table ORDERDETAILS(
BookID			INT			NOT NULL,
OrderID			INT			NOT NULL,
Quantity			INT,
PRIMARY KEY (BookID,OrderID));
#FOREIGN KEY(BookID) REFERENCES BOOKS(BookID));

create table CUSTOMERS(
CustomerID			INT			NOT NULL,
LastName			VARCHAR(15),
FirstName			VARCHAR(15),
Phone				VARCHAR(13),
PRIMARY KEY (CustomerID));

create table ORDERS(
OrderID			INT			NOT NULL,
CustomerID			INT			NOT NULL,
EmployeeID			INT			NOT NULL,
OrderDate			DATE,
ShippedDate			DATE,
ShipperID			INT,
PRIMARY KEY (OrderID));
#FOREIGN KEY(CustomerID) REFERENCES CUSTOMERS(CustomerID));

create table EMPLOYEES(
EmployeeID			INT			NOT NULL,
LastName			VARCHAR(15),
FirstName			VARCHAR(15),
PRIMARY KEY (EmployeeID));

create table SHIPPERS(
ShipperID			INT,
ShipperName			VARCHAR(15),
PRIMARY KEY (ShipperID));
#UNIQUE(ShipperName));


#ALTER TABLE ORDERDETAILS
#ADD CONSTRAINT fk_OrderID
#FOREIGN KEY(OrderID) REFERENCES ORDERS(OrderID));

#ALTER TABLE ORDERS
#ADD CONSTRAINT fk_EmployeeID
#FOREIGN KEY(EmployeeID) REFERENCES EMPLOYEES(EmployeeID));

#ALTER TABLE ORDERS
#ADD CONSTRAINT fk_ShipperID
#FOREIGN KEY(ShipperID) REFERENCES SHIPPERS(ShipperID));


INSERT INTO SUPPLIERS
VALUES (1, 'Amazon', 'Hamilton', 'Laurell', '605-145-1875');
INSERT INTO SUPPLIERS
VALUES (2, 'Ebay', 'Koontz', 'Dean', '605-244-1104');
INSERT INTO SUPPLIERS
VALUES (3, 'Booksamillion', 'Roberts', 'Nora', '916-787-3320');
INSERT INTO SUPPLIERS
VALUES (4, 'University', 'Carter', 'Stephen', '916-412-2004');

INSERT INTO BOOKS
VALUES (1, 'The Quickie', 15.94, 'James', 5, 3, 1);
INSERT INTO BOOKS
VALUES (2, 'Blaze', 13.24, 'Richard', 2, 3, 1);
INSERT INTO BOOKS
VALUES (3, 'The Navigator', 14.01, 'Clive', 10, 2, 1);
INSERT INTO BOOKS
VALUES (4, 'Birmingham', 19.99, 'Tim', 12, 3, 2);
INSERT INTO BOOKS
VALUES (5, 'North Carolina Ghosts', 7.95, 'Lynne', 5, 2, 2);
INSERT INTO BOOKS
VALUES (6, 'Why I still live in Louisiana', 5.95, 'Ellen', 30, 1, 3);
INSERT INTO BOOKS
VALUES (7, 'The World Is Flat', 30, 'Thomas', 17, 3, 4);

INSERT INTO SUBJECTS
VALUES (1, 'Fiction');
INSERT INTO SUBJECTS
VALUES (2, 'History');
INSERT INTO SUBJECTS
VALUES (3, 'Travel');
INSERT INTO SUBJECTS
VALUES (4, 'Technology');

INSERT INTO EMPLOYEES
VALUES (1, 'Larson', 'Erik');
INSERT INTO EMPLOYEES
VALUES (2, 'Steely', 'John');

INSERT INTO SHIPPERS
VALUES (1, 'UPS');
INSERT INTO SHIPPERS
VALUES (2, 'USPS');
INSERT INTO SHIPPERS
VALUES (3, 'FedEx');

INSERT INTO CUSTOMERS
VALUES (1, 'Lee', 'James', '916-541-4568');
INSERT INTO CUSTOMERS
VALUES (2, 'Smith', 'John', '916-057-0087');
INSERT INTO CUSTOMERS
VALUES (3, 'See', 'Lisa', '605-045-0010');
INSERT INTO CUSTOMERS
VALUES (4, 'Collins', 'Jackie', '605-044-6582');

INSERT INTO ORDERS
VALUES (1, 1, 1, '2021-08-01', '2021-08-03', 1);
INSERT INTO ORDERS
VALUES (2, 1, 2, '2021-08-04', NULL, NULL);
INSERT INTO ORDERS
VALUES (3, 2, 1, '2021-08-01', '2021-08-03', 2);
INSERT INTO ORDERS
VALUES (4, 4, 2, '2021-08-04', '2021-08-05', 1);

INSERT INTO ORDERDETAILS
VALUES (1, 1, 2);
INSERT INTO ORDERDETAILS
VALUES (4, 1, 1);
INSERT INTO ORDERDETAILS
VALUES (6, 2, 2);
INSERT INTO ORDERDETAILS
VALUES (7, 2, 3);
INSERT INTO ORDERDETAILS
VALUES (5, 3, 1);
INSERT INTO ORDERDETAILS
VALUES (3, 4, 1);
INSERT INTO ORDERDETAILS
VALUES (4, 4, 1);
INSERT INTO ORDERDETAILS
VALUES (7, 4, 1);