import requests
import json
import random

def random_order(data):
   # print(data)
   order_list=[]
   for item in data:
        rand_num = random.randint(0, 1)
        if (rand_num == 1):
            rand_amt = random.randint(1,5)
            order_list.append({item['id']: str(rand_amt), "item_name":item['name']})
   return (order_list)

if __name__ == '__main__':
    user = {}
    user['id'] = 'kjhgvjklerlsjoife'
    response = requests.get('http://127.0.0.1:5000/menu-item', json=user)
    # data = json.load(response.json()['data'])
    data = response.json()['data']
    print(data)
    order_list = random_order(data)
    order_data = {"payload": order_list, "user_id": 'kjhgvjklerlsjoife'}
    json_send = json.dumps(order_data)
    print(json_send)
    response2 = requests.post('http://127.0.0.1:5000/order', data=json_send)
    print(response2)
