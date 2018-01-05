#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import httplib
import socket


def verify_status_code(url, protocole):
    """
    Verification du status code d'une request get
    :param str url: lien du site a cheker 
    :param str protocole: protocole utiliser
    :return: 
    """
    try:
        if protocole == 'http':
            conn = httplib.HTTPConnection(url)
            conn.request("GET", "/")
            reponse = conn.getresponse()
            print'\nStatus : ', reponse.status
            print'\nRaison : ', reponse.reason
            print'\nVersion du protocole utilisée par le serveur : ', reponse.version
            print

        elif protocole == 'https':
            conn = httplib.HTTPSConnection(url)
            conn.request("GET", "/")
            reponse = conn.getresponse()
            print'\nStatus : ', reponse.status
            print'\nRaison : ', reponse.reason
            print'\nVersion du protocole utilisée par le serveur : ', reponse.version
            print
        else:

            print'\nVérification du protocol choisir! '
    except socket.gaierror as e:
        print("Erreur : %s" % e)
