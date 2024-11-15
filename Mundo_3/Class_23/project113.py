def leia_int():
    while True:
        try:
            nmr1 = int(input(f'\nTYPE AN INTEGER NUMBER: '))
        except (ValueError, TypeError):
            print(f'NOT AN INT NUMBER!')
            continue
        except (KeyboardInterrupt):
            print(f'\nUSER HAS TYPED NOTHING! PROGRAM FINISHED. ')
            break
        else:
            return nmr1
        
def leiafloat():
    while True:
        try:
            nmr2 = input(f'\nTYPE A FLOAT NUMBER: ').replace(',','.')
            nmr2 = float(nmr2)
        except(ValueError, TypeError):
            print(f'NOT A FLOAT NUMBER!')
            continue
        else:
            return nmr2

n1 = leia_int()
n2 = leiafloat()
print(f'\nYOU TYPED {n1, n2}.\nBYE, IT WAS A PLEASURE!\n')