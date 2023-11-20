# Si scriva una funzione verifica_lista che riceve in ingresso una lista
# L di interi ed un intero k. La funzione restituisce True se e solo se la lista L
# non contiene nessuna sotto-lista di lunghezza k avente valori strettamente crescenti
# Esempio: Se L=[4,5,5,6,1,1,2,2,5,3] allora verifica_lista(L,3) restituisce True perche' nessuna
# delle sotto-liste di lunghezza 3 [4,5,5], [5,5,6], [5,6,1], [6,1,1], [1,1,2], [1,2,2], [2,2,5], [2,5,3]
# ha valori strettamente crescenti.


def crea_sottoliste(L,k):
    sottoliste = []
    # i: indice mobile
    i = 0
    # itera fino alla fine della lista
    while i+k <= len(L):
        sottoliste.append(L[i:i+k])
        # avanza di un indice
        i += 1
    return sottoliste



def sottoliste_sono_strett_crescenti(sottoliste):
    # itera per ogni sottolista
    for sottolista in sottoliste:
        # itera nella sottolista fin quando non trovi almeno due valori che NON sono strettamente crescenti
        # questo soddisfa la condizione che l'intera sottolista non e' strettamente crescente
        # seleziona il primo valore
        ultimo_numero = sottolista[0]
        # indice mobile, parti dal secondo elemento della sottolista
        i = 1
        # inizializza
        strettamente_crescenti = True
        # parti dal secondo elemento della sottolista
        while strettamente_crescenti and i<len(sottolista):
            # se trovi un valore che e' maggiore dell'ultimo, allora la sottolista finora e' strettamente crescente
            # quindi questo valore attuale diventa l'ultimo nella prossima iterazione
            if sottolista[i] > ultimo_numero:
                print(ultimo_numero,sottolista[i])
                ultimo_numero = sottolista[i]
            # se ho trovato almeno un caso di valori non strettamente crescenti, esco dal loop
            # perche' questo mi basta per dire che l'intera sottolista NON e' strettamente crescente
            else:
                # esco dal while loop
                strettamente_crescenti = False
            i += 1
        # se esco dal loop con ancora strettamente crescenti vero, questo significa che l'intera sottolista e' strettamente crescente,
        # quindi almeno una sottolista non non soddisfa la condizione
        if strettamente_crescenti:
            return True
    # significa che hai verificato tutte le sottoliste, e nessuna sottolista ha valori strettamente crescenti
    return False



def verifica_lista(L,k):
    sottoliste = crea_sottoliste(L,k)
    print(sottoliste)
    if not sottoliste_sono_strett_crescenti(sottoliste):
        return True
    return False


L=[4,5,5,6,1,1,2,2,5,3]
print(verifica_lista(L,3))
