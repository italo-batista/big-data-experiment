#!/BIN/BASH

# Download spark
wget http://www-us.apache.org/dist/spark/spark-2.3.1/spark-2.3.1-bin-hadoop2.7.tgz;

tar -xzf spark-2.3.1-bin-hadoop2.7.tgz;

rm spark-2.3.1-bin-hadoop2.7.tgz;

mv spark-2.3.1-bin-hadoop2.7 /opt/spark-2.3.1

# Create symbolic link
ln -s /opt/spark-2.3.1  /opt/spark;

# Set vars
cat >> ~/.bashrc <<EOL
export SPARK_HOME=/opt/spark
export PATH=$SPARK_HOME/bin:$PATH
EOL

pip install pyspark;
