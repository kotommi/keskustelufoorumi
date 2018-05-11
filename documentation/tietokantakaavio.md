http://yuml.me/edit/74fd6f31

![diagram](http://yuml.me/74fd6f31.png)

```sqlite> .schema
CREATE TABLE category (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	title VARCHAR(144) NOT NULL, 
	description VARCHAR(255) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE role (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(50) NOT NULL, 
	description VARCHAR(255), 
	PRIMARY KEY (id), 
	UNIQUE (name)
);
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	active BOOLEAN, 
	PRIMARY KEY (id), 
	UNIQUE (name), 
	UNIQUE (username), 
	CHECK (active IN (0, 1))
);
CREATE TABLE user_role (
	role_id INTEGER, 
	user_id INTEGER, 
	FOREIGN KEY(role_id) REFERENCES role (id), 
	FOREIGN KEY(user_id) REFERENCES account (id)
);
CREATE TABLE thread (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	title VARCHAR(144) NOT NULL, 
	content VARCHAR(1000) NOT NULL, 
	category_id INTEGER NOT NULL, 
	user_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(category_id) REFERENCES category (id), 
	FOREIGN KEY(user_id) REFERENCES account (id)
);
CREATE TABLE post (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	content VARCHAR(1000) NOT NULL, 
	account_id INTEGER NOT NULL, 
	thread_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(thread_id) REFERENCES thread (id)
);
CREATE TABLE category_role (
	role_id INTEGER, 
	category_id INTEGER, 
	FOREIGN KEY(role_id) REFERENCES role (id), 
	FOREIGN KEY(category_id) REFERENCES category (id)
);```
