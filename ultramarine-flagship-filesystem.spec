Name:           ultramarine-flagship-filesystem
Version:        0.1.0
Release:        1%{?dist}
Summary:        Assets for Ultramarine Linux Flagship

License:        MIT
URL:            https://ultramarine-linux.org
Source0:        10_ultramarine-budgie.gschema.override
Source1:        ultramarine-marina.layout

Requires:       budgie-desktop

%description

%install
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas/
install %{SOURCE0} %{buildroot}%{_datadir}/glib-2.0/schemas/

mkdir -p %{buildroot}%{_datadir}/budgie-desktop/layouts/
install %{SOURCE1} %{buildroot}%{_datadir}/budgie-desktop/layouts/
install %{SOURCE1} %{buildroot}%{_datadir}/budgie-desktop/panel.ini


%files
%{_datadir}/glib-2.0/schemas/10_ultramarine-budgie.gschema.override
%{_datadir}/budgie-desktop/layouts/ultramarine-marina.layout
%{_datadir}/budgie-desktop/panel.ini



%changelog
* Wed May 18 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- 
