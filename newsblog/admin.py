from django.contrib import admin
from .models import Article, Category, CustomUser
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('pk', 'title')
    list_editable = ('is_published', )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user

        super(ArticleAdmin, self).save_model(
            request=request, obj=obj, form=form, change=change
        )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(CustomUser)

