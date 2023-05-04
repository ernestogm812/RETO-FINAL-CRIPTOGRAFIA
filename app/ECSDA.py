from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography import exceptions
import binascii
from ellipticcurve.utils.file import File
import sys

####ECSDA######
#signatureDer = File.read("/Users/macuser/Documents/TEC UNI/TEC SEM.6/Cryptography/Reto ECSDA/Andyboi.txt", "rb")
#data=signatureDer 

def digital_signature(data):

    ###another example#######
    private_key = ec.generate_private_key(ec.SECP384R1())
    public_key = private_key.public_key()
    pub=public_key.public_numbers()
    print ("Name of curve: ",pub.curve.name)
    try:  
        signature = private_key.sign(data,ec.ECDSA(hashes.SHA256()))
        print ("Good Signature: ",binascii.b2a_hex(signature).decode())
        return (binascii.b2a_hex(signature).decode())
        public_key.verify(signature, data, ec.ECDSA(hashes.SHA256()))
    except exceptions.InvalidSignature:
        print("A bad signature failed")
    else:
        print("Good signature verified")
    






