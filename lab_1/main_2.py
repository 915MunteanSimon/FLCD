nr1 ia_valoarea numar input("Enter value:")


daca restul_impartirii(nr1,2) este 0:
    afiseaza("nu este prim")
    termina_programul

parcurge_numere(it,3,radical(nr1),2):
    daca restul_impartirii(nr1,it) este 0:
        afiseaza("nu este prim")
        termina_programul

afiseaza("este prim")