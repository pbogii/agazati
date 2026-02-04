konyvek = []

with open('konyvek.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        nev = adatok[0]
        szul_ev = int(adatok[1])
        hal_ev = int(adatok[2])   if adatok[2] != "" else 2005
        nemzetiseg = adatok[3]
        cim = adatok[4]
        helyezes = int(adatok[5])
        konyv = {'nev ': nev,
                'szul_ev': szul_ev,
                'hal_ev': hal_ev,
                'nemzetiseg': nemzetiseg,
                'helyezes': helyezes }
        konyvek.append(konyv)

print(f'{konyvek=}')
