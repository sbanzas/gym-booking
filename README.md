# gym-booking
Due to covid restrictions my local gym enforces us to book a place if we want to assist. This can be done only 24h before the class and bookings tipically only last for a couple of minutes, so that means most of the days i forget and i dont get a place.

This script run on an schedule on heroku and automatically books a place in the gym for tomorrow at 19.30. It uses selenium to go through the booking process, it waits until the booking button is available and then sends a screenshot with the confirmation screen, either directly to you or a telegram bot you designed.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/benru89/gym-booking)


