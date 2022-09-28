# coin-data

An old proof-of-concept application from 2014 that collected statistics about crypto prices and calculated exponential moving averages. These would then be used to decide if it was time to buy or sell crypto.

It is retained here for reference purposes.

## Notes

Postgresql manager: pgadmin
Working with heroku and git: https://devcenter.heroku.com/articles/git
Working with heroku and python: https://devcenter.heroku.com/articles/getting-started-with-python

virtualenv

1. virtualenv --setuptools <name>
2. source <env>/bin/activate

Access DB URL: heroku pg:promote HEROKU_POSTGRESQL_ROSE_URL (makes available AS DATABASE_URL env var)
