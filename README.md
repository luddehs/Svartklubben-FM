# Svartklubben FM

Welcome to Svartklubben FM, a music blog dedicated to promoting music discovery and enhancing your listening experience. The app is targeted towards users who enjoy a wide range of music genres, whether you're looking for playlists curated to fit a specific mood or eager to discover tunes beyond the mainstream charts.

Svartklubben FM serves as a hub for music enthusiasts, offering frequently updated blogposts and the ability to subscribe to playlists, ensuring you always have music to enjoy.

The live link can be found here - []()

![Responsive]()

- [Svartklubben FM](#svartklubben-fm)
  * [User Experience (UX)](#user-experience-ux)
    + [User Stories](#user-stories)
    + [Design](#design)
      - [Colour Scheme](#colour-scheme)
      - [Imagery](#imagery)
      - [Fonts](#fonts)
      - [Wireframes](#wireframes)
  * [Agile Methodology](#agile-methodology)
  * [Data Model](#data-model)
  * [Testing](#testing)
  * [Security Features and Defensive Design](#security-features-and-defensive-design)
    + [User Authentication](#user-authentication)
    + [Form Validation](#form-validation)
    + [Database Security](#database-security)
    + [Custom error pages:](#custom-error-pages-)
  * [Features](#features)
    + [Header](#header)
    + [Footer](#footer)
    + [Home Page](#home-page)
    + [About Page](#about-page)
    + [Future Features](#future-features)
  * [Deployment - Heroku](#deployment---heroku)
  * [Forking this repository](#forking-this-repository)
  * [Cloning this repository](#cloning-this-repository)
  * [Languages](#languages)
  * [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
  * [Credits](#credits)
  * [Acknowledgments](#acknowledgments)

## User Experience (UX)

A visitor to Svartklubben FM is most likely an adult and a music enthusiast, although curiosity for music knows no age limit. They enjoy discovering music across various genres, appreciate reading blog posts about music and receiving curated playlists that fit their daily soundtrack.


### User Stories

#### EPIC | Site Administration
- As a site administrator I can manage items by creating, viewing, editing, and deleting them so that I can control the content on the website.
- As a site administrator I can sign in using a secure authentication method so that I can access the admin dashboard and manage the site effectively.
- As a site administrator I can remain signed in across different pages until I choose to sign out or my session expires so that I can manage the site efficiently without needing to sign in repeatedly.

#### EPIC | User Navigation
- As a site user I can naturally navigate around the site so that I can easily find the content I am looking for.
- As a site user I can view blog posts containing various content formats so that I can easily discover and listen to curated music selections.

#### EPIC | Content Management
- As a site user I can visit the about page to better understand the story and purpose of the site so that I feel a connection and trust in the content provided.

#### EPIC | User Interaction
- As a site user I can register and login to access the polls so that I can interact with the site creators and leave feedback by answering questions about the content of the site.

#### User stories not yet implemented

The following user stories were labeled as "Won't Have" on the GitHub project board and scoped out due to time constraints. They are intended to be implemented at a later date.

- As a site user I can register for the newsletter so that I receive regular updates and news directly to my email.
- As a site user I can support the site by giving a small amount using a service of my choice so that I can contribute to the upkeep and improvement of the site.



### Design

#### Colour Scheme

#### Imagery 

#### Fonts

#### Wireframes

<details>

 <summary>Landing Page</summary>

![Landing Page](docs/wireframes/landingpage-wf.png)
</details>

<details>

<summary>About Page</summary>

![About Page](docs/wireframes/about-wr.png)
</details>


<details>

<details>

<summary>Register</summary>

![Register](docs/wireframes/register-wr.png)
</details>

<summary>Sign In</summary>

![Sign In](docs/wireframes/signin-wr.png)
</details>

<details>

<summary>Account / Post</summary>

![Account / Post](docs/wireframes/account-post-wr.png)
</details>

## Agile Methodology

GitHub Projects was used to manage the development process with an agile approach. Please see the project board [here](https://github.com/users/luddehs/projects/2)

The four Epics listed above were documented as Milestones within the GitHub project. A GitHub Issue was created for each User Story and allocated to a corresponding Milestone (Epic). Each User Story includes defined acceptance criteria to clarify when the User Story is complete. The acceptance criteria are further broken down into tasks to facilitate the execution of the User Story.

## Data Model

## Testing

## Security Features and Defensive Design

### User Authentication

- Django's LoginRequiredMixin ensures that any requests to access secure pages by non-authenticated users are redirected to the login page. This guarantees that only logged-in users can access these pages.
- Django's UserPassesTestMixin restricts access based on specific permissions. It ensures that users can only edit or delete recipes and comments that they have authored. If a user fails the permission test, they receive an HTTP 403 Forbidden error.

### Form Validation 

### Database Security

### Custom error pages:

## Features

### Header


**Logo**

**Navigation Bar**


### Footer

### Home Page

### About Page

### Future Features

## Deployment

## Forking this repository

## Cloning this repository

## Languages

- Python
- Javascript
- HTML
- CSS

## Frameworks - Libraries - Programs Used

## Credits

## Acknowledgments
