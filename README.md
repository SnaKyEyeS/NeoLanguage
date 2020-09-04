# NeoLanguage

To annoy me, my friend Noé, when he was supposed to be studying (!!), transformed all the messages he sent me, passing them through 5 rules:
- Remove the first letter
- Reverse the letters
- Double the i's
- Invert the first two letters
- Remove the a's

This project is an attempt to create a "translator" to decrypt these messages.

## Requirements

#### Python
All the packages you will need are in the `requirements.txt` file. You can install them on your system or in a virtual environment using the `pip install -r requirements.txt` command.

This project comes with a small CLI to automatically encrypt/decrypt your messages. To explore this in more details, type `python3 cli.py --help`. \
I recommend creating a system alias to make a shortcut to this CLI (which you can add to your .bashrc ou .zshenv if you wish):
```
alias neo="/path/to/python3 /path/to/cli.py"

neo --help
neo write --help
neo read  --help
```

#### Marian
To decode the messages, we use Microsoft's Neural Machine Translator in C++, [marian](https://marian-nmt.github.io/). \
To run the decoder, you thus need to install Marian, then download the model and you are good to go !

###### Marian server

It is advised to run marian in "server mode" to avoid long loading times. To start the marian server, run:
```
./marian-server \
    --port 8080 \
    --config $folder_path/model/model.npz.best-cross-entropy.npz.decoder.yml \
    --beam-size 12 --normalize 1 \
    --mini-batch 64 --maxi-batch 10 \
    --maxi-batch-sort src
```

###### Translate a sentence
```
echo "t u upo u s 'ernîrtn ecv u texe ue u isi erss ns 'retu nse ? " | ./marian-decoder \
    --models $folder_path/model/model.npz \
    --vocabs $folder_path/model/vocab.neo.yml $folder_path/model/vocab.fr.yml
```

###### Train a new model
First, you need to generate a parallel corpus. To do so, a [script](/data/download.sh) is provided. Once the data is downloaded and translated/prepared, you can start the training by running:

```
./marian \
    --type amun \
    --model $folder_path/model/model.npz \
    --train-sets $folder_path/data/corpus.neo $folder_path/data/corpus.fr \
    --vocabs $folder_path/model/vocab.neo.yml $folder_path/model/vocab.fr.yml \
    --dim-vocabs 30000 30000 \
    --layer-normalization --dropout-rnn 0.2 --dropout-src 0.1 --dropout-trg 0.1 \
    --early-stopping 5 \
    --valid-freq 5000 --save-freq 5000 --disp-freq 1000 \
    --valid-sets $folder_path/data/corpus-dev.neo $folder_path/data/corpus-dev.fr \
    --valid-metrics cross-entropy \
    --log $folder_path/model/train.log --valid-log $folder_path/model/valid.log \
    --overwrite --keep-best \
    --seed 1111 --exponential-smoothing \
    --normalize=1 --beam-size=12 --quiet-translation
```
where you need to define a `folder_path` variable who points to the folder where you want to store the data and the models.
