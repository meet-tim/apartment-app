# apartment-app

# Django apartment listing App

The Django Airbnb App is a web application designed to facilitate the search for apartments. It provides a platform for property owners to list their properties, and users to search easily.

## Features

- **Property Listings:** Property owners can create listings for their vacation rentals, providing details such as property description, location, amenities, pricing, availability, and photos. Users can browse through the listings, view property details, and book their desired accommodations.

- **User Registration and Authentication:** The app supports user registration and authentication, allowing users to create accounts, log in securely, and personalize their experience within the app. Registered users can save favorite properties, manage bookings, and leave reviews.

- **Search and Filtering:** Users can search for vacation rentals based on location, dates, number of guests, and specific criteria such as amenities, property type, and price range. The app provides a user-friendly search interface with advanced filtering options to help users find their ideal accommodations.

## Installation

To install and run the Django Airbnb App on your local machine, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/meet-tim/apartment-app.git
   ```

2. Navigate to the project directory:

   ```
   cd apartment-app
   ```

3. Create a virtual environment:

   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - On macOS and Linux:

     ```
     source venv/bin/activate
     ```

   - On Windows:

     ```
     venv\Scripts\activate
     ```

5. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Set up the database:

   ```
   python manage.py migrate
   ```

7. Create a superuser (admin):

   ```
   python manage.py createsuperuser
   ```

8. Start the development server:

   ```
   python manage.py runserver
   ```

9. Open your web browser and navigate to `http://localhost:8000` to access the Django Airbnb App.

## Configuration

The Django Airbnb App can be configured by modifying the `config/settings.py` file. You can update the following settings:

- **Database:** Configure the database connection settings according to your requirements. By default, the app uses SQLite for local development.

- **Static and Media Files:** Configure the static and media file storage options, such as using a CDN or a local file system.

- **Email Settings:** Configure the email backend and credentials to enable features such as user registration, booking notifications, and password reset.


## Contributing

Contributions to the Django Airbnb App are welcome! If you encounter any bugs, have feature suggestions, or would like to contribute code improvements, please follow these steps:

1. Fork the repository.

2. Create a new branch:

   ```
   git checkout -b my-feature
   ```

3. Make the necessary changes and commit them:

   ```
   git commit -am 'Add my feature'
   ```

4. Push the changes to your forked repository:

   ```
   git push origin my-feature
   ```

5. Open a pull request on the main repository.

Please ensure your code follows the project's coding conventions and includes appropriate tests and documentation.

## License

The Django appartment App is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for both commercial and non-commercial purposes.
