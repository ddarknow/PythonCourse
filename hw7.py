#Reverse words in a string:

def reverse(st):
    x = st.split()
    x = list(reversed(x))
    return (" ".join(x))