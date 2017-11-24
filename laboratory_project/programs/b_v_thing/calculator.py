import numpy as np 

def calc(sn):
    snd = 'data/' + sn + '.txt'
    with open(snd) as f:
        lines = f.readlines()
    
    data = np.zeros([len(lines),5])
    
    for i in range(len(data)):
        if i in {0,1}:
            pass
        else:
            split = lines[i].split()
            for k in range(5):
                data[i][k] = split[k]
    return data

def b_v(sn):
    data = calc(sn)

    bv_value = data[:,1] - data[:,3]
    bv_value = np.delete(bv_value, [0,1], axis=0)
    bv_value = np.abs(bv_value)
    bv_value = np.average(bv_value)

    print(bv_value)

if __name__ == '__main__':
    b_v('2017hhz')
