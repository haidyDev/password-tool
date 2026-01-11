import secrets
import string


def generate_password(length=12, use_numbers=True, use_symbols=True):
    """Generate a cryptographically secure password.

    Guarantees at least one digit and one symbol if they are enabled.
    """

    pools = [string.ascii_letters]

    if use_numbers:
        pools.append(string.digits)

    if use_symbols:
        pools.append(string.punctuation)

    if length < len(pools):
        raise ValueError("Password length too short for selected options.")

    # Ensure at least one from each selected group
    password_chars = [secrets.choice(pool) for pool in pools]

    # Create full character set
    all_chars = "".join(pools)

    # Fill the rest
    password_chars += [
        secrets.choice(all_chars)
        for _ in range(length - len(password_chars))
    ]

    # Shuffle securely
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


if __name__ == "__main__":
    print("Password Generator 🔐")

    try:
        length = int(input("Anna salasanan pituus (oletus 12): ") or 12)
    except ValueError:
        print("Virheellinen syöte, käytetään oletusta (12).")
        length = 12

    include_numbers = input("Sisällytetäänkö numerot? (k/e, oletus k): ").lower() != "e"
    include_symbols = input("Sisällytetäänkö erikoismerkit? (k/e, oletus k): ").lower() != "e"

    try:
        password = generate_password(
            length=length,
            use_numbers=include_numbers,
            use_symbols=include_symbols
        )
        print(f"\nGeneroitu salasana: {password}")
    except ValueError as e:
        print(f"Virhe: {e}")
