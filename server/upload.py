import sys
import requests

# curl -X PUT -F result=@test.png http://127.0.0.1:5000/test2


def upload(file_name, file_path, machine_id, url):
    upload_file = (file_name, open(file_path, 'rb'))
    payload = {'result': upload_file}
    r = requests.post(url + machine_id, files=payload)
    print r.text

if __name__ == "__main__":
    url = "http://127.0.0.1:5000/"
    machine = "TEST"
    file_path = "tests/test.zip"
    file_name = file_path.split("/").last()

    upload(file_name, file_path, machine, url)
