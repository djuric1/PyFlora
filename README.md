			SEMINAR - PyFloraPosude app

SAŽETAK -> potrebno izraditi GUI aplikaciju za praćenje stanja ukrasnih i/ili začinskih biljaka (neke povrtne kulture također - rajčica) koje su posađene u posude s integriranim senzorima za mjerenje:
	- vlažnost zemlje
	- pH vrijednost i salinitet zemlje
	- razina svijetla koja dopire do biljke
	- temperatura zraka u prostoriji ili na otvorenom 	(terasa ili mali vrt)

-> Dodatna vrijednost koju treba čuvati je temperatura zraka, koju ćete preuzeti s Meteo stanice u Algebrinom kampusu (Zagreb, Črnomerec) preko Web API usluge. Ukoliko Web API usluga na Meteo stanici iz bilo kojeg razloga bude nedostupna, osigurajte zamjensku opciju generiranjem ovih podataka unutar spomenute skripte.

-> Posude sa senzora u aplikaciju šalju mjerenja preko integrirane Bluetooth veze.

-> Vrijednosti očitane sa svih senzora, simulirajte tako što ćete ih generirati u zasebnoj Python 
skripti koja će se pokretati svaki puta kada korisnik pritisne gumb „Sync“ 

----------------------------------------------------------------------------------

1. Dekompozicija
2. Paternizacija
3. Apstrakcija
4. Algoritam
	Dijagram toka/Pseudo kod
5. Evaluacija

----------------------------------------------------------------------------------

1. Dekompozicija PyFloraPosude
	1.1. Hardvare
	-> senzori + CPU = potrebno pronaći senzore za praćenje stanja uzgajane biljke, te kontrolu parametara za optimalan prinos biljke