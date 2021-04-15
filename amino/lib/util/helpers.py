import json
import base64

from hashlib import sha1
from functools import reduce
from secrets import token_hex

def generate_device_info():
    hardwareInfo = token_hex(20).upper()
    magicode = 'E9AF2D7F431E87A4F8C7B6F45EFC04B7E5F0EA4F'
    final = sha1(bytes.fromhex('01' + hardwareInfo + magicode)).hexdigest()
    device_id = '01' + hardwareInfo + final

    return {
        "device_id": device_id,
        "device_id_sig": "Aa0ZDPOEgjt1EhyVYyZ5FgSZSqJt",
        "user_agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/beyond1qlteue-user 5; com.narvii.amino.master/3.4.33562)"
    }

# okok says: please use return annotations :(( https://www.python.org/dev/peps/pep-3107/#return-values

def decode_sid(sid: str) -> dict:
    return json.loads(base64.b64decode(reduce(lambda a, e: a.replace(*e), ("-+","_/"), sid + "=" * (-len(sid) % 4)).encode())[1:-20].decode())

def sid_to_uid(SID: str) -> str: return decode_sid(SID)["2"]

def sid_to_ip_address(SID: str) -> str: return decode_sid(SID)["4"]