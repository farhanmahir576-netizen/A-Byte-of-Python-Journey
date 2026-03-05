def reverse (text):
	return text[::-1]
def is_palindrome(text):
	return text == reverse(text)

something = input ("Enter text:")
if is_palindrome(something):
	print("Yes, it is palindrome")
else:
	print("No, it is not palindrome")
