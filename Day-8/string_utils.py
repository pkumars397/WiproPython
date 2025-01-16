def is_palindrome(s):
    s = s.lower().replace(" ", "").replace(",", "").replace(".", "")  # Normalize string
    return s == s[::-1]