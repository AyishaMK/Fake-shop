# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from urllib.request import urlopen, Request
import json
import numpy
import statistics


class HTTPClient:
    fake_store_file = ""

    def read_webpage(self):
        req = Request(
            url='https://fakestoreapi.com/products',
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        self.fake_store_file = urlopen(req).read()
        return self.fake_store_file


class Store:
    def __init__(self, fake_store_file):
        self.fake_store_file = fake_store_file

    data = ""
    price_of_products = []
    description_of_products = []

    def extract_data(self):
        self.data = json.loads(self.fake_store_file.decode('utf-8'))
        for i in range(0, len(self.data)):
            self.price_of_products.append(self.data[i]['price'])

    def display_statistics(self):
        print("The statistics of the products of Fake Shop are as follows")
        mean_products = numpy.mean(self.price_of_products)
        round_mean_products = (round(float(mean_products), 2))
        print("Mean:" + str(round_mean_products))
        median_products = numpy.median(self.price_of_products)
        print("Median:" + str(median_products))
        mode_products = statistics.mode(self.price_of_products)
        print("Mode:" + str(mode_products))
        standard_deviation = numpy.std(self.price_of_products)
        round_standard_deviation = (round(float(standard_deviation), 2))
        print("Standard Deviation:" + str(round_standard_deviation))

    def display_frequency(self):
        resultant_description = " "
        for i in range(0, len(self.data)):
            self.description_of_products.append(self.data[i]['description'])

        resultant_description = resultant_description.join(self.description_of_products)
        split_it = resultant_description.split()
        for item in split_it:
            if item.isalpha() is not True:
                split_it.remove(item)

        uniques = []
        for word in split_it:
            if word not in uniques:
                uniques.append(word)

        counts = []
        for unique in uniques:
            count = 0
            for word in split_it:
                if word == unique:
                    count += 1
            counts.append((count, unique))

        counts.sort()
        counts.reverse()

        print("The 20 most frequently used words used in the description")
        for i in range(min(20, len(counts))):
            count, word = counts[i]
            # print('%s %d' % (word, count))
            print(word)


if __name__ == '__main__':
    httpClient = HTTPClient()
    file = httpClient.read_webpage()
    store = Store(file)
    store.extract_data()
    store.display_statistics()
    store.display_frequency()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
