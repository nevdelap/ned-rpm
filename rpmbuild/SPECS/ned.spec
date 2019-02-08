Name:           ned
Version:        1.2.8
Release:        1%{?dist}
Summary:        Like grep with replace, unlike sed, not only line oriented.

License:        GPLv3+
URL:            https://github.com/nevdelap/ned
Source0:        https://github.com/nevdelap/ned/archive/release.%{version}.tar.gz

BuildRequires:  rust

%description
For regular expression power users, ned is like grep,
but with powerful replace capabilities, and more powerful
than sed, as it isn't restricted to line oriented editing.

%prep
%setup -q -n %{name}-release.%{version}

%build
cargo build --release --locked

%check
cargo test --release --locked

%install
install -Dm755 target/release/ned %{buildroot}/usr/bin/ned
gzip < man/ned.1 > man/ned.1.gz
install -Dm 0644 man/ned.1.gz %{buildroot}/usr/share/man/man1/ned.1.gz

%files
%doc README.md LICENSE
/usr/bin/ned
/usr/share/man/man1/ned.1.gz

%changelog
* Sat Feb 9 2019 Nev Delap <nevdelap@gmail.com> 1.2.8-1
- Initial release.
