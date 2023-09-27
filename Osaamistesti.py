# alkuparametrit
matikka = 0
suomenkieli = 0
yleistieto = 0
kaikki_yhteensä = 0

# aloitus, kysymys 1 ja sen ehdot
print("Tervetuloa tohjelmoimaani monialaiseen osaamistestiin:")
print("*" * 50)
print()
k1 = int(input("Matikka, kysymys 1: Mikä on ensimmäinen luku, jonka on jaollinen sekä kahdella että kolmella? "))
if k1 == 6:
	print("Aivan oikein, sait pisteen!")
	matikka += 1
	kaikki_yhteensä += 1
elif k1 != 6:
	print("Väärä vastaus, jäit nollille.")

# toinen kysymys ja ehdot
print()
k2 = int(input("Matikka, kysymys 2: paljonko on 1 000 000 000 000 * 0? "))
if k2 == 0:
	print("Juuri näin, piste sinulle.")
	matikka += 1
	kaikki_yhteensä += 1
elif k2 != 0:
	print("Jäit nollille.")

# kolmas kysymys ja ehdot
print()
k3 = input("Matikka, kysymys 3: mitkä ovat yleisimmät kirjaimet yhtälöissä (esimerkkivastaus: a ja b)? ")
if k3 == "x ja y" or k3 == "y ja x":
	print("Upeaa, vatauksesi oli oikein!")
	matikka += 1
	kaikki_yhteensä += 1
elif k3 != "x ja y" or  k3 != "X ja Y":
	print("Väärä vastaus, et saanut pisteitä.")

# neljäs kysymys ja ehdot
print()
k4 = input("Suomenkieli, kysymys 1: mihinkä sanaluokkaan kuuluvat esim sanat :laulaa: ja :tanssia: ?")
if k4 == "verbi":
	print("Hienoa, oikein")
	suomenkieli += 1
	kaikki_yhteensä += 1
elif k4 != "verbi":
	print("Voi ei, väärin meni.")

# kysymys 5 ja ehdot
print()
k5 = input("Suomenkieli, kysymys 2: Tuleeko pisteen jälkeen väli vai ei (kyllä/ei)? ")
if k5 == "kyllä":
	print("Näin on!")
	suomenkieli += 1
	kaikki_yhteensä += 1
elif k5 != "kyllä":
	print("Väärin meni, hop hop takaisin äikän tunnille.")
	
# ja samalla kaavalla loppuun asti
print()
print("Suomenkieli, kysymys 3: Onko jokin seuraavista sanoista erisnimi? (kyllä/ei)")
print("ilmapallo")
print("joulu")
print("kukkakaali")
print("portugali")
k6 = input("Vastaus: ")
if k6 == "kyllä":
	print("Oikein, 1 piste tulee tilastoihisi.")
	suomenkieli += 1
	kaikki_yhteensä += 1
elif k6 != "kyllä":
	print("Ei mennyt oikein tällä kertaa.")

print()
k7 = input("Yleistieto, kysymys 1: Tupu, Hupu, ja kuka onkaan se kolmas")
if k7 == "Lupu" or k7 == "lupu":
	print("Hienoa, sait pisteen")
	yleistieto += 1
	kaikki_yhteensä += 1
if k7 != "Lupu" or k7 != "lupu":
	print("Väärin, et ole näköjään lukenut Aku ankkaa.!")

print()
k8 = input("Yleistieto, kysymys 1: suomen pääkaupunki ennen Helsinkiä: ")
if k8 == "Turku":
	print("Hyvä, olet ollut hereillä historian tunnilla.")
	yleistieto += 1
	kaikki_yhteensä += 1
elif k8 != "Turku":
	print("Väärin, tarkkuutta historiantunneilla!")

print()
k9 = input("Yleistieto, kysymys 3: Mikä maa järjesti vuoden 1952 olympialaiset? ")
if k9 == "Suomi":
	print("Oikea vastaus!")
	yleistieto += 1
	kaikki_yhteensä += 1
elif k9 != "Suomi":
	print("Voi ei, väärin meni.")

print()
print("Tilastosi:")
print(f"Matikka: pistet {matikka}")
print(f"Suomenkieli: pisteet {suomenkieli}")
print(f"Yleistieto: pisteet {yleistieto}")
print()
print(f"KAIKKI YHTEENSÄ: {kaikki_yhteensä}")
