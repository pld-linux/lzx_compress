Summary:	LZX compression package
Summary(pl.UTF-8):	Pakiet do kompresji LZX
Name:		lzx_compress
Version:	0
Release:	1
License:	GPL
Group:		Applications/Archiving
Source0:	http://www.speakeasy.org/~russotto/chm/%{name}.tar.gz
# Source0-md5:	bc0c2bb66f36b3753645c6a0a8e5ad75
URL:		http://www.speakeasy.org/~russotto/chm/lzx_compress.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An GPLed LZX compression engine, suitable for creating compressed CHM
files. Or for use in a CAB-making utility or for any other purpose LZX
is useful for.
 
%description -l pl.UTF-8
Silnik do kompresji LZX na licencji GPL, nadający się do tworzenia
skompresowanych plików CHM albo archiwów CAB, albo do czegokolwiek z
użyciem kompresji LZX.

%prep
%setup -q -n %{name}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -DLZ_ONEBUFFER -DLAZY"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_mandir}/man3}

install liblzxcomp.a $RPM_BUILD_ROOT%{_libdir}
install lzx_compress.h $RPM_BUILD_ROOT%{_includedir}
install lzx_compress.man3 $RPM_BUILD_ROOT%{_mandir}/man3/lzx_compress.3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%{_libdir}/liblzxcomp.a
%{_includedir}/lzx_compress.h
%{_mandir}/man3/lzx_compress.3*
