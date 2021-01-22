Name:           cross-@ARCH@-as
Version:        1.0+git1
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
mkdir -p %{buildroot}/opt/cross/libexec/gcc/@ARCH@-meego-linux-gnueabi
cd %{buildroot}/opt/cross/libexec/gcc/@ARCH@-meego-linux-gnueabi
ln -s ../../../bin/@ARCH@-meego-linux-gnueabi-as as

%files
%defattr(-,root,root,-)
%exclude /opt/cross/libexec/gcc/@ARCH@-meego-linux-gnueabi/documentation.list
%dir /opt/cross/libexec/gcc/@ARCH@-meego-linux-gnueabi
/opt/cross/libexec/gcc/@ARCH@-meego-linux-gnueabi/as
