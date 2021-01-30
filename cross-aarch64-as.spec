Name:           cross-aarch64-as
Version:        1.0+git2
Release:        1
Summary:        AS Hack
License:        BSD

Source101: precheckin.sh
Requires:  cross-aarch64-binutils

%description
Hack to make gcc find as during rust cross-builds

%prep

%build

%install
mkdir -p %{buildroot}/opt/cross/libexec/gcc/aarch64-meego-linux-gnu
cd %{buildroot}/opt/cross/libexec/gcc/aarch64-meego-linux-gnu
ln -s ../../../bin/aarch64-meego-linux-gnu-as as

%files
%defattr(-,root,root,-)
%exclude /opt/cross/libexec/gcc/aarch64-meego-linux-gnu/documentation.list
%dir /opt/cross/libexec/gcc/aarch64-meego-linux-gnu
/opt/cross/libexec/gcc/aarch64-meego-linux-gnu/as
