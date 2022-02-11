import phonenumbers
from phonenumbers import timezone, geocoder, carrier
from sqlalchemy import false
fun = True
while fun:
    phone_number = input('Enter the Phone Number with country code\n>')
    user_phone = phonenumbers.parse(phone_number)
    time = timezone.time_zones_for_number(user_phone)
    our_carrier = carrier.name_for_number(user_phone, "en")
    registration = geocoder.description_for_number(user_phone, "en")
    print(user_phone)
    print('Your time zone is', time)
    print('Your sim is', our_carrier)
    print('Your country is', registration)
    

