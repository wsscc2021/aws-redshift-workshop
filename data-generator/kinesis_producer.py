import json
import boto3
import threading
import time
from data_generator import DataGenerator

kinesis_client = boto3.client('kinesis')

STREAM_NAME = "myStream"

dataGenerator = DataGenerator()

while True:
    # generate random order data
    orders = dataGenerator.generate_orders(10000)
    # make threading
    threads = [
        threading.Thread(
            target=kinesis_client.put_records,
            kwargs={
                'Records': [
                    {
                        'Data': json.dumps(order),
                        'PartitionKey': order['id'],
                    }
                    for order in orders[n:n+100]
                ],
                'StreamName': STREAM_NAME
            }
        )
        for n in range(0,10000,100) # 10,000 orders data split by 100 amounts.
    ]
    # start threading
    for thread in threads:
        thread.start()
    # wait threading
    while threading.active_count() > 1:
        time.sleep(0.1)
    # if all threading is done, print message
    print(f"successfully, 10,000 orders data push to '{STREAM_NAME}'")