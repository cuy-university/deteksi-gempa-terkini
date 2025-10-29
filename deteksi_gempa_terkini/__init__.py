import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """
    Tanggal: 28 Oktober 2025
    Waktu: 08:31:20 WIB
    Magnitudo: 5,5
    Kedalaman: 10 km
    Koordinat Lokasi: LU=1,43 BT=121,77
    Pusat Gempa: Pusat gempa berada di laut 68 km TimurLaut Buol
    Dirasakan: Dirasakan (Skala MMI): III-IV Kab. Buol, II-III Kab. Pohuwato, II-III Tolitoli, II Kab. Gorontalo Utara
    :return:
    """
    try:
        content = requests.get('https://bmkg.go.id')
    except:
        return None
    if content.status_code ==200:
        soup = BeautifulSoup(content.text, 'html.parser')

        # 🔹 Ambil tanggal & waktu
        waktu_tag = soup.find('p',{'class':'mt-2 text-sm leading-[22px] font-medium text-gray-primary'})
        if waktu_tag:
            waktu_data = waktu_tag.text.split(', ')
            tanggal = waktu_data[0]
            waktu = waktu_data[1]
        else:
            tanggal = waktu = None

        # 🔹 Ambil magnitude & kedalaman
        info_divs = soup.find_all('div', class_='mt-0.5 flex items-center gap-2')
        if len(info_divs) >= 2:
            magnitude = info_divs[0].text.strip()
            kedalaman = info_divs[1].text.strip()
        else:
            magnitude = kedalaman = None

        #🔹 Ambil lokasi (biasanya di bawah elemen <span>)
        span_tags = soup.find_all('span', class_='text-base lg:text-lg font-bold text-black-primary')
        lokasi = None
        if len(span_tags) > 2:
            lokasi = span_tags[2].text.strip()  # biasanya elemen ke-3 berisi lokasi
        elif len(span_tags) > 1:
            lokasi = span_tags[1].text.strip()

        # ambil pusat
        pusat_tag = soup.find('p', class_='mt-4 text-xl lg:text-2xl font-bold text-black-primary')
        if pusat_tag:
            pusat = pusat_tag.text.strip()
        else:
            pusat = None

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['Magnitude'] = magnitude
        hasil['kedalaman'] = kedalaman
        hasil['lokasi'] = lokasi
        hasil['pusat'] = pusat
        return hasil

    else:
        return None

def tampilkan_data(result):
    if result is None:
        print("tidak bisa menemukan data gempa terkini")
        return
    print('gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitude {result['Magnitude']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi: {result['lokasi']}")
    print(f"Pusat {result['pusat']}")

if __name__ == '__main__':
    print('ini adalah package gempa terkini')
    print('hai')



