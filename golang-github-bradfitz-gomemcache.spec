# Run tests in check section
%bcond_without check

%global goipath         github.com/bradfitz/gomemcache
%global oldgoipath      gopkg.in/bradfitz/gomemcache.v1
%global oldgoname       %gorpmname %{oldgoipath}
%global commit          bc664df9673713a0ccf26e3b55a673ec7301088b

%global common_description %{expand:
This is a memcache client library for the Go programming language.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Go Memcached client library
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%package -n compat-%{oldgoname}-devel
Summary:    %{summary}
BuildArch:  noarch
 
%description -n compat-%{oldgoname}-devel
%{common_description}
 
This package contains compatibility glue for code that still imports the
%{oldgoipath} Go namespace.


%prep
%forgeautosetup


%install
%goinstall

install -m 0755 -vd %{buildroot}%{gopath}/src/%(dirname %{oldgoipath})
ln -s %{gopath}/src/%{goipath} %{buildroot}%{gopath}/src/%{oldgoipath}


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%files -n compat-%{oldgoname}-devel
%dir %{gopath}/src/%(dirname %{oldgoipath})
%{gopath}/src/%{oldgoipath}


%changelog
* Tue Nov 13 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20181113gitbc664df
- Bump to commit bc664df9673713a0ccf26e3b55a673ec7301088b

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git1952afa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180321git1952afa
- Update to new Go packaging

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitr60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Apr 5 2016 Matthias Runge <mrunge@redhat.com> - 0.1git-28b053d
- initial package
