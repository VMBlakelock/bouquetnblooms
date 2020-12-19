

<img src="static/images/mock-up-responsive.jpg">

# BouquetnBlooms

*Subscribe to have fresh BouquetBlooms everyday*

*Deployed to [Heroku](https://flask-saute-and-skewers.herokuapp.com/) and stored in [Github](https://github.com/)*

<hr>

## Contents

- [Introduction](#introduction)
- [Aim](#aim)
- [Purpose](#purpose)
- [UX](#ux)
- [Planes](#planes)
- [Features](#features)
- [Technologies](#technologies)
- [Testing](#testing)
- [Evaluation](#evaluation)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

<hr>

## Introduction

................................................

<hr>

### Aim

To create a full stack website that allows users to purchase a product or service.

Technologies to be used in the project are HTML/CSS/Javascript/Python3 and Django - v3.1.4.


### Purpose

BouquetBlooms is a floristry website in which users can subscribe to have fresh bouquets of flowers delivered to them monthly.

All users to the site will see the websites services. However only registered users can subscribe and order.


<hr>


## UX

## User stories

There are three types of users for this website, 'User Stories' for each user are discussed below:

### Guest User

As a guest user I want to:
 - navigate around the site easily.
 - find a navigation bar that links to other pages when clicked. 
 - understand the sites purpose upon landing.
 - be able to view the sites basic offerings.
 - be able to click social media icons to link out to other BouquetBlooms pages.
 - have the option to register to the site to be able to interact with the site, see more and make a purchase.

### Registered Account

As a registered user I want to:
 - see all site content.
 - log into the site easily.
 - log out successfully.
 - have buttons to click to login, log out and submit data.
 - be able to add services to my basket.
 - review the services in my basket before purchasing.
 - safe and secure area where I can add confidential data and payment details.
 - recieve and email when i've purchased something.
 - be able to cancel a subsription if I change my mind.
 - be notified of all my interactive actions.

### Admin User

As an admin user I want to:
- have full access to the site to ensure all content is viable.
- have access to be able to add more subscription offers to the site.
- edit any content posted by me.


### Website Owner

The website owner would like users of the website to:
-  Interact with the site.
-  Enjoy the site.
-  Find the site easy to register to and purchase services.

The website owner would like the website design to: 
- be clean and crisp with visuals that are minimal and of soft colours.
- have professional images that creates an instant attraction to the site.
- have whitespace to create flow.
- be easy to navigate.
- have a footer containing social media icon links.
- show the sites headquarters address.

<hr>

## The 5 Planes of content strategy

### Strategy

- BouquetBlooms is an e commerce website. It allows users to purchase a service. 
- This service is in the form of a subscription.
- The subscription is a one time payment and the service is then dispensed monthly by the retailer.
- The site features the 3 core languages of web development HTML, CSS and Javascript, as well as Python and Django. 
- The project uses a ...................... database. 
- There is a clear brand to the site that draws users and entices further interaction.
- Users who discover BouquetBlooms, love flowers and are excited to use the service.
- BouquetBlooms has the potential to become an excellent revenue generating business site. 
  Adding additional features (blog, client reviews for example) and marketing the site well could mean BouquetBlooms could generate even more revenues.
- During research there were other sites found that had the same 'subscription' concept, most offering a full inventory of products where as BouquetBlooms had just one subscription and one product set. 


### Scope 

- The site was developed with the intention of allowing users to subscribe and purchase a monthly BouquetBloom.
- The database of choice to build with was ...............
- It was scoped to provide ease of use.
- Have minimal pages, however must house a home page, registration page, log in page, log out page.
- Have and app that allowed users to purchase from the site.
- Be responsive on all devices.
- Be visually appealing that incorporated the beauty of  flowers and blooms in the front-end design.


### Structure

- BouquetBlooms site structure was created from the UX user stories - therefore developed with pages that were required to enable users to sign up and add data.
- All pages are designed identically with 3 sections - a navbar, content area and a footer.
- The Home page has 'Welcome' text that introduces the site. An 'About Us' section that gives instruction to join. A main image and 3 smaller images. 
- The Highlights page shows a selection of recipe content and images for all users to view. This can be updated and/or changed - as and when the owner wants.
- The Register page has a basic registration form with a button and a link to login if already registered.
- The Login page has a basic login form with a button and a link to register if not already a member. 
- Once logged in the Login page opens a Profile page, this shows a 'Welcome Back' text, a few enticing words and a links to the 'Add Recipe' 'Highlights' 'Recipes' Pages.
- The Add Recipe page is where users can add their own recipes. There is a form to complete and a 'Add Recipe' button to submit their recipe. 
  Once the recipe is submitted the user is redirected to the Recipes page with a flash message 'Recipe Successfully Added' here the user can see their new entry.
- The Recipes page is the home of user recipes already added. This is data stored in the MongoDB database.
- If logged in, a user can see all recipes in the database, with functionality to 'edit' or 'delete' their own.
- If the user wants to 'Edit' a recipe they created, they can click on the edit button and it will take them to the 'Edit Recipe' Page.
- The Edit Recipe page mirrors the Add Recipe page, however this has an additional 'Cancel' button in case the user changes their mind.
- If the user wants to 'Delete' an entry, they can click the 'Delete' button and the recipe will be deleted. The user is advised with a flash message 'Recipe has been deleted'.
- Users can only Edit or Delete their own recipes, buttons are not active on other users entries.
- Finally the Log Out page displays, a 'You have been logged out message' and the returns to the Log In page view.

### Skeleton

- Initially four wireframes where created - the three main pages of the site and a subscription page.
- These Desktop and Mobile wireframes demonstrate the basic design and structure of the site and the required elements each page needed. 
- All wireframes were created using [Balsamiq](https://balsamiq.com/wireframes/).

Desktop:

[Home](wireframes/base-desktop.png)
[Register](wireframes/register-desktop.png)
[Login](wireframes/login-desktop.png)
[Subscription](wireframes/subscription-desktop.png)

Mobile:

[Home](wireframes/base-mobile.png)
[Register](wireframes/register-mobile.png)
[Login](wireframes/login-mobile.png)
[Subscription](wireframes/subscription-mobile.png)

### Surface 

Front-end visuals where based on:
 - A great brand design.
 - Soft pastel colours in wallpapers.
 - Vibrant and professional flower and bouquet images.
 - Enticing and positive text.
 - It is anticipated that the user would feel happy and positive on landing on the site and feel they wanted to purchase something even if that wasnt their intention.

The typography colours and fonts where important to promote a calming effect but with a tempting feel good reaction that made the want to fullfil the sites output fully.
With vibrant flower images in all colours the sites aim was to incorporate the many different seasonal blooms on offer into its design. 

BouquetBlooms chose a simplistic design with whitespace so to not overpower the user.

 - colour: #555;  - from Colorcodehex 
 - font: 'Lato' - from Google Fonts

<hr>

## Features 

### Existing Features

**Multiple pages:** The site has multiple responsive pages, using the mobile first approach. 

**User friendly:** Each page has its own purpose and uses a simple mouse movement on desktop and scroll movement on mobiles and tablets to provide easy navigation. 

**Fonts and Colours:** Simplistic design incorporating only pastel colour and minimal text.

**Navbar:** A Bootstrap fixed Navbar at the top on desktop and a side navbar on mobiles and tablets. The navbar links to the site pages, this changes dependent on the users status: Logged in, Logged out.

**Button:** Chosen from Bootstrap the buttons when clicked do something and confirm user actions. Buttons are big and small an of different colours and provide 'word' instruction. 

**Forms:** Code from Bootstrap. The Register, Log In, pages both have forms on that are required to be completed. The forms are self explanatory.
They have input fields and textareas that are set with min-length and max-length classes.

**Icons:** Font Awesome icons are used on the form fields to provide instructions aswell as for design, the font awesome kit is used in the code. 

**Images:** Vibrant images are used in the design. Selected images provide an idea of the product on offer.

**Hyperlinks:** There is a hyperlink on the 'Register page', 'Login page' to redirect users to an alternative area dependent on their next wanted action.

**Search Bar:** Have a 'Search' bar, so users can search for specific recipe using key words.

**Footer:** The footer provides a clear indication of the end of the page.

**Social Media Links:** BouquetBlooms has various Social Media accounts therefore icons for these are found in the footer that will direct to the social site.

**Copyright:** Copyright logo - hosts the website owners own work.

########################################

**Flash Messages:** Flash messages provide feedback to users. Users that have an unsuccessful login will receive the message "Incorrect Username and/or Password".
The 'Registered users' will see, "Welcome, USERNAME" on login and on logging out user will receive the message "You have successfully logged out".
Flash messages are also used for confirming a recipe has been added, edited and deleted.

**Favourites Toggle:** A Favourites Toggle for the user to highlight if a recipe is a user favourite.

############################################

### Future Features

BouquetBlooms - Future features could include:

- Having a larger database of subscription packages for guest users to view and purchase.
- The subscriptions could be seasonal or weekly, have different price points.
- User profile to be created.
- Have a logo, that takes the BouquetBlooms text into something more memorable.
- Add a favicon so the sites logo is displayed in the browser tab for ease of navigation.
- A review score of the products.
- Feedback section to provide users with feedback on the sites product and services.
- Forgotten password feature, so passwords can be reset.
- A blog that gives advise and learnings on floristry.
- A messenger area where registered users can chat to a company employee live on the site.
- Expand the e commerce shop where users could order one time products and merchandise.

<hr>

## Technologies and Frameworks 


#### Technologies
- [HTML](https://www.w3schools.com/whatis/whatis_html.asp)
- [CSS](https://www.w3schools.com/css/css_intro.asp)
- [Javascript](https://www.w3schools.com/whatis/whatis_js.asp)
- [Python](https://www.python.org/doc/essays/blurb/)
- JSON

#### Frameworks
- [Django](https://www.djangoproject.com/)
    - The web application framework used in the project to allow fast and easy development of sites.

- [Werkzeug](https://palletsprojects.com/p/werkzeug/)
    - A web application library in Flask that was used to for secure authentication using password hashing.

- [Bootstrap](https://getbootstrap.com/)
    - A web based front-end framework that assists in responsiveness and styling that was used throughout the project.

- [JQuery](https://jquery.com/)
    - The JavaScript library used within the Materialize framework.

#### Database
- [........](https://www................../)
    - A document based database and the type of database used when developing this project

#### Text Editor
- [Gitpod](https://gitpod.io/)
    - A cloud based IDE, that uses prebuilt workspaces.

#### Version Control
- [Git](https://git-scm.com/)
    - Version control system that works within the Gitpod terminal. Used to commit and push recent code to GitHub.

#### Hosting Platform
- [Heroku](https://https://dashboard.heroku.com/)
    - The application platform used for the live deployed site.

- [Github](https://github.com/)
    - A repository store, used to house the sites repository.

#### Developer Tools
- [Google Dev Tools](https://developers.google.com/web/tools/chrome-devtools)

#### Colorcodehex
- [Colorcode](https://www.colorcodehex.com/022072.html)

#### Font Awesome
- [Font Awesome](https://fontawesome.com/)
    - Used for UX icons and getting 'kit' code.

#### RandomKeygen
- [RandomKeygen](https://www.randomKeygen.com/)
  - Site to select a secure SECRET_KEY password.

#### Validation sites
- [W3C Markup Validation](https://validator.w3.org/)
- [Jshint](https://jshint.com/)
- [PEP8](http://pep8online.com/)

<hr>

### Testing

Manual Testing was undertaken during the creation of this site. 
Testing included tests on various devices for responsiveness and UX aswell as testing code for bugs.
Code was validated for best practice.

 - Validation sites used:
   - W3C Markup Validator
   - Jshint
   - Pep8 Compliance

Below highlights the main issues, bugs and validation errors found during the development and how if possible the issues were rectified.
Some errors where not rectified, this was due to either lack of developer knowledge or due to time constraints for further reading of validation documentation and/or testing.


#### Issue 1

Issues with errors occurred when working on py files. I had to clear the errors Gitpod advised on. 
Most errors due to the 2 line spacing rule and using the tab key instead of spaces and also not entering to a new line.
Other errors included -*'lines being to long'* and *'Doctype must be declared'*.  
In previous module for using Flask it was advised that it is acceptable for the *'Doctype must be declared'* to be left uncleared as this was 
due to the linter Gitpod uses not understanding the template language Jinja. 

*When you save the file you might see a warning on the first line, 'Doctype must be declared first'. We can ignore this as the linter doesn't know how to properly read templating languages like Jinja*
Video: Flask Mini-Project 20 | 01 - Putting The Basics In Place (1e - Template Inheritance) 
[Code Institute](https://codeinstitute.net/)

Most errors where fixed except those of which the developer did not understand fully for example - 'imported but unused'.

#### Issue 2

SECRET KEY - During development the SECRET_KEY was accidently pushed to GitHub. The developer did not realise Django automatically
creates this and therefore pushed the code. On receiving the GitGuardian email the error was realized and a new env.py file was created
and a new Django SECRET_KEY added. However in the git commit history there is no confirmation code was pushed here as the next commit states *'index.html block content code added'*
Something for the developer to note for future 'all major changes and bug fixes to be commited and pushed for reference'.

#### Issue 3

When it came to adding datasets for the project it was advised to use [Kaggle](https://www.kaggle.com/).
However when researching and trying to download there was an error on the site *too many requests*. Reading through the documentation and forums it seems this is a 
known error. The developer requested advise from Code Institute on this matter to assist in moving forward with getting a dataset for the project.

#### Issue 4

During development the Gitpod terminal offered a warning. Advising that it was working with pip v20.2.4 and there was a new version and recommends and upgrade.
The developer followed the on terminal instructions and upgraded to v20.3.3.


#### Issue 5

At one point during development Python advised to install [Pillow](https://pillow.readthedocs.io/en/stable/). The developer did not have any knowledge of this imaging library.
The documentation was reviewed and the library was installed in the project.

#### Issue 6

It was found during development that the site definitely needed more pages adding. The initial four created an inception and wireframing wasn't going to be enough. 
This was to allow for guest users to see more than just the home page and register pages. It was realised the guest user needed to be enticed more. Therefore the Highlights page was created.
Furthermore the registered user required a profile page for when they logged in, and an add recipe, edit recipe and logout page. All additional pages have been created and are suitable for its purpose. 

### Validation sites

- When validating the code for HTML and CSS using [W3C Markup Validation](https://validator.w3.org/), errors where found and some were rectified, rectified errors included simple code errors and typos.
  However there were some errors the developer was unable to fix. Below shows a few examples.
  
  base.html
  - x errors found
  
  Error: xxx.
    At line x, column x   


- [Jshint](https://jshint.com/) for JS validation found error warnings, however many was of the same error. Unfortunately a fix wasn't implemented due to lack of understanding on how to resolve them and to time constraints. 
  Here are the errors for highlight.html
  - 4 errors found.

  Expected a string and instead saw %.
  Expected ':' and instead saw 'extends'.
  Expected '}' and instead saw '%'.
  Unrecoverable syntax error. (1% scanned).

- [PEP8](http://pep8online.com/) was used for testing Python errors.
  There were many errors on most pages, mostly referencing tabs and indentation. Again due to time constraints these errors were not rectified.
  Below are some common examples
    - missing whitespace around operator
    - trailing whitespace
    - indentation contains tabs


### Browsers tested

- Chrome: Using Google Developer Tools - Chrome was used for testing on Laptop, Tablet and Android devices.

- Safari: Safari wasn't used for testing on an I phone or Mac, due to not having physical access to these type of devices. However they were viewed on Google Dev Tools.

### Devices tested

On the final testing session the below devices where used to check if responsive, here are the outcomes.

Mobile:
- Android - Samsung Galaxy A40 - Outcome: All is responsive.
- Android - Samsung Galaxy A20 - Outcome: All is responsive.
- Android - Samsung Galaxy S10 - Outcome: All is responsive.

Laptop:
- Toshiba Satellite C850 - Outcome: All is responsive.
- HP Model I5 - Outcome: All is responsive.

The only responsive bug the developer found was on the [Techsini](https://techsini.com/multi-mockup/) - Responsive Mock up.
On the mock up it shows on I pad that the footer is half way up the page, however in Google Dev Tools this is not the case.
However due to not having an Apple Ipad to physically, it cannot be concluded the site is not responsive.   

<hr>
