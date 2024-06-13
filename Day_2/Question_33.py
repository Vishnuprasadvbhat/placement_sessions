sen = 'This is a sentence'


def largest(text):
    text = text.split()
    longest = max(text, key= len)
    return longest


nt = largest(sen)
print(nt)

sen =sen.split()
longest = max(sen, key=len)
print(longest)
