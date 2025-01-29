import crypt

def get_salt() -> str :
    return crypt.mksalt(crypt.METHOD_SHA256)