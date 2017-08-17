Restic
=======

Deploys restic binary and cron jobs to trigger restic commands

Requirements
------------

None

Role Variables
--------------

```yaml
restic_version: '0.7.0'
restic_bin_path: '/usr/local/bin'
restic_repo: '/tmp/test'
# this obviously goes into the vault
vault_repo_password: 'foobar'
```

Example configuration
---------------------

```yaml
# format:
# at: 'h m  dom mon dow'
# type: < 'db_mysql' | 'db_pgsql' >
restic_jobs:
  - at: '0 6  * * *'
    type: 'db_mysql'
    arg: 'blog'
  - at: '0 8  * * *'
    type: 'db_pgsql'
    arg: 'users'
    tags:
      - postgres
      - database
restic_jobs_raw:
  - command: 'restic backup /var'
    at: '0 4  * * *'
  - command: 'restic backup /home'
    at: '0 3  * * *'
    user: 'restic'
```

Which produces `/etc/cron.d/restic` file with the following content:

```
# restic backup jobs
# vi: ft=jinja.crontab

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
RESTIC_REPOSITORY=/tmp/test
RESTIC_PASSWORD_FILE=/var/lib/restic/repopw

0 6  * * *  root   mysqldump --routines --add-drop-table --default-character-set=utf8 blog | restic backup --stdin --stdin-filename db_mysql_blog.sql
0 8  * * *  root   su -c '/usr/bin/pg_dump --encoding=UTF8 "users"' postgres  | restic backup --stdin --stdin-filename db_pgsql_users.sql --tag postgres --tag database

0 4  * * *  root  restic backup /var
0 3  * * *  backup  restic backup /home
```


Usage
-----

See `tests/test.yml` for an example

License
-------

BSD
