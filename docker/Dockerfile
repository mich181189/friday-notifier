FROM fedora:37

RUN dnf update -y && dnf install -y python3-twilio && dnf clean all

COPY friday-notifier /friday-notifier
COPY friday-notifier.conf /etc/friday-notifier.conf

CMD /usr/bin/python3 /friday-notifier
