#==============================================================================
if platform.system().lower().startswith('win'):
    dllfile = 'ice_secp256k1.dll'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dllfile = dir_path + '/ice_secp256k1.dll'
    if os.path.isfile(dllfile) == True:
        pathdll = os.path.realpath(dllfile)
        ice = ctypes.CDLL(pathdll)
    else:
        print('File {} not found'.format(dllfile))

elif platform.system().lower().startswith('lin'):
    dllfile = 'ice_secp256k1.so'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dllfile = dir_path + '/ice_secp256k1.so'
    if os.path.isfile(dllfile) == True:
        pathdll = os.path.realpath(dllfile)
        ice = ctypes.CDLL(pathdll)