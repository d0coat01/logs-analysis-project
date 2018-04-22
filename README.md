# Logs Analysis Project
A python reporting tool that analyzes a newspaper database and describes what type of articles the site's readers enjoy.

## Example Output
Top 3 Articles of All Time

"Candidate is jerk, alleges rival" - 338647 views  
"Bears love berries, alleges bear" - 253801 views  
"Bad things gone, say good people" - 170098 views  
  
Top Authors of All Time  

Ursula La Multa - 507594 views  
Rudolf von Treppenwitz - 423457 views  
Anonymous Contributor - 170098 views  
Markoff Chaney - 84557 views  

Days Where 1% of Requests Lead to Errors  
  
Jul 17, 2016 - 2.3% errors  

## Installation
Make sure you have Vagrant installed.
1. download [VM configuration](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)
2. open zip and `cd vagrant`
3. `vagrant up`
4. `vagrant ssh`
5. `cd vagrant`
6. `git clone https://github.com/d0coat01/logs-analysis-project/`
7. `cd logs-analysis-project`
8. download [SQL data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) to your vagrant directory (this dir is shared with Vagrant VM)
9. `psql -d news -f newsdata.sql`
10. `psql -d news -f views.sql`

## Run
`python Reports.py`

## Code Navigation

- `Reports.py` - Contains a Reports class and prints out a report.
- `views.sql` - Creates three views called article_log, daily_errors, and daily_requests. These are all views based off of the log table exclusively, so they update automatically when log is edited.

### Created Views

*article_log*:  
`create view article_log as select split_part(split_part(path, '/article/', 2), '/', 1) as article_slug, id from log where path like '%/article/%';`

*daily_errors*:  
`create view daily_errors as select time::date as date, count(id) as error_count  
from log  
where status != '200 OK'  
group by date;`

*daily_requests*:  
`create view daily_requests as select time::date as date, count(id) as request_count  
from log  
group by date;`


## Sources
I built this off of Udacity's VM configuration and newspaper database.

## License
[MIT](https://choosealicense.com/licenses/mit/) License 2018. This code may be shared, copied, and changed freely.
