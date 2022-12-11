
import random

n = 8

def get_random_password(n) -> str:
# TODO написать функцию генерации случайных паролей
 s1 = "abcdefghijklmnopqrstuvwxyz"
 s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 s3 = "0123456789"

 return("".join(random.sample("abcdefghijklmnopqrstuvwxyz"+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"+"0123456789", n)))




print(get_random_password(8))





