%define		status		stable
%define		pearname	PHPUnit_Selenium
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Selenium RC integration for PHPUnit
Name:		php-phpunit-PHPUnit_Selenium
Version:	1.1.0
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	dc4834f7355fed5a067e04d5eb37d672
URL:		http://pear.phpunit.de/
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.9.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-channel(pear.phpunit.de)
Requires:	php-curl
Requires:	php-dom
Requires:	php-pear
Requires:	php-phpunit-PHPUnit >= 3.6.0
Requires:	php-reflection
Requires:	php-spl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Selenium RC integration for PHPUnit

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/PHPUnit/Extensions/SeleniumTestCase.php
%{php_pear_dir}/PHPUnit/Extensions/SeleniumTestCase
