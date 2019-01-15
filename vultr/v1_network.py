'''Partial class to handle Vultr Network API calls'''
from .utils import VultrBase, update_params

class VultrNetwork(VultrBase):
    '''Handles Vultr Account API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def create(self, dcid, description=None, params=None):
        params = update_params(
            params,
            {'DCID'        : dcid,
             'description' : description if description else str() }
        )
        return self.request('/v1/network/create', params, 'POST')

    def destroy(self, networkid):
        params = update_params(
            params,
            {'NETWORKID' : networkid}
        )
        return self.request('/v1/network/destroy', params, 'POST')

    def list(self, params=None):
        params = params if params else dict()
        return self.request('/v1/network/list', params, 'GET')
