from django.contrib import admin
from .models import Article,Category
# Register your models here..
def make_published(ModelAdmin,request,queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated ==1 :
        message_bit = 'یک مقاله  '
    else:
        message_bit = '{}مقاله  '.format(rows_updated)
    ModelAdmin.message_user(request,'{} با موفقیت یافت'.format(message_bit))
make_published.short_description= 'انتشار انتخاب شده ها'

def make_draft(ModelAdmin,request,queryset):
    rows_updated = queryset.update(status='d')
    if rows_updated ==1 :
        message_bit = 'یک مقاله  '
    else:
        message_bit = '{}مقاله  '.format(rows_updated)
    ModelAdmin.message_user(request,'{} با موفقیت یافت'.format(message_bit))
make_draft.short_description= 'پیش نویس انتخاب شده ها'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title','slug','parent','status')
    list_filter = (['status'])
    search_fields = ('title','slug')
    prepopulated_fields = {'slug':('title',)}
admin.site.register(Category,CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','thumbnail_tag','slug','author','jpublish','is_special','status','category_to_str')
    list_filter = ('publish','status','author')
    search_fields = ('title','description')
    prepopulated_fields = {'slug':('title',)}
    ordering = ['status','-publish']
    actions = [make_published,make_draft]
    
admin.site.register(Article,ArticleAdmin)