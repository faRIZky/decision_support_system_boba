
                    # FORMATTING MATRIKS
def display(string, array):
    print(f"===== HASIL {string}:")
    for row in array:
        formatted_row = ["{:.2f}".format(value) for value in row]
        print("[{}]".format(", ".join(formatted_row)))

                    # INISIALISASI DATA
data = [[2.7, 4.8, 750, 51, 11, 8, 5, 1],   # A1
        [2.7, 4.7, 700, 27, 12, 0, 4, 1],   # A2
        [2.7, 4.7, 500, 41, 12, 30, 5, 1],  # A3
        [2.7, 4.8, 250, 32, 12, 40, 4, 1],  # A4
        [3.3, 4.7, 400, 18, 15, 35, 4, 2],  # A5
        [4.6, 4.6, 650, 25, 15, 8, 3, 1]]   # A6

                    # INISIALISASI BOBOT
c1 = int(input("Masukan bobot untuk lokasi toko: "))
c2 = int(input("Masukan bobot untuk rating toko: "))
c3 = int(input("Masukan bobot untuk ukuran minuman: "))
c4 = int(input("Masukan bobot untuk harga minuman: "))
c5 = int(input("Masukan bobot untuk jam operasional toko: "))
c6 = int(input("Masukan bobot untuk kapasitas dine-in: "))
c7 = int(input("Masukan bobot untuk kebersihan toko: "))
c8 = int(input("Masukan bobot untuk ketersediaan Wi-fi gratis: "))

weight = [c1, c2, c3, c4, c5, c6, c7, c8]

weight_sum = sum(weight)
print(f"===== JUMLAH WEIGHT: \n{weight_sum}")
print()

                    # PERBAIKI BOBOT
weight_fixed = [w / weight_sum for w in weight]
print(f"===== HASIL PERBAIKAN WEIGHT: \n{weight_fixed}")
print()

                    # NORMALISASI DATA
data_normalized = []
for alternatif in data:
    alternatif_normalized = []
    for kriteria, value in enumerate(alternatif):

        data_max = max(alternatif[kriteria] for alternatif in data)
        data_min = min(alternatif[kriteria] for alternatif in data)

        kriteria_normalized = (data_max - value) / (data_max - data_min)
        alternatif_normalized.append(kriteria_normalized)
    data_normalized.append(alternatif_normalized)

display("NORMALISASI DATA", data_normalized)
print()

                    # NILAI S
data_normalized_times_weight = []
for alternatif in data_normalized:
    weighted_row = [value * weight_fixed[i] for i, value in enumerate(alternatif)]
    data_normalized_times_weight.append(weighted_row)

display("NORMALISASI X BOBOT", data_normalized_times_weight)
print()

s = [sum(row) for row in data_normalized_times_weight]
print(f"===== NILAI S: \n{s}")
print()

                    # NILAI R
r = [max(row) for row in data_normalized_times_weight]
print(f"===== NILAI R: \n{r}")
print()

                    # INDEX Q
## MIN MAX S
s_max = max(s)
s_min = min(s)
print(f"Nilai S MAX: {s_max}")
print(f"Nilai S MIN: {s_min}")
print()

## MIN MAX R
r_max = max(r)
r_min = min(r)
print(f"Nilai R MAX: {r_max}")
print(f"Nilai R MIN: {r_min}")
print()

## NILAI V
v = 0.5
print(f"Nilai V: {v}")
print()

## NILAI Q SETIAP ALTERNATIF
q = [((s[i] - s_min) / (s_max - s_min) * v + (r[i] - r_min) / (r_max - r_min) * (1 - v)) for i in range(len(s))]
print(f"===== NILAI Q: \n{q}")
print()

##ATTACH Q DENGAN ALTERNATIFNYA
alternatif = ["Xing fu tang",
              "Chatime",
              "KOI Thé",
              "Kopi Kenangan",
              "Kopi dari Hati",
              "555 Thai Tea"]
q_with_alternatif = []
q_with_alternatif = list(zip(q, alternatif))
print(f"===== NILAI Q DAN ALTERNATIF: \n{q_with_alternatif}")
print()

                    # PERANGKINGAN
## DESCENDING
ranked_indices = sorted(range(len(q)), key=lambda i: q[i], reverse=True)
# ranked_indices's output -- > [5, 3, 4, 1, 2, 0]

## DISPLAY RANKING KESELURUHAN
print("===== PERINGKAT:")
for i, index in enumerate(ranked_indices):
    print(f"Peringkat {i + 1}: Q = {q_with_alternatif[index]}")
print()

## DISPLAY THE BEST ALTERNATIVE
best = min(q_with_alternatif)
print(f"ALTERNATIF TERBAIK ADALAH {best}")