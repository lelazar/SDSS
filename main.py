"""
A projekt az SDSS adatokat használva analizálja az égi objektumok pozícióit és színeit.
Két osztályt tartalmaz: CelestialObject és Star, ami a 'CelestialObject' osztályból öröklődik.
A program feltételezi, hogy van egy SDSS adatokat tartalmazó CSV fájl (data_file = "sdss_data.csv") a kövekező oszlopokkal:
'ra', 'dec', 'u', 'g', 'r', 'i', 'z'. Ha másik fájt szeretnénk használni, a data_file változónkat kell módosítani ennek megfelelően.

A projekt futtatásához telepíteni kell a 'matplotlib' könyvtárat: pip install matplotlib

A program kiolvassa az adatokat és csillag objektumokat készít ('Star') ezekből az információkból.
Ezután ábrázolja a csillagok eloszlását az égen jobbra emelkedésük (RA - Right Ascension) és deklinációjuk
(Dec - Declination) alapján.

A CSV fájlt az alábbi SQL lekérdezéssel hoztam létre a 'https://skyserver.sdss.org/dr16/en/tools/search/sql.aspx' oldalon:
SELECT TOP 50000
   p.ra,p.dec,
   p.u,p.g,p.r,p.i,p.z
FROM PhotoObj AS p
   LEFT OUTER JOIN SpecObj AS s ON s.bestobjid = p.objid
WHERE
   p.ra>230.1 and p.ra<231.1
   AND p.dec>27.2 and p.dec<28.2

Az említett SQL parancs egy adatmintát hoz létre az első 50000 objektumból, amit talál az Abell 2065 galaxishalmazban.
Ez egy leglább 400 galaxisból álló halmaz: https://hu.wikipedia.org/wiki/Abell_2065
A CSV fájlt az alábbi honlapon található tutorial segítségével hoztam létre: http://burro.case.edu/Academics/Astr306/ClustAGN/getSDSS.html
Ahogy fentebb említettem, jelen esetben elegendőek voltak a következő oszlopok: 'ra', 'dec', 'u', 'g', 'r', 'i', 'z'.

Sajnos arra egyelőre nem találtam megoldást, hogy a fenti SQL parancsot úgy módosítsam, hogy más galaxisok adatait is le lehessen kérni hasonló módon...
Talán az alábbi honlap segítségével? https://skyserver.sdss.org/dr16/en/help/docs/realquery.aspx


Felhasznált weblapok és tutorial-ok:
https://www.sdss4.org/
https://classic.sdss.org/
https://astrodatascience.net/category/sdss/
https://pypi.org/project/sdss/
https://www.sdss4.org/dr16/irspec/catalogs/
https://skyserver.sdss.org/dr18/SearchTools/IQS
https://www.sdss4.org/dr17/tutorials/retrievefits/
http://burro.case.edu/Academics/Astr306/ClustAGN/getSDSS.html
https://skyserver.sdss.org/dr16/en/home.aspx
"""

import csv
import matplotlib.pyplot as plt


class CelestialObject:
    def __init__(self, ra, dec):
        self.ra = float(ra)
        '''
        A jobb felemelkedés (RA) a hosszúság égi megfelelője. Az RA kifejezhető fokban, de gyakrabban órában, percben és másodpercben adják meg: 
        az égbolt 24 óra alatt 360°-ot, vagy egy óra alatt 15°-ot fordul el. Tehát egy óra RA az égbolt 15°-os elforgatásával egyenlő.
        '''
        self.dec = float(dec)
        '''
        A deklináció (DEC) az égi szféra szélességi fokának megfelelője, és fokban van kifejezve,
        ahogy a szélesség is. A DEC esetében a + és - az északra, illetve a délre vonatkozik.
        Az égi egyenlítő 0° DEC, a sarkok +90° és -90°.
        '''

    def get_position(self):
        return self.ra, self.dec


class Star(CelestialObject):
    def __init__(self, ra, dec, u, g, r, i, z):
        super().__init__(ra, dec)
        self.colors = {
            "u": float(u),  # Ultraviolet
            "g": float(g),  # Green
            "r": float(r),  # Red
            "i": float(i),  # Infrared - 7600 A
            "z": float(z)   # Infrared - 9100 A
        }

    def get_z(self):
        return self.colors['z']


def read_sdss_data(file_path):
    stars = []  # Stack (verem) létrehozása

    # stars[] verem feltöltése a .CSV fájlból
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            star = Star(row['ra'], row['dec'], row['u'], row['g'], row['r'], row['i'], row['z'])
            if star.get_z() < 20 and star.get_z() > 19:
                stars.append(star)

    return stars


# A csillagok eloszlását megmutatjuk egy ablakban
def plot_ra_dec(stars):
    ra = [Star.get_position()[0] for Star in stars]
    dec = [Star.get_position()[1] for Star in stars]

    plt.scatter(ra, dec, s=1)  # Szórványrajz készítése. X koordináta: ra. Y koordináta: dec. ra + dec mátrix skalárisa: s=1, vagyis a jelölő mérete.
    plt.xlabel('Right Ascension (RA)')
    plt.ylabel('Declination (Dec)')
    plt.title('Stars Distribution in SDSS')
    plt.show()


if __name__ == "__main__":
    data_file = "sdss_data.csv"         # .CSV fájl kijelölése
    stars = read_sdss_data(data_file)   # .CSV fájl beolvasása

    # Ha minden helyes, meghívjuk plot függvényt, amely kirajzolja a csillagokat
    plot_ra_dec(stars)
