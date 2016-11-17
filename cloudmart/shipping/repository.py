from oscar.apps.shipping import repository
from oscar.apps.shipping import methods
from oscar.core import prices
from decimal import Decimal as D

class Standard(methods.Base):
    code = 'standard'
    name = 'Standard shipping'
    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('5.00'), incl_tax=D('5.00'))

class Express(methods.Base):
    code = 'express'
    name = 'Express shipping'
    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('10.00'), incl_tax=D('10.00'))

class Repository(repository.Repository):
    methods = (Standard(), Express())