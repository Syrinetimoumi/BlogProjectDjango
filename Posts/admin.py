from django.contrib import admin
from .models import Author, BlogPost

# Enregistrement du modèle Author dans l'admin
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

# Enregistrement du modèle BlogPost dans l'admin
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):  # Remarquez que nous utilisons BlogPostAdmin ici, pas AuthorAdmin
    list_display = ("title", "author", "created_on")  # Affichez ces champs dans l'admin
    list_editable = ("title",)  # Le champ 'title' peut être modifié directement depuis la liste
    list_display_links = ("author",)  # Le champ 'author' sera cliquable pour accéder à l'édition de l'article
    search_fields = ("title", "author__name")  # Permet de rechercher par titre et nom de l'auteur
    list_filter = ("author", "created_on")  # Permet de filtrer par auteur et par date de création
    list_per_page = 10  # Affiche 10 articles par page dans la liste d'administration
