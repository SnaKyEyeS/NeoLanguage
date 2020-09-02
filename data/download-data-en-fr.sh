#!/bin/bash -v

# Options
#  -o: specify output path for data
while getopts o: flag
do
    case "${flag}" in
        o) path=${OPTARG};;
    esac
done

# Get training data
wget -nc https://object.pouta.csc.fi/OPUS-ParaCrawl/v5/moses/en-fr.txt.zip          -O $path/paracrawl-en-fr.txt.zip
wget -nc https://object.pouta.csc.fi/OPUS-UNPC/v1.0/moses/en-fr.txt.zip             -O $path/unpc-en-fr.txt.zip
wget -nc https://object.pouta.csc.fi/OPUS-giga-fren/v2/moses/en-fr.txt.zip          -O $path/giga-fren-en-fr.txt.zip
wget -nc https://object.pouta.csc.fi/OPUS-EUbookshop/v2/moses/en-fr.txt.zip         -O $path/eubookshop-en-fr.txt.zip
wget -nc https://object.pouta.csc.fi/OPUS-MultiUN/v1/moses/en-fr.txt.zip            -O $path/multiun-en-fr.txt.zip
wget -nc https://object.pouta.csc.fi/OPUS-OpenSubtitles/v2018/moses/en-fr.txt.zip   -O $path/opensubtitles-en-fr.txt.zip

# Extract data
unzip -o $path/paracrawl-en-fr.txt.zip
unzip -o $path/unpc-en-fr.txt.zip
unzip -o $path/giga-fren-en-fr.txt.zip
unzip -o $path/eubookshop-en-fr.txt.zip
unzip -o $path/multiun-en-fr.txt.zip
unzip -o $path/opensubtitles-en-fr.txt.zip
