[![Language Machines Badge](http://applejack.science.ru.nl/lamabadge.php/valkuil-gecco)](http://applejack.science.ru.nl/languagemachines/) [![GitHub release](https://img.shields.io/github/release/LanguageMachines/frog.svg)](https://GitHub.com/proycon/valkuil-gecco/releases/) 
[![Project Status: Unsupported – The project has reached a stable, usable state but the author(s) have ceased all work on it. A new maintainer may be desired.](https://www.repostatus.org/badges/latest/unsupported.svg)](https://www.repostatus.org/#unsupported)


Valkuil.net powered by GECCO
-------------------------------

 by Maarten van Gompel, Antal van den Bosch
 Centre for Language Studies
 Radboud University Nijmegen

 Gelicenseerd onder de [Affero GNU Public License v3](https://www.gnu.org/licenses/agpl-3.0.html)

Valkuil.net is een automatische spellingcorrector voor het Nederlands die zowel
gewone typefouten als grammaticale fouten en verwarringen tussen bestaande
woorden opspoort. Valkuil is in eerste instantie online als web-applicatie
beschikbaar voor eindgebruikers op http://valkuil.net .

Valkuil.net is gebaseerd op grote hoeveelheden Nederlandse tekst, en niet op
taalkundige kennis of een vaste woordenlijst. De meeste modules in valkuil.net
zijn contextgebaseerd en statistisch: ze slaan alarm wanneer ze een woord
tegenkomen dat ze niet verwachten op basis van de omgeving waarin dat woord
staat. Het enthousiasme waarmee ze alarm slaan is instelbaar (klik op 'Toon
geavanceerde opties' in het invoerscherm).

Valkuil.net bevat modules voor hele specifieke verwarringen, zoals zei-zij,
maar ook voor fouten met vervoegingen zoals de bekende d-t-fout. Valkuil.net
doet ook zijn best om vergeten spaties of teveel gezette spaties op te sporen.

**Hoe goed is valkuil.net?** In het algemeen kan een spellingchecker twee soorten
fouten maken: het systeem kan fouten missen en kan vals alarm slaan.
Valkuil.net is, in tegenstelling tot de meeste andere spellingcorrectors,
ingesteld om niet te veel valse alarmen te genereren. De keerzijde van deze
voorzichtigheid is dat valkuil.net bij te grote onzekerheid ervoor kiest om
geen alarm te slaan, en zo mist het systeem wel eens fouten. Het streven is om
minder dan de helft van alle fouten te missen (en liefst veel minder). We komen
in de buurt.

**Wat leren we daarvan?i** Spellingcorrectie is moeilijk, en is daarom zo'n boeiend
onderzoeksonderwerp. Valkuil.net mist meer dan de helft van de fouten en slaat
in tweederde van de gevallen vals alarm. De vraag is wat erger is, en of we
niet wat meer valse alarmen moeten toelaten zodat we wat meer echte fouten
vinden. Wordt vervolgd...

**Wat gaat er fout?** Van alles, en in deze fouten zitten interessante patronen.
Het woord 'word' wordt bijvoorbeeld vaak onterecht verbeterd tot 'wordt'; de
andere kant op gaat veel beter, zoals psycholinguïst Dominiek Sandra ook bij
mensen ziet gebeuren. Hij verklaart dat als een frequentie-effect: 'wordt' komt
veel vaker voor dan 'word', en als we even niet goed opletten dan kiezen we
vaak onbewust voor de frequentere vorm. Valkuil.net valt in dezelfde valkuil
als mensen. Op basis van dit soort analyses kunnen we valkuil.net verbeteren,
niet door taalregels in te voeren, maar door valkuil.net te hertrainen op meer
of anders geselecteerde voorbeelden.

**Wat zit er onder de motorkap?** Data-gedreven, geheugengebaseerde
taaltechnologie aangredeven door [Gecco](https://github.com/proycon/gecco).
Ondanks dat de modules zich baseren op honderden miljoenen woorden Nederlandse
tekst zijn ze lichtgewicht en snel; ze maken veelal gebruik van
[Timbl](http://ilk.uvt.nl/timbl), een open source softwarepakket voor
geoptimaliseerde geheugengebaseerde classificatie, dat we sinds de jaren '90 in
Tilburg ontwikkelen. Andere modules zijn gebaseerd op [Colibri
Core](https://github.com/proycon/colibri-core).

Gecco wordt voornamelijk gebruikt als een webservice (middels
[CLAM](https://github.io/clam), waarboven een webapplicatie is ontwikkeld.
Intern werkt valkuil.net met het XML-formaat FoLiA, dat geschikt is voor de
representatie van gedetecteerde fouten, correctiesuggesties, en gekozen
correcties.

**Hoe kan ik Valkuil zelf draaien?** De makkelijkste optie is door vanuit je
programma verbinding te maken met onze Valkuil webservice, zie
https://webservices-lst.science.ru.nl .

Wil je Gecco met Valkuil lokaal draaien dan zul je zeer goede hardware moeten
hebben, met name veel geheugen (minimaal 32GB). We verwijzen naar de
[Gecco](https://github.com/proycon/gecco) pagina voor installatieinstructies.

Is Gecco eenmaal geinstalleerd, dan kan je de valkuil modellen uit deze git
repository gebruiken. De corpus bronnen waaruit deze modellen zijn samengesteld
kunnen we door restrictieve auteursrechten helaas niet openbaar beschikbaar
maken.

Slechts een klein aantal modellen zit daadwerkelijk in deze git repository, de
rest moet gedownload worden door het ``download-models.sh`` script aan te
roepen. Dit is een download van 500MB, maar neemt na decompressie rond de 1GB
in beslag.



