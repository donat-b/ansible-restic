from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_files(host):
    present = [
        "/etc/cron.d/restic-example",
        "/usr/local/bin/restic",
        "/var/lib/restic/passwd_example"
    ]
    if present:
        for file in present:
            f = host.file(file)
            assert f.exists
            assert f.is_file


def test_directories(host):
    present = [
        "/var/lib/restic"
    ]
    if present:
        for directory in present:
            d = host.file(directory)
            assert d.is_directory
            assert d.exists
