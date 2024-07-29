# S21 tribe tournaments
Site to displaying School 21 tribe tournaments

## Architecture 

### nginx/
`/` - home page (now pass)
`/tribe_tournaments/` - Landing with all campuses, all cores, all tribes, all peers.

### tribe_tournaments/

I think i can create static page, without client logic. I can draw from HTML file from my VDS.

### api/
Must process call from frontend to new data.

### updater/
Must get actual information from School API and update DB

### database/ | PostgreSQL
Main and single database for all data.

## TO DO


## MVP
Must display only KZN campus tribe tournament. Must work fast and look okay.


## TO DO after MVP
- Need autobackups to DB
