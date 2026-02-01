 CREATE TABLE sales (
    order_id VARCHAR PRIMARY KEY,
    order_date DATE,
    product VARCHAR,
    category VARCHAR,
    quantity INT,
    sales NUMERIC,
    region VARCHAR,
    customer_id VARCHAR
);
