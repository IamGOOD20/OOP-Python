

def version(patch, *args):
    num = '1.2.3.4.5.6.7.8.9.0.'
    if patch not in num:
        raise TypeError ('Mistake')
    else:
        return list(map(int, patch.split('.')))


print(version('we 2.3', 'patch 1'))
