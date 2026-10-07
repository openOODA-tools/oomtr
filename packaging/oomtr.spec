Name:           oomtr
Version:        0.1.0
Release:        1%{?dist}
Summary:        Interactive continuous network diagnostics combining ping and traceroute.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oomtr
Source0:        oomtr-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oomtr is a sovereign, capability-bounded LIVE ROUTE TRACER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oomtr
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oomtr-uninstall

%files
/usr/bin/oomtr
/usr/bin/oomtr-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
