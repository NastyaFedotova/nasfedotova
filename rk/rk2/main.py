from operator import itemgetter
class Conductor:
    def __init__(self, id, name, age, band_id):
        self.id = id
        self.name = name
        self.age = age
        self.band_id = band_id

class Band:
    def __init__(self, id, bandname):
        self.id = id
        self.bandname = bandname

class ConductorofBand:
    def __init__(self, band_id, conductor_id):
        self.band_id = band_id
        self.conductor_id = conductor_id

# Оркестры
bands = [
    Band(1, 'Адажио'), Band(2, 'Струнный'), Band(3, 'Альт'),
    Band(11, 'Джазовый'), Band(22, 'Симфонический'), Band(33, 'Гармония'),
    ]

 # Дирижеры
conductors = [
    Conductor(1, 'Карлос Клайбер', 73, 2),
    Conductor(2, 'Леонард Бернстайн', 71, 1),
    Conductor(3, 'Клаудио Аббадо', 79, 3),
    Conductor(4, 'Пьер Булез', 80, 3),
    Conductor(5, 'Карло Мария Джулини', 90, 1),
    ]
conductors_of_bands = [ConductorofBand(1, 5),
    ConductorofBand(3, 4),
    ConductorofBand(3, 4),
    ConductorofBand(1, 2),
    ConductorofBand(2, 1),

    ConductorofBand(33, 1),
    ConductorofBand(22, 2),
    ConductorofBand(33, 4),
    ConductorofBand(11, 3),
    ConductorofBand(22, 5),
    ]


def part_1(one_to_many):
    res_11 = [(b.bandname, list(number for number, _, n in one_to_many if n == b.bandname)) for b in bands if b.bandname[0] == 'А']
    return res_11


def part_2(one_to_many):
    res_12_unsorted = []

    for b in bands:
        b_conductors = list(filter(lambda i:  i[2] == b.bandname, one_to_many))
        b_age = list(f[1] for f in b_conductors if f[2] == b.bandname)
        if len(b_conductors) > 0:
            max_age = max(b_age)
            res_12_unsorted.append((b.bandname, max_age))


    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    return res_12


def part_3(many_to_many):
    res_13 = []

    for conductor, _, band in many_to_many:
        res_13.append((band, conductor))
    res_13 = sorted(res_13, key=itemgetter(1))
    return res_13


def main():
    one_to_many = [(c.name, c.age, b.bandname)
                   for c in conductors
                   for b in bands
                   if c.band_id == b.id]

    many_to_many_temp = [(b.bandname, conb.band_id, conb.conductor_id)
                         for b in bands
                         for conb in conductors_of_bands
                         if b.id == conb.band_id]

    many_to_many = [(c.name, c.age, band_bandname)
                    for band_bandname, band_id, conductor_id in many_to_many_temp
                    for c in conductors if c.id == conductor_id]

    print(one_to_many)

    print(many_to_many)

    print('Задание Г1')
    print(part_1(one_to_many))
    print('\nЗадание Г2')
    print(part_2(one_to_many))
    print('\nЗадание Г3')
    print(part_3(many_to_many))


if __name__ == '__main__':
    main()
