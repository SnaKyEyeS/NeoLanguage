#!/bin/bash -v

# Options
#  -o: specify output path for data
while getopts o: flag
do
    case "${flag}" in
        o) output_path=${OPTARG};;
    esac
done

# Save current dir
current_path=$(pwd)

# Move into $path
if [ -z ${output_path+x} ];
    then output_path=.;
fi
cd $output_path

# Get training data
wget -nc https://object.pouta.csc.fi/OPUS-MultiUN/v1/moses/en-fr.txt.zip            -O multiun-en-fr.txt.zip
wget -nc https://object.pouta.csc.fi/OPUS-EUbookshop/v2/moses/en-fr.txt.zip         -O eubookshop-en-fr.txt.zip
wget -nv https://object.pouta.csc.fi/OPUS-DGT/v2019/moses/en-fr.txt.zip             -O dgt-en-fr.txt.zip
wget -nc https://object.pouta.csc.fi/OPUS-OpenSubtitles/v2018/moses/en-fr.txt.zip   -O opensubtitles-en-fr.txt.zip
wget -nc https://object.pouta.csc.fi/OPUS-Wikipedia/v1.0/moses/en-fr.txt.zip        -O wikipedia-en-fr.txt.zip
wget -nc https://object.pouta.csc.fi/OPUS-TED2013/v1.1/moses/en-fr.txt.zip          -O ted2013-en-fr.txt.zip
wget -nc https://object.pouta.csc.fi/OPUS-EMEA/v3/moses/en-fr.txt.zip               -O emea-en-fr.txt.zip
wget -nc https://object.pouta.csc.fi/OPUS-ECB/v1/moses/en-fr.txt.zip                -O ecb-en-fr.txt.zip
wget -nc https://object.pouta.csc.fi/OPUS-Books/v1/moses/en-fr.txt.zip              -O books-en-fr.txt.zip

# Extract data
unzip -o multiun-en-fr.txt.zip
unzip -o eubookshop-en-fr.txt.zip
unzip -o dgt-en-fr.txt.zip
unzip -o opensubtitles-en-fr.txt.zip
unzip -o wikipedia-en-fr.txt.zip
unzip -o ted2013-en-fr.txt.zip
unzip -o emea-en-fr.txt.zip
unzip -o ecb-en-fr.txt.zip
unzip -o books-en-fr.txt.zip

# Rename files
mv Books.en-fr.fr           Books.fr
mv DGT.en-fr.fr             DGT.fr
mv ECB.en-fr.fr             ECB.fr
mv EMEA.en-fr.fr            EMEA.fr
mv EUbookshop.en-fr.fr      EUbookshop.fr
mv MultiUN.en-fr.fr         MultiUN.fr
mv OpenSubtitles.en-fr.fr   OpenSubtitles.fr
mv TED2013.en-fr.fr         TED2013.fr
mv Wikipedia.en-fr.fr       Wikipedia.fr

# Keep only the .fr files
find . -type f ! -name '*.fr' -delete

# Create corpus file & remove other files
cat Books.fr DGT.fr ECB.fr EMEA.fr EUbookshop.fr MultiUN.fr OpenSubtitles.fr TED2013.fr Wikipedia.fr > corpus-ordered.fr
rm  Books.fr DGT.fr ECB.fr EMEA.fr EUbookshop.fr MultiUN.fr OpenSubtitles.fr TED2013.fr Wikipedia.fr

# Shuffle
shuf corpus-ordered.fr > corpus-shuffled.fr
rm   corpus-ordered.fr

# Prepare data (translate to neo & clean empty/long sentences)
$current_path/../venv/bin/python $current_path/../prep.py $output_path
perl $current_path/clean-corpus.perl corpus-prep fr neo corpus-clean 1 80

# Make data splits
head -n -4000 corpus-clean.fr     > corpus.fr
head -n -4000 corpus-clean.neo    > corpus.neo

tail -n 4000  corpus-clean.fr     > corpus-dev-test.fr
tail -n 4000  corpus-clean.neo    > corpus-dev-test.neo

head -n 2000  corpus-dev-test.fr  > corpus-dev.fr
head -n 2000  corpus-dev-test.neo > corpus-dev.neo
tail -n 2000  corpus-dev-test.fr  > corpus-test.fr
tail -n 2000  corpus-dev-test.neo > corpus-test.neo
