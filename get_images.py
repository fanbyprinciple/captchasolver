import requests
import time

image_url0 = "https://www.indiannavy.nic.in/npo/image_captcha?sid=5764000&amp;ts=1621404450"
image_url1 = "https://www.indiannavy.nic.in/npo/image_captcha?sid=5765928&amp;ts=1621425112"
image_url2 = "https://www.indiannavy.nic.in/npo/image_captcha/5765937?sid=5765937&ts=1621425314"

#lets try downloading a 1000 images
for i in range(4000 -244):
    number = 5764928 + i +244
    ts_number = 1621424112 + i +244
    new_url = f"https://www.indiannavy.nic.in/npo/image_captcha?sid={number}&amp;ts={ts_number}"
    print(new_url)

    # delay
    time.sleep(5)

    r = requests.get(new_url)
    print(r)

    file_name = f"{i}.png"
    with open("saved/"+file_name, 'wb') as f:
        f.write(r.content)
