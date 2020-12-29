import pyqrcode
from pyqrcode import QRCode

import wifi_qrcode_generator

nameWifi = 'dlink'
passWord = '123'
typeEncrypt = 'WPA'
image = wifi_qrcode_generator.wifi_qrcode(
	nameWifi, False, typeEncrypt, passWord
)
image.save('testwifi.png');

# data = 'tel:0349881392'
# data = 'smsto:0349881392:content sms here'
# data="https://www.facebook.com/nguyen.hoangsang.9085";
# big_code = pyqrcode.create(data)
# big_code.png('code.png', scale=8)