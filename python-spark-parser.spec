Name:		python-spark-parser
Version:	1.9.0
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/s/spark-parser/spark_parser-%{version}.tar.gz
Summary:	An Earley-Algorithm Context-free grammar Parser Toolkit
URL:		https://pypi.org/project/spark-parser/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(click)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildArch:	noarch

%description
An Earley-Algorithm Context-free grammar Parser Toolkit

%prep
%autosetup -p1 -n spark_parser-%{version}
# py-modules lists a top-level example.py that the sdist does not ship.
python - << 'PY'
from pathlib import Path
p = Path("pyproject.toml")
text = p.read_text()
old = "py-modules = [\n    \"example\",\n]\n"
if old not in text:
    raise SystemExit("py-modules block missing")
p.write_text(text.replace(old, "", 1))
PY

%build
%py_build

%install
%py_install

%files
%{_bindir}/spark-parser-coverage
%{py_sitedir}/spark_parser
%{py_sitedir}/spark_parser-*.*-info
