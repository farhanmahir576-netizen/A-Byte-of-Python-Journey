import os
import time
import zipfile

# ১. যে ফোল্ডারের ব্যাকআপ নিতে চান (আগে ফোনে এই ফোল্ডারটি তৈরি করুন)
source = ['/storage/emulated/0/Documents/Pydroid3/world']

# ২. ব্যাকআপ ফাইলটি যেখানে জমা হবে
target_dir = '/storage/emulated/0/Documents/Pydroid3/backup'

# ফোল্ডার না থাকলে তৈরি করে নেবে
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# ৩. ফাইলের নাম (আজকের তারিখ এবং সময়)
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# ৪. জিপ ফাইল তৈরি করার লজিক
print("Backing up files...")
with zipfile.ZipFile(target, 'w') as zip_file:
    for folder in source:
        for root, dirs, files in os.walk(folder):
            for file in files:
                filepath = os.path.join(root, file)
                # জিপ ফাইলের ভেতরে পাথ সেট করা
                zip_file.write(filepath, os.path.relpath(filepath, os.path.join(folder, '..')))

print('Successful backup to:', target)
