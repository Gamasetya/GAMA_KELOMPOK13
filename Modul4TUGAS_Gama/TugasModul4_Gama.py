
def tampilkan_panduan():
    print("===================================")
    print("      SISTEM RATING FILM")
    print("===================================")
    print("Masukkan rating film dari 0 sampai 10.")
    print("Kategori: Sampah, Medioker, Bagus,")
    print("Bagus banget, dan Top markotop.")
    print("-----------------------------------")

def tentukan_kategori(rating):
    if rating < 2:
        return "Sampah"
    elif rating < 4:
        return "Medioker"
    elif rating < 6:
        return "Bagus"
    elif rating < 9:
        return "Bagus banget"
    else:
        return "Top markotop"

class Film:
    def __init__(self, judul, rating):
        self.judul = judul
        self.rating = rating

    def ambil_judul(self):
        return self.judul

    # METHOD NON-RETURN DENGAN PARAMETER
    def tampilkan_hasil(self, kategori):
        print("Judul film   :", self.judul)
        print("Rating       :", self.rating)
        print("Kategori     :", kategori)
        print("-----------------------------------")


tampilkan_panduan()

lanjut = "y"

while lanjut == "y":
    judul = input("Masukkan judul film: ")

    rating = -1
    while rating < 0 or rating > 10:
        rating = float(input("Masukkan rating (0-10): "))

        if rating < 0 or rating > 10:
            print("Rating tidak valid! Masukkan 0-10.")

    film = Film(judul, rating)

    kategori = tentukan_kategori(rating)

    nama_film = film.ambil_judul()

    print("\nHASIL PENILAIAN FILM")
    print("Film yang dinilai:", nama_film)

    film.tampilkan_hasil(kategori)

    lanjut = input("Nilai film lain? (y/n): ").lower()

print("Terima kasih telah menggunakan program!")
