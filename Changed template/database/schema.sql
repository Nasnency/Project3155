--modified for account type: 0=reader, 1=author
CREATE TABLE users (
    username VARCHAR(255) PRIMARY KEY NOT NULL,
    password_salt VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    session_type INTEGER(1) NOT NULL
);

--added for the comics
--primary key is the hidden "rowid" variable
CREATE TABLE comic (
    comic_id INTEGER PRIMARY_KEY AUTO_INCREMENT,
    page_name VARCHAR(255) NOT NULL,
    image_url VARCHAR(255)

);

--added for comments
CREATE TABLE comment (
    comment_id INTEGER PRIMARY_KEY AUTO_INCREMENT,
    username VARCHAR(255),
    content VARCHAR(2047),
    comic_id INTEGER
);

--adding table for comic pages--no longer needed - saving for posterity
--CREATE TABLE inventory (
--    id INTEGER PRIMARY KEY AUTOINCREMENT,
--    item_name VARCHAR(255) NOT NULL,
--    info VARCHAR(255) NOT NULL,
--    price DECIMAL(10,2) NOT NULL,
--    stock INTEGER NOT NULL,
--    image_url VARCHAR(255) NOT NULL,
--    category VARCHAR(255) NOT NULL
--);

--no longer needed - saving for posterity
--CREATE TABLE sales (
--    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
--    transaction_id VARCHAR(255) NOT NULL,
--    username VARCHAR(255) NOT NULL,
--    item_id INTEGER NOT NULL,
--    quantity INTEGER NOT NULL,
--    sale_date DATETIME NOT NULL,
--    cost DECIMAL(10,2) NOT NULL,
--    FOREIGN KEY (username) REFERENCES users(username),
--    FOREIGN KEY (item_id) REFERENCES inventory(id)
--);

