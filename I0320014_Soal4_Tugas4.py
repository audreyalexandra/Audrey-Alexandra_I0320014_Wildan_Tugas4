usia = int(input("Berapa usia kamu? "))
isQualified = input("Apakah Anda sudah lulus ujian kualifikasi (Y / T)? ").lower()

if usia >= 21 and isQualified == "y":
    print("Anda dapat mendaftar di kursus.")
else:
    print("Anda tidak dapat mendaftar di kursus.")