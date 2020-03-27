#!/bin/bash

rsync -zvh friday-notifier docker/friday-notifier
rsync -zvh config.json docker/friday-notifier.conf

