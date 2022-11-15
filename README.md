# Bottega Pia
This is a full-stack frameworks project built using Django, Python, HTML, CSS and JavaScript. This is a restaurant website designed to display menus to customers & allow them to make reservations. It is an Italian resturant that serves great food. This project has been built for educational purpose.

[Live application can be found here](https://bottegapia.herokuapp.com/)

# Table of Contents
- [Bottega Pia](#bottega-pia)
- [Table of Contents](#table-of-contents)
  - [User Experience](#user-experience)
  - [Scope](#scope)
  - [Structure](#structure)
    - [Databases](#databases)
      - [Menus](#menus)
      - [Reservations](#reservations)
  - [Skeleton](#skeleton)
  - [Surface](#surface)
  - [Features](#features)
    - [Current Features](#current-features)
      - [Home page](#home-page)
      - [Menus - Food \& Drinks](#menus---food--drinks)
      - [Reservations](#reservations-1)
      - [Contact Form](#contact-form)
  - [Technology Used](#technology-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Creating an Application with Heroku](#creating-an-application-with-heroku)
      - [Heroku](#heroku)
      - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## User Experience
The user will be looking for:
- Informative website, with information that is easy-to-find & concise
- Current, up-to-date menus
- A booking form to make reservation enquiries with the restaurant

This website will offer all of these things whilst also allowing for intuitive navigation and comfortability of use. 

Due to the age group of the users, it is assumed that most users will be viewing the site on their mobile phones and therefore creating something responsive is integral to the design, I have used Bootstrap elements & custom CSS to allow for this.

## Scope
In order to acheuve the desired user & business goals the following features will be included in this release:

- Responsive navbar that will navigate to the various pages throughout the site
- Landing page with brief information about the restaurant and links to the menu and reservations page
- Menus page, with links to food & drinks menu respectively
- Reservations page, with booking form to enquire with the restaurant
- Register/login feature using Django allauth
- Contact form using Google SMTP

## Structure
This website has been designed with simplicity in mind, each page only have entirely relevant information on it so that the user is able to find what they want quickly without having to read through unnessecary things. I have seperated out each key feature to really highlight their functionality to the user.

The website is made of three apps:
1. Website - core functionality
2. Menus - menu display
3. Reservations - reservations enquiries & customer management

### Databases
The menus and reservations app both require databases to store information so I have built custom models.

#### Menus
FoodItem & DrinksItem are the model names for the menus app, these are two standalone models that provide all of the information required to display the items as part of the restaurant's menu. Each item has a name, description, price, dietary

#### Reservations
There are 3 models in this app, Customer, Table & Reservation. The combination of these 3 models allow for customer details to be stored, reservation enquiries to be made & managed & also enable availability checks whilst the user is enquiring.

For each reservation, there will be a customer & table assigned to it. The customer is assigned during the enquiry process and the tables are assigned in the backend by the admin user. This works for users that are logged in and also those that aren't. Logged in users will have their details associated with the user email address as this is how they are located in the customer model.

The tables model is also used to determine what the availability of the restaurant is like and this logic prevents bookings from being made if there are no tables available at the specified date and time.

Database scheme for the menus

![here](assets/documents/images/menu-scheme.png)

![here](assets/documents/images/database_reservations.jpg)

## Skeleton
[Wireframes can be viewed here](assets/documents/wireframes/WIREFRAMES.md)

The theme of simplicity follows through to the design, I've used bootstrap columns and rows to divide the pages and tried to keep the same layout throughout so that the user has a sense of ease when on the various pages. 

## Surface
The colour pallete I have chosen for this website are from [coolers.co](https://coolors.co/5d737e-fdf7f7-64b6ac-e85d75-c76d7e). I like it because it has the Italian flag colours in it. I wanted a 'clean' feel and based it on greens to keep in theme with Italy. Italy will have a huge role in the design of the restaurant and the menu so I wanted there to be consistency.

![](assets/documents/images/bottega-theme.png)

I chose the fonts Exo and Roboto I wanted a bold/statement font to use for headings which is why I chose 'Exo' and then 'Roboto' for the general content as it's easier to read for the user.

## Features

### Current Features

#### Home page
- **Navigation bar**: The navigation bar has links to all the active pages for the user and are clearly labelled, the menus option has a dropdown link to take the user to the food or drink menu. If the user is logged in then 'Logout' will appear otehrwsie the user will be given the option to 'Register' or 'Login'/ 
- **Menus image with link**: This image is clickable and will take the user to the menus page.
- **Reservations image with link**: This image is clickable and will take the user to the reservations page.
- **Footer**: The footer displays some of the restaurants key information and has links to social accounts. 

#### Menus - Food & Drinks
- **Seperate menus**: Each page displays all sections of the menus seperately, each menu item has the Dish/Drink name, dish/drink description, price, dietary information & any allergens. 

#### Reservations
- **Reservation form**: This page consists of the customer & reservation model forms, they are displayed together to appear as one. If the user is logged in then their name & email address are pre-populated.

#### Contact Form
- **Contact form**:



## Technology Used
I have used several technologies that have enabled this design to work:
- [Django](https://www.djangoproject.com/)
    - Django is the framework that has been used to build the over project and it's apps.
- [Python](https://www.python.org/)
    - Python is the core programming language used to write all of the code in this application to make it fully functional.
- [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/)
    - For help with HTML and CSS layout 
- [Google Fonts](https://fonts.google.com/)
    - Used to obtain the fonts linked in the header, fonts used were Playfair and Cookie
- [Font Awesome](https://fontawesome.com/)
    - Used to obtain the icons used on the high scores and rules pages.
- [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
    - Used as a primary method of fixing spacing issues, finding bugs, and testing responsiveness across the project.
- [GitHub](https://github.com/)
    - Used to store code for the project after being pushed.
- [Git](https://git-scm.com/)
- Google [sheets](https://www.google.com/sheets/about/)
- [Canva](https://www.canva.com/)
    - For image editing for readme wireframes.
- [Cloudinary](https://cloudinary.com/)
    - For media storage
- [Balsamiq](https://balsamiq.com/)
  - For wireframes and flow charts
- [Pep8](http://pep8online.com/)
  - Used to test my code for any issues or errors.
- [Heroku](https://www.heroku.com/)
    - For Deployment of this website
- [Color Contrast Accessibility Validator](https://color.a11y.com/)
    - To help test colours I will use
- [Coolers] (https://coolors.co)
    - To help find colours to use
- [W3C Markup Validation Service](https://validator.w3.org/) 
    - Used to validate all HTML code written and used in this webpage.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - Used to validate all CSS code written and used in this webpage.
- [Freeformatter CSS Beautify](https://www.freeformatter.com/css-beautifier.html)
    - Used to accurately format my CSS code.
- [Freeformatter HTML Formatter](https://www.freeformatter.com/html-formatter.html)
    - Used to accurately format my HTML code.
- [AmIResponsive](http://ami.responsivedesign.is/)
    - Used to generate responsive image used in README file.

## Testing
Testing Document is found [here](https://docs.google.com/spreadsheets/d/15nLGvvOe-gkxcLGmvUc7a_84_5jA6UGyUBGgMEQ42Fg/edit#gid=0)

## Deployment
To deploy my django application, I used [Code Institute Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)
- Click the `Use This Template` button.
- Add a repository name and brief description. 

### Creating an Application with Heroku
I followed the below steps using the Code Institute tutorial and [Django Blog cheatsheat](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit)
The following command in the Gitpod CLI will create the relevant files needed for Heroku to install your project dependencies `pip3 freeze --local > requirements.txt`. 

1. Go to Heroku.com and log in; if you do not already have an account then you will need to create one.
2. Click the New dropdown and select Create New App.
3. Enter a name for your new project, all Heroku apps need to have a unique name, you will be prompted if you need to change it.
4. Select the region you are working in.
  
#### Heroku 
- In the resources tab you must install 'Heroku Postgres' in the add-ons section
- You can set it to hobby for free use.

You will need to set your Environment Variables - this is a key step to ensuring your application is deployed properly.
- In the Settings tab, click on `Reveal Config Vars` and set the following variables:
    - Add key: `PORT` & value `8000`
    - SECRET_KEY - to be set to your chosen key
    - CLOUDINARY_URL - to be set to your cloudinary API environment varible
    - DATABASE_URL - For Postgres database, which should be filled in when `Heroku Postgres` is selected from add-ons
    - DISABLE_COLLECTSTATIC, 1 - Untill its ready for release
 
#### Heroku Deployment

In the Deploy tab:
1. Connect your Heroku account to your Github Repository following these steps:
2. Click on the `Deploy` tab and choose `Github-Connect to Github`.
3. Enter the GitHub repository name and click on `Search`.
4. Choose the correct repository for your application and click on `Connect`.
5. You can then choose to deploy the project manually or automatically, automatic deployment will generate a new application every time you push a change to Github, whereas manual deployment requires you to push the `Deploy Branch` button whenever you want a change made.
6. Once you have chosen your deployment method and have clicked `Deploy Branch` your application will be built and you should see the below `View` button, click this to open your application:



## Credits

https://startbootstrap.com/theme/agency helped with header
https://docs.djangoproject.com/en/4.1/
https://github.com/pennersr/django-allauth
https://jqueryui.com/
https://www.youtube.com/watch?v=TZL-WFzvDJg email

Matt Rudge for his Django I think therefore I blog on [Code Institute](https://codeinstitute.net)



## Acknowledgements

I would like to thank my course mentor Ronan McClelland for his support and guidance throughout the course of the project and Kasia Bogucka and my peers from Msletb slack group for their support & feedback.