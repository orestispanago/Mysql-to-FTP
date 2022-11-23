# Mysql-to-FTP


Requirements:

```pip install pandas sqlalchemy PyMySQL```

To avoid overlapping cron job execution, use ```flock``` in crontab:

```
*/5 * * * * /usr/bin/flock -w 0 ~/flock_file.lock python3 ~/Mysql-to-FTP/db_to_ftp.py
```

To check if your cron job is running:

```
grep CRON /var/log/syslog
```

To make sure that ```flock``` works:

```
flock -n -x ~/flock_file.lock true || echo "LOCKED"
```