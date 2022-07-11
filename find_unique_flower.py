
def create_flowerdict(filename):
    flower_dict = {}
    with open(filename) as flowers:
        for flower in flowers:
            key, val = flower.lower().strip().split(': ')
            flower_dict[key.strip()] = val.strip()
    return flower_dict


def main():
    flower_d = create_flowerdict('flowers.txt')
    fullname = input('Enter your First [space] Last name only: ')
    first_name = fullname[0].lower()
    first_letter = first_name[0]
    print('Unique flower name with the first letter: {}'.format(
        flower_d[first_letter]))


main()
