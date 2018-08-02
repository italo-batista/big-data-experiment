#!/BIN/BASH

rm -r ~/data/recsys;
mkdir ~/data/recsys;

for filename in ~/data/*.xz
do
    tar -xvf $filename -C ~/data/recsys;
done
