import pandas as pd
from kafka import KafkaProducer
from json import dumps
import time

def produce():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x: dumps(x).encode('utf-8'))

    # Extracting data from our csv file and sending it to producer in loop
    df = pd.read_csv("data/all_stocks_5yr.csv")
    while True:
        stock_record = df.sample(1).to_dict(orient="records")[0]
        producer.send('stocks', value=stock_record)
        # wait for 30 seconds to send the next
        time.sleep(3)


if __name__ == "__main__":
    try:
        produce()
    except Exception as producer_error:
        print("Error in running producer process. ", producer_error)