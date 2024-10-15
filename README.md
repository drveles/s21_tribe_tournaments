# School 21 tribe tournaments
    Site to displaying School 21 tribe tournaments in real time.

Описание на русском [здесь](./README_RUS.md) <br>

Stack: `Python`, `SQL`, `Docker` <br>
Libs and frameworks: `Django`, `DjangoORM` <br>


## Architecture
### nginx
1. `/` - home page (now pass) <br> 
2. `/tournaments/` - all traffic directed to this application <br>

### django_app - /tournaments/
Main `MTV` web application. 
- Creates pages to users requests
- Creates models fo `SQL` DB using `Django ORM`
- Uses data from the DB to generate pages

### updater
Must get actual information from School API and update DB

### database 
Main and single database for all data


## MVP
- Must display KZN campus tribe tournament. 
- Must work fast and look okay.
- Must display current tournament in live time.


## TO DO here: [DEV canban](https://github.com/users/drveles/projects/6/views/1) 
