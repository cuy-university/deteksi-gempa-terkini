"""
Apliksi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""


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
    hasil = dict()
    hasil['tanggal'] = '28 Oktober 2025'
    hasil['waktu'] = '08:31:20 WIB'
    hasil['magnitudo'] = 5,5
    hasil['kedalaman'] = '10 km'
    hasil['lokasi'] = {'lu':1.43, 'bt':121.77}
    hasil['pusat'] = 'Pusat gempa berada di laut 68 km TimurLaut Buol'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): III-IV Kab. Buol, II-III Kab. Pohuwato, II-III Tolitoli, II Kab. Gorontalo Utara'

    return hasil


def tampilkan_data(result):
    print('gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi: LU={result['lokasi']['lu']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")


if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)
