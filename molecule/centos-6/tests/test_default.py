import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_init_script_reload(host):
    host.run_expect(0, "/etc/init.d/consul reload")


def test_init_script_stop(host):
    host.run_expect(0, "/etc/init.d/consul stop")


def test_init_script_start(host):
    host.run_expect(0, "/etc/init.d/consul start")
