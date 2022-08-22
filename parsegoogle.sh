#!/bin/bash
cat websitegoogle.txt | sed -e 's|^[^/]*//||' -e 's|/.*$||' | sort -u > webgoogle.txt