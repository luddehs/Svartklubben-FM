# Table of Contents
- [User Story Testing](#user-story-testing)
- [Validator Testing](#validator-testing)
  * [HTML](#html)
  * [CSS](#css)
  * [Javascript](#javascript)
  * [Python](#python)
  * [Lighthouse](#lighthouse)
- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing)
- [Manual Testing](#manual-testing)
  * [Site Navigation](#site-navigation)
  * [Home Page](#home-page)
  * [Blog Detail Page](#blog-detail-page)
  * [About Page](#about-page)
  * [Polls Index Page](#polls-index-page)
  * [Polls Detail Page](#polls-detail-page)
  * [Polls Results Page](#polls-results-page)
  * [Polls Delete Page](#polls-delete-page)
  * [Django All Auth Pages](#django-all-auth-pages)
- [Bugs](#bugs)
  * [Fixed Bugs](#fixed-bugs)
  * [Unfixed bugs](#unfixed-bugs)

## User Story Testing

### EPIC | User Navigation

#### Site Navigation

 *As a site user I can naturally navigate around the site so that I can easily find the content I am looking for.*

- A Navbar is visible on all pages, allowing the user to navigate to each section of the website.
- The title supports a link leading the user back to the landing page.
- The website features an "About" page that offers information about its purpose and background.
- The navbar displays options to register or log in.
 <details>

 <summary>Navigation Bar</summary>

![Navigation Bar](docs/readme_images/navbar-so.png)
</details>

<br/>

- Social media links is present the footer on all pages for easy access to the website's social media profiles.

<details>

 <summary>Footer</summary>

![Footer](docs/readme_images/footer.png)
</details>

<br/>

#### Select and View Blogposts

*As a site user I can view blog posts containing various content formats so that I can easily discover and listen to curated music selections.*

- Users can click on a blog post to enlarge it and view its content. The detailed view includes extended descriptions and other relevant information.
 <details>

 <summary>Blog Posts</summary>

![Blog Posts](docs/readme_images/blog-index.png)
</details>

<br/>

- Each blog post have its own section that includes a title, an image, a short description, and contains a clickable link that redirects the user to the corresponding source.
- The blog posts is designed to be responsive and look good on various devices, including desktops, tablets, and smartphones.

<details>

 <summary>Post Detail</summary>

![Post Detail](docs/readme_images/post-detail.png)
</details>

<br/>

### EPIC | User Navigation

#### Session Management

*As a site user I can remain signed in across different pages until I choose to sign out or my session expires so that I can manage the site efficiently without needing to sign in repeatedly.*

- The persistent login feature keeps users signed in across different pages until they manually sign out or the session expires.
<details>

 <summary>Navigation Bar</summary>

![Navigation Bar](docs/readme_images/navbar-si.png)
</details>

<br/>

- Signing out securely ends the session and redirects the user to a designated sign-out confirmation page or the home page.
<details>

 <summary>Sign Out</summary>

![Sign Out](docs/readme_images/sign-out.png)
</details>

<br/>

- All user actions are secure and protected against unauthorized access.

<br/>

 #### Super User Sign In

*As a site administrator I can sign in using a secure authentication method so that I can access the admin dashboard and manage the site effectively.*

- The sign-in page has fields for the administrator to enter their username and password.
- The sign-in process validates the administrator's credentials against the user database.
- After a successful sign-in, the administrator is redirected to the admin dashboard.
<details>

 <summary>Admin Sign In</summary>

![Admin Sign In](docs/readme_images/admin-si.png)
</details>

<br/>

#### CRUD Management

*As a site administrator I can manage items by creating, viewing, editing, and deleting them so that I can control the content on the website.*

- The site administrator has access to a management interface where they can view a list of all items.
- The management interface has options to create or add new entries, read or view existing entries, update or edit existing items, and delete or remove existing items.
- All changes made by the site administrator (create, read, update, delete) are reflected immediately in the database and on the website.
<details>

 <summary>Admin Panel</summary>

![Admin Panel](docs/readme_images/admin-panel.png)
</details>

<br/>

### EPIC | User Interaction

#### Site User Polls

*As a site user I can register and login to access the polls so that I can interact with the site creators and leave feedback by answering questions about the content of the site.*

- User registration and login functionality have been added to ensure that only authenticated users can participate in the polls.
- Logged-in users can access and participate in site polls.
<details>

 <summary>Polls Signed In</summary>

![Polls Signed In](docs/readme_images/polls-si.png)
</details>

<br/>

- Users can vote and then update or delete their choice.
<details>
  <summary>Polls CRUD</summary>

  ![Polls CRUD](docs/readme_images/polls-vote.png)  
  ![Polls CD](docs/readme_images/polls-cd.png)
</details>

<br/>
- All user actions are reflected with confirmation messages displayed on the website.
<details>
  <summary>Messages</summary>

  ![Message Succes](docs/readme_images/message-success.png)  
  ![Message Error](docs/readme_images/message-error.png)
  ![Message Info](docs/readme_images/message-info.png)
</details>

<br/>


## Validator Testing

### HTML

All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/). See results in below table.

| Page                   | Logged Out | Logged In |
|------------------------|------------|-----------|
| base.html              | No errors  | No errors |
| blog/index.html        | No errors  | No errors |
| blog/post_detail.html  | No errors  | No errors |
| about.html             | No errors  | No errors |
| polls/index.html       |    N/A     | No errors |
| polls/detail.html      |    N/A     | No errors |
| polls/results.html     |    N/A     | No errors |
| polls/delete.html      |    N/A     | No errors |
| signup.html            | No errors  |   N/A     |
| login.html             | No errors  |   N/A     |
| logout.html            |    N/A     | No errors |
| 400.html               | No errors  | No errors |
| 403.html               | No errors  | No errors |
| 404.html               | No errors  | No errors |
| 500.html               | No errors  | No errors |

### CSS
No errors were found when passing my CSS file through the official [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

 <details>

 <summary>CSS</summary>

![CSS Validation](docs/readme_images/css_validation.png)
 </details>

### Javascript
No errors were found when passing my javascript through [Jshint](https://jshint.com/) 

<details>

<summary>Jshint</summary>

![Jshint](docs/readme_images/jshint_validation.png)
</details>

### Python
All Python files were run through [Pep8](http://pep8online.com/) with no errors found.

### Lighthouse

Lighthouse validation was run on all pages (for both mobile and desktop versions) to assess accessibility and performance. 

| Page                  | Performance  | Accessibility | Best Practices  | SEO |
|-----------------------|:------------:|:-------------:|:---------------:|:---:|
|                       |              |               |                 |     |
| Desktop               |              |               |                 |     |
| base.html             |           95 |           100 |             100 | 100 |
| blog/index.html       |           95 |           100 |             100 | 100 |
| blog/post_detail.html |          100 |           100 |             100 | 100 |
| about.html            |           98 |           100 |             100 | 100 |
| polls/index.html      |           97 |            95 |             100 | 100 |
| polls/detail.html     |           99 |           100 |             100 | 100 |
| polls/results.html    |          100 |           100 |             100 | 100 |
| polls/delete.html     |           93 |           100 |             100 | 100 |
| signup.html           |          100 |            96 |             100 | 100 |
| login.html            |           99 |            96 |             100 | 100 |
| logout.html           |           95 |            96 |             100 | 100 |
|                       |              |               |                 |     |
| Mobile                |              |               |                 |     |
| base.html             |           76 |           100 |             100 | 100 |
| blog/index.html       |           76 |           100 |             100 | 100 |
| blog/post_detail.html |           93 |            96 |             100 | 100 |
| about.html            |           80 |           100 |             100 | 100 |
| polls/index.html      |           86 |            95 |             100 | 100 |
| polls/detail.html     |           91 |           100 |             100 | 100 |
| polls/results.html    |           93 |           100 |             100 | 100 |
| polls/delete.html     |           97 |           100 |             100 | 100 |
| signup.html           |           95 |            96 |             100 | 100 |
| login.html            |           92 |            96 |             100 | 100 |
| logout.html           |           92 |            96 |             100 | 100 |

## Browser Testing
- The website was tested on Google Chrome, Firefox, and Safari browsers, with no issues detected.

## Device Testing
- The website was tested on a range of devices, including desktop, laptop, tablet, and mobile, to verify responsiveness across different screen sizes in both portrait and landscape modes. It functioned as expected. Additionally, the responsive design was reviewed using Chrome Developer Tools across multiple device simulations, with the structural integrity remaining consistent for all sizes.

## Manual Testing

### Site Navigation
| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
|                       |            |                                                                    |           |
|                       |            |                                                                    |           |
|                       |            |                                                                    |           |

### Home Page
| Element               | Action  | Expected Result                 | Pass/Fail |
|-----------------------|---------|---------------------------------|-----------|
|                       |         |                                 |           |
|                       |         |                                 |           |
|                       |         |                                 |           |

### Blog Detail Page
| Element               | Action  | Expected Result                 | Pass/Fail |
|-----------------------|---------|---------------------------------|-----------|
|                       |         |                                 |           |
|                       |         |                                 |           |
|                       |         |                                 |           |

### About Page
| Element               | Action  | Expected Result                 | Pass/Fail |
|-----------------------|---------|---------------------------------|-----------|
|                       |         |                                 |           |
|                       |         |                                 |           |
|                       |         |                                 |           |

### Polls Index Page
| Element               | Action  | Expected Result                 | Pass/Fail |
|-----------------------|---------|---------------------------------|-----------|
|                       |         |                                 |           |
|                       |         |                                 |           |
|                       |         |                                 |           |

### Polls Detail Page
| Element               | Action  | Expected Result                 | Pass/Fail |
|-----------------------|---------|---------------------------------|-----------|
|                       |         |                                 |           |
|                       |         |                                 |           |
|                       |         |                                 |           |

### Polls Results Page
| Element               | Action  | Expected Result                 | Pass/Fail |
|-----------------------|---------|---------------------------------|-----------|
|                       |         |                                 |           |
|                       |         |                                 |           |
|                       |         |                                 |           |

### Polls Delete Page
| Element               | Action  | Expected Result                 | Pass/Fail |
|-----------------------|---------|---------------------------------|-----------|
|                       |         |                                 |           |
|                       |         |                                 |           |
|                       |         |                                 |           |

### Django All Auth Pages
| Element               | Action  | Expected Result                 | Pass/Fail |
|-----------------------|---------|---------------------------------|-----------|
|                       |         |                                 |           |
|                       |         |                                 |           |
|                       |         |                                 |           |

## Bugs 

### Fixed Bugs

### Unfixed bugs:
There are no known unfixed bugs. 