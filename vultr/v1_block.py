'''Partial class to handle Vultr Account API calls'''
from .utils import VultrBase

class VultrBlockStore(VultrBase):
    '''Handles Vultr Account API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def attach(self, params=None):
        raise NotImplementedError()

    def create(self, params=None):
        raise NotImplementedError()

    def delete(self, params=None):
        raise NotImplementedError()

    def detach(self, params=None):
        raise NotImplementedError()

    def label_set(self, params=None):
        raise NotImplementedError()

    def list(self, params=None):
        ''' /v1/block/list
        GET - block
        Retrieve information about the c

        Link: https://www.vultr.com/api/#block
        '''
        params = params if params else dict()
        return self.request('/v1/block/list', params, 'GET')

    def resize(self, params=None):
        raise NotImplementedError()
