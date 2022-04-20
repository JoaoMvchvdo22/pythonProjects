import time
import emoji

int(input('Digite o código para explodir os fogos: '))
for c in range(11, 0, -1):
    print(c-1)
    time.sleep(1)
print(emoji.emojize('\U0001f4a5 BOOM \U0001f4a5', language='alias'))