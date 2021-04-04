import ipfshttpclient


ipfs_client = None


def ipfs_client_get():
    global ipfs_client
    return ipfs_client


def ipfs_client_set_maddr(maddr: str):
    global ipfs_client

    try:
        client = ipfshttpclient.connect(maddr)
    except Exception:
        ipfs_client = None
    else:
        ipfs_client = client
