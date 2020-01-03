# Generated by Django 3.0 on 2020-01-03 04:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('men_number', models.IntegerField()),
                ('women_number', models.IntegerField()),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('venue', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('userinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='match.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fromid', to='match.UserInfo')),
                ('to_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toid', to='match.Posts')),
            ],
        ),
        migrations.CreateModel(
            name='ChatRoomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roomuser_roomid', to='match.ChatRoom')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roompost_postid', to='match.Posts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roomuser_userid', to='match.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500)),
                ('chat_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_roomid', to='match.ChatRoom')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_postid', to='match.Posts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_userid', to='match.UserInfo')),
            ],
        ),
    ]
