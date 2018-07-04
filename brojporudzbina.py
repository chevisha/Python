import pandas as p
Proizvodi = p.read_csv("files/products.csv")
n = p.read_csv("files/orders.csv")

m = len(set(n["order_id"]))
PR = len(set(Proizvodi["product_id"]))
korisnici = len(set(n["user_id"]))



print("Broj korisnika: " + str(korisnici) )
print(" broj proizvoda:" + str(PR))
print(" broj narudzbina: " + str(m))
