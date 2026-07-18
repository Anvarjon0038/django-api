from tastypie.authentication import ApiKeyAuthentication

class CustomAuthentification(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
        if request.method!='GET':
            return super().is_authenticated(request, **kwargs)
        return True
