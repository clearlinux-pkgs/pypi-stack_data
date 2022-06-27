#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-stack_data
Version  : 0.3.0
Release  : 5
URL      : https://files.pythonhosted.org/packages/b9/90/9a4f8d32db76d39484f6d6f8b366b0c549767ff3e9d5ae6161caec226d06/stack_data-0.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b9/90/9a4f8d32db76d39484f6d6f8b366b0c549767ff3e9d5ae6161caec226d06/stack_data-0.3.0.tar.gz
Summary  : Extract data from python stack frames and tracebacks for informative displays
Group    : Development/Tools
License  : MIT
Requires: pypi-stack_data-license = %{version}-%{release}
Requires: pypi-stack_data-python = %{version}-%{release}
Requires: pypi-stack_data-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(asttokens)
BuildRequires : pypi(executing)
BuildRequires : pypi(pure_eval)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
# stack_data
[![Tests](https://github.com/alexmojaki/stack_data/actions/workflows/pytest.yml/badge.svg)](https://github.com/alexmojaki/stack_data/actions/workflows/pytest.yml) [![Coverage Status](https://coveralls.io/repos/github/alexmojaki/stack_data/badge.svg?branch=master)](https://coveralls.io/github/alexmojaki/stack_data?branch=master) [![Supports Python versions 3.5+](https://img.shields.io/pypi/pyversions/stack_data.svg)](https://pypi.python.org/pypi/stack_data)

%package license
Summary: license components for the pypi-stack_data package.
Group: Default

%description license
license components for the pypi-stack_data package.


%package python
Summary: python components for the pypi-stack_data package.
Group: Default
Requires: pypi-stack_data-python3 = %{version}-%{release}

%description python
python components for the pypi-stack_data package.


%package python3
Summary: python3 components for the pypi-stack_data package.
Group: Default
Requires: python3-core
Provides: pypi(stack_data)
Requires: pypi(asttokens)
Requires: pypi(executing)
Requires: pypi(pure_eval)

%description python3
python3 components for the pypi-stack_data package.


%prep
%setup -q -n stack_data-0.3.0
cd %{_builddir}/stack_data-0.3.0
pushd ..
cp -a stack_data-0.3.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656369504
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-stack_data
cp %{_builddir}/stack_data-0.3.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-stack_data/44c582803d7005baacb1ad03bcc5ad393cbdd95f
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-stack_data/44c582803d7005baacb1ad03bcc5ad393cbdd95f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
