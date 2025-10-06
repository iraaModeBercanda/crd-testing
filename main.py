import time
import string

def tulis_huruf():
    # nama file
    nama_file = "ini_text.txt"
    
    # perulangan tak terbatas sampai dihentikan manual
    while True:
        with open(nama_file, "a") as file:  # "a" supaya terus menambahkan isi
            for huruf in string.ascii_lowercase:  # a-z
                file.write(huruf + "\n")
                file.flush()  # pastikan langsung tertulis ke file
                print(f"Menulis huruf: {huruf}")  # feedback ke terminal
                time.sleep(5)  # jeda 5 detik

if __name__ == "__main__":
    try:
        tulis_huruf()
    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh pengguna.")
