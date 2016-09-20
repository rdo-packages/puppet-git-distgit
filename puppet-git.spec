%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-git
%global commit 5e862242466de4ae654a5de5ef4c1bc4e4b9f92e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


%define upstream_name puppet-git
%global commit 5e862242466de4ae654a5de5ef4c1bc4e4b9f92e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-git
Version:        0.4.0
Release:        1%{?alphatag}%{?dist}
Summary:        Module for installing Git or Gitosis.
License:        Apache-2.0

URL:            https://github.com/puppetlabs/puppetlabs-git

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Module for installing Git or Gitosis.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/git/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/git/



%files
%{_datadir}/openstack-puppet/modules/git/


%changelog
* Tue Sep 20 2016 Haikel Guemar <hguemar@fedoraproject.org> - 0.4.0-1.5e86224.git
- Newton update 0.4.0 (5e862242466de4ae654a5de5ef4c1bc4e4b9f92e)


