import pygame

pygame.init()

# Fonction pour afficher le menu
def afficher_menu():
    menu_font = pygame.font.Font("freesansbold.ttf", 80)
    titre = menu_font.render("Typing Game", True, (255, 255, 255))
    instruction = menu_font.render("Appuyez sur ESPACE pour commencer", True, (255, 255, 255))
    
    fenetre.blit(titre, (400, 100))
    fenetre.blit(instruction, (300, 300))
    pygame.display.flip()

# Fenêtre du jeu
pygame.display.set_caption("Typing Game")
fenetre = pygame.display.set_mode((800, 600))  # Changer la résolution à 800x600

# Arrière-plan
background = pygame.image.load('typinggame/image.jpg')
background = pygame.transform.scale(background, (800, 600))  # Adapter l'image à la résolution de la fenêtre

enCours = True
menu = True

# Boucle principale
while enCours:
    
    if menu:
        afficher_menu()
    
    # Boucle pour les événements
    for event in pygame.event.get():
        # Événement de fermeture
        if event.type == pygame.QUIT:
            enCours = False
            pygame.quit()
        
        # Touche pressée
        elif event.type == pygame.KEYDOWN:
            # Touche Espace pour commencer le jeu
            if event.key == pygame.K_SPACE:
                menu = False

    if not menu:
        # Arrière-plan
        fenetre.blit(background, (0, 0))  # Ajuster la position de l'arrière-plan
        pygame.display.flip()
