import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

version = '0.8.1'


def test_restic_executable(host):
    f = host.file('/usr/local/bin/restic')

    assert f.exists
    assert f.is_symlink
    assert f.user == 'root'
    assert f.group == 'root'

    linked = f.linked_to
    fl = host.file(f.linked_to)
    assert linked == '/opt/restic/bin/restic-'+version
    assert fl.user == 'root'
    assert fl.group == 'root'
    assert fl.mode == 0o755


def test_cronfile(host):
    f = host.file('/etc/cron.d/restic-test')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o640
    with host.sudo():
        assert f.contains('RESTIC_PASSWORD="testpassword"')


def test_restic_version(host):
    cmd = host.run('restic version')
    line = cmd.stdout.splitlines()[0]
    assert line == 'restic '+version


def test_repo(host):
    with host.sudo():
        cmd = host.run(
            'RESTIC_PASSWORD="testpassword" restic -r /backup snapshots'
        )
    assert cmd.rc == 0
