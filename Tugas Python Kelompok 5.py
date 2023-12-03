import json                                                     #Mengimpor modul JSON untuk bekerja dengan data JSON.

class ProjectManager:                                           #Mendefinisikan kelas ProjectManager untuk mengelola proyek.
    def __init__(self, project_file='project_data.json'):       #Metode konstruktor kelas ProjectManager yang dijalankan saat objek dibuat. Menginisialisasi atribut, termasuk nama file proyek dan data proyek.
        self.project_file = project_file                        #Menetapkan atribut project_file dengan nama file proyek yang diberikan atau nilai default 'project_data.json'.
        self.project_data = self.load_project_data()            #Menetapkan atribut project_data dengan memanggil metode load_project_data() untuk membaca data proyek dari file.

    def load_project_data(self):                                #Metode untuk membaca data proyek dari file JSON.
        try:                                                    #Blok percobaan untuk membaca file JSON.
            with open(self.project_file, 'r') as file:          #Membuka file JSON untuk dibaca.
                project_data = json.load(file)                  #Membaca data proyek dari file JSON.
        except FileNotFoundError:                               #Tangkapan jika file tidak ditemukan.
            project_data = {"tasks": []}                        #Jika file tidak ditemukan, inisialisasi data proyek dengan struktur kosong.
        return project_data                                     #Mengembalikan data proyek.

    def save_project_data(self):                                #Metode untuk menyimpan data proyek ke file JSON.
        with open(self.project_file, 'w') as file:
            json.dump(self.project_data, file, indent=2)

    def add_task(self, task_name):                              #Metode untuk menambahkan tugas baru ke proyek.
        task = {"name": task_name, "status": "Menunggu Persetujuan"}
        self.project_data["tasks"].append(task)
        self.save_project_data()
        print(f'Proyek "{task_name}" Sukses Ditambahkan.')

    def remove_task(self, task_name):                           #Metode untuk menghapus tugas dari proyek.
        tasks = self.project_data["tasks"]
        for task in tasks:
            if task["name"] == task_name:
                tasks.remove(task)
                self.save_project_data()
                print(f'Task "{task_name}" removed successfully.')
                return
        print(f'Task "{task_name}" not found.')

    def assign_task(self, task_name, assignee):                 #Metode untuk menetapkan penugasan kepada tugas.
        for task in self.project_data["tasks"]:
            if task["name"] == task_name:
                task["assignee"] = assignee
                task["status"] = "Sedang Dilakukan"
                self.save_project_data()
                print(f'Proyek "{task_name}" Disetujui Oleh {assignee}.')

    def track_progress(self):                                   #Metode untuk melacak kemajuan proyek dan menampilkan laporan.
        for task in self.project_data["tasks"]:
            print(f'Proyek: {task["name"]}, Mensetujui: {task.get("assignee", "Belum Ditandai")}, Status: {task["status"]}')

if __name__ == "__main__":                                      #Blok kode yang akan dijalankan jika skrip dijalankan sebagai program utama (bukan diimpor sebagai modul).
    project_manager = ProjectManager()                          #Membuat objek ProjectManager saat skrip dijalankan.

    while True:                                                 #Looping tanpa akhir untuk memungkinkan pengguna memilih operasi hingga mereka memilih untuk keluar.
        print("\nSistem Pengelolaan Proyek")
        print("1. Tambah Proyek")
        print("2. Hapus Proyek")
        print("3. Tandai Proyek")
        print("4. Lacak Tugas")
        print("5. Keluar")

        choice = input("Masukkan pilihan Anda (1-5): ")

        if choice == "1":
            task_name = input("Masukan Nama Proyek: ")
            project_manager.add_task(task_name)
        elif choice == "2":
            task_name = input("Masukan Nama Proyek: ")
            project_manager.remove_task(task_name)
        elif choice == "3":
            task_name = input("Masukan Nama Proyek: ")
            assignee = input("Masukan Nama Yang Mensetujui Proyek: ")
            project_manager.assign_task(task_name, assignee)
        elif choice == "4":
            project_manager.track_progress()
        elif choice == "5":
            break
        else:
            print("Pilihan tidak valid. Masukkan angka antara 1 dan 5.")
