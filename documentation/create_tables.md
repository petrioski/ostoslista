# SQL-lauseet taulujen luontiin

```sql
CREATE TABLE category (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(500) NOT NULL,
        PRIMARY KEY (id)
)


CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        username VARCHAR(144) NOT NULL,
        password VARCHAR(144) NOT NULL,
        role VARCHAR(144) NOT NULL,
        PRIMARY KEY (id)
)


CREATE TABLE list (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(500) NOT NULL,
        done BOOLEAN NOT NULL,
        account_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        CHECK (done IN (0, 1)),
        FOREIGN KEY(account_id) REFERENCES account (id)
)


CREATE TABLE item (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(500) NOT NULL,
        unit_type VARCHAR(144) NOT NULL,
        category_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(category_id) REFERENCES category (id)
)


CREATE TABLE purchase (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        amount INTEGER NOT NULL,
        collected BOOLEAN NOT NULL,
        item_id INTEGER NOT NULL,
        list_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        CHECK (collected IN (0, 1)),
        FOREIGN KEY(item_id) REFERENCES item (id),
        FOREIGN KEY(list_id) REFERENCES list (id) ON DELETE cascade
)



CREATE TABLE user_list (
        user_id INTEGER NOT NULL,
        list_id INTEGER NOT NULL,
        FOREIGN KEY(user_id) REFERENCES account (id),
        FOREIGN KEY(list_id) REFERENCES list (id)
)
```
