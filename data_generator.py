import datetime
import random
import uuid
import json

CATEGORIES = {   # quantity, gender, ages  , season , quantity
    'T-shirts': {
        'quantity': 10,              # 1 ~ 10
        'price_weights': [60,30,5,4,1], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [1,1,1,1],    # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [1,1],     # [M, F]
        'season_weights': [1,1,1,1], # [spring, summer, fall, winter]
    },
    'shirts': {
        'quantity': 7,               # 1 ~ 10
        'price_weights': [10,30,40,10,5], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [1,1,1,1],    # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [80,20],   # [M, F]
        'season_weights': [1,1,1,1], # [spring, summer, fall, winter]
    },
    'hoodie': {
        'quantity': 7,                  # 1 ~ 10
        'price_weights': [10,30,40,10,5], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [35,35,15,15],   # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [1,1],        # [M, F]
        'season_weights': [15,5,60,20], # [spring, summer, fall, winter]
    },
    'sweater': {
        'quantity': 7,                  # 1 ~ 10
        'price_weights': [10,40,30,10,5], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [15,15,35,35],   # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [30,70],      # [M, F]
        'season_weights': [15,5,60,20], # [spring, summer, fall, winter]
    },
    'sweatshirts': {
        'quantity': 8,                  # 1 ~ 10
        'price_weights': [10,40,30,10,5], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [1,1,1,1],       # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [1,1],        # [M, F]
        'season_weights': [60,5,20,15], # [spring, summer, fall, winter]
    },
    'blouse': {
        'quantity': 3,                  # 1 ~ 10
        'price_weights': [5,40,30,15,5], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [40,40,10,10],   # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [0,1],        # [M, F]
        'season_weights': [60,5,20,15], # [spring, summer, fall, winter]
    },
    'raincoat': {
        'quantity': 1,                # 1 ~ 10
        'price_weights': [5,40,30,15,5], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [40,40,10,10], # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [70,30],    # [M, F]
        'season_weights': [5,85,5,5], # [spring, summer, fall, winter]
    },
    'suit': {
        'quantity': 2,                   # 1 ~ 10
        'price_weights': [0,5,5,30,60], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [40,40,10,10],    # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [70,30],       # [M, F]
        'season_weights': [60,10,20,10], # [spring, summer, fall, winter]
    },
    'dress': {
        'quantity': 2,                   # 1 ~ 10
        'price_weights': [0,5,5,30,60], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [40,40,10,10],    # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [0,1],         # [M, F]
        'season_weights': [60,10,20,10], # [spring, summer, fall, winter]
    },
    'sports wear': {
        'quantity': 6,                   # 1 ~ 10
        'price_weights': [5,15,15,60,5], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [15,15,35,35],    # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [1,1],         # [M, F]
        'season_weights': [1,1,1,1],     # [spring, summer, fall, winter]
    },
    'jean': {
        'quantity': 9,                  # 1 ~ 10
        'price_weights': [5,20,60,10,5], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [1,1,1,1],        # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [1,1],         # [M, F]
        'season_weights': [1,1,1,1],     # [spring, summer, fall, winter]
    },
    'short pants': {
        'quantity': 5,                 # 1 ~ 10
        'price_weights': [5,30,50,10,5], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [1,1,1,1],      # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [1,1],       # [M, F]
        'season_weights': [10,80,5,5], # [spring, summer, fall, winter]
    },
    'skirts': {
        'quantity': 3,                   # 1 ~ 10
        'price_weights': [5,30,50,10,5], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [40,40,10,10],    # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [0,1],         # [M, F]
        'season_weights': [40,20,30,10], # [spring, summer, fall, winter]
    },
    'padded jacket': {
        'quantity': 4,                 # 1 ~ 10
        'price_weights': [0,1,9,20,70], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [1,1,1,1],      # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [0,1],       # [M, F]
        'season_weights': [5,5,20,70], # [spring, summer, fall, winter]
    },
    'trench coat': {
        'quantity': 4,                 # 1 ~ 10
        'price_weights': [0,1,9,20,70], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [40,40,10,10],  # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [70,30],     # [M, F]
        'season_weights': [5,5,20,70], # [spring, summer, fall, winter]
    },
    'jacket': {
        'quantity': 4,                  # 1 ~ 10
        'price_weights': [0,1,9,60,30], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [1,1,1,1],       # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [1,1],        # [M, F]
        'season_weights': [30,5,30,25], # [spring, summer, fall, winter]
    },
    'boots': {
        'quantity': 2,                   # 1 ~ 10
        'price_weights': [0,10,25,60,5], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [40,40,10,10],    # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [0,1],         # [M, F]
        'season_weights': [25,10,25,40], # [spring, summer, fall, winter]
    },
    'heels': {
        'quantity': 2,                   # 1 ~ 10
        'price_weights': [0,10,25,60,5], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [40,40,10,10],    # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [0,1],         # [M, F]
        'season_weights': [25,40,25,10], # [spring, summer, fall, winter]
    },
    'shoes': {
        'quantity': 8,                  # 1 ~ 10
        'price_weights': [0,10,25,60,5], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [1,1,1,1],        # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [1,1],         # [M, F]
        'season_weights': [1,1,1,1],     # [spring, summer, fall, winter]
    },
    'hat': {
        'quantity': 3,                  # 1 ~ 10
        'price_weights': [5,25,60,15,5], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [1,1,1,1],        # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [1,1],         # [M, F]
        'season_weights': [1,1,1,1],     # [spring, summer, fall, winter]
    },
    'tie': {
        'quantity': 2,                   # 1 ~ 10
        'price_weights': [5,25,40,35,5], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [1,1,1,1],        # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [1,0],         # [M, F]
        'season_weights': [1,1,1,1],     # [spring, summer, fall, winter]
    },
    'socks': {
        'quantity': 10,                  # 1 ~ 10
        'price_weights': [60,20,10,10,0], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [1,1,1,1],        # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [1,1],         # [M, F]
        'season_weights': [1,1,1,1],     # [spring, summer, fall, winter]
    },
    'scarfs': {
        'quantity': 1,                  # 1 ~ 10
        'price_weights': [40,40,10,10,0], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [10,10,40,40],   # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [10,90],      # [M, F]
        'season_weights': [15,5,60,20], # [spring, summer, fall, winter]
    },
    'stocking': {
        'quantity': 4,                   # 1 ~ 10
        'price_weights': [60,20,10,10,0], # ~25, 25~50, 50~100, 100~200, 200~
        'age_weights': [40,40,10,10],    # [20-29, 30-39, 40-49, 50-59]
        'gender_weights': [0,1],         # [M, F]
        'season_weights': [30,10,30,30], # [spring, summer, fall, winter]
    },
}

class DataGenerator:

    def __init__(self):
        print("start")
        self.make_customers(10000)
        print("end of make_customers")
        self.make_products(50)
        print("end of make_products")
        self.make_orders(100)
        print("end of make_orders")

    def get_birthday(self, customer: dict) -> datetime.datetime:
        return datetime.datetime.strptime(customer['birthday'], "%m/%d/%Y")

    def distribute_quantity_per_category(self, quantity: int):
        category_list = [ k for k in CATEGORIES.keys() ]
        weights = [ v['quantity'] for v in CATEGORIES.values() ]
        random_categories = random.choices(category_list, weights=weights, k=quantity)
        for k in CATEGORIES.keys():
            CATEGORIES[k]['quantity'] = random_categories.count(k)

    def make_birthday(self) -> str:
        birth_year = datetime.datetime.now().year - random.randint(15,70)
        birthday = datetime.datetime(birth_year,1,1) + datetime.timedelta(days=random.randint(1,365))
        return datetime.datetime.strftime(birthday, "%m/%d/%Y")

    def make_customers(self, quantity: int) -> list:
        self.customers = [
            {
                "id": str( uuid.uuid4() ),
                "birthday": self.make_birthday(),
                "gender": random.choice(['M','F'])
            }
            for _ in range(quantity)
        ]

    def make_products(self, quantity: int) -> dict:
        result = dict()
        for category,attr in CATEGORIES.items():
            identity = [ str(uuid.uuid4()) for _ in range(quantity) ]
            price_list = [ '~25', '25~50', '50~100', '100~200', '200~' ]
            random_price = random.choices(price_list, weights=attr['price_weights'], k=quantity)
            price = [
                {
                    '~25'    : round(random.uniform(1,25), 2),
                    '25~50'  : round(random.uniform(25,50), 2),
                    '50~100' : round(random.uniform(50,100), 2),
                    '100~200': round(random.uniform(100,200), 2),
                    '200~'   : round(random.uniform(200,1000), 2),
                }.get(item, -1)
                for item in random_price
            ]
            result[category] = [
                {
                    'id': identity[idx],
                    'price': price[idx],
                    'priceUnit': 'dallor',
                    'category': category,
                }
                for idx in range(quantity)
            ]
        self.products = result

    def make_orders(self, quantity: int) -> list:
        self.distribute_quantity_per_category(quantity)
        result = list()
        for category,attr in CATEGORIES.items():
            # get invoice date time
            invoice_datetime: list = self.make_invoice_datetime(
                attr['quantity'], attr['season_weights'])
            # get product
            product: list = random.choices(self.products[category], k=attr['quantity'])
            # get age of customer
            age_list = [ 20, 30, 40, 50 ]
            age: list = random.choices(age_list, weights=attr['age_weights'], k=attr['quantity'])
            result += [
                {
                    "id": str(uuid.uuid4()),
                    "invoiceDatetime": invoice_datetime[idx],
                    "product": product[idx],
                    "customer": self.get_customer(invoice_datetime[idx], age[idx]),
                }
                for idx in range(attr['quantity'])
            ]
        self.orders = result

    def make_invoice_datetime(self, quantity: int, season_weights: list) -> list:
        #
        # The function make a invoice of ordered.
        now_year = datetime.datetime.now().year
        invoice_years = [
            datetime.datetime(now_year - random.randint(1,5),1,1)
            for _ in range(quantity)
        ]
        #
        # season
        # spring : Mar(3) ~ May(5)
        # summer : Jun(6) ~ Aug(8)
        # fall   : Sep(9) ~ Nov(11)
        # winter : Dec(12) ~ Feb(2)
        season_list = [ 'spring', 'summer', 'fall', 'winter' ]
        season: list = random.choices(season_list, weights=season_weights, k=quantity)
        season_days = [
            {
                'spring': random.randint(60,151),
                'summer': random.randint(152,243),
                'fall'  : random.randint(244,334),
                'winter': random.choice([random.randint(0,59), random.randint(334,363)])
            }.get(item, -1)
            for item in season
        ]
        #
        # period
        # dawn     : 00:00 ~ 08:00
        # morning  : 08:00 ~ 12:00
        # afternoon: 12:00 ~ 18:00
        # night    : 18:00 ~ 00:00
        period_list = [ 'dawn', 'morning', 'afternoon', 'night' ]
        period_weights = [ 1, 3, 6, 10 ]
        random_period: list = random.choices(period_list, weights=period_weights, k=quantity)
        period_seconds = [
            {
                'dawn'     : random.randint(0,       3600*8-1),
                'morning'  : random.randint(3600*8 , 3600*12-1),
                'afternoon': random.randint(3600*12, 3600*18-1),
                'night'    : random.randint(3600*18, 3600*24-1),
            }.get(item, -1)
            for item in random_period
        ]
        #
        # invoice datetime format is "mm/dd/yyyy HH:MM:SS T"
        return [
            datetime.datetime.strftime(
                invoice_year + datetime.timedelta(days=season_days[idx],seconds=period_seconds[idx]),
                "%m/%d/%Y %H:%M:%S"
            )
            for idx, invoice_year in enumerate(invoice_years)
        ]

    def get_customer(self, invoice_datetime: str, age: int) -> dict:
        # print(invoice_datetime, age)
        year  = datetime.datetime.strptime(invoice_datetime, "%m/%d/%Y %H:%M:%S").year
        month = datetime.datetime.strptime(invoice_datetime, "%m/%d/%Y %H:%M:%S").month
        day   = datetime.datetime.strptime(invoice_datetime, "%m/%d/%Y %H:%M:%S").day
        delta = datetime.datetime(year,month,day) - datetime.datetime(year,1,1)

        min_birthday = datetime.datetime(year-age,1,1) + delta
        max_birthday = datetime.datetime(year-age-10,1,1) + delta

        return random.choice([
            customer
            for customer in self.customers
                if datetime.datetime.strptime(customer['birthday'],"%m/%d/%Y")
                    < min_birthday
                and datetime.datetime.strptime(customer['birthday'],"%m/%d/%Y")
                    > max_birthday
        ])

if __name__ == "__main__":
    dataGenerator = DataGenerator()
    print(dataGenerator.orders[0])