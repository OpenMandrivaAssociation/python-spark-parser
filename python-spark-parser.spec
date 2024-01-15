Name:		python-spark-parser
Version:	1.8.9
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/spark-parser/spark_parser-%{version}.tar.gz
Summary:	An Earley-Algorithm Context-free grammar Parser Toolkit
URL:		https://pypi.org/project/spark-parser/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
An Earley-Algorithm Context-free grammar Parser Toolkit

%prep
%autosetup -p1 -n spark_parser-%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/spark-parser-coverage
%{py_sitedir}/spark_parser
%{py_sitedir}/spark_parser-*.*-info
