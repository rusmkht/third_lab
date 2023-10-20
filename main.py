import random

n = int(input("Сан енгізіңіз: ") ) # Қолданушыдан N-ды сұраймыз
i = 1  # Есепкішті іске асырамыз
while i <= n:
    if i % 2 == 0:  # Сан жұп, онда оны шығарамыз
        print(i)
    i += 1

f = int(input("Сан енгізіңіз: "))  # Қолданушыдан N-ды сұраймыз
summa = 1  # Нәтижесін сақтау үшін өзгермейтін айнымалын анықтаймыз
i = 1  # Есепкішті іске асырамыз
while i <= f:
    summa *= i  # Факториалды есептейміз
    i += 1
print("N санның факториалы =", summa)

while True:
    num_search = int(input("Сан енгізіңіз: "))  # Қолданушыдан санды сұраймыз
    if num_search == 42:
        break  # Сан 42 болса, циклді аяқтау
print("Сан 42 табылды, бағытын аяқтау!!!")

str1 = input("Сөзді енгізіңіз: ")  # Қолданушыдан сөзді сұраймыз
count = 0  # Есепшіді іске асырамыз

for char in str1:
    if char == 'а' or char == 'А':  # 'а' қәріпінің барма екенін тексереміз
        count += 1

print(f"Сөзде 'а' әрекетінің саны: {count}")

sum_of_digits = input("Санды енгізіңіз: ")  # Қолданушыдан санды сұрау етеміз
summa = 0  # Сандардың суммасын сақтау үшін өзгермейтін айнымалды іске асырамыз

for digit in sum_of_digits:
    if digit.isdigit():  # Символ сандары болса
        num_digit = int(digit)  # Символды екілеу
        summa += num_digit  # Суммаға санды қосамыз

print("Сандардың суммасы:", summa)

fibonacci = int(input("Фибоначчи жолдарын қанша алайын көрсеткізгіңіз: "))  # Қолданушыдан N-ды сұрау етеміз
i = 0
f1 = 0
f2 = 1
print(f1)  # Бірінші Фибоначчи санды шығарамыз
print(f2)  # Екінші Фибоначчи санды шығарамыз

while i < fibonacci - 2:
    i += 1
    sum = f1 + f2  # Келесі Фибоначчи санды есептейміз
    f1 = f2
    f2 = sum
    print(sum)  # Келесі Фибоначчи санды шығарамыз

str2 = input("Сөзді енгізіңіз: ")  # Қолданушыдан сөзді сұрау етеміз
sum_str = ""  # Теріске аудару үшін айнымалды іске асырамыз

for i in range(len(str2) - 1, -1, -1):
    sum_str += str2[i]  # Сөзді теріске аударамыз

print("Теріске аударылған сөз:", sum_str)

sum = 0  # Сумманы сақтау үшін айнымалды іске асырамыз
while True:
    numberrr = int(input("Санды енгізіңіз: "))  # Қолданушыдан санды сұраймыз
    if numberrr == 0:  # Сан 0 болса, циклді аяқтау
        break
    if numberrr % 2 == 0:  # Сан жұп болса, оны өткіземіз
        continue
    sum += numberrr  # жұп санды суммаға қосамыз

print("Жуықсан сандардың суммасы:", sum)

randnum = random.randint(1, 100)  # 1-ден 100-ге дейін жасырыған сан
print(randnum)  # Тесттерді көру үшін жасырыған санды шығарамыз

while True:
    numwin = int(input("Санды анықтаңыз: ") ) # Қолданушыдан санды сұраймыз
    if randnum > numwin:
        print("Сан үлкен")
    elif randnum < numwin:
        print("Сан аз")
    else:
        print("Құттықтаймыз! Сіз санды анықтадыңыз!")
        break

str222 = input("Сөзді енгізіңіз: ")  # Қолданушыдан сөзді сұраймыз
pal = ""  # Теріс аудару үшін айнымалды іске асырамыз

for i in range(len(str222) - 1, -1, -1):
    pal += str222[i]  # Сөзді теріс аударамыз

if pal == str222:
    print("Бұл - палиндром")
else:
    print("Бұл - палиндром емес")

x = int(input("Санды енгізіңіз: "))  # Қолданушыдан X санды сұраймыз
y = int(input("Степенді енгізіңіз: ") ) # Қолданушыдан Y степенін сұраймыз
i = 1
summm = 1
while i <= y:
    summm *= x  # X-ні Y дәрежесін есептеу
    i += 1
print(f"{x} санның {y} дарежесі = {summm}")

n = int(input("N санды енгізіңіз: "))  # Қолданушыдан N санды сұраймыз
i = 2

while i <= n:
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)  # Жәй санды шығарамыз
    i += 1

number = input("Санды енгізіңіз: ")  # Қолданушыдан санды сұраймыз
reversed_number = number[::-1]  # Санды теріске аударамыз
print("Санды теріске аудару:", reversed_number)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input(":Жәй санын тексеру үшін санды енгізіңіз: "))

while True:
    if is_prime(number):
        print(f"{number} - Жәй сан.")
        break
    else:
        print(f"{number} - Жәй сан емес.")
        number += 1

def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            encrypted_text += shifted_char
        else:
            encrypted_text += char

    return encrypted_text

user_input = input("Сөзді енгізіңіз: ")  # Қолданушыдан сөзді сұраймыз
shift = int(input("Жылжыту қатар санын енгізіңіз (бүтін сан): ") ) # Қолданушыдан жылжыту қатар санын сұрау етеміз

encrypted_text = caesar_cipher(user_input, shift)
print("Шифрланған сөз:", encrypted_text)
