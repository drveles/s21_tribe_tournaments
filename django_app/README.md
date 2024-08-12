# Django app structure

## Logic 
I think i can create static page, without client logic. I can draw from HTML file from my VDS.

`/tournaments/` - Landing with all campuses, all cores, all tribes, all peers. <br>
`/tournaments/<slug:campus_name>/` - all tribes for this campus <br> 
`/tournaments/<slug:campus_name>/<slug:tribe_name/` - all peers for this tribe <br> 

## Models 
### campuses
```py
id: int,
name: str,
slug: str,
```
### tournaments
```py
id: int,
name: str,
start: timestamp,
end: timestamp,
```

### tribes
```py
id: int,
name: str,
slug: str,
campus_id: int,
master: str,
parallel: str,
visibility: bool, 
capacity: int,
curr_points: int,
prev_points: int,
```

### peers
```py
id: int, 
name: str,
campus_id: int,
curr_tribe_id: int,
prev_tribe_id: int,
level: int,
wave: str,
curr_points: str,
prev_points: str,
```
