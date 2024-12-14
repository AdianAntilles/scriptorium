#!/bin/env bash

elements=($(pwgen 12 12))
echo ${elements[@]}

python3.12 -c "import random; import sys; elements=sys.argv[1:]; print('Ausgewählt: ' + random.choice(elements))" "${elements[@]}"
