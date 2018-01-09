# Integrazione dati Open Civitas 

Questa procedura ha portato all'inserimento nei dati Open Civitas relativi ai fabbisogni le seguenti variabili:

* `Codice_Istat`: Codice ISTAT
* `Denominazione Italiana`: Nome comune 
*  `Provincia`: Provincia
*  `Sigla Provincia`: Sigla capoluogo di provincia cui appartiene il comune 
*  `Codice_Provincia`: Codice capoluogo di provincia cui appartiene il comune 
*  `Regione`: Regione cui appartiene il comune 
*  `Sigla Regione`: Sigla regione cui appartiene il comune 
*  `Codice_Regione`: Codice regione cui appartiene il comune 
*  `AreaGeo`: Area geografica (definita da ISTAT) cui il comune appartiene

## Contenuti dei file pushed

* `Uniformare_OpenCivitas.ipynb`:

> L'IPython notebook descrive le procedure utilizzate per integrare i dati. In una prima parte si trovano i singoli passi svolti. La procedura viene poi riuassunta in un modulo ed applicata agli altri file, svolgendo per ogni file i necessari sanity check. Le variabili aggiunte non dovrebbe presentare null values, pe ril 2013, mentre per i dati relativi al 2010 non ci sono NaN eccetto che per 3 comuni specificati nel Notebook.

* `lista_comuni.txt`: 

> Contiene le informazioni relative ai comuni Italiane

* `'Elenco_comuni_italiani_1¯_gennaio_2010.xls'`:

> Contiene informazioni sui comuni italiani, usato per colmare buchi di `lista_comuni.txt`

* `ripartizioni_regioni_province.xls`:

> Contiene informazioni su regioni e province, usato per completare i nuovi campi inseriti