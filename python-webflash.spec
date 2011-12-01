%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define package WebFlash
%define alphaver a9

Name:           python-webflash
Version:        0.1
Release:        0.2.%{alphaver}%{?dist}
Summary:        Portable flash messages for WSGI apps

Group:          Development/Languages
License:        MIT
URL:            http://python-rum.org/wiki/WebFlash
Source0:        http://pypi.python.org/packages/source/W/%{package}/%{package}-%{version}%{alphaver}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel python-setuptools-devel
BuildRequires:  python-nose python-simplejson
BuildRequires:  python-coverage

Requires:       python-simplejson

%description
WebFlash is a library to display "flash" messages in python web applications.
These messages are usually used to provide feedback to the user (eg: you
changes have been saved, your credit card number has been stolen, ...). One
important characteristic they must provide is the ability to survive a redirect
(ie: display the message in a page after being redirected from a form
submission).

%prep
%setup -q -n %{package}-%{version}%{alphaver}

%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

%check
PYTHONPATH=$(pwd) nosetests

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%{python_sitelib}/*


%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.2.a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 21 2009 Luke Macken <lmacken@redhat.com> 0.1-0.1.a9
- Update to 0.1a9
- Add python-coverage to the BuildRequires

* Wed Jan 21 2009 Luke Macken <lmacken@redhat.com> 0.1-0.1.a8
- Initial package for Fedora
