from tkinter import *

root = Tk()

root.geometry("300x600")
root.title("SPK VIKOR BOBA ")

def myClick():

    def display(string, array):
        print(f"===== HASIL {string}:")
        for row in array:
            formatted_row = ["{:.2f}".format(value) for value in row]
            print("[{}]".format(", ".join(formatted_row)))

    # Get the values from the entry widgets and convert them to integers
    c1_value = int(c1_input.get())
    c2_value = int(c2_input.get())
    c3_value = int(c3_input.get())
    c4_value = int(c4_input.get())
    c5_value = int(c5_input.get())
    c6_value = int(c6_input.get())
    c7_value = int(c7_input.get())
    c8_value = int(c8_input.get())


    # Create an array from the input values
    weight = [c1_value, c2_value, c3_value, c4_value, c5_value, c6_value, c7_value, c8_value]
    weight_sum = sum(weight)
    print(f"===== JUMLAH WEIGHT: \n{weight_sum}")
    print()


    # INISIALISASI DATA
    data = [[2.7, 4.8, 750, 51, 11, 8, 5, 1],  # A1
            [2.7, 4.7, 700, 27, 12, 0, 4, 1],  # A2
            [2.7, 4.7, 500, 41, 12, 30, 5, 1],  # A3
            [2.7, 4.8, 250, 32, 12, 40, 4, 1],  # A4
            [3.3, 4.7, 400, 18, 15, 35, 4, 2],  # A5
            [4.6, 4.6, 650, 25, 15, 8, 3, 1]]  # A6

    # PERBAIKI BOBOT
    weight_sum = sum(weight)
    weight_fixed = [w / weight_sum for w in weight]

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
    result_label.config(text="Alternatif terbaik adalah " + str(best))


# === C1
c1_label = Label(root, text="bobot lokasi:")
c1_label.grid(row=0, column=0)

c1_input = Entry(root, width=35, borderwidth=5)
c1_input.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# === C2
c2_label = Label(root, text="bobot rating: ")
c2_label.grid(row=2, column=0)

c2_input = Entry(root, width=35, borderwidth=5)
c2_input.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# === C3
c3_label = Label(root, text="bobot ukuran minuman: ")
c3_label.grid(row=5, column=0)

c3_input = Entry(root, width=35, borderwidth=5)
c3_input.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

# === C4
c4_label = Label(root, text="bobot harga minuman: ")
c4_label.grid(row=7, column=0)

c4_input = Entry(root, width=35, borderwidth=5)
c4_input.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

# === C5
c5_label = Label(root, text="bobot jam operasional: ")
c5_label.grid(row=9, column=0)

c5_input = Entry(root, width=35, borderwidth=5)
c5_input.grid(row=10, column=0, columnspan=3, padx=10, pady=10)

# === C6
c6_label = Label(root, text="bobot kapasitas dine-in:")
c6_label.grid(row=11, column=0)

c6_input = Entry(root, width=35, borderwidth=5)
c6_input.grid(row=12, column=0, columnspan=3, padx=10, pady=10)

# === C7
c7_label = Label(root, text="bobot kebersihan toko: ")
c7_label.grid(row=13, column=0)

c7_input = Entry(root, width=35, borderwidth=5)
c7_input.grid(row=14, column=0, columnspan=3, padx=10, pady=10)

# === C8
c8_label = Label(root, text="bobot ketersediaan Wi-Fi gratis: ")
c8_label.grid(row=15, column=0)

c8_input = Entry(root, width=35, borderwidth=5)
c8_input.grid(row=16, column=0, columnspan=3, padx=10, pady=10)

# === RESULT
myButton = Button(root, text="Submit!", command=myClick)
myButton.grid(row=17, column=0, columnspan=3)

result_label = Label(root, text="Result: ")
result_label.grid(row=18, column=0, columnspan=3)


root.mainloop()
