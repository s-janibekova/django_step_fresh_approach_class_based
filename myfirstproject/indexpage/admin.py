from django.contrib import admin
from .models import Article

# Register your models here.
@admin.register(Article)
class ArticleModel(admin.ModelAdmin):

  def body_short(self, obj: Article):
    return f'{obj.body[:2]}...'

  list_display = ['id', 'title','body_short', 'type', 'pub_date']