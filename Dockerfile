FROM python:3.10-slim-buster

ENV STRIPE_PUBLIC_KEY="pk_test_51MhTtvDzknVSuWagVjCQZCJHvE049oFr9wTQvZDnJatAw5zu5UjewGcXFPYOlMRJ2b9H98AueoajuapDTSGqYLdr00gp8XOL0e"

ENV STRIPE_SECRET_KEY="sk_test_51MhTtvDzknVSuWag6nlqoYoG8T8rXL8VNg1w7Z5WI3EccEqOY2BrUryrMi2gDbRWFb0PkTQnSMpYsZvZxPDGmfmR001rw6JBDO"

WORKDIR /django_stripe

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=django_stripe.settings

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["python", "create_superuser.py"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
