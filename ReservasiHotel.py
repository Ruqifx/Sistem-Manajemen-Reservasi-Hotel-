class Hotel:
    def __init__(self):
        self.rooms = []  # List untuk menyimpan informasi kamar
        self.stack = []  # Stack untuk implementasi LIFO
        self.queue = []  # Queue untuk implementasi FIFO

    def add_room(self, room_id, room_type, price):
        room = {"ID": room_id, "Type": room_type, "Price": price, "Status": "available"}
        self.rooms.append(room)
        self.stack.append(room)
        self.queue.append(room)
        print(f"Kamar {room_id} berhasil ditambahkan.")

    def display_rooms(self):
        if not self.rooms:
            print("Tidak ada kamar yang tersedia.")
            return
        print("\nDaftar Kamar:")
        print(f"{'ID':<10} {'Tipe':<15} {'Harga':<10} {'Status':<10}")
        print("-" * 45)
        for room in self.rooms:
            print(f"{room['ID']:<10} {room['Type']:<15} {room['Price']:<10} {room['Status']:<10}")
        print()

    def update_room(self, room_id, new_type=None, new_price=None):
        for room in self.rooms:
            if room["ID"] == room_id:
                if new_type:
                    room["Type"] = new_type
                if new_price:
                    room["Price"] = new_price
                print(f"Kamar {room_id} berhasil diperbarui.")
                return
        print(f"Kamar {room_id} tidak ditemukan.")

    def delete_room(self, room_id):
        for room in self.rooms:
            if room["ID"] == room_id:
                self.rooms.remove(room)
                self.stack.remove(room)
                self.queue.remove(room)
                print(f"Kamar {room_id} berhasil dihapus.")
                return
        print(f"Kamar {room_id} tidak ditemukan.")

    def search_room(self, room_id):
        for room in self.rooms:
            if room["ID"] == room_id:
                print(f"Kamar Ditemukan: {room}")
                return room
        print(f"Kamar {room_id} tidak ditemukan.")
        return None

    def sort_rooms_by_price(self):
        self.rooms.sort(key=lambda x: x["Price"])
        print("Kamar berhasil diurutkan berdasarkan harga.")

    def display_stack(self):
        if not self.stack:
            print("Stack kosong.")
            return
        print("\nKamar dalam Stack (LIFO):")
        for room in reversed(self.stack):
            print(f"{room['ID']} - {room['Type']} ({room['Price']})")
        print()

    def display_queue(self):
        if not self.queue:
            print("Queue kosong.")
            return
        print("\nKamar dalam Queue (FIFO):")
        for room in self.queue:
            print(f"{room['ID']} - {room['Type']} ({room['Price']})")
        print()

# Menu Utama
def main_menu():
    hotel = Hotel()
    while True:
        print("=== Sistem Reservasi Hotel ===")
        print("1. Tambah Kamar")
        print("2. Tampilkan Semua Kamar")
        print("3. Update Kamar")
        print("4. Hapus Kamar")
        print("5. Cari Kamar")
        print("6. Urutkan Kamar Berdasarkan Harga")
        print("7. Tampilkan Kamar di Stack (LIFO)")
        print("8. Tampilkan Kamar di Queue (FIFO)")
        print("9. Keluar")
        choice = input("Pilih menu (1-9): ")
        print()
        if choice == "1":
            room_id = input("Masukkan ID Kamar: ")
            room_type = input("Masukkan Tipe Kamar: ")
            price = float(input("Masukkan Harga Kamar: "))
            hotel.add_room(room_id, room_type, price)
        elif choice == "2":
            hotel.display_rooms()
        elif choice == "3":
            room_id = input("Masukkan ID Kamar yang ingin diupdate: ")
            new_type = input("Masukkan Tipe Baru (kosongkan jika tidak ingin mengubah): ")
            new_price = input("Masukkan Harga Baru (kosongkan jika tidak ingin mengubah): ")
            new_price = float(new_price) if new_price else None
            hotel.update_room(room_id, new_type if new_type else None, new_price)
        elif choice == "4":
            room_id = input("Masukkan ID Kamar yang ingin dihapus: ")
            hotel.delete_room(room_id)
        elif choice == "5":
            room_id = input("Masukkan ID Kamar yang ingin dicari: ")
            hotel.search_room(room_id)
        elif choice == "6":
            hotel.sort_rooms_by_price()
        elif choice == "7":
            hotel.display_stack()
        elif choice == "8":
            hotel.display_queue()
        elif choice == "9":
            print("Terima kasih telah menggunakan Sistem Reservasi Hotel!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

# Jalankan Program
if __name__ == "__main__":
    main_menu()
