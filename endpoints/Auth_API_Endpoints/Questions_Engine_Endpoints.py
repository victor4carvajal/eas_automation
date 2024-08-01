"""
Endpoints of questions
"""
class Questions_Endpoint_Endpoints:
    "class for questions endpoints"

    def questions_url(self,suffix=''):
        "append api endpoint to the base url"
        return self.auth_api_base_url+'api/v1/questions'+suffix

    def get_questions(self,headers,):
        "gets questions"
        url = self.questions_url(f"")
        response = self.get(url,headers=headers)
        return {
            'text':response.get('text',None),
            'json_response':response.get('json_response',{}),
            'status_code':response.get('status_code',None),
            'error':response.get('error',None)
        }