# S21 tribe tournaments
Site to displaying School 21 tribe tournaments

## Architecture
### nginx/
`/` - home page (now pass) <br>
`/tournaments/` - Landing with all campuses, all cores, all tribes, all peers. <br>
`/tournaments/<slug:campus_name>/` <br>
`/tournaments/<slug:campus_name>/<slug:tribe_name/` <br>

### django_app
I think i can create static page, without client logic. I can draw from HTML file from my VDS.

### updater
Must get actual information from School API and update DB

### database/ | PostgreSQL
Main and single database for all data.

#### Structure 
##### campuses
```py
id: int,
name: str,
```
##### tournaments
```py
id: int,
name: str,
start: timestamp,
end: timestamp,
```

##### tribes
```py
id: int,
name: str,
campus_id: int,
capacity: int,
parallel: str,
visibility: bool, 
master: str,

curr_tribe_points: int,
prev_tribe_points: int,
```

##### peers
```py
id: int, #need auto-generation
name: str,
campus_id: int,
tribe_id: int,
level: int,
wave: str,
curr_tribe_points: str,
prev_tribe_points: str,
```

## MVP
- Must display only KZN campus tribe tournament. 
- Must work fast and look okay.
- Must display only current tournament

## TO DO - migrate to [DEV canban](https://github.com/users/drveles/projects/6/views/1) 
- learning Django
- Making tournaments page
- Making tribe page
- Making drveles.ru page
- Making 404 page

## TO DO after MVP - migrate to canban DEV 
