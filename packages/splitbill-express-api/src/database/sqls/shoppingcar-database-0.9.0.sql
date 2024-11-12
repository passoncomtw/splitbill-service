create extension moddatetime;

DROP TABLE IF EXISTS "public"."users";
-- This script only contains the table creation statements and does not fully represent the table in the database. Do not use it as a backup.

-- Table Definition
CREATE TABLE "public"."users" (
    "id" int generated always as identity primary key UNIQUE,
    "name" varchar(30) NOT NULL, -- COMMENT '使用者名稱',
    "password" varchar(255) NOT NULL, -- COMMENT '登入密碼',
    "phone" varchar(30) NOT NULL, -- COMMENT '使用者手機號碼 example: 0987654321',
    "created_at" TIMESTAMP default current_timestamp,
    "updated_at" TIMESTAMP default null
);

create trigger tri_bu_users_updated_at
before update
on users
for each row
execute function moddatetime(updated_at);

DROP TABLE IF EXISTS "public"."merchants";
-- This script only contains the table creation statements and does not fully represent the table in the database. Do not use it as a backup.

-- Table Definition
CREATE TABLE "public"."merchants" (
    "id" int generated always as identity primary key UNIQUE,
    "name" varchar(30) NOT NULL, -- COMMENT 商家名稱,
    "password" varchar(30) NOT NULL, -- COMMENT 後台登入密碼,
    "phone" varchar(30) NOT NULL UNIQUE, -- COMMENT 商家聯絡手機,
    "email" varchar(30) NOT NULL UNIQUE, -- COMMENT 商家 Email,
    "created_at" TIMESTAMP default current_timestamp,
    "updated_at" TIMESTAMP default NULL
);

create trigger tri_bu_merchants_updated_at
before update
on merchants
for each row
execute function moddatetime(updated_at);

-- Indices
CREATE UNIQUE INDEX merchants_email_key ON public.merchants USING btree (email);
CREATE UNIQUE INDEX merchants_phone_key ON public.merchants USING btree (phone);

DROP TABLE IF EXISTS "public"."products";
-- This script only contains the table creation statements and does not fully represent the table in the database. Do not use it as a backup.

-- Table Definition
CREATE TABLE "public"."products" (
    "id" int generated always as identity primary key UNIQUE,
    "name" varchar(30) NOT NULL, -- COMMENT '產品名稱',
    "price" decimal(10,2) NOT NULL, -- COMMENT '產品價格',
    "description" varchar(255) DEFAULT NULL, -- COMMENT '產品描述',
    "subtitle" varchar(255) DEFAULT NULL, --  COMMENT '產品次主題',
    "stock_amount" NUMERIC(11) DEFAULT 0, --  COMMENT '產品庫存數量'
    "merchant_id" int NOT NULL, -- COMMENT '商家id, merchants.id'
    "created_at" TIMESTAMP default current_timestamp,
    "updated_at" TIMESTAMP default null,
    CONSTRAINT fk_products_merchants FOREIGN KEY(merchant_id) REFERENCES merchants(id)
);

create trigger tri_bu_products_updated_at
before update
on products
for each row
execute function moddatetime(updated_at);

DROP TABLE IF EXISTS "public"."orders";
-- This script only contains the table creation statements and does not fully represent the table in the database. Do not use it as a backup.

-- Table Definition
CREATE TABLE "public"."orders" (
    "id" UUID PRIMARY KEY DEFAULT gen_random_uuid() UNIQUE,
    "user_id" int NOT NULL, -- COMMENT '會員id, users.id'
    "product_count" NUMERIC DEFAULT 0, -- COMMENT 產品數量
    "total_amount" NUMERIC DEFAULT 0, -- COMMENT 訂單總額
    "created_at" TIMESTAMP default current_timestamp,
    "updated_at" TIMESTAMP default null,
    "is_paid" bool NOT NULL DEFAULT FALSE,
    CONSTRAINT fk_orders_users FOREIGN KEY(user_id) REFERENCES users(id)
);

create trigger tri_bu_orders_updated_at
before update
on orders
for each row
execute function moddatetime(updated_at);

DROP TABLE IF EXISTS "public"."order_items";
-- This script only contains the table creation statements and does not fully represent the table in the database. Do not use it as a backup.

-- Table Definition
CREATE TABLE "public"."order_items" (
    "id" int generated always as identity primary key UNIQUE,
    "product_id" int NOT NULL, -- COMMENT '產品id, products.id'
    "merchant_id" int NOT NULL, --  COMMENT '商家id, merchants.id'
    "order_id" UUID NOT NULL, -- COMMENT '訂單id, orders.id'
    "amount" int NOT NULL, -- COMMENT '產品價格'
    "created_at" TIMESTAMP default current_timestamp,
    "updated_at" TIMESTAMP default null,
    CONSTRAINT fk_order_items_products FOREIGN KEY(product_id) REFERENCES products(id),
    CONSTRAINT fk_order_items_merchants FOREIGN KEY(merchant_id) REFERENCES merchants(id),
    CONSTRAINT fk_order_items_orders FOREIGN KEY(order_id) REFERENCES orders(id)
);

create trigger tri_bu_order_items_updated_at
before update
on order_items
for each row
execute function moddatetime(updated_at);

-- Table Definition
CREATE TABLE "public"."shoppingcars" (
    "id" int generated always as identity primary key UNIQUE,
    "user_id" int NOT NULL, -- COMMENT '會員id, users.id',
    "product_count" int NOT NULL, --  COMMENT '產品數量'
    "total_amount" decimal(10,2) DEFAULT 0, -- 購物車總額
    "created_at" TIMESTAMP default current_timestamp,
    "updated_at" TIMESTAMP default null,
    CONSTRAINT fk_orders_users FOREIGN KEY(user_id) REFERENCES users(id)
);

create trigger tri_bu_shoppingcars_updated_at
before update
on shoppingcars
for each row
execute function moddatetime(updated_at);

-- Table Definition
CREATE TABLE "public"."shoppingcar_items" (
    "id" int generated always as identity primary key UNIQUE,
    "product_id" int NOT NULL, -- COMMENT '產品id, products.id'
    "merchant_id" int NOT NULL, --  COMMENT '商家id, merchants.id'
    "shoppingcar_id" int NOT NULL, --  COMMENT '購物車id, shoppingcars.id'
    "amount" numeric NOT NULL, -- COMMENT '產品數量'
    "created_at" TIMESTAMP default current_timestamp,
    "updated_at" TIMESTAMP default null,
    CONSTRAINT fk_shoppingcar_items_products FOREIGN KEY(product_id) REFERENCES products(id),
    CONSTRAINT fk_shoppingcar_items_merchants FOREIGN KEY(merchant_id) REFERENCES merchants(id),
    CONSTRAINT fk_shoppingcar_items_shoppingcars FOREIGN KEY(shoppingcar_id) REFERENCES shoppingcars(id)
);

create trigger tri_bu_shoppingcar_items_updated_at
before update
on shoppingcar_items
for each row
execute function moddatetime(updated_at);

DROP TABLE IF EXISTS "public"."backend_users";
-- This script only contains the table creation statements and does not fully represent the table in the database. Do not use it as a backup.

-- Table Definition
CREATE TABLE "public"."backend_users" (
    "id" int generated always as identity primary key UNIQUE,
    "account" varchar(30) NOT NULL, -- COMMENT '後台使用者帳號'
    "password" varchar(255) NOT NULL, -- COMMENT '後台使用者密碼'
    "created_at" TIMESTAMP default current_timestamp,
    "updated_at" TIMESTAMP default null,
);

create trigger tri_bu_backend_users_updated_at
before update
on backend_users
for each row
execute function moddatetime(updated_at);
