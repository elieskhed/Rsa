import rsa

rsa = rsa()

#Coté expediteur
#exemple de clés publique d'un destinataire:
#e=565
#n=283189

rsa.encrypt("Help !",565,283189)

