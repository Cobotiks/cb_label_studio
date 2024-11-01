from django.db import migrations
from django.db import connection
from django.conf import settings

from core.models import AsyncMigrationStatus
from core.redis import start_job_async_or_sync

import logging
logger = logging.getLogger(__name__)
migration_name = '0052_auto_20241101_1941'

if connection.vendor == 'sqlite':
    sql_update_created_at = """
    UPDATE tasks_tasklock
    SET created_at = datetime(expire_at, %s);
    """
    sql_params = (f'-{settings.TASK_LOCK_TTL} seconds',)
else:
    sql_update_created_at = """
    UPDATE tasks_tasklock
    SET created_at = expire_at - INTERVAL %s;
    """
    sql_params = ('%s seconds' % settings.TASK_LOCK_TTL,)

def forward_migration(migration_name):
    migration = AsyncMigrationStatus.objects.create(
        name=migration_name,
        status=AsyncMigrationStatus.STATUS_STARTED,
    )
    logger.info(f'Start async migration {migration_name}')

    with connection.cursor() as cursor:
        cursor.execute(sql_update_created_at, sql_params)

    migration.status = AsyncMigrationStatus.STATUS_FINISHED
    migration.save()
    logger.info(f'Async migration {migration_name} complete')

def forwards(apps, schema_editor):
    # Dispatch migrations to rqworkers
    start_job_async_or_sync(forward_migration, migration_name=migration_name)

def backwards(apps, schema_editor):
    pass

class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('tasks', '0051_tasklock_created_at'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
