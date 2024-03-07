#!/bin/bash
# Spell check dokumenta na srpskom

for f in $(find * -name '*.tex'); do 
aspell --lang=sr -t -c $f;
done
