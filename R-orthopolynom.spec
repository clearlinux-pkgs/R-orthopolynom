#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-orthopolynom
Version  : 1.0.6.1
Release  : 13
URL      : https://cran.r-project.org/src/contrib/orthopolynom_1.0-6.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/orthopolynom_1.0-6.1.tar.gz
Summary  : Collection of Functions for Orthogonal and Orthonormal
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-polynom
BuildRequires : R-polynom
BuildRequires : buildreq-R

%description
polynomials and their recurrence relations. Additional
        functions are provided to calculate the derivative, integral,
        value and roots of lists of polynomial objects.

%prep
%setup -q -n orthopolynom
cd %{_builddir}/orthopolynom

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664809939

%install
export SOURCE_DATE_EPOCH=1664809939
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/orthopolynom/DESCRIPTION
/usr/lib64/R/library/orthopolynom/INDEX
/usr/lib64/R/library/orthopolynom/Meta/Rd.rds
/usr/lib64/R/library/orthopolynom/Meta/features.rds
/usr/lib64/R/library/orthopolynom/Meta/hsearch.rds
/usr/lib64/R/library/orthopolynom/Meta/links.rds
/usr/lib64/R/library/orthopolynom/Meta/nsInfo.rds
/usr/lib64/R/library/orthopolynom/Meta/package.rds
/usr/lib64/R/library/orthopolynom/NAMESPACE
/usr/lib64/R/library/orthopolynom/R/orthopolynom
/usr/lib64/R/library/orthopolynom/R/orthopolynom.rdb
/usr/lib64/R/library/orthopolynom/R/orthopolynom.rdx
/usr/lib64/R/library/orthopolynom/help/AnIndex
/usr/lib64/R/library/orthopolynom/help/aliases.rds
/usr/lib64/R/library/orthopolynom/help/orthopolynom.rdb
/usr/lib64/R/library/orthopolynom/help/orthopolynom.rdx
/usr/lib64/R/library/orthopolynom/help/paths.rds
/usr/lib64/R/library/orthopolynom/html/00Index.html
/usr/lib64/R/library/orthopolynom/html/R.css
