
# Instagram
## Instagram-App, 21st of October 2019
### By Aline Nicole UWAMARIYA
## Description
Instagram app is a web application which is created to be a website for the popular photo.
## Code scaffolding
Run python3.6 manage.py runserver when you want to implement the features of the landing pages and other pages.

## BDD
### Behaviour
We want our application to:
1.Sign in to the application to start using.
2.Upload my pictures to the application.
3.See my profile with all my pictures.
4.Follow other users and see their pictures on my timeline.
5.Like a picture and leave a comment on it.
## Input Examples
1.search users by profile.
2.Create a profile,registering,sign in,log in,leave a comment,etc

## Output Examples
any User will be able to see the photos he/she has posted and their likes and comments, and the user may be able to search for other users.

## TDD
I test my project using Python3.6 manage.py test insta(my app-name).

## Setup/Installation Requirements

1.Your application should be accessible to users on both desktop and mobile formats. You must ensure that your application is responsive to different screen sizes.
2.Your application should have a clean, simple, well-organized user interface. Ensure you choose a consistent colour scheme and use appropriate fonts for your application. Also, you MUST create a mockup design for your application before you begin development.
3.Your Project should contain an Image model with the following properties:

a.Image
b.Image Name.
c.Image Caption.
d.Profile Foreign key
e.Likes
f.Comments

4.Create the Profile model with the following properties:

a.Profile Photo
b.Bio

5.Your Image model should contain at least the following methods:

a.save_image() - Save an image to the database.
b.delete_image() - Delete image from the database.
c.update_caption() - Update image caption in the database.

6.You should write tests for each of these methods and make sure you implement error handlers to prevent your application from crashing.
7.our project must have a search form that when submitted calls a search function in the view function and redirects to a search results page.
8.When a user clicks on an Image he/she should be redirected to where the image is displayed and should also see the details of the Image.

9.Your application should have a solid authentication system that allows users to sign in or register into the application before using it. When a user registers with your application they should receive a confirmation email.

## Technology used
Python3.6
Django
Heroku
Bootstrap4

## My link repository on above

## Contact me on aline.nicole7@gmail.com
## Title Licence
Copyright(c)2019 Aline Nicole UWAMARIYA
