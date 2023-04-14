frase = 'aaaooo'

i = 0
HowMuch_times = 0
Most_Appeared = ''

while i < len(frase):
    now_letter = frase[i]

    if now_letter == ' ':
        i += 1
        continue

    HowMuch_now = frase.count(now_letter)

    if HowMuch_times < HowMuch_now:
        HowMuch_times = HowMuch_now
        Most_Appeared = now_letter

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{Most_Appeared}" que apareceu '
    f'{HowMuch_times}x'
)