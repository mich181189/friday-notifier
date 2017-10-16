Name:           friday-notifier
Version:        0.4
Release:        1%{?dist}
Summary:        Sends text messages using the Twilio SMS API on fridays

License:        WTFPL
URL:            http://michaelcullen.name
Source0:        %{name}-%{version}.tar.gz

Requires:       python3
Requires:		%{py3_dist twilio}
Requires(pre): shadow-utils
Requires: crontabs
BuildRequires:	%{py3_dist pylint}

BuildArch: noarch

%description
Sends text messages every Friday to one or more numbers

%prep
%autosetup

%build
%py3_build

%check
pylint-3 friday-notifier

%install
mkdir -p %{buildroot}%{_sysconfdir}/cron.d

%py3_install

install -m 644 cronfile %{buildroot}%{_sysconfdir}/cron.d/friday-notifier
install -m 640 config.json %{buildroot}%{_sysconfdir}/friday-notifier.conf

%pre
getent group friday-notifier >/dev/null || groupadd -r friday-notifier
getent passwd friday-notifier >/dev/null || \
    useradd -r -g friday-notifier -d / -s /sbin/nologin \
    -c "Account for running friday-notifer cron job" friday-notifier

%files
%{_bindir}/friday-notifier
%{python3_sitelib}/friday_notifier*
%config(noreplace) %{_sysconfdir}/cron.d/friday-notifier

%attr(640, root, friday-notifier) %config(noreplace) %{_sysconfdir}/friday-notifier.conf



%changelog
* Sun Oct 15 2017 Michael Cullen <michael@cullen-online.com> 0.4-1
- switched to setup.py
* Tue Oct 03 2017 Michael Cullen <michael@cullen-online.com> 0.3-1
- Added PyLint support to build
- Varied messages
* Sun Aug 27 2017 Michael Cullen <michael@cullen-online.com> 0.2-1
- Add support for API keys
- Add debug mode
* Sat Aug 26 2017 Michael Cullen <michael@cullen-online.com> 0.1-1
- Initial Package
