# SDSS

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
