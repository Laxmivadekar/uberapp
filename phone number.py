import phonenumbers
# from text import number
from phonenumbers import geocoder
number='+917893867233'
ch_number=phonenumbers.parse(number,'CH')
print(geocoder.description_for_number(ch_number,'en'))

from phonenumbers import carrier
service_number=phonenumbers.parse(number,'RO')
print(carrier.name_for_number(service_number,'en'))