import os
import time
import zipfile
from pathlib import Path

# ১. কনফিগারেশন:  Path ব্যবহার করা হয়েছে যা উইন্ডোজ এবং অ্যান্ড্রয়েড উভয় ক্ষেত্রে পাথ এরর কমায়
SOURCES = [Path('/storage/emulated/0/Documents/notes')]
TARGET_DIR = Path('/storage/emulated/0/Documents/backup')

# ২. টার্গেট ডিরেক্টরি চেক এবং তৈরি
def create_backup():
    if not TARGET_DIR.exists():
        TARGET_DIR.mkdir(parents=True, exist_ok=True)
        print(f"Directory has been created: {TARGET_DIR}")

    # ৩. ফাইলের নাম নির্ধারণ (তারিখ এবং সময় অনুযায়ী)
    timestamp = time.strftime('%Y%m%d_%H%M%S')
    target_zip = TARGET_DIR / f"backup_{timestamp}.zip"
    print("Backup getting started......")

# ৪. জিপ ফাইল তৈরি (Context Manager ব্যবহার করে)
    try:
        with zipfile.ZipFile(target_zip, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for source_path in SOURCES:
                if not source_path.exists():
                    print(f"Warning: Couldn't find {source_path}")
                    continue

# ফোল্ডারের ভেতরের সব ফাইল খুঁজে বের করা (Recursive):
                if source_path.is_dir():
                    for file in source_path.rglob('*'):
# আরকাইভের ভেতর সঠিক স্ট্রাকচারে ফাইল যোগ করা:
                        if file.is_file():
                            zip_file.write(file, file.relative_to(source_path.parent))
                else:
                    zip_file.write(source_path, source_path.name)

        print(f"Backup Done Successfully!")
        print(f"File Location: {target_zip}")

    except Exception as e:
        print(f"Backup Failed!")
        print(f"Error Detail: {e}")

if __name__ == "__main__":
    create_backup()
