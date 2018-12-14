from functools import lru_cache
@lru_cache(maxsize=500)
def terbilang(nominal):
    satuan = ['','satu','dua','tiga','empat','lima','enam','tujuh','delapan','sembilan','sepuluh','sebelas']
    num = int(nominal)
    if num < 20:
        if num <= 11:
            return satuan[num]
        if num<20:
            return satuan[num-10] + ' belas'
    elif num < 100:
        return terbilang(num/10) + ' puluh ' + terbilang(num%10) 
    elif num < 1000:
        if num < 200:
            return 'seratus ' + terbilang(num%100)
        else:
            return terbilang(num/100) + ' ratus ' + terbilang(num%100)
    elif num < 1000000:
        if num < 2000:
            return 'seribu ' + terbilang(num%1000)
        else:
            return terbilang(num/1000) + ' ribu ' + terbilang(num%1000)
    elif num < 1000000000:
        return terbilang(num/1000000) + ' juta ' + terbilang(num%1000000)
    elif num < 1000000000000:
         return terbilang(num/1000000000) + ' miliar ' + terbilang(num%1000000000)
    elif num < 1000000000000000:
         return terbilang(num/1000000000000) + ' triliun ' + terbilang(num%1000000000000)   
    else:
        return '!!!!!'