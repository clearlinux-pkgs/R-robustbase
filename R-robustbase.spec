#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-robustbase
Version  : 0.93.0
Release  : 10
URL      : https://cran.r-project.org/src/contrib/robustbase_0.93-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/robustbase_0.93-0.tar.gz
Summary  : Basic Robust Statistics
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-robustbase-lib
Requires: R-DEoptimR
Requires: R-GGally
Requires: R-ggplot2
Requires: R-matrixStats
Requires: R-xtable
BuildRequires : R-DEoptimR
BuildRequires : R-GGally
BuildRequires : R-ggplot2
BuildRequires : R-matrixStats
BuildRequires : R-xtable
BuildRequires : clr-R-helpers

%description
Tools allowing to analyze data with robust methods.  This includes
 regression methodology including model selections and multivariate
 statistics where we strive to cover the book "Robust Statistics,
 Theory and Methods" by 'Maronna, Martin and Yohai'; Wiley 2006.

%package lib
Summary: lib components for the R-robustbase package.
Group: Libraries

%description lib
lib components for the R-robustbase package.


%prep
%setup -q -c -n robustbase

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1525294852

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1525294852
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library robustbase
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library robustbase
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library robustbase
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library robustbase|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/robustbase/CITATION
/usr/lib64/R/library/robustbase/Copyrights
/usr/lib64/R/library/robustbase/DESCRIPTION
/usr/lib64/R/library/robustbase/INDEX
/usr/lib64/R/library/robustbase/Meta/Rd.rds
/usr/lib64/R/library/robustbase/Meta/data.rds
/usr/lib64/R/library/robustbase/Meta/demo.rds
/usr/lib64/R/library/robustbase/Meta/features.rds
/usr/lib64/R/library/robustbase/Meta/hsearch.rds
/usr/lib64/R/library/robustbase/Meta/links.rds
/usr/lib64/R/library/robustbase/Meta/nsInfo.rds
/usr/lib64/R/library/robustbase/Meta/package.rds
/usr/lib64/R/library/robustbase/Meta/vignette.rds
/usr/lib64/R/library/robustbase/NAMESPACE
/usr/lib64/R/library/robustbase/NEWS.Rd
/usr/lib64/R/library/robustbase/R/robustbase
/usr/lib64/R/library/robustbase/R/robustbase.rdb
/usr/lib64/R/library/robustbase/R/robustbase.rdx
/usr/lib64/R/library/robustbase/data/Rdata.rdb
/usr/lib64/R/library/robustbase/data/Rdata.rds
/usr/lib64/R/library/robustbase/data/Rdata.rdx
/usr/lib64/R/library/robustbase/demo/determinMCD.R
/usr/lib64/R/library/robustbase/doc/aggr_results.Rdata
/usr/lib64/R/library/robustbase/doc/asymptotic.max.bias.Rdata
/usr/lib64/R/library/robustbase/doc/error.distributions.R
/usr/lib64/R/library/robustbase/doc/estimating.functions.R
/usr/lib64/R/library/robustbase/doc/fastMcd-kmini.R
/usr/lib64/R/library/robustbase/doc/fastMcd-kmini.Rnw
/usr/lib64/R/library/robustbase/doc/fastMcd-kmini.pdf
/usr/lib64/R/library/robustbase/doc/graphics.functions.R
/usr/lib64/R/library/robustbase/doc/index.html
/usr/lib64/R/library/robustbase/doc/lmrob_simulation.R
/usr/lib64/R/library/robustbase/doc/lmrob_simulation.Rnw
/usr/lib64/R/library/robustbase/doc/lmrob_simulation.pdf
/usr/lib64/R/library/robustbase/doc/psi_functions.R
/usr/lib64/R/library/robustbase/doc/psi_functions.Rnw
/usr/lib64/R/library/robustbase/doc/psi_functions.pdf
/usr/lib64/R/library/robustbase/doc/simulation.functions.R
/usr/lib64/R/library/robustbase/doc/simulation.init.R
/usr/lib64/R/library/robustbase/external/d1k27.rda
/usr/lib64/R/library/robustbase/help/AnIndex
/usr/lib64/R/library/robustbase/help/aliases.rds
/usr/lib64/R/library/robustbase/help/paths.rds
/usr/lib64/R/library/robustbase/help/robustbase.rdb
/usr/lib64/R/library/robustbase/help/robustbase.rdx
/usr/lib64/R/library/robustbase/html/00Index.html
/usr/lib64/R/library/robustbase/html/R.css
/usr/lib64/R/library/robustbase/include/robustbase.h
/usr/lib64/R/library/robustbase/libs/symbols.rds
/usr/lib64/R/library/robustbase/po/en@quot/LC_MESSAGES/R-robustbase.mo
/usr/lib64/R/library/robustbase/xtraR/ex-funs.R
/usr/lib64/R/library/robustbase/xtraR/lmrob-trace_lev.R
/usr/lib64/R/library/robustbase/xtraR/m-s_fns.R
/usr/lib64/R/library/robustbase/xtraR/mcnaive.R
/usr/lib64/R/library/robustbase/xtraR/plot-psiFun.R
/usr/lib64/R/library/robustbase/xtraR/subsample-fns.R
/usr/lib64/R/library/robustbase/xtraR/test_LTS.R
/usr/lib64/R/library/robustbase/xtraR/test_MCD.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/robustbase/libs/robustbase.so
/usr/lib64/R/library/robustbase/libs/robustbase.so.avx2
/usr/lib64/R/library/robustbase/libs/robustbase.so.avx512
