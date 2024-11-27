import pyautogui as pag
import time

def tag_all():
    # Input jumlah anggota grup dan pesan yang ingin dikirim
    n = int(input("Masukkan jumlah anggota grup: "))
    message = input("Masukkan pesan yang ingin dikirim: ")
    n_members = n-1

    # Delay 5 detik untuk membuka aplikasi WhatsApp
    time.sleep(5)

    # Mengetik pesan yang ingin dikirim
    pag.typewrite(message)
    pag.hotkey('shift', 'enter')

    # Melakukan tag ke setiap anggota grup
    for i in range(n_members):
        # Menekan tombol '@' untuk memulai tag
        pag.press('@')
        time.sleep(0.5)

        # Menekan tombol panah bawah sekali untuk memilih anggota grup
        pag.press('down')
        time.sleep(0.2)

        # Menekan tombol enter untuk melakukan tag ke anggota tersebut
        pag.press('enter')
        time.sleep(0.5)

# Menjalankan fungsi tag_all
tag_all()
pag.press('enter')