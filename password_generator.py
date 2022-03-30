# 3 büyük harf, 3 küçük harf, 3 rakam ve 2 tane de özel karakter 
# içerecek şifre generatör kodu yazalım.

# Solution

uppers = [chr(random.randint(65,90)) for i in range(3)]
lowers = [chr(random.randint(97,122)) for i in range(3)]
numbers = [chr(random.randint(48,57)) for i in range(3)]
chars = chr(random.randint(33,47)) + chr(random.randint(58,64))
pasw = "".join(lowers) + "".join(uppers) + "".join(numbers) + chars
pasw
# şuan sıralı verdi şimdi karıştıralım 

pass_list = list(pasw)
pass_list

random.shuffle(pass_list)
"".join(pass_list)



# son kısım için fonksiyon tanımladık.

def karıştır(password) :
    templist = list(password)
    random.shuffle(templist)
    return "".join(templist)

karıştır(pasw)
