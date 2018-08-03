# Set up Database
bash install_mongo.sh;

sudo apt-get install python-setuptools python-dev build-essential -y;
sudo easy_install pip;
pip install pymongo;

bash create_db.sh;


# Set up Spark (PySpark)

bash install_java8.sh;

bash install_spark.sh;
