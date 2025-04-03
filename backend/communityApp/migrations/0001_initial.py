# Generated by Django 5.1.6 on 2025-03-20 09:37

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('community_based_on', models.CharField(max_length=50)),
                ('rules', models.TextField(blank=True, max_length=500, null=True)),
                ('communityImage_url', models.URLField(default='https://res.cloudinary.com/dttdxreiq/image/upload/v1740721608/x4nd59qhqts2l670xzwx.png')),
                ('bannerImage_url', models.URLField(default='https://res.cloudinary.com/dttdxreiq/image/upload/v1740691299/vlcgkfx6ul17fvokugpv.png')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('text_field', models.TextField(max_length=1000)),
                ('media_file', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('likes_count', models.IntegerField(default=0)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='communityApp.community')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True, null=True)),
                ('profileImage_url', models.URLField(default='https://res.cloudinary.com/dttdxreiq/image/upload/v1740721608/x4nd59qhqts2l670xzwx.png')),
                ('bannerImage_url', models.URLField(default='https://res.cloudinary.com/dttdxreiq/image/upload/v1740691299/vlcgkfx6ul17fvokugpv.png')),
                ('date_joined', models.DateField(auto_now_add=True, null=True)),
                ('user_status', models.BooleanField(default=False)),
                ('saved_posts', models.ManyToManyField(blank=True, related_name='saved_by', to='communityApp.post')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='communityApp.profile'),
        ),
        migrations.AddField(
            model_name='post',
            name='shares',
            field=models.ManyToManyField(blank=True, related_name='shared_posts', to='communityApp.profile'),
        ),
        migrations.AddField(
            model_name='community',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='communities_joined', to='communityApp.profile'),
        ),
        migrations.AddField(
            model_name='community',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communities_created', to='communityApp.profile'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comments', models.TextField(blank=True, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='communityApp.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='communityApp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('replies', models.TextField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='communityApp.comments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='communityApp.profile')),
            ],
        ),
    ]
