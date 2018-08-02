#!/BIN/BASH

cd ~

wget https://repo.continuum.io/archive/Anaconda2-4.2.0-Linux-x86_64.sh

bash Anaconda2-4.2.0-Linux-x86_64.sh -b -p ~/anaconda

rm Anaconda2-4.2.0-Linux-x86_64.sh

echo 'export PATH="~/anaconda/bin:$PATH"' >> ~/.bashrc 

source .bashrc

conda update conda
