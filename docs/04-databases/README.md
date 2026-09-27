# 🗄️ Database-Related Files

Database systems produce many kinds of files.

| Format | Typical role |
|---|---|
| `.sql` | SQL scripts / dumps |
| `.db` | generic database file |
| `.sqlite` / `.sqlite3` | SQLite database |
| `.mdb` | Microsoft Access database |
| `.accdb` | modern Access database |
| `.dump` | database dump; meaning depends on tool |
| `.bak` | backup; semantics depend on software |

## SQLite

A SQLite database can be stored as a single file:

```text
application.sqlite3
```

It may contain:

- tables
- indexes
- views
- triggers
- metadata

## SQL files

A `.sql` file is normally a text script rather than a database itself.

It may contain:

```sql
CREATE TABLE ...
INSERT INTO ...
CREATE INDEX ...
```

## Important distinction

```text
SQL script ≠ database file ≠ backup format
```

Always identify the database engine before restoring or importing a file.
