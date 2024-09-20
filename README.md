# datielezioni-volt

## Descrizione
Questo progetto consiste in una analisi statistica dei risultati elettorali dei candidati di Volt, Silvia Panini e Marcello Saltarelli, alle elezioni europee del 2024 in Italia.
Questi dati sono stati utilizzati per creare mappe coropletiche, utili a visualizzare la distribuzione dei voti sul territorio.
Queste mappe sono poi state rese disponibili tramite una webapp.

Il progetto si divide in tre parti, i cui punti significativi saranno descritti di seguito

## Scraping Eligendo
Non essendo disponibili su internet i dati delle preferenze dei singoli candidati divisi per comune e in formato machine-readable, è servito creare uno script per creare il dataset scaricando i dati dalla piattaforma Eligendo. 
Fortunatamente una parte del lavoro era già stata fatta [in questo progetto](https://github.com/ondata/elezioni_europee_2024) di OnData.

Ispezionando il sito di eligendo si può vedere l'url della API che viene richiamata dalla webapp per ottenere i dati delle preferenze, che ha questo formato:
https://eleapi.interno.gov.it/siel/PX/prefeEI/DE/20240609/TE/01/PR/{provincia}/CM/{comune}/AG/0008
dove {provincia} e {coumne} sono codici identificativi dei rispettivi.

Lo script parte da un file "insieme.csv" preso dal progetto di OnData, il quale contiene dati riguardanti i comuni e sull'affluenza, e ci aggiunge due colonne con il numero di preferenze dei nostri candidati. Infine l'output viene salvato nella cartella "dati" con il nome "insieme_with_votes.csv".

## Analisi
Questa parte del progetto è uno script che esegue alcuni calicoli sui dati rapportandoli al numero di elettori, e crea le mappe coropletiche.

I dati spaziali usati per creare le mappe sono in formato topojson, formato analogo al geojson, ma più compresso, e sono stati scaricati da [questo progetto](https://github.com/openpolis/geojson-italy) di Openpolis.

Le mappe poi vengono salvate all'interno della cartella "webapp/templates/maps".

## Webapp
La webapp utilizzata per visualizzare i dati e renderli disponibili al pubblico, è basata su Flask.
Per il deployment della webapp è stata utilizzata la procedura consultabile in [questa guida](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-22-04).

## Prerequisiti
Per eseguire gli script è necessario avere installato Python 3.12.
Per installare i moduli necessari eseguire il comando ``python -m pip install -r requirements.txt`` nella cartella di progetto.
