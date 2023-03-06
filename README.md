# PythonDB
I wrote this program while working at Start-Up Chile in order to make it possible for people in my team to transition away from relying on company-wide google sheets for critical information. The intention was to make an SQL database that would mirror any changes in the google sheets, and vice versa. Hence, people could continue using google sheets if they prefer, but we could better manage permission and distribution of data by integrating an SQL database with other communication tools.

## Connector
The connector is the mo imports a single google sheet, converts it to mysql, and makes a new table on a designated mysql database. When you call the script the json file can be updated to choose what google sheet to connect to, as well as what sql database to connect to. You have to provide your own credentials json file, as well as share the sheet with your service account email.

***

## ~Actual app is hosted on [pythonanywhere](pythonanywhere.com)~
This app is no longer in use. If you want access send me a DM.

## Unfinished features
- Django powered service to allow individual startups to request their specifict information. 
