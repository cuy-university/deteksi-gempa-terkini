"""
Apliksi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
MODULARISASI DENGAN PACKAGE
"""
import deteksi_gempa_terkini

if __name__ == '__main__':
    print('Aplikasi utama')
    result = deteksi_gempa_terkini.ekstraksi_data()
    deteksi_gempa_terkini.tampilkan_data(result)

