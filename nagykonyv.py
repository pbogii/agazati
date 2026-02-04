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
        konyv = {'nev': nev,
                'szul_ev': szul_ev,
                'hal_ev': hal_ev,
                'nemzetiseg': nemzetiseg,
                'cim': cim,
                'helyezes': helyezes }
        konyvek.append(konyv)

# print(f'{konyvek=}')
#3.2 feladat
print(f"3.2. feladat: Az állományban {len(konyvek)} db könyv adatai szerepelnek.")

#3.3 feladat
magyar_konyvek = []
for konyv in konyvek:
    if konyv['nemzetiseg'] == 'magyar':
        magyar_konyvek.append(konyv)


# print(len(magyar_konyvek))

legjobb_konyv = magyar_konyvek[0]
for konyv in magyar_konyvek:
    if konyv['helyezes'] < legjobb_konyv['helyezes']:
        legjobb_konyv = konyv

print(f"3.3 feladat: A legjobb helyezést elért magyar könyv: {legjobb_konyv['nev']}: {legjobb_konyv['cim']}")

#3.4 feladat
van = False
for konyv in konyvek:
    if konyv['nemzetiseg'] == "német":
        print("3.4. feladat: A listában szerepel német író könyve.")
        van = True
        break

if van:
    print("3.4. feladat: A listában szerepel német író könyve.")
else:
    print("3.4. feladat: A listában NEM szerepel német író könyve.")

#3.5 feladat

idosebb_mint_90 = []
for konyv in konyvek:
    if ((konyv["hal_ev"] - konyv["szul_ev"]) >= 90):
        idosebb_mint_90.append(konyv['nev'])
    
print(f"3.5. feladat: 90 évesnél idősebb írók :{set(idosebb_mint_90)}")



