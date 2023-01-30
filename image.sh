#!/bin/bash

echo "Working on $1"
exiftool $1
binwalk $1
steghide extract -sf $1
