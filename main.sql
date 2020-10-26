CREATE TABLE customer(
  customer_id     INT NOT NULL UNIQUE PRIMARY KEY,
  last_name       VARCHAR(25) NOT NULL,
  given_name      VARCHAR(25) NOT NULL,
  middle_initial  CHAR,
  address         VARCHAR(255) NOT NULL,
  city            VARCHAR(25) NOT NULL,
  mobile          VARCHAR(25),
  landline        VARCHAR(25),
  postal_code     INT NOT NULL,
  birth_date      DATE NOT NULL,
  age             AS (CONVERT(INT,CONVERT(CHAR(8),CURRENT_DATE(),112))-CONVERT(CHAR(8),birth_date,112))/10000
);
CREATE TABLE item(
  item_no     INT NOT NULL UNIQUE PRIMARY KEY,
  category    VARCHAR(25) NOT NULL,
  description VARCHAR(255),
  risk_level  ENUM('Low', 'Medium', 'High', 'Very High') NOT NULL,
  amount      FLOAT NOT NULL,
  FOREIGN KEY (risk_level) REFERENCES risk(risk_level) ON DELETE RESTRICT
);
CREATE TABLE pawn_ticket(
  ticket_no     INT NOT NULL UNIQUE PRIMARY KEY,
  pawn_date     DATE NOT NULL DEFAULT CURRENT_DATE(),
  due_date      AS pawn_date + interval '1 month',
  payment_date  DATE DEFAULT due_date
);
CREATE TABLE risk(
  risk_level    ENUM('Low', 'Medium', 'High', 'Very High') NOT NULL UNIQUE PRIMARY KEY,
  interest_rate FLOAT NOT NULL
);
CREATE TABLE inventory_tag(
  item_no       INT NOT NULL UNIQUE PRIMARY KEY,
  customer_name VARCHAR(255) NOT NULL,
  description   VARCHAR(255),
  category      VARCHAR(25) NOT NULL,
  pawn_date     DATE NOT NULL,
  amount        FLOAT NOT NULL
  FOREIGN KEY (item_no) REFERENCES item(item_no) ON DELETE RESTRICT
);
CREATE TABLE receipt(
  payment_date  DATE
);
