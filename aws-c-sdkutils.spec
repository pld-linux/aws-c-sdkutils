#
# Conditional build:
%bcond_without	tests		# unit tests
#
Summary:	AWS C SDKUTILS library
Summary(pl.UTF-8):	Biblioteka AWS C SDKUTILS
Name:		aws-c-sdkutils
Version:	0.2.4
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/awslabs/aws-c-sdkutils/releases
Source0:	https://github.com/awslabs/aws-c-sdkutils/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	067e81c3b5206b38e2947fe24a58c44f
URL:		https://github.com/awslabs/aws-c-sdkutils
BuildRequires:	aws-c-common-devel
BuildRequires:	cmake >= 3.9
BuildRequires:	gcc >= 5:3.2
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C99 library implementing AWS SDK specific utilities. Includes
utilities for ARN parsing, reading AWS profiles, etc...

%description -l pl.UTF-8
Biblioteka C99 z implementacją narzędzi specyficznych dla AWS SDK.
Zawiera narzędzia do analizy ARN, odczytu profili AWS itp.

%package devel
Summary:	Header files for AWS C SDKUTILS library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AWS C SDKUTILS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	aws-c-common-devel

%description devel
Header files for AWS C SDKUTILS library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AWS C SDKUTILS.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%if %{with tests}
%{__make} test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NOTICE README.md
%attr(755,root,root) %{_libdir}/libaws-c-sdkutils.so.1.0.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libaws-c-sdkutils.so
%{_includedir}/aws/sdkutils
%{_libdir}/cmake/aws-c-sdkutils
