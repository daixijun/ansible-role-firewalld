Role Name
=========

[![Build Status](https://travis-ci.org/daixijun/ansible-role-firewalld.svg?branch=master)](https://travis-ci.org/daixijun/ansible-role-firewalld)

防火墙配置

Requirements
------------

* RHEL/CentOS >= 7.0
* firewalld >= 0.2.11

Role Variables
--------------

```yaml
firewalld_disabled: true  # 是否关闭firewalld, 默认为关闭状态
firewalld_rules: []       # 防火墙规则列表, 参考 ansible-doc firewalld
```

Dependencies
------------

None

Example Playbook
----------------

关闭firewalld

```yaml
- hosts: servers
  roles:
     - { role: daixijun.firewalld }
```

开启https服务

```yaml
- hosts: servers
  roles:
    - role: daixijun.firewalld
      firewalld_disabled: false
      firewalld_rules:
        - service: https
          permanent: true
          state: enabled
```

License
-------

BSD

Author Information
------------------

Xijun Dai <daixijun1990@gmail.com>
