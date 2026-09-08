#!/usr/bin/env python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with a given size and position."""

        # Vérifie que size est bien un entier.
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Vérifie que size n'est pas négatif.
        if size < 0:
            raise ValueError("size must be >= 0")

        # Stocke la taille dans l'attribut privé.
        self.__size = size

        # Passe par le setter pour valider et stocker la position.
        self.position = position

    def area(self):
        """Calculates the area of the square."""

        # Aire = côté × côté.
        return self.__size ** 2

    @property
    def position(self):
        """Getter for the position of the square."""

        # Permet de récupérer la position.
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position of the square."""

        # Vérifie que position est un tuple de 2 entiers
        # et que les deux valeurs sont positives ou nulles.
        if (
            not isinstance(value, tuple) or len(value) != 2
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or value[0] < 0 or value[1] < 0
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )

        # Si la position est valide, on la stocke.
        self.__position = value

    @property
    def size(self):
        """Getter for the size of the square."""

        # Permet de récupérer la taille.
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size of the square."""

        # Vérifie que la nouvelle taille est un entier.
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        # Vérifie que la nouvelle taille n'est pas négative.
        if value < 0:
            raise ValueError("size must be >= 0")

        # Stocke la nouvelle taille.
        self.__size = value

    def my_print(self):
        """Prints the square using the '#' character."""

        # Si la taille est 0, on affiche simplement une ligne vide.
        if self.__size == 0:
            print()
            return

        # position[1] représente le nombre de lignes vides
        # à afficher AVANT le carré.
        for _ in range(self.position[1]):
            print()

        # Affiche chaque ligne du carré.
        for _ in range(self.__size):
            # position[0] représente le nombre d'espaces
            # à mettre AVANT chaque ligne du carré.
            print(
                self.position[0] * " " + "#" * self.__size
            )

    def __str__(self):
        """Returns a string representation of the square."""

        # Si la taille est 0, on retourne une chaîne vide.
        if self.__size == 0:
            return ""

        # On commence avec une chaîne vide.
        result = ""

        # position[1] représente les lignes vides
        # avant le carré.
        for _ in range(self.position[1]):
            result += "\n"

        # Construction du carré ligne par ligne.
        for i in range(self.size):

            # Ajoute les espaces horizontaux puis les #.
            result += (
                self.position[0] * " "
                + "#" * self.size
            )

            # Ajoute un retour à la ligne ENTRE les lignes,
            # mais pas après la dernière.
            if i != self.size - 1:
                result += "\n"

        # __str__ doit retourner une chaîne, pas faire print().
        return result
