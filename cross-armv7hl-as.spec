Name:           cross-armv7hl-as
Version:        0.1+git1
Release:        1
Summary:        AS Hack
License:        BSD

Requires:  cross-armv7hl-binutils

%description
Hack to make gcc find as during rust cross-builds

%prep

%build

%install
mkdir -p %{buildroot}/opt/cross/libexec/gcc/armv7hl-meego-linux-gnueabi
cd %{buildroot}/opt/cross/libexec/gcc/armv7hl-meego-linux-gnueabi
ln -s ../../../bin/armv7hl-meego-linux-gnueabi-as as

%files
%defattr(-,root,root,-)
%exclude /opt/cross/libexec/gcc/armv7hl-meego-linux-gnueabi/documentation.list
%dir /opt/cross/libexec/gcc/armv7hl-meego-linux-gnueabi
/opt/cross/libexec/gcc/armv7hl-meego-linux-gnueabi/as
