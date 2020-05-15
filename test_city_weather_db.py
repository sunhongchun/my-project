import unttest

class TestCityWeatherDbCase(unittest.TestCase):

    def test_save(self):
        sunDb = SunDb()
        sunDb.save({"name": "sunhongchun", "class": "net19049"})
        sunDb.show_all()
        self.assertEqual(4,sunDb.find_all)


if __name__ =="__main__";
    unittest.main