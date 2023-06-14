import csv
import matplotlib.pyplot as plt


class CelestialObject:
    def __init__(self, ra, dec):
        self.ra = float(ra)
        self.dec = float(dec)

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
    stars = []

    # stars[] fill with data from the .CSV file
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            star = Star(row['ra'], row['dec'], row['u'], row['g'], row['r'], row['i'], row['z'])
            if star.get_z() < 20 and star.get_z() > 19:
                stars.append(star)

    return stars


def plot_ra_dec(stars):
    ra = [Star.get_position()[0] for Star in stars]
    dec = [Star.get_position()[1] for Star in stars]

    plt.scatter(ra, dec, s=1)
    plt.xlabel('Right Ascension (RA)')
    plt.ylabel('Declination (Dec)')
    plt.title('Stars Distribution in SDSS')
    plt.show()


if __name__ == "__main__":
    data_file = "sdss_data.csv"         # .CSV file select
    stars = read_sdss_data(data_file)   # .CSV file read

    plot_ra_dec(stars)
