%global pkg_name mojo-parent
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        32
Release:        4.9%{?dist}
Summary:        Codehaus MOJO parent project pom file

License:        ASL 2.0
URL:            http://mojo.codehaus.org/
Source0:        http://repo1.maven.org/maven2/org/codehaus/mojo/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix}codehaus-parent
BuildRequires:  %{?scl_prefix}maven-enforcer-plugin

%description
Codehaus MOJO parent project pom file

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
# Cobertura plugin is executed only during clean Maven phase.
%pom_remove_plugin :cobertura-maven-plugin
# wagon-webdav-jackrabbit is not available in Fedora
%pom_xpath_remove "pom:extension[pom:artifactId[text()='wagon-webdav-jackrabbit']]"

cp %SOURCE1 .
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_alias : org.codehaus.mojo:mojo
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE-2.0.txt

%changelog
* Thu Jan 15 2015 Michal Srb <msrb@redhat.com> - 32-4.9
- Fix directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 32-4.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 32-4.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 32-4.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 32-4.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 32-4.4
- Mass rebuild 2014-02-18

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 32-4.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 32-4.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 32-4.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 32-4
- Mass rebuild 2013-12-27

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
