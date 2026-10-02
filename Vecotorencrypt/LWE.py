import numpy as np


KEY_MATRIX = np.array([
    [3, 2, 1, 4, 2, 7],
    [1, 4, 2, 3, 2, 1],
    [2, 1, 3, 8, 8, 4],
    [5, 2, 7, 1, 3, 6],
    [4, 9, 1, 2, 5, 8],
    [1, 3, 8, 4, 7, 2]
])

def lwe_demo():

    original_data = np.array([83, 69, 67,82,69,84])
    print(f"1. Original data: {original_data} ('Secret')\n")


    perfect_coord = np.dot(KEY_MATRIX, original_data)
    print(f"2. New matrix: {perfect_coord} \n")


    noise = np.random.uniform(-0.4, 0.4, size=6)


    public_coord = perfect_coord + noise

    print("what the hacker would see ")
    print(public_coord)
    print("(Prøv at bruge standard lineær algebra på det der... det fejler!)")


    print("\n--- DEKRYPTERING MED NØGLEN ---")


    inverse_matrix = np.linalg.inv(KEY_MATRIX)


    messy_result = np.dot(inverse_matrix, public_coord)

    print(f"\n3. Råt resultat fra computeren før afrunding:")
    print(messy_result)


    clean_result = np.round(messy_result).astype(int)

    recovered_text = "".join(chr(val) for val in clean_result)
    print(f"\n4. Færdig dekrypteret tekst:")
    print(f"{clean_result} -> '{recovered_text}'")

if __name__ == "__main__":
    lwe_demo()