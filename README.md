# Bottega Pia
This is a full-stack frameworks project built using Django, Python, HTML, CSS and JavaScript. This is a restaurant website designed to display menus to customers & allow them to make reservations. It is an Italian resturant that serves great food. This project has been built for educational purpose.

[Live application can be found here](https://bottegapia.herokuapp.com/)

# Table of Contents
- [Bottega Pia](#bottega-pia)
- [Table of Contents](#table-of-contents)
  - [User Experience](#user-experience)
  - [Scope](#scope)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
  - [Surface](#surface)
  - [Technology Used](#technology-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Creating an Application with Heroku](#creating-an-application-with-heroku)
      - [Heroku](#heroku)
      - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)

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
- Register/login feature
- Contact form

## Structure
This website has been designed with simplicity in mind, each page only have entirely relevant information on it so that the user is able to find what they want quickly without having to read through unnessecary things. I have seperated out each key feature to really highlight their functionality to the user.

Database scheme for the menus

![here](assets/documents/images/menu-scheme.png)

## Skeleton
[Wireframes can be viewed here](assets/documents/wireframes/WIREFRAMES.md)

The theme of simplicity follows through to the design, I've used bootstrap columns and rows to divide the pages and tried to keep the same layout throughout so that the user has a sense of ease when on the various pages. 

## Surface
The colour pallete I have chosen for this website are from [coolers.co](https://coolors.co/5d737e-fdf7f7-64b6ac-e85d75-c76d7e). I like it because it has the Italian flag colours in it. I wanted a 'clean' feel and based it on greens to keep in theme with Italy. Italy will have a huge role in the design of the restaurant and the menu so I wanted there to be consistency.

![](assets/documents/images/bottega-theme.png)

I chose the fonts Exo and Roboto I wanted a bold/statement font to use for headings which is why I chose 'Exo' and then 'Roboto' for the general content as it's easier to read for the user.




## Technology Used
I have used several technologies that have enabled this design to work:
- [Django](https://www.djangoproject.com/)
    - Django is the framework that has been used to build the over project and it's apps.
- [Python](https://www.python.org/)
    - Python is the core programming language used to write all of the code in this application to make it fully functional.
- [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/)
    - For help with HTML and CSS layout 

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