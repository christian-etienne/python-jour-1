#Créez des variables représentant un produit (nom, prix unitaire, quantité en stock).

nom = "coca"
prix_unitaire = 12
quantite_en_stock = 50

#Affichez en console les informations du produit de manière formatée. pour écrire de maniere formatee, on utilisera des f strings 

print (f" le prix du {nom} est de {prix_unitaire} sur une quantité de {quantite_en_stock}")


#Demandez à l’utilisateur de saisir la quantité de produits qu’il souhaite acheter

quantite_en_s = int (input ("quantite souhaite?"))
print ((quantite_en_s * prix_unitaire), "il reste" , (quantite_en_s - quantite_en_stock), "en stock maintenant")

#Le prix d’un produit à subi l’inflation et à augmenté de 10%. Mettre à jour la variable correspondante.
