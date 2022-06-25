import datetime
import random
import uuid
import json
import time

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
        self.customers: list = self._generate_customers(10000)
        self.products: dict  = self._generate_products(50)

    def _generate_customers(self, quantity: int) -> list:
        #
        # generate random customers who is buy the product in real-world.
        # in order to form an even age group, it is recommended that the quanti-
        # ty of customers be 10,000 or more.
        # 
        return [
            {
                "id": str(uuid.uuid4()), # random unique identity of customer
                "birthday": self._random_birthday(), # random birthday
                "gender": random.choice(['M','F']) # random gender M or F
            }
            for _ in range(quantity)
        ]

    def _random_birthday(self) -> datetime.datetime:
        # 
        # generate random birthday of 20 ~ 70 years-old based on now.
        #
        # make a random year of birth
        birth_year = datetime.datetime.now().year - random.randint(20,70)
        #
        # make a random day of birth in that year
        birthday = datetime.datetime(birth_year,1,1) \
                    + datetime.timedelta(days=random.randint(1,365))
        #
        # return type of birthday is datetime.datetime
        return birthday

    def _generate_products(self, quantity: int) -> dict:
        #
        # generate random products that contains unique identity and prices.
        #
        products = dict()
        for category,attr in CATEGORIES.items():
            #
            # gengerate random unique identity of products in category.
            identities = [ str(uuid.uuid4()) for _ in range(quantity) ]
            #
            # define price group of product.
            price_group_list = [ '~25', '25~50', '50~100', '100~200', '200~' ]
            #
            # pick up random price groups based on the price_weights of the cat-
            # egory.
            price_groups = random.choices(
                price_group_list, weights=attr['price_weights'], k=quantity)
            #
            # generate random prices within price_groups that is pick up above.
            prices = [
                { # it is python's switch-case statement, is not dictionary.
                    '~25'    : round(random.uniform(1,25), 2),
                    '25~50'  : round(random.uniform(25,50), 2),
                    '50~100' : round(random.uniform(50,100), 2),
                    '100~200': round(random.uniform(100,200), 2),
                    '200~'   : round(random.uniform(200,1000), 2),
                }.get(price_group, -1)
                for price_group in price_groups
            ]
            #
            # generate products that combine the generated informations.
            products[category] = [
                {
                    'id': identities[idx],
                    'price': prices[idx],
                    'priceUnit': 'dallor',
                    'category': category,
                }
                for idx in range(quantity)
            ]
        return products

    def generate_orders(self, quantity: int) -> list:
        #
        # generate orders that is information that is customers buying products.
        #
        # total quantity distribute to each categories based on defined weights.
        self._distribute_quantity_per_category(quantity)
        orders = list()
        for category,attr in CATEGORIES.items():
            #
            # generate invoice datetime based on defined season weights.
            invoice_datetime: list = self._generate_invoice_datetime(
                attr['quantity'], attr['season_weights'])
            # 
            # pick up random products within a category by a defined quantity.
            products = random.choices(
                self.products[category], k=attr['quantity'])
            #
            # define age groups.
            age_group_list = [ 20, 30, 40, 50 ]
            #
            # pick up random age group within a age group list.
            age_groups = random.choices(
                age_group_list, weights=attr['age_weights'], k=attr['quantity'])
            #
            # generate orders that combined generated information above.
            orders += [
                {
                    "id": str(uuid.uuid4()),
                    "invoiceDatetime": invoice_datetime[idx],
                    "product": products[idx],
                    "customer": self._get_customer(
                                    invoice_datetime[idx], age_groups[idx]),
                }
                for idx in range(attr['quantity'])
            ]
        # 
        # convert the customer birthday from datetime.datetime to string before 
        # orders return.
        return list(map(self._convert_birthday,orders))

    def _convert_birthday(self, order: dict) -> dict:
        #
        # convert the customer birthday from datetime.datetime to string.
        if type(order['customer']['birthday']) == datetime.datetime:
            order['customer']['birthday'] = order['customer']['birthday'].strftime("%m/%d/%Y")
        return order

    def _generate_invoice_datetime(self, quantity: int, season_weights: list) -> list:
        #
        # generate invoice datetime that is time of customer buy the product.
        now_year = datetime.datetime.now().year
        #
        # generate random year of occured invoice.
        invoice_years = [
            datetime.datetime(now_year - random.randint(1,5),1,1)
            for _ in range(quantity)
        ]
        #
        # define season of the invoice.
        # spring : Mar(3) ~ May(5)
        # summer : Jun(6) ~ Aug(8)
        # fall   : Sep(9) ~ Nov(11)
        # winter : Dec(12) ~ Feb(2)
        season_list = [ 'spring', 'summer', 'fall', 'winter' ]
        #
        # pick up seasons based on  defined weights.
        seasons: list = random.choices(
            season_list, weights=season_weights, k=quantity)
        #
        # make season days in year for timedelta.
        season_days = [
            {
                'spring': random.randint(60,151),
                'summer': random.randint(152,243),
                'fall'  : random.randint(244,334),
                'winter': random.choice([random.randint(0,59), random.randint(334,363)])
            }.get(season, -1)
            for season in seasons
        ]
        #
        # define period of the invoice.
        # dawn     : 00:00 ~ 08:00
        # morning  : 08:00 ~ 12:00
        # afternoon: 12:00 ~ 18:00
        # night    : 18:00 ~ 00:00
        period_list = [ 'dawn', 'morning', 'afternoon', 'night' ]
        #
        # define period weights.
        period_weights = [ 1, 3, 6, 10 ]
        #
        # pick up period based on defined period weights above.
        periods: list = random.choices(
            period_list, weights=period_weights, k=quantity)
        #
        # convert periods to period_seconds for timedelta.
        period_seconds = [
            {
                'dawn'     : random.randint(0,       3600*8-1),
                'morning'  : random.randint(3600*8 , 3600*12-1),
                'afternoon': random.randint(3600*12, 3600*18-1),
                'night'    : random.randint(3600*18, 3600*24-1),
            }.get(period, -1)
            for period in periods
        ]
        #
        # add season and period information to invoice_datetime
        # invoice datetime format is "mm/dd/yyyy HH:MM:SS T"
        return [
            datetime.datetime.strftime(
                invoice_year + datetime.timedelta(days=season_days[idx],seconds=period_seconds[idx]),
                "%m/%d/%Y %H:%M:%S"
            )
            for idx, invoice_year in enumerate(invoice_years)
        ]

    def _get_customer(self, invoice_datetime: str, age: int) -> dict:
        #
        # slicing year and month and day from invoice datetime
        invoice_datetime = datetime.datetime.strptime(invoice_datetime, 
                                                        "%m/%d/%Y %H:%M:%S")
        year  = invoice_datetime.year
        month = invoice_datetime.month
        day   = invoice_datetime.day
        delta = datetime.datetime(year,month,day) - datetime.datetime(year,1,1)
        #
        # define low limit and upper limit for birthday
        min_birthday = datetime.datetime(year-age,1,1) + delta
        max_birthday = datetime.datetime(year-age-10,1,1) + delta
        #
        # return random customer within defined range of birthday
        return random.choice([
            customer
            for customer in self.customers
                if customer['birthday'] < min_birthday
                and customer['birthday'] > max_birthday
        ])

    def _distribute_quantity_per_category(self, quantity: int):
        #
        # distribute quantity to each categories based on weights.
        # 
        category_list = [ k for k in CATEGORIES.keys() ]
        weights = [ v['quantity'] for v in CATEGORIES.values() ]
        q_categories = random.choices(category_list, weights=weights, k=quantity)
        for k in CATEGORIES.keys():
            CATEGORIES[k]['quantity'] = q_categories.count(k)

if __name__ == "__main__":
    dataGenerator = DataGenerator()
    orders = dataGenerator.generate_orders(10000)
    print(orders[0])