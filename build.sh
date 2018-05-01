#!/bin/bash
echo Compressing tar gzip
tar -c -f www/workshop.tar.gz -z sessions scripts data solutions
echo Compressing zip
zip -q -r www/workshop.zip sessions scripts data solutions
ls www/workshop.*