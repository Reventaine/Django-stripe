# Django-stripe
Django app with Stripe API included<br>
## <a href="https://kind-river-b102c72d34ab4214bc176ba7236916e6.azurewebsites.net">Try it</a>

## Installation

1. Download and unpack code fron repo.
2. Create superuser <code>python manage.py createsuperuser</code> and set environment variables for stripe API <code>setx STRIPE_PUBLIC_KEY "YOUR STRIPE PUBLIC KEY", setx STRIPE_SECRET_KEY "YOUR STRIPE SECRET HERE"</code>
3. Run app <code>python manage.py runserver</code>
4. Go to http://127.0.0.1:8000/admin/ and create your Items, Discounts and Taxes.

![Screenshot 2023-03-06 123814](https://user-images.githubusercontent.com/56644580/223059281-256918cb-a030-4000-a78d-ebc1060a7d45.jpg)

5. http://127.0.0.1:8000/ to start using the app.

## Using Docker

1. <code>docker build -t docker_stripe .</code>
2. <code>docker run -p 8000:8000 docker_stripe</code>
3. And go through steps 4 and 5 from Installation.

![Screenshot 2023-03-06 123837](https://user-images.githubusercontent.com/56644580/223059322-5197ac96-568c-4a20-94fe-6f56fdfd362d.jpg)

![Screenshot 2023-03-06 123907](https://user-images.githubusercontent.com/56644580/223059343-72849d45-0025-43d7-ae59-c28b1ba26d94.jpg)

![Screenshot 2023-03-06 124131](https://user-images.githubusercontent.com/56644580/223059744-3400bbf7-bb98-414c-a70f-06ea585d7ac5.jpg)

![Screenshot 2023-03-06 124921](https://user-images.githubusercontent.com/56644580/223061666-bc6a6afa-aa70-49a9-b144-56f01f17e26d.jpg)

