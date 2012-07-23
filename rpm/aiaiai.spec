# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.23
# 
# >> macros
# << macros

Name:       aiaiai
Summary:    Kernel patch validation scripts
Version:    0.0.20120718
Release:    1
Group:      Development/Tools/Other
License:    Intel Proprietary
URL:        http://git.infradead.org/users/dedekind/aiaiai.git
Source0:    %{name}-%{version}.tar.bz2
Source1:    tarball.sh
Source100:  aiaiai.yaml
Requires:   libshell


%description
Set of scripts for kernel patch testing/validation.




%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
#pushd external
make
#popd
# << build pre



# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
install -d %{buildroot}%{_bindir}
find external/* -executable -type f -exec install '{}' %{buildroot}%{_bindir}/ \;
find . -maxdepth 1 -executable -type f -exec install '{}' %{buildroot}%{_bindir}/ \;
install aiaiai-sh-functions %{buildroot}%{_bindir}/
# << install pre

# >> install post
# << install post






%files
%defattr(-,root,root,-)
# >> files
%{_bindir}/*
# << files

