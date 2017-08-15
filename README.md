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
    arg: 'pgdatabase'
    tags:
      - postgres
restic_jobs_raw:
  - command: 'restic backup /var'
    at: '0 4  * * *'
  - command: 'restic backup /home'
    at: '0 3  * * *'
    user: 'restic'
```

Usage
-----

See `tests/test.yml` for an example

License
-------

BSD
