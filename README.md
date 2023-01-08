# README #

This README would normally document whatever steps are necessary to get your application up and running.

### How to work with alembic migrations

* Initialize db migrations: alembic init alembic
* Generate new migration: alembic revision -m "create table"
* Upgrade migrations: alembic upgrade head 
* Downgrade to prev migration: alembic downgrade -1
