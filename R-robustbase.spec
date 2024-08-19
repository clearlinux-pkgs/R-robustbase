#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v18
# autospec commit: f35655a
#
Name     : R-robustbase
Version  : 0.99.4
Release  : 71
URL      : https://cran.r-project.org/src/contrib/robustbase_0.99-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/robustbase_0.99-4.tar.gz
Summary  : Basic Robust Statistics
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-robustbase-lib = %{version}-%{release}
Requires: R-robustbase-license = %{version}-%{release}
Requires: R-DEoptimR
BuildRequires : R-DEoptimR
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Tools allowing to analyze data with robust methods.  This includes
 regression methodology including model selections and multivariate
 statistics where we strive to cover the book "Robust Statistics,
 Theory and Methods" by 'Maronna, Martin and Yohai'; Wiley 2006.

%package lib
Summary: lib components for the R-robustbase package.
Group: Libraries
Requires: R-robustbase-license = %{version}-%{release}

%description lib
lib components for the R-robustbase package.


%package license
Summary: license components for the R-robustbase package.
Group: Default

%description license
license components for the R-robustbase package.


%prep
%setup -q -n robustbase
pushd ..
cp -a robustbase buildavx2
popd
pushd ..
cp -a robustbase buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724077284

%install
export SOURCE_DATE_EPOCH=1724077284
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-robustbase
cp %{_builddir}/robustbase/inst/Copyrights %{buildroot}/usr/share/package-licenses/R-robustbase/a3b9c9fccbc9ea2dae228a0a603b79330dad23ec || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/robustbase/po/de/LC_MESSAGES/R-robustbase.mo
/usr/lib64/R/library/robustbase/po/de/LC_MESSAGES/robustbase.mo
/usr/lib64/R/library/robustbase/po/en@quot/LC_MESSAGES/R-robustbase.mo
/usr/lib64/R/library/robustbase/po/en@quot/LC_MESSAGES/robustbase.mo
/usr/lib64/R/library/robustbase/tests/LTS-specials.R
/usr/lib64/R/library/robustbase/tests/MCD-specials.R
/usr/lib64/R/library/robustbase/tests/MCD-specials.Rout.save
/usr/lib64/R/library/robustbase/tests/MT-tst.R
/usr/lib64/R/library/robustbase/tests/NAcoef.R
/usr/lib64/R/library/robustbase/tests/NAcoef.Rout.save
/usr/lib64/R/library/robustbase/tests/OGK-ex.R
/usr/lib64/R/library/robustbase/tests/OGK-ex.Rout.save
/usr/lib64/R/library/robustbase/tests/Qn-Sn-plots.R
/usr/lib64/R/library/robustbase/tests/Rsquared.R
/usr/lib64/R/library/robustbase/tests/Rsquared.Rout.save
/usr/lib64/R/library/robustbase/tests/binom-ni-small.R
/usr/lib64/R/library/robustbase/tests/binom-ni-small.Rout.save
/usr/lib64/R/library/robustbase/tests/binom-no-x.R
/usr/lib64/R/library/robustbase/tests/comedian-tst.R
/usr/lib64/R/library/robustbase/tests/exact-fit-categorical.R
/usr/lib64/R/library/robustbase/tests/glmrob-1.R
/usr/lib64/R/library/robustbase/tests/glmrob-specials.R
/usr/lib64/R/library/robustbase/tests/huber-etc.R
/usr/lib64/R/library/robustbase/tests/huber-etc.Rout.save
/usr/lib64/R/library/robustbase/tests/large-values.R
/usr/lib64/R/library/robustbase/tests/lmrob-data.R
/usr/lib64/R/library/robustbase/tests/lmrob-ex12.R
/usr/lib64/R/library/robustbase/tests/lmrob-methods.R
/usr/lib64/R/library/robustbase/tests/lmrob-methods.Rout.save
/usr/lib64/R/library/robustbase/tests/lmrob-psifns.R
/usr/lib64/R/library/robustbase/tests/lmrob-psifns.Rout.save
/usr/lib64/R/library/robustbase/tests/m-s-estimator.R
/usr/lib64/R/library/robustbase/tests/mc-etc.R
/usr/lib64/R/library/robustbase/tests/mc-strict.R
/usr/lib64/R/library/robustbase/tests/nlregrob-tst.R
/usr/lib64/R/library/robustbase/tests/nlrob-tst.R
/usr/lib64/R/library/robustbase/tests/poisson-ex.R
/usr/lib64/R/library/robustbase/tests/psi-rho-etc.R
/usr/lib64/R/library/robustbase/tests/psi-rho-etc.Rout.save
/usr/lib64/R/library/robustbase/tests/small-sample.R
/usr/lib64/R/library/robustbase/tests/small-sample.Rout.save
/usr/lib64/R/library/robustbase/tests/subsample.R
/usr/lib64/R/library/robustbase/tests/tlts.R
/usr/lib64/R/library/robustbase/tests/tlts.Rout.save
/usr/lib64/R/library/robustbase/tests/tmcd.R
/usr/lib64/R/library/robustbase/tests/weights.R
/usr/lib64/R/library/robustbase/tests/weights.Rout.save
/usr/lib64/R/library/robustbase/tests/wgt-himed-xtra.R
/usr/lib64/R/library/robustbase/tests/wgt-himed.R
/usr/lib64/R/library/robustbase/tests/wgt-himed.Rout.save
/usr/lib64/R/library/robustbase/xtraR/ex-funs.R
/usr/lib64/R/library/robustbase/xtraR/lmrob-trace_lev.R
/usr/lib64/R/library/robustbase/xtraR/m-s_fns.R
/usr/lib64/R/library/robustbase/xtraR/mcnaive.R
/usr/lib64/R/library/robustbase/xtraR/platform-sessionInfo.R
/usr/lib64/R/library/robustbase/xtraR/plot-psiFun.R
/usr/lib64/R/library/robustbase/xtraR/styleData.R
/usr/lib64/R/library/robustbase/xtraR/subsample-fns.R
/usr/lib64/R/library/robustbase/xtraR/test-tools.R
/usr/lib64/R/library/robustbase/xtraR/test_LTS.R
/usr/lib64/R/library/robustbase/xtraR/test_MCD.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/robustbase/libs/robustbase.so
/V4/usr/lib64/R/library/robustbase/libs/robustbase.so
/usr/lib64/R/library/robustbase/libs/robustbase.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-robustbase/a3b9c9fccbc9ea2dae228a0a603b79330dad23ec
