"""
Endpoints of about
"""
class About_Endpoint_Endpoints:
    "class for about endpoints"

    def about_url(self,suffix=''):
        "append api endpoint to the base url"
        return self.auth_api_base_url+'api/v1/about'+suffix

    def get_version(self,headers,):
        "gets version"
        url = self.about_url(f"/version")
        response = self.get(url,headers=headers)
        return {
            'text':response.get('text',None),
            'json_response':response.get('json_response',{}),
            'status_code':response.get('status_code',None),
            'error':response.get('error',None)
        }