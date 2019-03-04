Harrison Weiss

Part 1:

A:
SELECT model
FROM PC
WHERE speed >= 3.00
GROUP BY model;

B:
SELECT maker
FROM
    Product p
    JOIN Laptop l ON l.model = p.model
WHERE l.hd >= 100
GROUP BY maker;

C:
SELECT p.model, pc.model, l.price
FROM
    Laptop l
    JOIN Product p ON p.model = l.model
    JOIN PC pc ON pc.model = p.model
WHERE p.maker = 'B'
GROUP BY p.model, pc.model, p.type;

D:
SELECT model
FROM
    Printer p
    JOIN Product pt ON pt.model = p.model
WHERE p.color = 'Y'
GROUP BY p.model;

E:
SELECT maker
FROM
    Product p
    JOIN Laptop l ON l.model = p.model
    JOIN PC pc ON pc.model = p.model
WHERE pc.maker = NULL
GROUP BY maker;