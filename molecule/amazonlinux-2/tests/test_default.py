import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_init_script_reload(host):
    cmd = host.run("/etc/init.d/consul reload")
    assert cmd.succeeded


def test_init_script_stop(host):
    cmd = host.run("/etc/init.d/consul stop")
    assert cmd.succeeded


def test_init_script_start(host):
    cmd = host.run("/etc/init.d/consul start")
    assert cmd.succeeded
