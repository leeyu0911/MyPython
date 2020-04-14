import appex as app
from objc_util import nsurl,UIApplication
import re

appurl = app.get_url()
print(appurl)
try:
	appid = re.search(r'[0-9]{10}', appurl)
	print(appid.group())
except:
	appid = re.search(r'[0-9]{9}', appurl)
	print(appid.group())

app = UIApplication.sharedApplication()
URL = 'pricetag://app?id=' + appid.group()
app.openURL_(nsurl(URL))
