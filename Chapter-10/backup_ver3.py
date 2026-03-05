import os
import time
import zipfile
from pathlib import Path

# ১. কনফিগারেশন (Pathlib ব্যবহার করে যা আধুনিক পাইথনের স্ট্যান্ডার্ড)
# আপনার সোর্স এবং ব্যাকআপ ডিরেক্টরি
source_dirs = [Path('/storage/emulated/0/Documents/notes')]
target_base_dir = Path('/storage/emulated/0/Documents/Backup')

# ২. আজকের তারিখ এবং সময়ের ফরম্যাট
today = target_base_dir / time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

# ৩. ইউজারের কাছ থেকে কমেন্ট নেওয়া
comment = input('Enter a comment:').strip()

# জিপ ফাইলের নাম নির্ধারণ (f-string ব্যবহার করে)
if not comment:
    zip_file_name = f"{now}.zip"
else:
    zip_file_name = f"{now}_{comment.replace(' ', '_')}.zip"

target_file_path = today / zip_file_name

# ৪. ডিরেক্টরি তৈরি করা (যদি না থাকে)
# exist_ok=True দিলে ফোল্ডার অলরেডি থাকলে এরর দেবে না
today.mkdir(parents=True, exist_ok=True)

print(f"Starting Backup Version 3.0...")
print(f"Target: {target_file_path}")

# ৫. জিপ তৈরির মূল প্রক্রিয়া (Pythonic Context Manager)
try:
    with zipfile.ZipFile(target_file_path, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
        for source in source_dirs:
            if source.exists():
                if source.is_dir():
# ফোল্ডারের ভেতরের সব ফাইল খুঁজে বের করা (Recursive)
                    for file in source.rglob('*'):
# শুধুমাত্র ফাইলগুলো জিপে যোগ করা (ফোল্ডার নয়)
                        if file.is_file():
                            backup_zip.write(file, file.relative_to(source.parent))
                else:
                    backup_zip.write(source, source.name)
            else:
                print(f"Warning: {source} does not exist. Skipping.")

    print(f"\nSuccessful backup!")
    print(f"Location: {target_file_path}")

except PermissionError:
    print("\nError: Storage permission denied! Please allow storage access in Pydroid 3 settings.")
except Exception as e:
    print(f"\nBackup Failed! Error: {e}")
