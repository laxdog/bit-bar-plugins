#!/usr/bin/env bash
# coding=utf-8
#
# <bitbar.title>GHS</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>laxdog</bitbar.author>
# <bitbar.author.github>laxdog</bitbar.author.github>
# <bitbar.desc>Displays GHS</bitbar.desc>
#
# by laxdog

out=$(ssh -i ~/.ssh/id_rsa_laxdog laxdog.duckdns.org -l dog "tail -n 1 stats/*| grep GHS | cut -f 12 -d ',' | cut -f 2 -d ' ' | cut -f 1 -d '.' | tr '\n' '#' | sed 's/#/℃ /g'")
num=$(echo $out | tr ' ' '\n' | wc -l | sed 's/\ *//' )
echo "[$num] $out"
