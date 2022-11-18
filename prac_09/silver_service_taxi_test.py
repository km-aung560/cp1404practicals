"""
Silver Service Taxi Test Program
"""
from prac_09.silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi("Lexus", 200, 4.5)
print(my_taxi)
my_taxi.drive(18)
print(my_taxi)
print(my_taxi.get_fare())




