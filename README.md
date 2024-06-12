# This project covers the following topics:

* Setting up a local kafka and zookeeper docker containers
* Setting up a producer job to imitate a stream of input records, generating and sending data to kafka topic every 3 seconds
* Setting up a consumer job that collects the data from topic and stores in Amazon s3 bucket
* Reading the files from S3 bucket using pyspark for processing
