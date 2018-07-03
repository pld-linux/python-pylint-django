#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	pylint-django
Summary:	Pylint plugin for hangling Django code
# Name must match the python module/package name (as in 'import' statement)
Name:		python-%{module}
Version:	0.7.1
Release:	4
License:	GPL v2
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/p/pylint-django/%{module}-%{version}.tar.gz
# Source0-md5:	4e170e1276bb00ad4996f24daae1786e
URL:		https://github.com/landscapeio/pylint-django
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%{?with_tests:BuildRequires:	python-pylint-plugin-utils}
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%{?with_tests:BuildRequires:	python3-pylint-plugin-utils}
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pylint-django is a Pylint plugin to aid Pylint in recognising and
understandingerrors caused when using the Django framework.

%package -n python3-%{module}
Summary:	Pylint plugin for hangling Django code
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
pylint-django is a Pylint plugin to aid Pylint in recognising and
understandingerrors caused when using the Django framework.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/pylint_django
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/pylint_django-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/pylint_django
%{py3_sitescriptdir}/pylint_django-%{version}-py*.egg-info
%endif
