from crypto.ascon import encrypt, decrypt
from utils.qr import generate_qr
import time

def generate_vfid(fid):
    timestamp = str(int(time.time()))
    return fid + timestamp

def create_qr(fid):
    vfid = generate_vfid(fid)
    encrypted_vfid = encrypt(vfid)
    generate_qr(encrypted_vfid)
    return encrypted_vfid

def process_scan(encrypted_data):
    try:
        decrypted_vfid = decrypt(encrypted_data)
        fid = decrypted_vfid[:16]
        return fid
    except:
        return None