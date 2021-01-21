Name:           cross-aarch64-as
Version:        0.1+git1
Release:        1
Summary:        AS Hack
License:        BSD

Requires:  cross-aarch64-binutils

%description
Hack to make gcc find as during rust cross-builds

%prep

%build

%install
mkdir -p %{buildroot}/opt/cross/libexec/gcc/aarch64-meego-linux-gnueabi
cd %{buildroot}/opt/cross/libexec/gcc/aarch64-meego-linux-gnueabi
ln -s ../../../bin/aarch64-meego-linux-gnueabi-as as

%files
%defattr(-,root,root,-)
%exclude /opt/cross/libexec/gcc/aarch64-meego-linux-gnueabi/documentation.list
%dir /opt/cross/libexec/gcc/aarch64-meego-linux-gnueabi
/opt/cross/libexec/gcc/aarch64-meego-linux-gnueabi/as
