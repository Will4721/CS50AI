import numpy as np

# 1. Nøglen: En 3x3 matrix (Vores hemmelige 3D-rum)
KEY_MATRIX = np.array([
    [3, 2, 1, 4, 2, 7],
    [1, 4, 2, 3, 2, 1],
    [2, 1, 3, 8, 8, 4],
    [5, 2, 7, 1, 3, 6],
    [4, 9, 1, 2, 5, 8],
    [1, 3, 8, 4, 7, 2]
])

def lwe_demo():
    # Data vi vil skjule: "abc" (ASCII: 97, 98, 99)
    original_data = np.array([83, 69, 67,82,69,84])
    print(f"1. Original data: {original_data} ('Secret')")

    # Den rene matematik (Uden støj - den som en hacker kan regne baglæns)
    perfect_coord = np.dot(KEY_MATRIX, original_data)

    # 2. LWE MAGIEN: Vi opretter bevidst støj (tilfældige decimaler)
    # Støjen skal være stor nok til at skjule sporet, men lille nok til vi kan runde den væk
    noise = np.random.uniform(-0.4, 0.4, size=6)

    # 3. Det offentlige koordinat (Det vi gemmer i databasen)
    public_coord = perfect_coord + noise

    print(f"\n2. Det hackeren ser (Støjfyldt koordinat):")
    print(public_coord)
    print("(Prøv at bruge standard lineær algebra på det der... det fejler!)")

    # --- NU SKAL VI DEKRYPTERE ---
    print("\n--- DEKRYPTERING MED NØGLEN ---")

    # Vi bruger den inverse matrix (vores låsesmed) for at regne os tilbage
    inverse_matrix = np.linalg.inv(KEY_MATRIX)

    # Computeren regner baglæns fra det støjfyldte koordinat
    messy_result = np.dot(inverse_matrix, public_coord)

    print(f"\n3. Råt resultat fra computeren før afrunding:")
    print(messy_result)

    # 4. The Closest Vector Problem løses ved hjælp af basal afrunding
    # Fordi vi har den rigtige matrix, er fejlen fordelt rigtigt, og vi kan bare runde af til nærmeste hele tal (int)
    clean_result = np.round(messy_result).astype(int)

    recovered_text = "".join(chr(val) for val in clean_result)
    print(f"\n4. Færdig dekrypteret tekst:")
    print(f"{clean_result} -> '{recovered_text}'")

if __name__ == "__main__":
    lwe_demo()