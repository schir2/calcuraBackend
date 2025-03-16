import uuid

from django.utils.text import slugify


def generate_slug_from_title(obj) -> str:
    base_slug = slugify(obj.title)
    slug = base_slug
    if not obj.slug or not obj.slug.startswith(base_slug):
        slug = base_slug
        if obj._meta.model.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{uuid.uuid4().hex[:8]}"
    return slug
