#!/bin/bash

python3 compile.py $1 | pandoc --to=html5 --css github.css --self-contained --metadata title="NOTES" -o tmp.html && firefox tmp.html
