from RegressaoLinear import RegressaoLinear

def reader(file_name):
    x, y = [], []
    with open(file_name, 'r') as file:
        for l in file.read().split('\n'):
            words = list(l.split(','))
            x.append([1, int(words[0]), int(words[1])])
            y.append(int(words[2]))
    return x, y

if __name__ == "__main__":
    x, y = reader('data.txt')
    
    h = lambda teta, x: sum([(teta[i]*x[i]) for i in range(len(x))])
    #def h(teta, x): return sum((a * b) for a, b in zip(teta, x))
        
    r = RegressaoLinear(x, y, h)
    r.solve()

    print(r.test([1, 2104, 3]))
