__author__ = 'sanand'

# to reverse a text

def reverse(text):
    if len(text) < 1:
        return text
    return reverse(text[1:]) + text[0]

#s = "sacheen"

print(reverse("sacheen"))

