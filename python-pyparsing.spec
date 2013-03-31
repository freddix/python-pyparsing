%define 	module	pyparsing

Summary:	pyparsing - a Python module for creating executing simple grammars
Name:		python-%{module}
Version:	1.5.7
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/pyparsing/%{module}-%{version}.tar.gz
# Source0-md5:	b610eee4da882f0c9d063eaf83dc8fbf
URL:		http://pyparsing.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The parsing module is an alternative approach to creating and
executing simple grammars, vs. the traditional lex/yacc approach, or
the use of regular expressions. The parsing module provides a library
of classes that client code uses to construct the grammar directly in
Python code.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{py_sitescriptdir}/pyparsing.py[co]

