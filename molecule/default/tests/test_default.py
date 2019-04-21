import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_firewalld_disabled(host):
    service = host.service("firewalld")

    assert not service.is_enabled
    assert not service.is_running
