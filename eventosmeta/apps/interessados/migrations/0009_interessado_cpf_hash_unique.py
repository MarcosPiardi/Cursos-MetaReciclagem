# Migration 0009 — Adiciona unique=True ao cpf_hash
# Executada APÓS popular_cpf_hash garantir que todos os registros têm hash único

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("interessados", "0008_interessado_cpf_hash"),
    ]

    operations = [
        migrations.AlterField(
            model_name="interessado",
            name="cpf_hash",
            field=models.CharField(
                blank=True,
                default="",
                help_text="SHA-256 do CPF — gerado automaticamente, não editar",
                max_length=64,
                unique=True,
                verbose_name="Hash do CPF",
            ),
        ),
    ]

    