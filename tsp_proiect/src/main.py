from tsp_proiect.src.utils import backtracking, io_utils, performance
import time

from tsp_proiect.src.utils.io_utils import *
from tsp_proiect.src.utils.backtracking import *
from tsp_proiect.hill_climbing_tsp import *

if __name__ == "__main__":
    filename = io_utils.get_orase(120)
    n, matrice = citeste_matrice(filename)
    start = time.perf_counter()

    # _traseu_optim, _cost_minim = rezolva_tsp(filename)

    end = time.perf_counter()


    # print("BKT", _traseu_optim, _cost_minim)
    print(f"Time taken: {end - start:.6f} seconds")



    start = time.perf_counter()
    _traseu_optim, _cost_minim = rezolva_hill_climbing(matrice, n)
    end = time.perf_counter()

    print("Hill C", _traseu_optim, _cost_minim)
    print(f"Time taken: {end - start:.6f} seconds")
