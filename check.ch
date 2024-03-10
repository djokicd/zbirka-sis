#!/bin/bash
# Spell check dokumenta na srpskom
export ASPELL_CONF="dont-backup;"
for f in $(find * -name '*.tex'); do 
aspell --lang=sr -t -c $f;
done
