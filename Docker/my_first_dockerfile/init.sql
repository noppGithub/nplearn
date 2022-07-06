-- create schema
CREATE SCHEMA IF NOT EXISTS nplearn_schema
AUTHORIZATION dockeruser;

-- create table

CREATE table nplearn_schema.customer(customer_id int, customer_name varchar(255), customer_address varchar(255));

-- insert data

INSERT into nplearn_schema.customer(customer_id, customer_name, customer_address)
values(1,
       'nplearn',
       '123 street');


INSERT into nplearn_schema.customer(customer_id, customer_name, customer_address)
values(2,
       'np',
       '321 street');


INSERT into nplearn_schema.customer(customer_id, customer_name, customer_address)
values(3,
       'learn',
       '111 street');

-- end