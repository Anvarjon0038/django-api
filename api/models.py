from tastypie.resources import ModelResource
from shop.models import Category,Course
from .authentification import CustomAuthentification
from tastypie.authorization import Authorization

#/api/v1/course/id
#api/v1/categories/id


class CategoryResource(ModelResource):
    class Meta:
        queryset=Category.objects.all()
        resource_name='categories'
        allowed_methods=['get']

class CourseResourse(ModelResource):
    class Meta:
        queryset=Course.objects.all()
        resource_name='courses'
        allowed_methods=['get','post','delete']
        authentication=CustomAuthentification()
        authorization=Authorization()

    def hydrate(self,bundle):
        bundle.obj.category_id=bundle.data['category_id']
        return bundle

    def dehydrate(self, bundle):
        bundle.data['category_id']=bundle.obj.category
        return bundle

    def dehydrate_title(self,bundle):
        #return bundle.data['title'].lower()
        return bundle.data['title'].upper()
