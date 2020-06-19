import pymongo

class SunhongchunDb():
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.book_weather = self.client['weather']
        self.sheet_weather = self.book_weather['sheet_weather_3']

    def save(self,data):
        self.sheet_weather.insert_one(data)

    def show_all(self):
        all=self.sheet_weather.find()
        for each in all:
            print(each)

    def find(self,condition):
        return self.sheet_weather.find()

    def delete(self):
        return self.sheet_weather.delete()


if __name__=="__main__":
    # client=pymongo.MongoClient('localhost',27017)
    # book_weather=client['weather']
    # sheet_weather=book_weather['sheet_weather_3']
    # print(sheet_weather)
    # sheet_weather.insert_one({"name":"sunhongchun","class":"net19049"})
    sunhongchunDb=SunhongchunDb()
    sunhongchunDb.save({"name":"sunhongchun","class":"net19049"})
    sunhongchunDb.show_all()