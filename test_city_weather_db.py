import unittest

class TestCityWeatherDbCase(unittest.TestCase):

    def test_save(self):
        sunhongchunDb = SunhongchunDb()
        sunhongchunDb.save({"name": "sunhongchun", "class": "net19049"})
        sunhongchunDb.show_all()
        results=sunhongchunDb.find({"name":"sunhongchun"})

        # self.assertEqual(4,sunDb.find_all())
        for each in results:
            self.assertEqual("sunhongchun",each['name'])
            self.assertEqual("net19049", each['class'])
            # print(each)
        sunhongchunDb.delete()
        def test_save_all(self):
            sunhongchun=Sunhongchun()
            codes=sunhongchun.get_city_code())
            for each in codes:
                print(next(codes))
            sunhongchun.get_weather("CN101010200")





if __name__ =="__main__":
    unittest.main()