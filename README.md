# Logs Analysis Project
A python reporting tool that analyzes a newspaper database and describes what type of articles the site's readers enjoy.

## Installation
Make sure you have Vagrant installed.
1. download [VM configuration](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)
2. open zip and `cd vagrant`
3. `vagrant up`
4. `vagrant ssh`
5. `cd vagrant`
6. 1. `git clone https://github.com/d0coat01/logs-analysis-project/`
7. `cd logs-analysis-project`
3. download [SQL data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) to your vagrant directory (this dir is shared with Vagrant VM)
4. `psql -d news -f newsdata.sql`
4. `psql -d news -f views.sql`
5. `python Reports.py`

## Code Navigation

- Reports.py - Contains a Reports class and prints out the report.
- views.sql - Creates three views called article_log, daily_errors, and daily_requests. These are all views based off of the log table exclusively, so they update automatically when log is edited.


## Sources
I built this off of Udacity's VM configuration and newspaper database.

## License
[MIT](https://choosealicense.com/licenses/mit/) License 2018. This code may be shared, copied, and changed freely.
