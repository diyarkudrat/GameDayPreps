

# GameDayPreps

An application where coaches can keep track of their team's roster and itinerary schedule. This application also includes an attendance system where the coach marks the attendance status for each player in each event. It keeps previous attendance records of previous events.

# Getting Started

These instructions will give you the prerequisites to get this project up and running in your local machine. See deployment for notes on how to deploy the project on a live system.

# Prerequisites

1. pip3 install django

To have access to the unique built-in features for this framework

2. pip3 install gunicorn

For deployment purposes

3. Add Latest Bootstrap CSS and JS links to base template

This site was built using [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/).

# Deployment

To deploy live on Heroku you have to do 2 things:

    1. Add Procfile to root directory that contains

        web: gunicorn projectname.wsgi --log-file -
    
    2. Add requirements.txt to root directory that contains

        django==2.2.7
        gunicorn

# TechStack

    -Django
    -Bootstrap, html

