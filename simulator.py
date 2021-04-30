import requests
import json
import random
import sys

def random_order(data):
    order_list=[]
    picked = []
    n = len(data)
    
    rand_len = random.randint(1, n)
    
    for i in range(rand_len):
        rand_item_idx = random.randint(0, n-1)
        
        while rand_item_idx in picked:
            rand_item_idx = random.randint(0, n-1)
            
        picked.append(rand_item_idx)
        item = data[rand_item_idx]
        rand_amt = random.randint(1,3)
        
        order_list.append({"menu_id": item['id'], "amount": str(rand_amt), "item_name":item['name']})
    
    return (order_list)

def fulfill_orders(user_id):
    response = requests.post(f'http://127.0.0.1:5000/inventory?user_id={user_id}')
    print("ORDERS_FULFILLED: ", response.status_code)

if __name__ == '__main__':
    which = sys.argv[1]
    user_id = 'BQ93RVR6vrRS5baWd4LZra6rj103'

    if which == 'o':
        response = requests.get(f'http://127.0.0.1:5000/menu-item?user_id={user_id}')
        print(json.dumps(response.json(), indent=4))
        data = response.json()['data']
        order_list = random_order(data)
        order_data = {"payload": order_list}
        json_send = json.dumps(order_data)
        print(json_send)
        response2 = requests.post(f'http://127.0.0.1:5000/order?user_id={user_id}', data=json_send)
        print(json.dumps(response2.json(), indent=4))
    elif which == 'f':
        fulfill_orders(user_id)
