from decouple import config, Csv

consumer_key = config("CONSUMER_KEY")
consumer_secret = config("CONSUMER_SECRET")
business_short_code = config("SHORTCODE")
phone_number =config("PHONE_NUMBER")
pass_key = config("LNM_PASSKEY")
call_back_url = config("CALL_BACK_URL")
test_msisdn = config("TEST_MSISDN")
shortcode = config("BUSINESS_SHORTCODE")