%define upstream_name puppetlabs-git

Name:           puppet-git
Version:        XXX
Release:        XXX
Summary:        Module for installing Git or Gitosis.
License:        Apache-2.0

URL:            https://github.com/puppetlabs/puppetlabs-git

Source0:        https://github.com/puppetlabs/puppetlabs-git/archive/%{version}.tar.gz

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

