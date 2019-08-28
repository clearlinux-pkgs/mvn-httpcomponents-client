#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-httpcomponents-client
Version  : 4.0.2
Release  : 10
URL      : https://github.com/apache/httpcomponents-client/archive/4.0.2.tar.gz
Source0  : https://github.com/apache/httpcomponents-client/archive/4.0.2.tar.gz
Source1  : https://repo.maven.apache.org/maven2/org/apache/httpcomponents/httpcomponents-client/4.5.6/httpcomponents-client-4.5.6.pom
Source2  : https://repo.maven.apache.org/maven2/org/apache/httpcomponents/httpmime/4.3.5/httpmime-4.3.5.jar
Source3  : https://repo.maven.apache.org/maven2/org/apache/httpcomponents/httpmime/4.3.5/httpmime-4.3.5.pom
Source4  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.0.2/httpclient-4.0.2.jar
Source5  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.0.2/httpclient-4.0.2.jar
Source6  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.0.2/httpclient-4.0.2.pom
Source7  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.0.2/httpclient-4.0.2.pom
Source8  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.2.1/httpclient-4.2.1.jar
Source9  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.2.1/httpclient-4.2.1.pom
Source10  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.2.3/httpclient-4.2.3.jar
Source11  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.2.3/httpclient-4.2.3.pom
Source12  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.3.5/httpclient-4.3.5.jar
Source13  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.3.5/httpclient-4.3.5.pom
Source14  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.4.1/httpclient-4.4.1.jar
Source15  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.4.1/httpclient-4.4.1.pom
Source16  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.5.2/httpclient-4.5.2.jar
Source17  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.5.2/httpclient-4.5.2.pom
Source18  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.5.6/httpclient-4.5.6.jar
Source19  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.5.6/httpclient-4.5.6.pom
Source20  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcomponents-client/4.0.2/httpcomponents-client-4.0.2.pom
Source21  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcomponents-client/4.2.1/httpcomponents-client-4.2.1.pom
Source22  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcomponents-client/4.2.3/httpcomponents-client-4.2.3.pom
Source23  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcomponents-client/4.3.5/httpcomponents-client-4.3.5.pom
Source24  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcomponents-client/4.4.1/httpcomponents-client-4.4.1.pom
Source25  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcomponents-client/4.5.2/httpcomponents-client-4.5.2.pom
Source26  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpmime/4.5.6/httpmime-4.5.6.jar
Source27  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpmime/4.5.6/httpmime-4.5.6.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-httpcomponents-client-data = %{version}-%{release}
Requires: mvn-httpcomponents-client-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
Apache HttpComponents Client
============================
Welcome to the HttpClient component of the Apache HttpComponents project.

%package data
Summary: data components for the mvn-httpcomponents-client package.
Group: Data

%description data
data components for the mvn-httpcomponents-client package.


%package license
Summary: license components for the mvn-httpcomponents-client package.
Group: Default

%description license
license components for the mvn-httpcomponents-client package.


%prep
%setup -q -n httpcomponents-client-4.0.2

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-httpcomponents-client
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-httpcomponents-client/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-client/4.5.6
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-client/4.5.6/httpcomponents-client-4.5.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpmime/4.3.5
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpmime/4.3.5/httpmime-4.3.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpmime/4.3.5
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpmime/4.3.5/httpmime-4.3.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.0.2
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.0.2/httpclient-4.0.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.0.2
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.0.2/httpclient-4.0.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.0.2
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.0.2/httpclient-4.0.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.0.2
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.0.2/httpclient-4.0.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.2.1
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.2.1/httpclient-4.2.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.2.1
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.2.1/httpclient-4.2.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.2.3
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.2.3/httpclient-4.2.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.2.3
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.2.3/httpclient-4.2.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.3.5
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.3.5/httpclient-4.3.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.3.5
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.3.5/httpclient-4.3.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.4.1
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.4.1/httpclient-4.4.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.4.1
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.4.1/httpclient-4.4.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.5.2
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.5.2/httpclient-4.5.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.5.2
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.5.2/httpclient-4.5.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.5.6
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.5.6/httpclient-4.5.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.5.6
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.5.6/httpclient-4.5.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-client/4.0.2
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-client/4.0.2/httpcomponents-client-4.0.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-client/4.2.1
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-client/4.2.1/httpcomponents-client-4.2.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-client/4.2.3
cp %{SOURCE22} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-client/4.2.3/httpcomponents-client-4.2.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-client/4.3.5
cp %{SOURCE23} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-client/4.3.5/httpcomponents-client-4.3.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-client/4.4.1
cp %{SOURCE24} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-client/4.4.1/httpcomponents-client-4.4.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-client/4.5.2
cp %{SOURCE25} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-client/4.5.2/httpcomponents-client-4.5.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpmime/4.5.6
cp %{SOURCE26} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpmime/4.5.6/httpmime-4.5.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpmime/4.5.6
cp %{SOURCE27} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpmime/4.5.6/httpmime-4.5.6.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.0.2/httpclient-4.0.2.jar
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.0.2/httpclient-4.0.2.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.2.1/httpclient-4.2.1.jar
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.2.1/httpclient-4.2.1.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.2.3/httpclient-4.2.3.jar
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.2.3/httpclient-4.2.3.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.3.5/httpclient-4.3.5.jar
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.3.5/httpclient-4.3.5.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.4.1/httpclient-4.4.1.jar
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.4.1/httpclient-4.4.1.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.5.2/httpclient-4.5.2.jar
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.5.2/httpclient-4.5.2.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.5.6/httpclient-4.5.6.jar
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpclient/4.5.6/httpclient-4.5.6.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-client/4.0.2/httpcomponents-client-4.0.2.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-client/4.2.1/httpcomponents-client-4.2.1.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-client/4.2.3/httpcomponents-client-4.2.3.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-client/4.3.5/httpcomponents-client-4.3.5.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-client/4.4.1/httpcomponents-client-4.4.1.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-client/4.5.2/httpcomponents-client-4.5.2.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-client/4.5.6/httpcomponents-client-4.5.6.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpmime/4.3.5/httpmime-4.3.5.jar
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpmime/4.3.5/httpmime-4.3.5.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpmime/4.5.6/httpmime-4.5.6.jar
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpmime/4.5.6/httpmime-4.5.6.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-httpcomponents-client/LICENSE.txt
