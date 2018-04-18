#!/bin/bash
cat categories.sql | heroku pg:psql
