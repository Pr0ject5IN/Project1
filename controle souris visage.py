import cv2
import pyautogui     

# Charger le classificateur pré-entraîné pour détecter les visages
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialiser la capture vidéo à partir de la caméra par défaut (indice 0)
cap = cv2.VideoCapture(0)

while True:                                               # Boucle infinie pour traiter la vidéo en temps réel
    ret, frame = cap.read()                               # Lire une image depuis la camera (ret = succès, frame = image)
    if not ret:                                           # Si la capture a une erreur, arreter la boucle
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)        # Convertir l'image en niveaux de gris (pour la détection)

    faces = face_cascade.detectMultiScale(                # Détecter les visages dans l'image en niveaux de gris
        gray,                                             # Image en niveaux de gris
        scaleFactor=1.1,                                  # Paramètre pour réduire la taille de l'image à chaque étape
        minNeighbors=5,                                   # Nombre de voisins (nombre de points pour detecter unvisage)
        minSize=(30, 30)                                  # Taille minimale des rectangles de détection
    )

    for (x, y, w, h) in faces:                            # Boucle à travers toutes les détections de visages
        face_center_x = x + w // 2                        # Calculer le centre X du rectangle visage
        face_center_y = y + h // 2                        # Calculer le centre Y du rectangle visage

        screen_width, screen_height = pyautogui.size()    # Obtenir les dimensions de l'écran 

        cursor_x = int(face_center_x / frame.shape[1]     # Convertir les coordonnées X
                        * screen_width)                  # par rapport à la largeur de l'écran
        cursor_y = int(face_center_y / frame.shape[0]     # Convertir les coordonnées Y
                        * screen_height)                 # par rapport à la hauteur de l'écran

        pyautogui.moveTo(cursor_x, cursor_y)              # Déplacer le curseur de la souris 

        cv2.rectangle(frame,                              # Dessiner un rectangle autour du visage 
                      (x, y),                             # Coin haut a gauche du rectangle
                      (x + w, y + h),                     # Coin bas a droite du rectangle
                      (255, 0, 0),                        # Couleur du rectangle (bleu en BGR)
                      2)                                  # Épaisseur

    cv2.imshow("Face Detection", frame)                  # Afficher l'image  avec les rectangles visages 

    if cv2.waitKey(1) & 0xFF == ord('q'):                 # Vérifier si la touche 'q' est appuyer pour quitter
        break

cap.release()                                             
cv2.destroyAllWindows()                                   
