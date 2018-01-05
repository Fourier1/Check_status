#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from verify_status_code import verify_status_code


def set_options():
    """
    Entrer les options
    :return: 
    """
    parser = ArgumentParser()
    parser.add_argument('-u',
                        '--url',
                        dest='url',
                        required='True',
                        type=str,
                        help='Entrer l\'URL cible.')
    parser.add_argument('-p',
                        '--protocol',
                        dest='protocol',
                        required='True',
                        type=str,
                        help='Spécification du protocole sur l\'URL cible.')

    args = parser.parse_args()
    options = args.__dict__
    return options


if __name__ == '__main__':
    options = set_options()

    s = verify_status_code(options['url'],
                           options['protocol'])
