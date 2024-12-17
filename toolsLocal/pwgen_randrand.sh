#!/bin/env zsh

if [[ -n $1 ]]; then length=$1; else length=12; fi
if [[ -n $2 ]]; then elements=$2; else elements=12; fi

elements=($(pwgen $length $elements))
echo $elements[@] 

choice=$((RANDOM %${#elements[@]} +1 ))
echo "Ausgewählt: ${elements[$choice]}"
