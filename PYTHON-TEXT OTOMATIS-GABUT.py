import pyautogui
import time


# Masukkan teks yang ingin diketik secara otomatis
text = input("Masukkan teks yang ingin diketik secara otomatis: ")

# Masukkan jumlah pengulangan
num_iterations = int(input("Masukkan jumlah pengulangan: "))
time.sleep(5)

# Loop untuk jumlah pengulangan yang ditentukan
for _ in range(num_iterations):
    # Loop melalui setiap karakter dalam teks
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(0.1)  # Jeda X detik antara setiap karakter

    # Tekan tombol Enter untuk mengirimkan teks
    pyautogui.press('enter')


