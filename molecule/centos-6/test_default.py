import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_init_script_reload(host):
    cmd = host.run("/etc/init.d/consul reload")
    assert cmd.rc == 0
