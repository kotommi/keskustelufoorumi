#!/bin/bash
cat categories.sql | sqlite3 application/posts.db
cat roles.sql | sqlite3 application/posts.db
