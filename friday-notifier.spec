Name:           friday-notifier
Version:        0.3
Release:        1%{?dist}
Summary:        Sends text messages using the Twilio SMS API on fridays

License:        WTFPL
URL:            http://michaelcullen.name
Source0:        friday-notifier
Source1:		cronfile
Source2:		config.json
Source3:		pylintrc

Requires:       python3
Requires:	python3-twilio
Requires(pre): shadow-utils
Requires: crontabs
BuildRequires:	python3-pylint

BuildArch: noarch

%description
Sends text messages every Friday to one or more numbers

%prep

%build

%check
cp %{SOURCE0} .
cp %{SOURCE3} .
pylint-3 friday-notifier

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_sysconfdir}/cron.d
install -m 755 %{SOURCE0} %{buildroot}%{_bindir}/friday-notifier
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/cron.d/friday-notifier
install -m 640 %{SOURCE2} %{buildroot}%{_sysconfdir}/friday-notifier.conf

%pre
getent group friday-notifier >/dev/null || groupadd -r friday-notifier
getent passwd friday-notifier >/dev/null || \
    useradd -r -g friday-notifier -d / -s /sbin/nologin \
    -c "Account for running friday-notifer cron job" friday-notifier

%files
%{_bindir}/friday-notifier
%config(noreplace) %{_sysconfdir}/cron.d/friday-notifier

%attr(640, root, friday-notifier) %config(noreplace) %{_sysconfdir}/friday-notifier.conf



%changelog
* Tue Oct 03 2017 Michael Cullen <michael@cullen-online.com> 0.3-1
- Added PyLint support to build
- Varied messages
* Sun Aug 27 2017 Michael Cullen <michael@cullen-online.com> 0.2-1
- Add support for API keys
- Add debug mode
* Sat Aug 26 2017 Michael Cullen <michael@cullen-online.com> 0.1-1
- Initial Package
