import os
import time
import zipfile

source = ['/storage/emulated/0/Documents/Pydroid3/world']
target_dir = '/storage/emulated/0/Documents/Pydroid3/backup'

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# ১. আজকের তারিখ নিয়ে একটি ফোল্ডার বানানো (আরো গোছানো রাখার জন্য)
today = target_dir + os.sep + time.strftime('%Y%m%d')
# ২. বর্তমান সময় ফাইলের নামের জন্য
now = time.strftime('%H%M%S')

# ইউজারের কাছ থেকে কমেন্ট নেওয়া
comment = input('Enter a comment --> ')

if len(comment) == 0: # যদি ইউজার কিছু না লেখে
    target = today + os.sep + now + '.zip'
else:
    # নামের মাঝখানে স্পেস থাকলে তা আন্ডারস্কোর দিয়ে রিপ্লেস করা
    target = today + os.sep + now + '_' + \
             comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# ৩. ব্যাকআপ শুরু
print("Backing up files...")
with zipfile.ZipFile(target, 'w') as zip_f:
    for folder in source:
        for root, dirs, files in os.walk(folder):
            for file in files:
                filepath = os.path.join(root, file)
                zip_f.write(filepath, os.path.relpath(filepath, os.path.join(folder, '..')))

print('Successful backup to:', target)
