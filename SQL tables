CREATE TABLE "countries" (
	"code_AI"	INTEGER,
	"name"	TEXT,
	PRIMARY KEY("code_AI" AUTOINCREMENT)
);
CREATE TABLE "flights" (
	"flight_id"	INTEGER,
	"timestamp"	TEXT,
	"remaining_seats"	INTEGER,
	"origin_country_id"	INTEGER,
	"dest_country_id"	INTEGER,
	FOREIGN KEY("origin_country_id") REFERENCES "countries"("code_AI"),
	FOREIGN KEY("dest_country_id") REFERENCES "countries"("code_AI"),
	PRIMARY KEY("flight_id" AUTOINCREMENT)
);
CREATE TABLE "tickets" (
	"ticket_id"	INTEGER,
	"user_id"	INTEGER,
	"flight_id"	INTEGER,
	FOREIGN KEY("user_id") REFERENCES "users"("id_AI"),
	FOREIGN KEY("flight_id") REFERENCES "flights"("flight_id"),
	PRIMARY KEY("ticket_id" AUTOINCREMENT)
);
CREATE TABLE "users" (
	"id_AI"	INTEGER,
	"full_name"	TEXT,
	"password"	TEXT,
	"real_id"	TEXT UNIQUE,
	PRIMARY KEY("id_AI" AUTOINCREMENT)
);
