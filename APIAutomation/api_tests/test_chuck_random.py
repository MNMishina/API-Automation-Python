import requests


class Test_new_joke:

    # def __init__(self):
    #     pass

    # def test_create_new_random_joke(self):
    #     """ Creation of random joke"""
    #
    #     url = "https://api.chucknorris.io/jokes/random"
    #     print(url)
    #     result = requests.get(url)
    #     print(str(result.status_code))
    #     print(result.text)
    #     assert 200 == result.status_code
    #     print("Success")
    #     result.encoding = 'utf-8'  # important !
    #     check = result.json()
    #     check_info = check.get("categories")
    #     check_info_value = check.get("value")
    #     print(check_info)
    #     print(check_info_value)
    #     assert check_info == []
    #     assert check_info_value is not None

    def test_create_random_joke_by_category(self):
        """ Creation of random joke by category """

        category = "sport"
        url = "https://api.chucknorris.io/jokes/random?category=" + category
        print(url)
        result = requests.get(url)
        print(str(result.status_code))
        print(result.text)
        assert 200 == result.status_code
        print("Success")
        result.encoding = 'utf-8'  # important !
        check = result.json()
        check_info = check.get("categories")
        check_info_value = check.get("value")
        print(check_info)
        print(check_info_value)
        assert check_info == ["sport"]
        assert check_info_value is not None

    def test_category_not_found(self):
        category_1 = "spor"
        url_1 = "https://api.chucknorris.io/jokes/random?category=" + category_1
        print(url_1)
        result_1 = requests.get(url_1)
        print(str(result_1.status_code))
        print(result_1.text)
        assert 404 == result_1.status_code
        print("Not Found")
        result_1.encoding = 'utf-8'  # important !


# random_joke = Test_new_joke()
# random_joke.test_create_new_random_joke()

sport_joke = Test_new_joke()
sport_joke.test_category_not_found()
