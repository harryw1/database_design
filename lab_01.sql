Harrison Weiss
Neel Verma

CREATE TABLE `orders` (
	`order_number`	INTEGER,
	`order_date`	TEXT,
	`customer_name`	TEXT,
	`customer_street`	TEXT,
	`customer_city`	TEXT,
	`customer_state`	TEXT,
	`customer_zip`	INTEGER,
	`customer_country`	TEXT,
	`pc_model`	INTEGER,
	`pc_speed`	REAL,
	`pc_ram`	INTEGER,
	`pc_hd`	INTEGER,
	`pc_price`	INTEGER,
	PRIMARY KEY(`order_number`)
);

insert into orders (order_date, pc_model, pc_speed, pc_ram, pc_hd, pc_price, customer_name, customer_street, customer_city, customer_state, customer_zip, customer_country, order_number)
    VALUES ('2015/11/03', 1004, 2.8, 1024, 250, 649, 'Kasandra Cryer', '884 Meadow Lane', 'Bardstown', 'KY', '40004', 'US', 36);
insert into orders (order_date, pc_model, pc_speed, pc_ram, pc_hd, pc_price, customer_name, customer_street, customer_city, customer_state, customer_zip, customer_country, order_number)
    VALUES ('2014/10/02', 1005, 3.2, 512, 250, 630, 'Ferne Linebarger', '172 Academy Street', 'Morton Grove', 'IL', '60053', 'US', 172);
insert into orders (order_date, pc_model, pc_speed, pc_ram, pc_hd, pc_price, customer_name, customer_street, customer_city, customer_state, customer_zip, customer_country, order_number)
    VALUES ('2016/02/06', 1008, 2.2, 2048, 250, 770, 'Britany Manges', '114 Fawn Court', 'Antioch', 'TN', '37013', 'US', 236);
insert into orders (order_date, pc_model, pc_speed, pc_ram, pc_hd, pc_price, customer_name, customer_street, customer_city, customer_state, customer_zip, customer_country, order_number)
    VALUES ('2015/02/11', 1010, 2.8, 2048, 300, 770, 'Alma Secrist', '877 Cherry Street', 'Augusta', 'GA', '30906', 'US', 245);
insert into orders (order_date, pc_model, pc_speed, pc_ram, pc_hd, pc_price, customer_name, customer_street, customer_city, customer_state, customer_zip, customer_country, order_number)
    VALUES ('2015/04/16', 1012, 2.8, 1024, 160, 649, 'Sanda Archer', '948 Penn Street', 'New Rochelle', 'NY', '10801', 'US', 272);
insert into orders (order_date, pc_model, pc_speed, pc_ram, pc_hd, pc_price, customer_name, customer_street, customer_city, customer_state, customer_zip, customer_country, order_number)
    VALUES ('2009/06/07', 1009, 2, 1024, 250, 650, 'Michal Verona', '225 Surrey Lane', 'Windermere', 'FL', '34786', 'US', 278);
insert into orders (order_date, pc_model, pc_speed, pc_ram, pc_hd, pc_price, customer_name, customer_street, customer_city, customer_state, customer_zip, customer_country, order_number)
    VALUES ('2014/05/16', 1007, 2.2, 1024, 200, 510, 'Yuki Maio', '163 Route 2', 'Warminster', 'PA', '18974', 'US', 321);
insert into orders (order_date, pc_model, pc_speed, pc_ram, pc_hd, pc_price, customer_name, customer_street, customer_city, customer_state, customer_zip, customer_country, order_number)
    VALUES ('2008/04/12', 1006, 3.2, 1024, 320, 1049, 'Alma Secrist', '877 Cherry Street', 'Augusta', 'GA', '30906', 'US', 345);
insert into orders (order_date, pc_model, pc_speed, pc_ram, pc_hd, pc_price, customer_name, customer_street, customer_city, customer_state, customer_zip, customer_country, order_number)
    VALUES ('2015/09/29', 1002, 2.1, 512, 250, 995, 'Nichole Chiles', '997 Columbia Street', 'Avon', 'IN', '46123', 'US', 431);
insert into orders (order_date, pc_model, pc_speed, pc_ram, pc_hd, pc_price, customer_name, customer_street, customer_city, customer_state, customer_zip, customer_country, order_number)
    VALUES ('2012/04/23', 1005, 3.2, 512, 250, 630, 'Nichole Chiles', '997 Columbia Street', 'Avon', 'IN', '46123', 'US', 435);
insert into orders (order_date, pc_model, pc_speed, pc_ram, pc_hd, pc_price, customer_name, customer_street, customer_city, customer_state, customer_zip, customer_country, order_number)
    VALUES ('2012/04/19', 1007, 2.2, 1024, 200, 510, 'Kasandra Cryer', '884 Meadow Lane', 'Bardstown', 'KY', '40004', 'US', 504);
insert into orders (order_date, pc_model, pc_speed, pc_ram, pc_hd, pc_price, customer_name, customer_street, customer_city, customer_state, customer_zip, customer_country, order_number)
    VALUES ('2013/12/17', 1009, 2, 1024, 250, 650, 'Margy Avis', '888 Virginia Street', 'Kokomo', 'IN', '46901', 'US', 562);
insert into orders (order_date, pc_model, pc_speed, pc_ram, pc_hd, pc_price, customer_name, customer_street, customer_city, customer_state, customer_zip, customer_country, order_number)
    VALUES ('2015/11/21', 1004, 2.8, 1024, 250, 649, 'Britany Manges', '144 Fawn Court', 'Antioch', 'TN', '37013', 'US', 583);
insert into orders (order_date, pc_model, pc_speed, pc_ram, pc_hd, pc_price, customer_name, customer_street, customer_city, customer_state, customer_zip, customer_country, order_number)
    VALUES ('2003/10/04', 1010, 2.8, 2048, 300, 770, 'Elana Shahid', '206 High Street', 'Bolingbrook', 'IL', '60440', 'US', 643);
insert into orders (order_date, pc_model, pc_speed, pc_ram, pc_hd, pc_price, customer_name, customer_street, customer_city, customer_state, customer_zip, customer_country, order_number)
    VALUES ('2012/02/15', 1004, 2.8, 1024, 250, 649, 'Kasandra Cryer', '884 Meadow Lane', 'Bardstown', 'KY', '40004', 'US', 712);
insert into orders (order_date, pc_model, pc_speed, pc_ram, pc_hd, pc_price, customer_name, customer_street, customer_city, customer_state, customer_zip, customer_country, order_number)
    VALUES ('2010/01/04', 1011, 2.86, 2048, 160, 959, 'Michal Verona', '225 Surrey Lane', 'Windermere', 'FL', '34786', 'US', 737);
insert into orders (order_date, pc_model, pc_speed, pc_ram, pc_hd, pc_price, customer_name, customer_street, customer_city, customer_state, customer_zip, customer_country, order_number)
    VALUES ('2010/08/06', 1003, 1.42, 512, 80, 478, 'Marvella Searcy', '782 Edgewood Road', 'Smyrna', 'GA', '30080', 'US', 863);

select pc_hd from orders where order_date < '2011/12/31';
select pc_model from orders where customer_state == 'IN';
select customer_name, customer_street from orders where pc_price >=850; and order_date >= '2013/01/01';
select pc_model from orders where pc_speed > 2.8 and pc_price < 600;