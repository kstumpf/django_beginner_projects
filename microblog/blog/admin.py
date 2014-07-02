from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    # Allows us to browse posts based on creation date.
    date_hierarchy = "created_at"

    # Lets us control which fields show up in the admin forum (and controls orders).
    fields = ("published", "title", "slug", "content", "author")

    # Control the lists shown on the list pages table.
    list_display = ["published", "title", "updated_at"]

    # Lets us control which column should be linked to the instance (edit page).
    list_display_links = ["title"]

    # Makes some comments editable from the list page.
    list_editable = ["published"]

    # Provides us with a set of filters to organize the list.
    list_filter = ["published", "updated_at", "author"]

    # SLUG FIELD DOESN'T AUTO-UPDATE
    prepopulated_fields = {"slug": ("title",)}

    search_fields = ["title", "content"]

admin.site.register(Post, PostAdmin)
