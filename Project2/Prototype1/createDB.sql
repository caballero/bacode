CREATE TABLE professor (
	pid INT PRIMARY KEY,
	name TEXT,
	affiliation TEXT,
	email TEXT,
	phone TEXT
	);

CREATE TABLE student (
	aid INT PRIMARY KEY,
	name TEXT,
	affiliation TEXT,
	email TEXT,
	phone TEXT
	);

CREATE TABLE skills (
	sid INT PRIMARY KEY,
	skill TEXT
	);

CREATE TABLE interests (
	iid INT PRIMARY KEY,
	interest TEXT
	);

CREATE TABLE jobs (
	jid INT PRIMARY KEY,
	job TEXT,
	description TEXT,
	pid INT,
	skills TEXT,
	interests TEXT
	);

INSERT INTO professor VALUES (1, "Albus Dumbledore", "Hogwarts", "director@hogwards.edu", "555-4545");
INSERT INTO professor VALUES (2, "Severus Snape", "Slytherin", "snape@hogwards.edu", "555-4542");
INSERT INTO professor VALUES (3, "Minerva McGonagall", "Griffindor", "mcgonadall@hogwards.edu", "555-4544");

INSERT INTO student VALUES (1, "Harry Potter", "Griffindor", "hpotter@hogwards.edu", "555-3001");
INSERT INTO student VALUES (2, "Ron Weasley", "Griffindor", "rweasley@hogwards.edu", "555-3002");
INSERT INTO student VALUES (3, "Draco Malfoy", "Slytherin", "dmalfoy@hogwards.edu", "555-3011");
INSERT INTO student VALUES (4, "Luna Lovegood", "Griffindor", "llovegood@hogwards.edu", "555-3004");

INSERT INTO skills VALUES (1, "Magic potion preparation");
INSERT INTO skills VALUES (2, "Fire spells");
INSERT INTO skills VALUES (3, "Wind spells");
INSERT INTO skills VALUES (4, "Water spells");
INSERT INTO skills VALUES (5, "Dark magic defense spells");

INSERT INTO interests VALUES (1, "Water spells");
INSERT INTO interests VALUES (2, "Fire spells");
INSERT INTO interests VALUES (3, "Wind spells");
INSERT INTO interests VALUES (4, "Magical creatures");
INSERT INTO interests VALUES (5, "Muggles studies");

INSERT INTO jobs VALUES (1, "Dragon care", "Take care of my dragon", 1, "1,2,4", "4");
INSERT INTO jobs VALUES (2, "Transmutation potion", "Prepare my potions, no pay", 2, "1", "");
