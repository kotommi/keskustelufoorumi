#!/bin/bash
cat categories.sql | heroku pg:psql
cat roles.sql | heroku pg:psql
