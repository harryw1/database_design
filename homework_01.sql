Harrison Weiss

/* PART 1 */

CREATE TABLE IF NOT EXISTS "Outcomes" (
	"ship"	TEXT,
	"battle"	TEXT,
	"result"	TEXT,
	PRIMARY KEY("ship","battle")
);
CREATE TABLE IF NOT EXISTS "Battles" (
	"name"	TEXT,
	"date"	TEXT,
	PRIMARY KEY("name","date")
);
CREATE TABLE IF NOT EXISTS "Ships" (
	"name"	TEXT,
	"class"	TEXT,
	"launched"	INTEGER,
	PRIMARY KEY("name","launched")
);
CREATE TABLE IF NOT EXISTS "Classes" (
	"class"	TEXT,
	"type"	TEXT,
	"country"	TEXT,
	"numGuns"	INTEGER,
	"bore"	REAL,
	"displacement"	REAL,
	PRIMARY KEY("class","type","country")
);

ALTER TABLE Classes DROP "bore";
ALTER TABLE Ships ADD "yard" TEXT;

/* PART 2 */

SELECT "class", "country" FROM "Classes" WHERE "bore" >= 16
SELECT "name" FROM "Ships" WHERE "launched" < 1921
SELECT "ship" FROM "Outcomes" WHERE "result" == "sunk"