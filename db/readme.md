# DATABASE readme
PostgreSQL to store all data.

## Structure 
### campuses
```py
id: int,
name: str,
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
campus_id: int,
capacity: int,
parallel: str,
visibility: bool, 
master: str,

curr_tribe_points: int,
prev_tribe_points: int,
```

### peers
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
