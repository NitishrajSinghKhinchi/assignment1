"""This is group by owner function """

def group_by_owners(d):
    d1={}
    for key,value in d.items():
        if value not in d1:
            d1[value]=[]
            d1[value].append(key)
        else:
            d1[value].append(key)
    return d1

if __name__ == '__main__':
    d={
        'Input.txt':'Randy',
        'Code.py':'Stan',
        'Output.txt':'Randy',
        'num.py':'Bana',
        'pd.py':'Bana',
        'data.csv':'Raj'
    }
    print(group_by_owners(d))
    