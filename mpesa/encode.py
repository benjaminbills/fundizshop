import base64
import keys
from timestamp import timestamp


def encode():
    data_to_encode = keys.business_short_code + keys.pass_key + timestamp()
    encoded_string = base64.b64encode(data_to_encode.encode())
    password = encoded_string.decode('utf-8')
    print(password)


encode()
