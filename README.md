# PythonDB
I wrote this program to make it possible for people in my team to transition away from relying on company-wide google sheets for critical information. The intention was to make an SQL database that would mirror any changes in the google sheets, and vice versa. 

The project is split in two parts

## Connector
The connector imports a single google sheet, converts it to mysql, and makes a new table on a designated mysql database. When you call the script the json file can be updated to choose what google sheet to connect to, as well as what sql database to connect to. You have to provide your own credentials json file, as well as share the sheet with your service account email.

## Analytical module (incomplete)
This part serves as a backend to a django app that retrieves and formats data which it then exports. Idea being to let startups request the information themselves.

***

## ~Actual app is hosted on [pythonanywhere](pythonanywhere.com)~
This app is no longer in use. If you want access send me a DM.

## Features
- Automatically update mysql database based on google sheet
