from django.db import migrations

ARTICLE_TITLE = "How Jordan Peterson's Mind Was Forged: The Evolution of a Thinker"


def remove_article(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Post.objects.filter(title=ARTICLE_TITLE).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_seed_peterson_article'),
    ]

    operations = [
        migrations.RunPython(remove_article, migrations.RunPython.noop),
    ]
