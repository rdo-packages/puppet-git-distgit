%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-git
%global commit 4e4498e3db218cefc27e40b7eb4e442177ccab28
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-git
Version:        0.4.0
Release:        3%{?alphatag}%{?dist}
Summary:        Module for installing Git or Gitosis.
License:        ASL 2.0

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
* Thu Feb 09 2017 Alfredo Moralejo <amoralej@redhat.com> 0.4.0-3.4e4498egit
- Ocata update 0.4.0 (4e4498e3db218cefc27e40b7eb4e442177ccab28)

