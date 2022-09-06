#!/bin/bash

find . -name '*.log' |  xargs grep -oHE 'execute time: +[0-9]+s' | awk -F'execute time: ' '{print $2 "\t" $1}' | sed 's/:$//g' | sort -h
