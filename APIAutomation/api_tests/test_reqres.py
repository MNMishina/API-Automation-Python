import requests


class Test_create_new_user:
    def test_create_user(self):
        base_url = "https://reqres.in"
        post_resource = "/api/users"
        post_url = base_url + post_resource
        print(post_url)

        json_for_create_user = {
            "name": "morpheus",
            "job": "leader"
        }
        result_post = requests.post(post_url, json=json_for_create_user)
        print(str(result_post.status_code))
        result_post.encoding = 'utf-8'
        print(result_post.text)

        assert 201 == result_post.status_code
        check = result_post.json()
        check_name = check.get("name")
        assert check_name == "morpheus"
        check_job = check.get("job")
        assert check_job == "leader"
        print("Success")

    def test_get_user(self):
        base_url = "https://reqres.in"
        get_resource = "/api/users/2"
        get_url = base_url + get_resource
        print(get_url)
        result = requests.get(get_url)
        print(str(result.status_code))
        print(result.text)

        assert 200 == result.status_code
        print("Success")
        result.encoding = 'utf-8'  # important !
        check = result.json()
        check_id = check.get("data").get("id")
        assert check_id == 2
        print("User's id is: " + str(check_id))

        check_email = check.get("data").get("email")
        assert check_email == "janet.weaver@reqres.in"
        print("User's email is: " + check_email)

        check_first_name = check.get("data").get("first_name")
        assert check_first_name == "Janet"
        print("User's first name is: " + check_first_name)

        check_last_name = check.get("data").get("last_name")
        assert check_last_name == "Weaver"
        print("User's last name is: " + check_last_name)

    def test_update_user(self):
        base_url = "https://reqres.in"
        put_resource = "/api/users/2"
        put_url = base_url + put_resource
        print(put_url)

        json_for_update_user = {
            "name": "morpheus",
            "job": "zion resident"
        }
        result_put = requests.put(put_url, json=json_for_update_user)
        print(str(result_put.status_code))
        result_put.encoding = 'utf-8'
        print(result_put.text)

        assert 200 == result_put.status_code
        check = result_put.json()
        check_name = check.get("name")
        assert check_name == "morpheus"
        check_job = check.get("job")
        assert check_job == "zion resident"
        print("Success")

    def test_delete_user(self):
        base_url = "https://reqres.in"
        delete_resource = "/api/users/2"
        delete_url = base_url + delete_resource
        print(delete_url)
        result = requests.delete(delete_url)
        print(str(result.status_code))

        assert 204 == result.status_code
        print("Success")
