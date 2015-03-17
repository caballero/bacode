CREATE TABLE professor (
	pid INT AS PRIMARY KEY,
	name TEXT,
	affiliation TEXT,
	email TEXT,
	phone TEXT
	);

CREATE TABLE student (
	aid INT AS PRIMARY KEY,
	name TEXT,
	affiliation TEXT,
	email TEXT,
	phone TEXT
	);

CREATE TABLE skills (
	sid INT AS PRIMARY KEY,
	skill TEXT
	);

CREATE TABLE interests (
	iid INT AS PRIMARY KEY,
	interest TEXT
	);

CREATE TABLE jobs (
	jid INT AS PRIMARY KEY,
	job TEXT,
	description TEXT,
	pid INT,
	skills TEXT,
	interests TEXT
	);
