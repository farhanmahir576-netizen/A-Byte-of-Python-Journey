import os
import time
import zipfile
from pathlib import Path

# ১. কনস্ট্যান্ট সেটিংস (সবকিছু এক জায়গায় গুছিয়ে রাখা)
SOURCE_DIR = Path('/storage/emulated/0/Documents/notes')
BACKUP_BASE_DIR = Path('/storage/emulated/0/Documents/Backup')

# ২. তারিখ ও সময় অনুযায়ী পাথ তৈরি
def create_backup():
    today = BACKUP_BASE_DIR / time.strftime('%Y%m%d')
    now = time.strftime('%H%M%S')

# ৩. ইউজারের ইনপুট নেওয়া
    comment = input('Enter a comment:').strip()
    
# ফাইলের নাম নির্ধারণ (f-string ব্যবহার করে)
    file_suffix = f"_{comment.replace(' ', '_')}" if comment else ""
    target_zip = today / f"{now}{file_suffix}.zip"

# ৪. ডিরেক্টরি নিশ্চিত করা
    try:
        today.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"Error creating directory: {e}")
        return

# ৫. জিপ ফাইল তৈরির মূল প্রক্রিয়া (Context Manager ব্যবহার করে)
    print(f"Backup starting: {target_zip.name}...")
    
    try:
        with zipfile.ZipFile(target_zip, 'w', zipfile.ZIP_DEFLATED) as zip_out:
            if not SOURCE_DIR.exists():
                print(f"Source {SOURCE_DIR} not found!")
                return

# ফোল্ডারটি রিকার্সিভলি জিপ করা
            for file_path in SOURCE_DIR.rglob('*'):
# জিপের ভেতরে ফাইলগুলো সুন্দরভাবে সাজানো (Relative Path)
                zip_out.write(file_path, file_path.relative_to(SOURCE_DIR.parent))
                
        print("-" * 30)
        print(f"Backup Successful!")
        print(f"Location: {target_zip}")
        print("-" * 30)

    except Exception as e:
        print(f"Backup Failed!\nError: {e}")

if __name__ == '__main__':
    create_backup()
