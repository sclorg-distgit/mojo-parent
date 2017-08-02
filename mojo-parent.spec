%{?scl:%scl_package mojo-parent}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}mojo-parent
Version:        40
Release:        4.1%{?dist}
Summary:        Codehaus MOJO parent project pom file

License:        ASL 2.0
URL:            http://www.mojohaus.org/mojo-parent/
Source0:        https://github.com/mojohaus/mojo-parent/archive/%{pkg_name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}maven-local

%description
Codehaus MOJO parent project pom file

%prep
%setup -q -n %{pkg_name}-%{pkg_name}-%{version}
# Cobertura plugin is executed only during clean Maven phase.
%pom_remove_plugin :cobertura-maven-plugin
# Not needed in Fedora.
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-checkstyle-plugin

cp %SOURCE1 .

%build
%mvn_alias : org.codehaus.mojo:mojo
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 40-4.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Michael Simacek <msimacek@redhat.com> - 40-3
- Remove dependency on site-plugin and checkstyle-plugin

* Thu Aug 11 2016 Michael Simacek <msimacek@redhat.com> - 40-2
- Update upstream URLs

* Thu Aug 11 2016 Michael Simacek <msimacek@redhat.com> - 40-1
- Update to upstream version 40

* Mon Apr 11 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 39-1
- Update to upstream version 39

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 31 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 38-1
- Update to upstream version 38

* Fri Aug  7 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 37-2
- Remove maven-enforcer-plugin from POM

* Wed Aug  5 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 37-1
- Update to upstream version 37

* Thu Jul 23 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 36-1
- Update to upstream version 36

* Tue Jul 21 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 35-1
- Update to upstream version 35

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Michael Simacek <msimacek@redhat.com> - 34-2
- Add BR maven-site-plugin

* Mon Oct 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 34-1
- Update to upstream version 34

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 33-3
- Rebuild to regenerate Maven auto-requires

* Wed May 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 33-2
- Regenerate requires

* Mon Mar 10 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 33-1
- Update to upstream version 33

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 32-3
- Add ASL 2.0 license text to rpms

* Mon Apr 22 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 32-2
- Update to latest upstream (#948704)

* Fri Feb  8 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 31-1
- Update to upstream version 31

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 30-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 17 2013 Michal Srb <msrb@redhat.com> - 30-4
- Build with xmvn

* Fri Jan  4 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 30-3
- Disable maven-plugin-cobertura

* Tue Nov 27 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 30-2
- Install additional depmap
- Resolves: rhbz#880619

* Mon Jul 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 30-1
- Update to upstream version 30

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 7 2011 Alexander Kurtakov <akurtako@redhat.com> 29-1
- Update to latest upstream.

* Tue Mar  8 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 28-2
- Remove parent from pom.xml (no codehaus-parent in Fedora now)

* Mon Mar  7 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 28-1
- Update to latest upstream

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 16 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 24-5
- Add component-javadoc to R

* Thu Sep 16 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 24-4
- Add forgotten jpackage-utils BR

* Tue Sep 14 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 24-3
- Change to license used by upstream (ASL 2.0)

* Mon Sep  6 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 24-2
- Removed %%build section and BRs (not really needed)

* Mon Sep  6 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 24-1
- Initial version of the package
