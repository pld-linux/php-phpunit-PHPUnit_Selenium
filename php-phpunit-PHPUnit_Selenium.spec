%include	/usr/lib/rpm/macros.php
%define		status		stable
%define		pearname	PHPUnit_Selenium
Summary:	%{pearname} - Selenium RC integration for PHPUnit
Name:		php-phpunit-PHPUnit_Selenium
Version:	1.0.2
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	1df5e1af44e5f54ae57c8a177ab5dadf
URL:		http://pear.phpunit.de/
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-channel(pear.phpunit.de)
Requires:	php-pear
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
%{php_pear_dir}/PHPUnit/Extensions/Story/SeleniumTestCase.php
