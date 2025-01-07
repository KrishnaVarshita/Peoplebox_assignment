create database assignment3;
use assignment3;

-- 1. Createing tables
create table categories(
	categoryid int primary key auto_increment,
    namee varchar(100) not null
);

create table customers(
	Customerid int primary key auto_increment,
    fullname varchar(20) not null,
    email varchar(50) not null unique,
    contact varchar(15) not null,
    address TEXT
    );

create table Products(
	productid int primary key auto_increment,
    productdescription text,
    productname varchar(50) not null,
    categoryid int not null,
    price decimal(10,2),
    stock int not null,
	foreign key (categoryid) references categories(categoryid)
);

create table Orders(
	Orderid int primary key auto_increment,
    Customerid int not null,
    orderdate DATETIME default current_timestamp,
    foreign key (Customerid) references customers(Customerid)
    );

create table Order_items(
	orderItemID int primary key auto_increment,
    productid int not null,
    Orderid int not null,
    quantity int not null,
    foreign key (productid) references Products(productid),
    foreign key (Orderid) references Orders(Orderid)
    );
   
-- Insert Data 
INSERT INTO categories (namee)
VALUES ('mobile phones'), ('Tablet'), ('laptop'), ('headphones'), ('tv');

INSERT INTO customers(fullname, email, contact, address)
VALUES 
('JohnDoe', 'john.doe@example.com', '1234567890', '123 Elm Street'),
('JaneSmith', 'jane.smith@example.com', '0987654321', '456 Oak Avenue'),
('AliceBrown', 'alice.brown@example.com', '1122334455', '789 Pine Road'),
('BobDavis', 'bob.davis@example.com', '5566778899', '101 Maple Lane'),
('CharlieMiller', 'charlie.miller@example.com', '6677889900', '102 Willow Way'),
('EmmaWilson', 'emma.wilson@example.com', '7788990011', '103 Birch Blvd'),
('OliverTaylor', 'oliver.taylor@example.com', '8899001122', '104 Cedar Drive'),
('SophiaAnderson', 'sophia.anderson@example.com', '9900112233', '105 Walnut Street');

INSERT INTO Products(productname, productdescription, price, stock, categoryid)
VALUES 
('Samsung S22+', 'Samsung best, Latest model smartphone', 69999.99, 10, 1),
('Iphone 16 pro max', 'just another iphone', 129999.99, 15, 1),
('HP pavilion', '13th Generation Intel® Core™ i5 processor; Windows 11', 98999.99, 6, 3),
('Samsung tv s9', 'Cheap and best', 34999.99, 25, 5),
('airdopes 141', 'affordable, good quality earbuds', 1000.00, 50, 4),
('Dell', 'High-performance laptop with 12th Gen Intel Core i7', 149999.99, 5, 3),
('OnePlus 11R', 'Flagship killer smartphone with Snapdragon 8+ Gen 1', 44999.99, 20, 1),
('iPad Air', 'Powerful tablet with M1 chip', 59999.99, 12, 2),
('Sony WH-1000XM5', 'Premium noise-canceling headphones', 29999.99, 8, 5),
('Logitech MX Master 3S', 'Advanced wireless mouse with ergonomic design', 7499.99, 30, 4);

INSERT INTO Orders(Customerid)
VALUES 
(1), (1), (2), (3), (3), (4), (5), (6), (7), (8), (1), (2);

INSERT INTO Order_Items(Orderid, productid, quantity)
VALUES 
(1, 1, 2), (1, 3, 1), 
(2, 2, 1), 
(3, 1, 3), 
(4, 4, 2), (4, 1, 5),
(5, 5, 1), (5, 5, 2),
(6, 1, 1), (7, 1, 2),
(8, 4, 1), (9, 5, 1), (10, 3, 4),
(11, 1, 5), (12, 3, 1);



-- 4. Find top 3 customers by order value
SELECT c.fullname, SUM(oi.quantity * p.price) AS total_value FROM customers c
JOIN Orders o ON c.Customerid = o.Customerid
JOIN Order_Items oi ON o.Orderid = oi.Orderid
JOIN Products p ON oi.productid = p.productid
GROUP BY c.Customerid
ORDER BY total_value DESC
LIMIT 3;

-- 4b List products with low stock (below 10)
select productname, stock from Products
where stock <10;

-- 4c Calculate revenue by category
SELECT cat.namee AS category_name, SUM(oi.quantity * p.price) AS revenue
FROM categories cat
JOIN products p ON cat.categoryid = p.categoryid
JOIN Order_items oi ON p.productid = oi.productid
GROUP BY cat.categoryid;

-- 4d Show orders with their items and total amount
SELECT o.Orderid, c.fullname AS customer_name, SUM(oi.quantity * p.price) AS total_amount
FROM Orders o
JOIN Customers c ON o.Customerid = c.Customerid
JOIN Order_Items oi ON o.Orderid = oi.Orderid
JOIN Products p ON oi.productid = p.productid
GROUP BY o.Orderid, customer_name;


-- view
CREATE VIEW order_summary AS
SELECT 
    o.Orderid,
    c.fullname,
    COUNT(DISTINCT oi.productid) AS unique_products,
    SUM(oi.quantity) AS total_quantity,
    SUM(oi.quantity * p.price) AS total_amount,
    o.orderdate
FROM Orders o
JOIN Customers c ON o.Customerid = c.Customerid
JOIN Order_Items oi ON o.Orderid = oi.Orderid
JOIN Products p ON oi.productid = p.productid
GROUP BY o.Orderid;

-- procedure
DELIMITER //
CREATE PROCEDURE UpdateStock(productid INT, quantity INT, operation CHAR(1))
BEGIN
    IF operation = 'I' THEN
        UPDATE Products SET stock = stock - quantity WHERE productid = productid;
    ELSEIF operation = 'D' THEN
        UPDATE Products SET stock = stock + quantity WHERE productid = productid;
    END IF;
END //
DELIMITER ;

-- triggers
DELIMITER //
CREATE TRIGGER UpdateStockOnInsert
AFTER INSERT ON Order_Items
FOR EACH ROW
BEGIN
    CALL UpdateStock(NEW.Productid, NEW.quantity, 'I');
END //

CREATE TRIGGER UpdateStockOnDelete
AFTER DELETE ON Order_Items
FOR EACH ROW
BEGIN
    CALL UpdateStock(OLD.Productid, OLD.quantity, 'D');
END //
DELIMITER ;





