# Generated by Django 4.1.5 on 2023-02-20 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dev', '0011_alter_credit_produit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credit',
            name='client',
        ),
        migrations.RemoveField(
            model_name='credit',
            name='produit',
        ),
        migrations.RemoveField(
            model_name='credit',
            name='quantite',
        ),
        migrations.RemoveField(
            model_name='credit',
            name='total_credits',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='updated',
        ),
        migrations.AlterField(
            model_name='produit',
            name='prix',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.CreateModel(
            name='ClientProduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dev.client')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dev.produit')),
            ],
        ),
        migrations.AddField(
            model_name='credit',
            name='client_produits',
            field=models.ManyToManyField(to='dev.clientproduit'),
        ),
    ]