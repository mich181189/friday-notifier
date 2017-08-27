Name:           friday-notifier
Version:        0.2
Release:        1%{?dist}
Summary:        Sends text messages using the Twilio SMS API on fridays

License:        WTFPL
URL:            http://michaelcullen.name
Source0:        friday-notifier
Source1:	cronfile
Source2:	config.json

Requires:       python3
Requires:	python3-twilio
Requires(pre): shadow-utils
Requires: crontabs

BuildArch: noarch

%description
Sends text messages every Friday to one or more numbers

%prep


%build


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
* Sun Aug 27 2017 Michael Cullen <michael@cullen-online.com> 0.2-1
- Add support for API keys
- Add debug mode
* Sat Aug 26 2017 Michael Cullen <michael@cullen-online.com> 0.1-1
- Initial Package
