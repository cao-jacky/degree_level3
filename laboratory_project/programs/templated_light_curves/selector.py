# -*- coding: utf-8 -*-

import plotter

def supernova():
    sne = ['2017hhz', '2017hle']

    for i in range(len(sne)):
        plotter.data(sne[i])

if __name__ == '__main__':
    supernova()
