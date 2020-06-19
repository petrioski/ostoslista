# SQL-kyselyt oleellisimmista käyttäjätoiminnoista

**uusi käyttäjä voi luoda tunnukset**
```sql
BEGIN
SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS account_password, account.role AS account_role
FROM account
WHERE account.username = ?
 LIMIT ? OFFSET ?
INSERT INTO account (date_created, date_modified, name, username, password, role) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)
COMMIT
```

**sisäänkirjautuminen**
```sql
BEGIN
 SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS account_password, account.role AS account_role
FROM account
WHERE account.username = ? AND account.password = ?
 LIMIT ? OFFSET ?
ROLLBACK
```



**käyttäjä näkee omat ostoslistansa**

```sql
SELECT list.id AS list_id, list.date_created AS list_date_created, list.date_modified AS list_date_modified, list.name AS list_name, list.done AS list_done, list.account_id AS list_account_id
FROM list
WHERE list.account_id = ?
ORDER BY list.done, list.date_modified DESC
```

**käyttäjä voi luoda uuden ostoslistan**
```sql
INSERT INTO list (date_created, date_modified, name, done, account_id)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)
```

**käyttäjä voi poistaa ostoslistan**

```sql
DELETE FROM list WHERE list.id = ?
```


**käyttäjä voi lisätä eri tuotteita, joiden pohjalta lisäillä ostoksia ostolistoja**

```sql
INSERT INTO item (date_created, date_modified, name, unit_type, category_id)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)
```


**käyttäjä voi lisätä tuotekategorian tuotteelle**

```sql
INSERT INTO category (date_created, date_modified, name) VALUES
(CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?)
```

**Käyttäjä voi lisätä tuotteen listalle**

```sql
INSERT INTO purchase (date_created, date_modified, amount, collected, item_id, list_id)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)
```

**käyttäjä voi poistaa tuotteen listalta**

```sql
DELETE FROM purchase WHERE purchase.id = ?
```

**käyttäjä näkee tuotteet ryhmiteltynä kategorioihin ostoslistalla**

```sql
SELECT purchase.id AS purchase_id, purchase.date_created AS purchase_date_created, purchase.date_modified AS purchase_date_modified, purchase.amount AS purchase_amount, purchase.collected AS purchase_collected, purchase.item_id AS purchase_item_id, purchase.list_id AS purchase_list_id
FROM purchase
WHERE purchase.list_id = ? ORDER BY purchase.item_id
```

```sql
SELECT category.name FROM item LEFT JOIN category  ON item.category_id = category.id
WHERE item.id = ?
```


**käyttäjä voi merkitä tuotteen ostetuksi (löydetyksi) ostoslistalla**
```sql
UPDATE purchase SET date_modified=CURRENT_TIMESTAMP, collected=? WHERE purchase.id = ?
```

**kategorioiden yhteydessä listataan kuinka monta tuotetta on**
```sql
SELECT a.name, a.id, COUNT(b.id) as item_count
  FROM category as a
  LEFT JOIN item as b
    ON a.id = b.category_id
  GROUP BY a.name, a.id
  ORDER BY COUNT(b.id) DESC, a.name
```

**käyttäjän yhteenvetotilasto ostohistoriastaan**
```sql
SELECT item.name, count(purchase.id) as purchase_times
FROM purchase
LEFT JOIN item
    ON purchase.item_id = item.id
LEFT JOIN list
    ON purchase.list_id = list.id
WHERE
    list.account_id = :id
GROUP BY
    item.name
ORDER BY count(purchase.id) DESC
```
