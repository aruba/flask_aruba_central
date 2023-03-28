#
# Import Aruba Central Base
from pycentral.base import ArubaCentralBase
from utility.central_info import central_info

def get_client():
    ssl_verify = True
    client = ArubaCentralBase(central_info=central_info,
                               ssl_verify=ssl_verify)

    return(client)
