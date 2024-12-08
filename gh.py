import qrcode

# Daftar URL publik file HTML (unggah file ini ke layanan seperti Google Drive terlebih dahulu)
html_urls = [
    "https://drive.google.com/file/d/your_file_id_1/view?usp=sharing",  # Ganti dengan URL file pertama
    "https://drive.google.com/file/d/your_file_id_2/view?usp=sharing",  # Ganti dengan URL file kedua
]

# Membuat QR Code untuk setiap URL
for i, url in enumerate(html_urls, start=1):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Simpan QR Code sebagai gambar
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"tanaman_{i}_qr.png")

print("QR Code berhasil dibuat untuk semua URL publik.")
