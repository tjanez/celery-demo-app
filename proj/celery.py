from __future__ import absolute_import

from celery import Celery

app = Celery("proj", broker="amqp://", backend="amqp://", include=["proj.tasks"])

# Load configuration from the configuration object
app.config_from_object("proj.celeryconfig")

# Update the configuration
app.conf.update(
	CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
	app.start()

