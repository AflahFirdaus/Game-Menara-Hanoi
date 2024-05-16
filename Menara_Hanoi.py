class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.head
        self.head = self.head.next
        return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None

    def to_list(self):
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return result[::-1]

class MenaraHanoi:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.tiang = {
            'A': LinkedList(),
            'B': LinkedList(),
            'C': LinkedList()
        }
        for disk in range(num_disks, 0, -1):
            self.tiang['A'].push(disk)

    def cetak_tiang(self):
        for tower in ['A', 'B', 'C']:
            print(f"{tower}: {self.tiang[tower].to_list()}")
        print("\n")

    def pindah_cakram(self, dari_tiang, ke_tiang):
        if self.tiang[dari_tiang].is_empty():
            print(f"Error: Tiang {dari_tiang} kosong.")
            return False
        if not self.tiang[ke_tiang].is_empty() and self.tiang[ke_tiang].peek() < self.tiang[dari_tiang].peek():
            print(f"Anda Tidak bisa memindahkan cakram yang lebih besar ke atas cakram yang lebih kecil.")
            return False
        disk = self.tiang[dari_tiang].pop()
        self.tiang[ke_tiang].push(disk)
        print(f"Pindah cakram {disk} dari {dari_tiang} ke {ke_tiang}")
        self.cetak_tiang()
        return True

    def sudah_selesai(self):
        return self.tiang['C'].to_list() == list(range(self.num_disks, 0, -1))

def game():
    num_disks = int(input("Masukkan jumlah cakram: "))
    hanoi = MenaraHanoi(num_disks)
    print("Keadaan awal:")
    hanoi.cetak_tiang()

    while not hanoi.sudah_selesai():
        dari_tiang = input("Pindah dari (A, B, C): ").strip().upper()
        ke_tiang = input("Pindah ke (A, B, C): ").strip().upper()
        if dari_tiang in 'ABC' and ke_tiang in 'ABC':
            hanoi.pindah_cakram(dari_tiang, ke_tiang)
        else:
            print("Input tidak valid. Harap masukkan A, B, atau C.")

    print("Selamat! Anda berhasil menyelesaikan Game Menara Hanoi.")
    return input('Apakah ingin bermain lagi? (Y / T): ').strip().upper() == "Y"

def main():
    print('Selamat Datang di Game Menara Hanoi')
    while True:
        print('1. Main')
        print('2. Keluar')
        pilih = input('Pilih Menu Ke: ').strip()
        if pilih == "1":
            while game():
                pass
        elif pilih == "2":
            print('Keluar. Terima kasih!')
            break
        else:
            print('Input tidak valid!')

if __name__ == "__main__":
    main()
