inventario = {

0 : {"nome": "Il PC di ...", "quantità": 1, "prezzo": 3999},
1 : {"nome": "Nintendo Switch 2", "quantità": 10, "prezzo": 449},
2 : {"nome": "GTA VI", "quantità": 3, "prezzo": 100}
}

def stampare():
    for chiave in inventario:
            print(f"{chiave} {inventario[chiave]}")

def aggiungere_prodotto():
    nome=input("inserisci il nome del prodotto: ")
    quantità=int(input("inserisci quantità: "))
    prezzo=int(input("inserisci il prezzo del prodotto: "))
    inventario[len(inventario)+1]={"nome": nome, "quantità": quantità, "prezzo":prezzo}

def messaggio():
    print("--------------------------------------------------------")
    print("premi zero per chiudere il programma")
    print("premi uno per aggiungere un prodotto nell'inventario")
    print("premi cinque per stampare l'inventario")
    print("--------------------------------------------------------")




while True:
    messaggio()
    x=int(input("menu: "))
    if x ==1:
        aggiungere_prodotto()
    elif x==0:
        break
    elif x==5:
        stampare()
