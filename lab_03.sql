Harrison Weiss
Neel Verma

Part 1:

A.
SELECT name, COUNT(serial_number)
FROM Orders
JOIN Customers
ON Orders.customer_id = Customers.id
GROUP BY name;

B.
SELECT name, SUM(mo.price)
FROM 
    Customers c
    JOIN Orders o ON o.customer_id = c.id
    JOIN Machines m ON m.serial_number = o.serial_number
    JOIN Model mo ON m.model_number = mo.id
GROUP BY o.name;

C.
SELECT city, state, SUM(mo.price)
FROM
    Customers c
    JOIN Orders o ON o.customer_id = c.id
    JOIN Machines m ON m.serial_number = o.serial_number
    JOIN Model mo ON m.model_number = mo.id
GROUP BY city, state;

D.
SELECT mo.id, COUNT(m.model_number)
FROM
    Model mo
    LEFT JOIN Machines m ON m.model_number = mo.id
GROUP BY mo.id;

E.
SELECT man.name, man.phone_number
FROM
    Manufacturer man
    JOIN Model mo ON man.id = mo.man_id
    LEFT JOIN Machines m on mo.id = m.model_number
GROUP BY man.name
HAVING COUNT(m.serial_number) < 3

PART 2:

A.
SELECT * FROM Manufacturer
WHERE Manufacturer.id IN(
    SELECT Model.man_id FROM Model WHERE Model.id NOT IN(
        SELECT Machines.model_number FROM Machines GROUP BY (Machines.model_number) HAVING COUNT(Machines.serial_number) < 10
    )
)

B.
select * from Customers where Customers.id in (
  select Orders.customer_id from Orders group by (Orders.customer_id) having count(Orders.customer_id) < 10) or (
    Customers.id not in (select Orders.customer_id from Orders))

C.