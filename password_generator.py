import random
import string

def generate_password(length=12, use_numbers=True, use_symbols=True):
    """Generoi vahvan salasanan perusparametreilla.
    
    Args:
        length (int): Salasanan pituus.
        use_numbers (bool): Sisällytetäänkö numerot.
        use_symbols (bool): Sisällytetäänkö erikoismerkit.
    
    Returns:
        str: Generoitu salasana.
    """

    # Perusmerkistö: isot ja pienet kirjaimet
    characters = string.ascii_letters

    if use_numbers:
        characters += string.digits
    
    if use_symbols:
        characters += string.punctuation

    # Satunnainen valinta merkistöstä
    password = "".join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    print("Password Generator 🔐")
    
    try:
        length = int(input("Anna salasanan pituus (oletus 12): ") or 12)
    except ValueError:
        print("Virheellinen syöte, käytetään oletusta (12).")
        length = 12

    include_numbers = input("Sisällytetäänkö numerot? (k/e, oletus k): ").lower() != "e"
    include_symbols = input("Sisällytetäänkö erikoismerkit? (k/e, oletus k): ").lower() != "e"
    
    password = generate_password(
        length=length,
        use_numbers=include_numbers,
        use_symbols=include_symbols
    )

    print(f"\nGeneroitu salasana: {password}")
