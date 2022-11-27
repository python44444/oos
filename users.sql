-- -------------------------------------------------------------
-- TablePlus 4.7.1(428)
--
-- https://tableplus.com/
--
-- Database: peewee_db.sqlite
-- Generation Time: 2022-11-27 11:24:05.1390
-- -------------------------------------------------------------


CREATE TABLE "users" ("id" INTEGER NOT NULL PRIMARY KEY, "name" VARCHAR(255) NOT NULL, "password" VARCHAR(255) NOT NULL, "title" VARCHAR(255) NOT NULL, "body" VARCHAR(255) NOT NULL);

INSERT INTO "users" ("id", "name", "password", "title", "body") VALUES
('1', 'ちんちん', 'sha256$LydpeUJn7dJ5Ka1E$a67d2705fd53a67c0692c7942ff061fcbda1a0d96692f31b426a0ba8b4e7433e', 'title', 'body');
