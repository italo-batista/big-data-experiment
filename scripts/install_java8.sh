#!/BIN/BASH

#sudo apt-get update;

#sudo apt-get install openjdk-8-jdk;

echo $(java -version);

# Setup JAVA_HOME and JRE_HOME Variable
cat >>  /etc/environment <<EOL
JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"
JRE_HOME="/usr/lib/jvm/java-8-openjdk-amd64/jre"
EOL

source /etc/environment;

echo $JAVA_HOME;

