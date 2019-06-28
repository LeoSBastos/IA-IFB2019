#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:46:48 2019

@author: Jeronimo Hermano e Leonardo Bastos
"""
#Definicao da classe carro que tem seu modelo, eixo x(Carbono),
#eixo y(Milhagem) e sua classe(Centroid).
class Carro():
    
    def __init__(self, modelo, carbono, milhagem):
        self.modelo = modelo
        self.x = float(carbono)
        self.y = float(milhagem)
        self.classe = -1
