#!/usr/bin/python3
# Author: Lucas C. Tavano & Lucas Amin
# Date: 13/01/2018

from Crypto.Cipher import PKCS1_OAEP  # pip3 install Crypto, pip3 install pycrypto
from Crypto.PublicKey import RSA
from helper import exceptionLogger
from helper import syscall


class crypto():
    @staticmethod
    def encrypt_RSA(public_key_loc, message):
        '''
        param: public_key_loc Path to public key
        param: message String to be encrypted
        return base64 encoded encrypted string
        '''

        key = open(public_key_loc, "r").read()
        rsakey = RSA.importKey(key)
        rsakey = PKCS1_OAEP.new(rsakey)
        encrypted = rsakey.encrypt(message.encode())  # [1:]
        return encrypted

    @staticmethod
    def decrypt_RSA(private_key_loc, encrypted_message):
        '''
        param: public_key_loc Path to public key
        param: message String to be encrypted
        return base64 encoded encrypted string
        '''

        key = open(private_key_loc, "r").read()
        rsakey = RSA.importKey(key)
        rsakey = PKCS1_OAEP.new(rsakey)
        encrypted = rsakey.decrypt(encrypted_message)

        return str(encrypted)
