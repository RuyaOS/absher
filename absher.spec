%global pname absher
%global purl https://absher.sa
%global pver 0.1
%global prel 2
%global pasum منصة أبشر
%global pesum Absher Platform
%global plic GPLv3


Name: %{pname}
Version: %{pver}
Release: %{prel}%{?dist}
Summary: %{pesum}
Summary(ar): %{pasum}
License: %{plic}
URL: %{purl}
Source0: %{pname}
Source1: %{pname}.png
Source2: %{pname}.appdata.xml
Source3: %{pname}.desktop
Requires: webkit2gtk3
Buildarch: noarch

%description
%{pesum}

%description -l ar
%{pasum}

%prep
cp %{S:0} %{S:1} %{S:2} %{S:3} .
sed -i "s:/usr/share:%{_datadir}:g" %{name}

%install
#mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/appdata
mkdir -p %{buildroot}%{_datadir}/pixmaps

#cp -pr data %{buildroot}%{_datadir}/%{name}

#install -Dp -m 0644 index.html %{buildroot}%{_datadir}/%{name}
install -Dp -m 0755 %{name} %{buildroot}%{_bindir}
install -Dp -m 0755 %{name}.desktop %{buildroot}%{_datadir}/applications
install -Dp -m 0644 %{name}.appdata.xml %{buildroot}%{_datadir}/appdata
install -Dp -m 0644 %{name}.png %{buildroot}%{_datadir}/pixmaps



%files
#%{_datadir}/%{name}/*
#%{_datadir}/%{name}/index.html
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png


%changelog
* Fri Oct 7 2022 Mosaab Alzoubi <mosaab[AT]parmg[DOT]sa> - 0.1-2
- Enhance the comment

* Wed Oct 5 2022 Mosaab Alzoubi <mosaab[AT]parmg[DOT]sa> - 0.1-1
- Initial
