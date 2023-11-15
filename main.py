print("=========================================")

############## Projet Email Slicer ##############

# Generer un programme qui recupere le nom d'utilisateur et le domaine d'un email

print("=========================================")

def mail(mailContent):
    """renvoie le nom d'utilisateur et le domaine de la messagerie"""

    name,domaine = mailContent.split("@")
    return name,domaine
# jeux de tests

print(mail("yoh@mail.com"))
print(mail("personne@mail.com"))

