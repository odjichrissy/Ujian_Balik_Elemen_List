'''
=========================================================================
Soal 2 - Membalik posisi element list
=========================================================================
'''
def balikPosisi(list_awal):
    panjang_list = len(list_awal)
    list_akhir = [1] * panjang_list

    for i in list_awal:
        panjang_list -= 1
        list_akhir[panjang_list]= i
    return(list_akhir)

            
print(balikPosisi([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(balikPosisi(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
print(balikPosisi(['Messi', 'Suarez', 'Coutinho', 'Dembele', 'Rakitic']))