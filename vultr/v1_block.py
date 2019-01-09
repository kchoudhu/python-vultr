'''Partial class to handle Vultr Account API calls'''
from .utils import VultrBase, update_params

class VultrBlockStore(VultrBase):
    '''Handles Vultr Account API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def attach(self, params=None):
        raise NotImplementedError()

    def create(self, dcid, size_gb, label=None, params=None):
        params = update_params(
            params,
            {'DCID'    : dcid,
             'size_gb' : size_gb,
             'label'   : label if label else str() }
        )
        return self.request('/v1/block/create', params, 'POST')

    def delete(self, subid, params=None):
        params = update_params(
            params,
            {'SUBID'   : subid }
        )
        return self.request('/v1/block/delete', params, 'POST')

    def detach(self, params=None):
        raise NotImplementedError()

    def label_set(self, subid, label, params=None):
        params = update_params(
            params,
            {'SUBID' : subid,
             'label' : label }
        )
        return self.request('/v1/block/label_set', params, 'POST')

    def list(self, params=None):
        params = params if params else dict()
        return self.request('/v1/block/list', params, 'GET')

    def resize(self, params=None):
        raise NotImplementedError()
