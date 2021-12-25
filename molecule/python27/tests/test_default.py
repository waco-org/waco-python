import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_python3(host):
    assert '3' in host.check_output('/usr/bin/python3 --version')


def test_python2(host):
    assert '2' in host.check_output('/usr/bin/python2 --version 2>&1')


def test_source_python(host):
    f = host.file('/opt/Python-2.7/bin/python2.7')
    assert f.exists
    assert f.user == 'python'
    assert f.group == 'python'

    assert '2.7.18' in host.check_output(
        '/opt/Python-2.7/bin/python2.7 --version 2>&1')


def test_venv_python(host):
    f = host.file('/opt/venv-2.7/dev/bin/python2.7')
    assert f.exists
    assert f.user == 'python'
    assert f.group == 'python'

    assert '2.7.18' in host.check_output(
        '/opt/venv-2.7/dev/bin/python2.7 --version 2>&1')


def test_ansible(host):
    res = host.run('/opt/*venv*/ansible/bin/ansible --version')

    assert res.rc == 0


def test_mercurial(host):
    res = host.run('/opt/*venv*/hg/bin/hg --version')

    assert res.rc == 0


def test_sphinx(host):
    res = host.run('/opt/*venv*/*/bin/sphinx-quickstart --version')

    assert res.rc == 0
