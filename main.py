"""
Apliksi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
MODULARISASI DENGAN PACKAGE
"""
from deteksi_gempa_terkini import ekstraksi_data, tampilkan_data

if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)
