#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Yoav Ram <yoav@yoavram.com>
import click


def factorial(n):
	'''Calculate the factorial of n using recursion.
	'''
	if n < 1:
		return 1
	else:
		return n * factorial(n-1)


@click.argument('n', type=int)
@click.command()
def main(n):
	f = factorial(n)
	print("n! =", f)
	

if __name__ == '__main__':
	main()