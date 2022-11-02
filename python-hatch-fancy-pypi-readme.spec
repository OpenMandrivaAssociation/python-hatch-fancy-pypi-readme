Name:		python-hatch-fancy-pypi-readme
Version:	22.8.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/h/hatch-fancy-pypi-readme/hatch_fancy_pypi_readme-%{version}.tar.gz
Summary:	Fancy PyPI READMEs with Hatch
URL:		https://pypi.org/project/hatch-fancy-pypi-readme/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Fancy PyPI READMEs with Hatch

%prep
%autosetup -p1 -n hatch_fancy_pypi_readme-%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/hatch-fancy-pypi-readme
%{py_sitedir}/hatch_fancy_pypi_readme
%{py_sitedir}/hatch_fancy_pypi_readme-*.*-info
