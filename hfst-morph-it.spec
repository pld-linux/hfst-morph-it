Summary:	HFST morphological analysis transducer for Italian language
Summary(pl.UTF-8):	Automat HFST do analizy morfologicznej dla języka włoskiego
Name:		hfst-morph-it
# or 20110316?
Version:	0
Release:	1
License:	LGPL v2+ or CC-BY-SA v2.0
Group:		Applications/Text
# source is hfst-italian.tar.gz, but it doesn't contain scripts
Source0:	http://downloads.sourceforge.net/hfst/hfst-italian-installable.tar.gz
# Source0-md5:	aafdac9fcb7b79227dd3509baee6cec1
Patch0:		%{name}-DESTDIR.patch
URL:		http://hfst.sourceforge.net/
Requires:	hfst
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an Italian morphological transducer for HFST. It's based on
Morph-it! <http://sslmit.unibo.it/morphit/>.

%description -l pl.UTF-8
Ten pakiet zawiera automat dla HFST do analizy morfologicznej języka
włoskiego. Jest oparty na Morph-it! <http://sslmit.unibo.it/morphit/>.

%prep
%setup -q -n hfst-italian-installable
%patch -P0 -p1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/italian-analyze.sh
%attr(755,root,root) %{_bindir}/italian-generate.sh
%{_datadir}/hfst/it
