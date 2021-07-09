# Fundizshop
A multi-vendor ecommerce web application.
Users can add products to cart and checkout using Mpesa or Paypal.

## [Usage](https://fundizshop.herokuapp.com/)

## Installation Instruction
To get the code..
1. Cloning the repository:
  ```bash
  git clone https://github.com/benjaminbills/fundizshop.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd fundizshop
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```
3. Migrate the application
  ```bash
  python3 manage.py makemigrations && migrate
  ```
4. Running the application
  ```bash
  python3 manage.py runserver
  ```

Open the application on your browser `127.0.0.1:8000`.

### Development

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request

### Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/benjaminbills/fundizshop/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/benjaminbills/fundizshop/issues/new). Please include sample queries and their corresponding results.

### Contributors
[Benjamin Obafemi](https://github.com/benjaminbills)

[Joy Kirii](https://github.com/Wakarende)

[Alvin Awour](https://github.com/Alvin-21)

[Paul Ngigi](https://github.com/Paul-Ngigi)

[Maryam Muchai](https://github.com/MaryamMuchai)

## Technologies Used.

- [Python](https://www.python.org/)- version 3.8.5.
- [Bootstrap](https://getbootstrap.com/)- version 5.0
- [Django](https://www.djangoproject.com/) - version 3.2
- [Django-oscar](http://oscarcommerce.com/) - version 3.0.2
- [Fontawesome](https://fontawesome.com/) - version 5
- [Cloudinary](https://cloudinary.com/)
- [sweetalert2](https://sweetalert2.github.io/)
- [Check requirements for more details](https://github.com/benjaminbills/fundizshop/blob/master/requirements.txt)

## Contact Information
If you have any enquiries you can reach out to us on the following emails
1. obafemibenjamins@gmail.com
2. joykirii@gmail.com
3. maryammuchai@gmail.com
4. alvinawuor8@gmail.com
5. paulkush7777@gmail.com

### Copyright and License
[MIT License](https://github.com/benjaminbills/fundizshop/blob/master/License)

