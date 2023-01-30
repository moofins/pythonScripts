#!/bin/bash

echo "" > enumMoofinsOut.log
echo "Starting first nmap scan..."
nmap $1 -v -sC -sV > enumMoofinsOut.log
cat enumMoofinsOut.log | grep -n PORT > $portGrep	#grab line numbers for PORT STATE VERSION line
$portSeparator=":"
