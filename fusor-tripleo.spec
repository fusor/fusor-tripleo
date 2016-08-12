%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

Name:           fusor-tripleo
Version:        1.0.0
Release:        0%{?dist}
Summary:        fusor-ooo meta package

License:        GPL

Requires:       python-netifaces
Requires:       python-ipaddress
Requires:       python-tripleoclient
Requires:       %{?scl_prefix}rubygem-egon
Requires:       fusor-undercloud-release
Requires:       fusor-undercloud-installer
Requires:       fusor-undercloud-initial-setup
Requires:       redhat-access-insights

Requires:       puppet
Requires:       haproxy
Requires:       ipxe-bootimgs
Requires:       mariadb
Requires:       mariadb-devel
Requires:       mariadb-server
Requires:       memcached
Requires:       os-apply-config
Requires:       os-cloud-config
Requires:       os-collect-config
Requires:       os-net-config
Requires:       os-refresh-config
Requires:       tftp-server
Requires:       xinetd
Requires:       libxslt-devel
Requires:       gcc-c++
Requires:       automake
Requires:       tcpdump
Requires:       traceroute
Requires:       python-virtualenv
Requires:       docker-registry
Requires:       openwsman-python
Requires:       python-proliantutils
Requires:       rabbitmq-server
Requires:       mod_wsgi

Requires:       openstack-aodh-api
Requires:       openstack-aodh-common
Requires:       openstack-aodh-evaluator
Requires:       openstack-aodh-notifier
Requires:       openstack-aodh-listener
Requires:       openstack-ceilometer-alarm
Requires:       openstack-ceilometer-api
Requires:       openstack-ceilometer-central
Requires:       openstack-ceilometer-collector
Requires:       openstack-ceilometer-notification
Requires:       openstack-glance
Requires:       openstack-heat-api
Requires:       openstack-heat-api-cfn
Requires:       openstack-heat-api-cloudwatch
Requires:       openstack-heat-engine
Requires:       openstack-ironic-api
Requires:       openstack-ironic-conductor
Requires:       openstack-ironic-inspector
Requires:       openstack-keystone
Requires:       openstack-neutron
Requires:       openstack-neutron-ml2
Requires:       openstack-neutron-openvswitch
Requires:       openstack-nova-api
Requires:       openstack-nova-cert
Requires:       openstack-nova-common
Requires:       openstack-nova-compute
Requires:       openstack-nova-conductor
Requires:       openstack-nova-console
Requires:       openstack-nova-novncproxy
Requires:       openstack-nova-scheduler
Requires:       openstack-puppet-modules
Requires:       openstack-selinux
Requires:       openstack-swift
Requires:       openstack-swift-account
Requires:       openstack-swift-container
Requires:       openstack-swift-object
Requires:       openstack-swift-proxy
Requires:       openstack-tempest
Requires:       openstack-tripleo-api

Requires:       rhosp-director-images
Requires:       rhosp-director-images-ipa

BuildArch:      noarch

Provides:       qci-tripleo

%description
Meta-package to install all requirements for Fusor-TripleO/QCI-TripleO.

%prep

%build

%install

%files

%changelog
