# PythonDB
Automatic database interaction for global networks database.

The project is split in two parts

## Connector
The connector imports a single google sheet, converts it to mysql, and makes a new table on a designated mysql database.

## Analytical module
This part serves as a backend to a django app that retrieves and formats data which it then exports. Idea being to let startups request the information themselves.

***

## Actual app is hosted on [pythonanywhere](pythonanywhere.com)
If you want access write to me at baltasar.salamon@startupchile.org

## Features
- Automatically update mysql database based on google sheet
