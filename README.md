

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
