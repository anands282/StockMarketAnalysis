import json
from kafka import KafkaConsumer
from json import loads
from s3fs import S3FileSystem


def consume():
    consumer = KafkaConsumer('stocks', bootstrap_servers=['localhost:9092'],
                             value_deserializer=lambda x: loads(x.decode('utf-8')))
    while True:
        s3_connection = S3FileSystem()
        for i, stock in enumerate(consumer):
            with s3_connection.open(f"s3://stock-market-project-store/stock_market_analysis_part{i}.json") as file:
                json.dump(stock.value, file)


if __name__ == "__main__":
    try:
        consume()
    except Exception as consumer_error:
        print("Error in running consumer process. ", consumer_error)