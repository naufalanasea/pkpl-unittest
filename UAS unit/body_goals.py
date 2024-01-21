def body_goals(tinggi, gender):
    if gender.lower() == 'lakilaki':
        berat_badan_ideal = (tinggi - 100) - ((tinggi - 100) * 0.1)
    elif gender.lower() == 'perempuan':
        berat_badan_ideal = (tinggi - 100) - ((tinggi - 100) * 0.15)
    else:
        raise ValueError("Inputan Anda Tidak Valid. Gunakan 'lakilaki' atau 'perempuan'.")

    return berat_badan_ideal


if __name__ == "__main__":
    height = float(input("Tinggi badan dalam cm: "))
    gender = input("'lakilaki' atau 'perempuan': ")

    try:
        berat_badan_ideal = body_goals(height, gender)
        print(f"Berat badan ideal : {berat_badan_ideal:.2f} kg")
    except ValueError as e:
        print(e)
#uas
