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
# format is:
# [ 'h m  dom mon dow', 'backup /' ]
# which produces the following line:
# m h  dom mon dow  root   restic -p "${RESTIC_PASSWORD_FILE}" backup /
restic_jobs:
  - [ '0 4  * * *', 'backup /var' ]
  - [ '0 6  * * *', 'backup /usr' ]
```

Usage
-----

See `tests/test.yml` for an example

License
-------

BSD
