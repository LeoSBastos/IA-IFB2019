#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:46:48 2019

@author: jeronimo
"""

class Carro():
    
    def __init__(self, modelo, carbono, milhagem):
        self.modelo = modelo
        self.x = float(carbono)
        self.y = float(milhagem)
        self.classe = -1