from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_files(host):
    present = [
        "/usr/local/bin/restic",
        "/etc/cron.d/restic-backblaze-example",
        "/etc/cron.d/restic-s3-example",
        "/var/lib/restic/passwd_backblaze-example",
        "/var/lib/restic/passwd_s3-example"
    ]
    if present:
        for file in present:
            f = host.file(file)
            assert f.exists
            assert f.is_file


def test_directories(host):
    present = [
        "/var/lib/restic",
        "/var/log/restic"
    ]
    if present:
        for directory in present:
            d = host.file(directory)
            assert d.is_directory
            assert d.exists
