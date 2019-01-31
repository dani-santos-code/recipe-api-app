# Recipe App 🍱

A Django app that displays recipes and its ingredients.

# Tech Stack 🚜

In this project, we use Docker to easily manage our environment. We use Postgres for the database. We use Django and the REST framework. We run integration tests with Travis CI.

# Starting the app 🎳

1. If you don't have Docker installed, please do so: https://hub.docker.com/editions/community/docker-ce-desktop-mac

2. To make sure your Docker is running correctly, run `docker -v`

3. In your root directory, build the Docker container by running `docker-compose build`

4. Run `docker-compose run app sh -c "django-admin.py startproject app ."` to create a new Django project
