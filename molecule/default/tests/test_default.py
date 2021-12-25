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
    f = host.file('/opt/Python-3.9/bin/python3.9')
    assert f.exists
    assert f.user == 'python'
    assert f.group == 'python'

    assert '3.9.0' in host.check_output(
        '/opt/Python-3.9/bin/python3.9 --version')


def test_venv_python(host):
    f = host.file('/opt/venv-3.9/dev/bin/python3.9')
    assert f.exists
    assert f.user == 'python'
    assert f.group == 'python'

    assert '3.9.0' in host.check_output(
        '/opt/venv-3.9/dev/bin/python3.9 --version')


def test_ansible(host):
    res = host.run('/opt/*venv*/ansible/bin/ansible --version')

    assert res.rc == 0


def test_mercurial(host):
    res = host.run('/opt/*venv*/hg/bin/hg --version')

    assert res.rc == 0


def test_sphinx(host):
    res = host.run('/opt/*venv*/*/bin/sphinx-quickstart --version')

    assert res.rc == 0
