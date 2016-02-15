import hashlib

def _md5_for_file(f, block_size=2**20):
    md5 = hashlib.md5()
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)
    return md5.hexdigest()

def md5_for_file(fname):
    with open(fname, 'rb') as f:
        return _md5_for_file(f)
