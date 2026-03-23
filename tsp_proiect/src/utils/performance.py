import time
import matplotlib.pyplot as plt

from tsp_proiect.src.utils.io_utils import get_orase, citeste_matrice
from tsp_proiect.src.utils.backtracking import rezolva_tsp
from tsp_proiect.src.utils.hill_climbing_tsp import rezolva_hill_climbing


def ruleaza_experiment():
    """
    Runs a performance comparison experiment between Backtracking
    and Hill Climbing approaches for solving the Traveling Salesman Problem (TSP).

    The function:
    - Generates random distance matrices for different numbers of cities.
    - Measures execution time for both algorithms.
    - Stores and prints the results.
    - Plots the performance comparison using both linear and logarithmic scales.
    - Saves the resulting plot as an image file.

    The results are displayed in two subplots:
        1. Linear scale comparison
        2. Logarithmic scale comparison

    Returns:
        None
    """
    valori_n_bt = [5, 7, 8, 10, 12, 14,15, 16]
    valori_n_hc = [5, 7, 8, 10, 12, 15, 20, 30, 50, 70, 100]

    timpi_bt = []
    timpi_hc = []

    # Backtracking
    for n in valori_n_bt:
        filename = get_orase(n)
        _, matrice = citeste_matrice(filename)

        start = time.perf_counter()
        rezolva_tsp(filename)
        durata = time.perf_counter() - start

        print(f"Backtracking cu N={n} -> {durata:.6f} sec")
        timpi_bt.append(durata)

    # Hill climbing
    for n in valori_n_hc:
        filename = get_orase(n)
        _, matrice = citeste_matrice(filename)

        start = time.perf_counter()
        rezolva_hill_climbing(matrice, n)
        durata = time.perf_counter() - start

        print(f"[HC] N={n} -> {durata:.6f} sec")
        timpi_hc.append(durata)


    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # --- Subplot stanga (linear) ---
    axes[0].plot(valori_n_bt, timpi_bt, marker='o', label="Backtracking")
    axes[0].plot(valori_n_hc, timpi_hc, marker='o', label="Hill Climbing")
    axes[0].set_title("Comparatie performanta (scara liniara)")
    axes[0].set_xlabel("Numar orase (N)")
    axes[0].set_ylabel("Timp executie (sec)")
    axes[0].legend()
    axes[0].grid()

    # --- Subplot dreapta (log) ---
    axes[1].semilogy(valori_n_bt, timpi_bt, marker='o', label="Backtracking")
    axes[1].semilogy(valori_n_hc, timpi_hc, marker='o', label="Hill Climbing")
    axes[1].set_title("Comparatie performanta (scara logaritmica)")
    axes[1].set_xlabel("Numar orase (N)")
    axes[1].set_ylabel("Timp executie (log scale)")
    axes[1].legend()
    axes[1].grid()

    plt.tight_layout()
    plt.savefig("comparare_performanta.png")
    plt.show()
