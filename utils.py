# utils.py

def nilai_ke_label(nilai):
    if 85 <= nilai <= 100:
        return "A"
    elif 80 <= nilai <= 84:
        return "A-"
    elif 75 <= nilai <= 79:
        return "B+"
    elif 70 <= nilai <= 74:
        return "B"
    elif 65 <= nilai <= 69:
        return "B-"
    elif 60 <= nilai <= 64:
        return "C"
    elif 50 <= nilai <= 59:
        return "C"
    elif 40 <= nilai <= 49:
     	return "D"
    else:
        return "E"


def label_ke_bobot(label):
    bobot = {
        "A": 4.0,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3.0,
        "B-": 2.7,
        "C": 2.0,
        "D": 1.0,
        "E": 0.0
    }
    return bobot.get(label, 0)


def hitung_ip(nilai_list, sks_list):
    if not nilai_list or not sks_list:
        return "Nilai atau SKS belum diinput."

    if len(nilai_list) != len(sks_list):
        return "Jumlah nilai dan SKS tidak sama."

    total_bobot = 0
    total_sks = 0

    for nilai, sks in zip(nilai_list, sks_list):
        total_bobot += label_ke_bobot(nilai) * sks
        total_sks += sks

    return round(total_bobot / total_sks, 2)