" I partie Transformation des fichiers audio "
    
    " Séparation des fichiers train en deux "
        " X_train, X_test, y_train, y_test = train_test_split("
        " X, y, test_size=0.33, random_state=42) "
    " Lire les differents fichier audio ' Train/test ' à la chaine "
    " Utiliser le module AIFC sur les fichiers "
    " Effectuer une rFFT(Fast Fourier Transform) discrète de dimension 1 sur les train"
    " Prend que les premiers 1000kHz du fichier et enregistrement dans un vecteur numpy " 

" II partie : Etalonnage de nos données"

    " Utilisation Scikit learn et attribution des 1/0 pour les trains "

" III partie : Attribution des 1/0 pour les test ( avec % d'erreur ) "

    " Comparation des fichiers Test avec notre base de données"
    " Enregistrer le tout dans un tableau "
    " Comparaison des résultats avec les 1/0 "
