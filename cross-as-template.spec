Name:           cross-@ARCH@-as
Version:        1.0+git2
Release:        1
Summary:        AS Hack
License:        BSD

Source101: precheckin.sh
Requires:  cross-@ARCH@-binutils

%description
Hack to make gcc find as during rust cross-builds

%prep

%build

%install
mkdir -p %{buildroot}/opt/cross/libexec/gcc/@ARCH@-meego-linux-@ABI@
cd %{buildroot}/opt/cross/libexec/gcc/@ARCH@-meego-linux-@ABI@
ln -s ../../../bin/@ARCH@-meego-linux-@ABI@-as as

%files
%defattr(-,root,root,-)
%exclude /opt/cross/libexec/gcc/@ARCH@-meego-linux-@ABI@/documentation.list
%dir /opt/cross/libexec/gcc/@ARCH@-meego-linux-@ABI@
/opt/cross/libexec/gcc/@ARCH@-meego-linux-@ABI@/as
