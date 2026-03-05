import os
import time
import zipfile
from pathlib import Path

# ১. কনফিগারেশন (Path অবজেক্ট ব্যবহার করে)- যে ফোল্ডারটি ব্যাকআপ নিতে চান
source_dir = Path('/storage/emulated/0/Documents/notes') 
# যেখানে ব্যাকআপ ফাইলটি সেভ হবে
base_backup_path = Path('/storage/emulated/0/Documents/backup')

# ২. সময় অনুযায়ী নাম তৈরি
today = base_backup_path / time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
target_zip = today / f"{now}.zip"

# ৩. ফোল্ডার তৈরি (যদি না থাকে)
# parents=True মানে মেইন ফোল্ডার না থাকলেও তৈরি হবে
#exist_ok=True মানে থাকলে Error দেবে না
today.mkdir(parents=True, exist_ok=True)
print(f"Backup target directory: {today}")

# ৪. জিপ ফাইল তৈরির মূল প্রক্রিয়া
try:
    print("Running Backup Version 2....")
    with zipfile.ZipFile(target_zip, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for file in source_dir.rglob('*'):
# rglob('*') দিয়ে ফোল্ডারের ভেতরের সব ফাইল ও সাব-ফোল্ডার খুঁজে বের করা হয়
            if file.is_file():
                zip_file.write(file, arcname=file.relative_to(source_dir.parent))
# arcname ব্যবহার করে জিপের ভেতর অপ্রয়োজনীয় পাথ বাদ দেওয়া হয়
    print(f"Successfully created backup: {target_zip}")

except Exception as e:
    print(f"Backup FAILED! Error: {e}")
