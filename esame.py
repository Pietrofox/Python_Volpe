#esame russo 25/09/2023 by Pietro Volpe

#definizione della classe per le eccezioni personalizzate
class ExamException(Exception):
    pass

#classe CSVTimeSeriesFile per la gestione dei dati CSV
class CSVTimeSeriesFile:
    #il metodo '__init__' accetta il nome del fle CSV e lo 
    #memorizza nell'attributo 'self.name'
    def __init__(self, name):
        self.name = name

    #metodo get_data interno alla classe 'CSVTimeSeriesFile' che tenta di aprire il file
    #e restituisce una lista di liste
    #CSV specificato nel costruttore ('self.name') usando la funzione 'open'
    def get_data(self):
        try:
            datafile = open(self.name)

    #se il file non viene trovato il messaggio stampato a schermo sarà 'File not found'
        except FileNotFoundError:
            raise ExamException("Error, File not found")

        #viene iizializzata una lista vuota chiamata 'my_list'
        my_list = []

        #viene inizializzato un ciclo 'for' utilizzato per
        #iterare attraverso le righe del file.
        
        for line in datafile:
            #ogni riga viene suddivisa in una lista usando
            #come separatore una virgola
            my_list.append(line.split(","))
            #la lista risultante viene aggiunta a my_list
            #il valore dell'ultima colonna (i passeggeri)
            #viene convertito in intero
    
            try:
                my_list[-1][-1] = int(my_list[-1][-1])
            #se la conversione non è possibile viene
            #sollevata un'eccezione
            #'ExamException' con il messaggio 
            #'Not a numerical value'
            except:
                ExamException("Error, Not a numerical value")
        #alla fine il metodo restituisce 'my_list' a partire
        #dalla seconda riga.
        #prchè la prima viene esclusa dato che contiene
        #"date, passengers", che non servono
        
        return my_list[1:]


#questa funzione è usata per elaborare i dati CSV e creare un dizionario che raggruppa 
#i dati anno per anno
def helperfunction(time_series):
    #apro il file come lista
    my_list = CSVTimeSeriesFile(time_series).get_data()#viene usato il metodo get_data
    #della classe 'CSVTimeSeriesFile' per ottenere i dati e
    #memorizzarli nella variabile 'my_list'
   
    #creo dizionario vuoto chiamto 'my_dict'
    my_dict = {}
    
    #leggo solo l'anno del primo elemento, cioè i primi 4
    #caratteri e lo confronto con l'anno corrente 
    #('creo la variabile current_year' con l'anno del primo
    #elemento)
    current_year = my_list[0][0][0:4]
    temp_list = [] #inizializzazione di una lista temporanea per raccogliere i dati 
#del mese corrente

    #popolo la temp_list ciclando anno per anno
    for line in my_list:
        year = line[0][0:4]
        #se l'anno non è cambiato aggiungo il valore del mese a 'temp_list'
        if current_year == year:
            temp_list.append(line[1])
        #else se l'anno è passato a quello successivo
        else:
            my_dict[current_year] = temp_list
            #azzero la temp list e aggiorno l'anno corrente
            temp_list = []
            current_year = year
            temp_list.append(line[1])

    #per inserire l'ultimo anno        
    my_dict[current_year] = temp_list
    
    #alla fine del ciclo restituisco il dizionario 'my_dict'
    return my_dict

#creazione della funzione 'detect_similar_monthly_variations'
def detect_similar_monthly_variations(time_series, years):
    
    #lista da returnare (serve a registrare se i valori sono simili)
    confront = []

    #creo dizionario con la mia funzione
    my_dict = helperfunction(time_series)
    
    #estraggo i dati contenuti nella lista years
    try:
        year_1 = my_dict[str(years[0])]
        year_2 = my_dict[str(years[1])]
    except Exception:
        raise ExamException("Error, Anno non trovato")
        

    #parte ALGEBRICA del file python
    #liste da popolare con la sottrazione tra i mesi e variabili di appoggio
    year1calc = []
    year2calc = []
    current = None
    next = None
    
    if len(year_1) < 12 or len(year_2) < 12:
        raise ExamException("Error Anno non valido")
    if len(year_2) < 12:
        raise ExamException("Error, Anno non valido")
    
    #ciclo for per calcolare la variazione mensile tra i due anni
    for month in range(len(year_1)-1):
        current = year_1[month]
        next = year_1[month+1]
        year1calc.append(abs(current-next))

    for month in range(len(year_2)-1):
        current = year_2[month]
        next = year_2[month+1]
        year2calc.append(abs(current-next))

    for month in range(len(year1calc)):
        #se la differenza assoluta tra le variazioni mensili esce <=2 viene aggiunto 
        #'True' a 'confront', altrimenti viene aggiunto     'False'
        if abs(year1calc[month]-year2calc[month]) <= 2:
            confront.append(True)
        else:
            confront.append(False)

    #viene restituita la lista 'confront' con i risultati del
    #confronto tra le variazioni mensili 
    return confront



#CODICE PRINCIPALE
#definisco la classe 'years' con due anni
years = [1949,1950]
#chiamo la funzione 'detect_similar_monthly_variations' con il nome del file CSV e la 
#lista 'years' come argomenti. memorizzo il risultato nella variabile 'x'
x = detect_similar_monthly_variations("data.csv",years)
#il risultato 'x' viene stampato a schermo per mostrare se lae variazioni mensili tra i 
#due anni sopra specificati sono simili o meno
#utyilizzo il ciclo for per stampare su più linee altrimenti l'output 
#sarebbe stato rimasto tutto su una singola linea separato da virgole
#for value in x:
print(x)