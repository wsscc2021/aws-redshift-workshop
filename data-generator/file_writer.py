import json
from data_generator import DataGenerator

dataGenerator = DataGenerator()
n = 10
for i in range(1,n+1):
    orders = dataGenerator.generate_orders(10000)
    with open(f"output/data_{i:0>5}.json", "w") as file:
        for order in orders:
            file.write(json.dumps(order) + "\n")