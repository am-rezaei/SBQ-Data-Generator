# importing the requests library
import requests
import random

# api-endpoint
baseUrl = "http://sbq.mycloudservice.ir:5000"


def send_data_to_service():
    print("Generating Random Data")
    for x in range(2):
        lat = "46.1" + str(random.randint(1000, 9999))
        for y in range(2):
            lng = "-74.5" + str(random.randint(1000, 9999))
            obj_type = 'object';
            value = random.randint(3, 20)
            if random.randint(0, 10) % 2 == 0:
                obj_type = 'magnetic';
                value = value / 20;
            result_obj = {
                "lat": lat,
                "lng": lng,
                "value": value,
                "type": obj_type
            };
            requests.post(url=baseUrl + "/add", json=result_obj);
            print(result_obj);


send_data_to_service()
