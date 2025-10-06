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
                file.flush()  # langsung tulis ke file
                print(f"Menulis huruf: {huruf} (tunggu 1 menit...)")
                time.sleep(60)  # jeda 1 menit per huruf

if __name__ == "__main__":
    try:
        tulis_huruf()
    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh pengguna.")
