# ১. টুপল আনপ্যাকিং
def get_status():
    return (200, 'Success')

status_code, message = get_status()
print(f"Status: {status_code}, Message: {message}")

# ২. ল্যাম্বডা ফাংশন
points = [{'x': 2, 'y': 3}, {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
print("Sorted Points (by y):", points)

# ৩. লিস্ট কমপ্রিহেনশন
numbers = [1, 2, 3, 4, 5]
doubled_odds = [n * 2 for n in numbers if n % 2 != 0]
print("Doubled Odd Numbers:", doubled_odds)
