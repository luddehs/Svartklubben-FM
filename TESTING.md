# Table of Contents
- [User Story Testing](#user-story-testing)
- [Validator Testing](#validator-testing)
  * [HTML](#html)
    + [Fixed Errors](#fixed-errors)
    + [Unfixed Errors](#unfixed-errors)
  * [CSS](#css)
  * [Javascript](#javascript)
  * [Python](#python)
  * [Lighthouse](#lighthouse)
- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing)
- [Manual Testing](#manual-testing)
  * [Site Navigation](#site-navigation)
  * [Home Page](#home-page)
  * [](#)
  * [](#r)
  * [](#)
  * [](#)
  * [](#)
  * [](#)
  * [](#)
  * [Django All Auth Pages](#django-all-auth-pages)
- [Bugs](#bugs)
  * [Fixed Bugs](#fixed-bugs)
    + [](#)
    + [](#)
  * [Unfixed bugs:](#unfixed-bugs-)¨


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
| base.html             |            0 |             0 |               0 |   0 |
| blog/index.html       |            0 |             0 |               0 |   0 |
| blog/post_detail.html |            0 |             0 |               0 |   0 |
| polls/index.html      |            0 |             0 |               0 |   0 |
| polls/detail.html     |            0 |             0 |               0 |   0 |
| polls/results.html    |            0 |             0 |               0 |   0 |
| polls/delete.html     |            0 |             0 |               0 |   0 |
| signup.html           |            0 |             0 |               0 |   0 |
| login.html            |            0 |             0 |               0 |   0 |
| logout.html           |            0 |             0 |               0 |   0 |
|                       |              |               |                 |     |
| Mobile                |              |               |                 |     |
| base.html             |            0 |             0 |               0 |   0 |
| blog/index.html       |            0 |             0 |               0 |   0 |
| blog/post_detail.html |            0 |             0 |               0 |   0 |
| polls/index.html      |            0 |             0 |               0 |   0 |
| polls/detail.html     |            0 |             0 |               0 |   0 |
| polls/results.html    |            0 |             0 |               0 |   0 |
| polls/delete.html     |            0 |             0 |               0 |   0 |
| signup.html           |            0 |             0 |               0 |   0 |
| login.html            |            0 |             0 |               0 |   0 |
| logout.html           |            0 |             0 |               0 |   0 |
|                       |              |               |                 |     |