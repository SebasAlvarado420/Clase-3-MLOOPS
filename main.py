def suma(num_1 : int, num_2 : int) -> int:
    return num_1 + num_2

def resta(num_1 : int, num_2 : int) -> int:
    return num_1 - num_2



def gato(animal: str):
    if animal == 'cat':
        return True
    else:
        return False


if __name__ == '__main__':
    print(suma(num_1=2, num_2=4))
    print(resta(num_1=2, num_2=5))
    print(gato(animal='cat'))