#!/BIN/BASH

# Add Mong Repo
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927

# Install and verify
echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list

sudo apt-get update

sudo apt-get install -y mongodb-org

sudo mv files/mongodb.service /etc/systemd/system/

# Start services

sudo systemctl start mongodb

sudo systemctl status mongodb

sudo systemctl enable mongodb
