pkatedoriat = {"te":"extra","ma":"matematiikka","su":"suomenkieli","yt":"yleistieto"}
katedoriat = {i:0 for i in pkatedoriat.keys()}
class kysymys:
	def __init__(self,kysymys,vastaus,katedoria):
		self.ky,self.va,self.ka = kysymys,vastaus,katedoria
	def kysy(self):
		if input(f"{self.ky} : ") in self.va:
			katedoriat[self.ka]+=1
			print("Oikein")
		else:
			print("Väärin")
kysymykset=[
kysymys("Mikä on ensimmäinen luku, joka on jaollinen sekä kahdella että kolmella?",("6"),"ma")
,kysymys("Paljonko on 1 000 000 000 000 * 0? ",("0"),"ma")
,kysymys("Mitkä ovat yleisimmät kirjaimet yhtälöissä (esimerkkivastaus: a ja b)?",("x ja y","y ja x"),"ma")
,kysymys("mihinkä sanaluokkaan kuuluvat esim sanat :laulaa: ja :tanssia: ?",("verbi","verbi"),"su")
,kysymys("Tuleeko pisteen jälkeen väli vai ei (kyllä/ei)?",("kyllä"),"su")
,kysymys("""Onko jokin seuraavista sanoista erisnimi? (kyllä/ei)?
ilmapallo
joulu
kukkakaali
portugali""",("kyllä"),"su")
,kysymys("Tupu, Hupu, ja kuka onkaan se kolmas",("Lupu","lupu"),"yt")
,kysymys("Mikä oli suomen pääkaupunki ennen Helsinkiä?",("Turku"),"yt")
,kysymys("Mikä maa järjesti vuoden 1952 olympialaiset?",("Suomi"),"yt")
,kysymys("Kuka tekee koodiinsa turhaa toistoa?",("miro"),"te")
]
for i in kysymykset:
	i.kysy()
print(f"Yhteensä sait {sum(katedoriat.values())} pistettä.")
print("Katedorioittain:")
for i in katedoriat:
	print(f"{pkatedoriat[i]} : {katedoriat[i]}")
