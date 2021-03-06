%define		status		stable
%define		pearname	PHPUnit_Selenium
Summary:	%{pearname} - Selenium RC integration for PHPUnit
Name:		php-phpunit-PHPUnit_Selenium
Version:	1.3.3
Release:	3
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	33ee2caf975d6e657ee63f24d4224956
Patch0:		peardeps.patch
URL:		http://pear.phpunit.de/
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.9.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(curl)
Requires:	php(dom)
Requires:	php(reflection)
Requires:	php(spl)
Requires:	php-channel(pear.phpunit.de)
Requires:	php-pear
Requires:	phpunit >= 3.7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_pear ExitHandler.php

%description
Selenium RC integration for PHPUnit

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup
%patch0 -p1

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
%{php_pear_dir}/PHPUnit/Extensions/SeleniumTestSuite.php
%{php_pear_dir}/PHPUnit/Extensions/Selenium2TestCase.php
%{php_pear_dir}/PHPUnit/Extensions/Selenium2TestCase
%{php_pear_dir}/PHPUnit/Extensions/SeleniumBrowserSuite.php
%{php_pear_dir}/PHPUnit/Extensions/SeleniumCommon
