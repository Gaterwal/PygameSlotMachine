import pygame  # Recup composants
import numpy
import time

pygame.init()

"""Classes et fonctions"""
# Classe pour gérer la notion d'emplacement
class Location(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('assets/bomb.png')
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    # Setters pour l'image
    def set_image(self, image):
        self.image = image


def launch():
    global Gold
    # choix au   selon les probabilités
    random = numpy.random.choice(weapons, 3, p=weapons_chance)
    left_weapon = weapons_tuple[random[0]]
    center_weapon = weapons_tuple[random[1]]
    right_weapon = weapons_tuple[random[2]]

    # Chargement des images
    left_location.set_image(left_weapon)
    center_location.set_image(center_weapon)
    right_location.set_image(right_weapon)
    victory = (random[0] == random[1] == random[2])

    # Vérification de l'équivalence des armes
    if not victory:
        lose = pygame.image.load('assets/lose.PNG')
        textlose = font2.render("Vous perdez 10 Gold", True, (0, 0, 0))
        display.blit(textlose, (190, 500))
        display.blit(lose, (130, 475))
        pygame.display.update()
        time.sleep(0.7)
        print("lose")

    else:
        weapon = random[0]
        earnedgold = amount_gold[weapon]
        Gold += earnedgold
        win = pygame.image.load('assets/coins.PNG')
        print(f"You got 3 {weapon}s !  You earned {Gold} Gold")
        textwin = font2.render(f"Vous avez 3 {weapon}s !!!", True, (0, 0, 0))
        textwin2=font2.render(f"Vous gagnez {earnedgold} Gold", True, (255, 215, 0))
        display.blit(textwin, (190, 500))
        display.blit(textwin2, (190, 525))

        display.blit(win, (130, 475))
        pygame.display.update()
        time.sleep(2)
        print("win")


"""Paramètres fenêtres"""
# Création de la fenêtre
width = 550
height = 600
display = pygame.display.set_mode((650, 620))  # Dimension fenêtre
pygame.display.set_caption("RPG Slot Machine - Gaterwal")  # Nom de la fenêtre
white_color = [255, 255, 255]  # Couleur du fond
back = pygame.image.load('assets/slot.png')  # Charger image arrière plan
wallet = pygame.image.load('assets/wallet.png')
gold_picture = pygame.image.load('assets/gold.PNG')
# Dictionnaire d'image
weapons_tuple = {
    "Bombe": pygame.image.load('assets/bomb.png'),
    "Epée": pygame.image.load('assets/sword.png'),
    "Arc": pygame.image.load('assets/bow.png'),
    "Hache": pygame.image.load('assets/axe.png'),
    "Shuriken": pygame.image.load('assets/shuriken.png')}
pygame.font.init()  # Initialiser la police
font = pygame.font.SysFont("Calibri", 30)  # Mettre une police générale
font2 = pygame.font.SysFont("Calibri", 20)  # Mettre une police pour les Gold
font2.set_bold(True)  # Mettre en gras
font3 = pygame.font.SysFont("Garamond", 30)  # Mise et Gain
font4 = pygame.font.SysFont("Calibri", 18)  # Mettre une police pour les Gold


# Chargement des emplacements
height_emplacement = height / 2.4
locations = pygame.sprite.Group()
left_location = Location(165, height_emplacement)
center_location = Location(238, height_emplacement)
right_location = Location(311, height_emplacement)
bomb_location = Location(500, 100)
sword_location = Location(500, 165)
bow_location = Location(500, 240)
axe_location = Location(500, 315)
shuriken_location = Location(500, 390)
result_location = Location(238, 500)

# Rangement dans l'emplacement du groupe
locations.add(left_location)
locations.add(center_location)
locations.add(right_location)
locations.add(bomb_location)
locations.add(axe_location)
locations.add(bow_location)
locations.add(sword_location)
locations.add(shuriken_location)

"""Variables"""
# Argent du joueur
Gold = 1000

# Liste des items
weapons = ["Bombe", "Hache", "Arc", "Epée", "Shuriken"]

# Création d'un dictionnaire Key-Value pour les gold obtenus selon l'item
amount_gold = {
    "Shuriken": 5,
    "Hache": 15,
    "Arc": 50,
    "Epée": 150,
    "Bombe": 5000,

}
# Probabilité de tomber sur l'image
weapons_chance = [0.03, 0.30, 0.20, 0.10, 0.37]

"""Interface Pygame"""
# Boucle pour maintenir fenêtre pygame active jusqu'à croix sortie
running = True

while running:
    # Arrière plan blanc
    display.fill(white_color)
    # Injecter image (fond)
    display.blit(back, (0, 0))
    display.blit(wallet, (0, 460))
    # Injecter emplacements
    locations.draw(display)
    # Afficher le nombre de Gold à l'écran
    text = font2.render(str(Gold) + " gold", True, (255, 215, 0))
    display.blit(text, (35, 565))
    text2 = font3.render("Gains", True, (0, 0, 0))
    display.blit(text2, (570, 50))
    bomb_location.set_image(weapons_tuple["Bombe"])
    text3 = font4.render("3 X ="+str(amount_gold["Bombe"]), True, (0, 0, 0))
    display.blit(text3, (570, 130))
    sword_location.set_image(weapons_tuple["Epée"])
    text6 = font4.render("3 X =" + str(amount_gold["Epée"]), True, (0, 0, 0))
    display.blit(text6, (570, 200))
    bow_location.set_image(weapons_tuple["Arc"])
    text5 = font4.render("3 X ="+str(amount_gold["Arc"]), True, (0, 0, 0))
    display.blit(text5, (570, 275))
    axe_location.set_image(weapons_tuple["Hache"])
    text4 = font4.render("3 X =" + str(amount_gold["Hache"]), True, (0, 0, 0))
    display.blit(text4, (570, 350))
    shuriken_location.set_image(weapons_tuple["Shuriken"])
    text7 = font4.render("3 X ="+str(amount_gold["Shuriken"]), True, (0, 0, 0))
    display.blit(text7, (570, 425))
    display.blit(gold_picture, (600, 560))
    text9 = font3.render("Mise", True, (0, 0, 0))
    display.blit(text9, (570, 520))
    text10 = font2.render("10", True, (0, 0, 0))
    display.blit(text10, (570, 580))

    #  Affichez l'action pour l'utilisateur
    info = font3.render("Pour jouer, appuyez sur la barre espace", True, (0, 0, 0))
    display.blit(info, (40, 20))

    # Actualisation display
    pygame.display.flip()

    # Maintenir ouvert jusqu'à la fermeture
    for event in pygame.event.get():
        # Vérifie si le joueur appuie sur une touche
        if event.type == pygame.KEYDOWN:
            # Vérifie si c'est sur la touche Espace
            if event.key == pygame.K_SPACE and Gold >= 0:
                launch()  # Appel de la fonction launch
                Gold -= 10  # Mise de 10 gold

        if event.type == pygame.QUIT:
            running = False
            quit()




