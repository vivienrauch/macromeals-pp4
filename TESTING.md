# **Testing**

## **Code Validation**

<details>
<summary>HTML</summary>

The HTML files were validated with the [W3C Validator Service](https://validator.w3.org/).

- Home page - PASS

![html-validation-home](docs/html-validation-home-page.jpg)

- Sign Up - PASS

![html-validation-signup](docs/html-validation-signup.jpg)

- Sign In - PASS

![html-validation-signin](docs/html-validation-login.jpg)

- Logout - PASS

![html-validation-logout](docs/html-validation-logout.jpg)

- Recipes - PASS

![html-validation-recipes](docs/html-validation-recipes.jpg)


- Recipe detail

![html-validation-recipe](docs/html-validation-recipe.jpg)

- Add Recipe - 
I get several warnings and errors which either come from the crispy forms,
the summernote widgets or from the curly braces

Page source code:
![html-validation-add-recipe](docs/html-validation-add-recipe.jpg)

Workspace html file:
![html-validation-add-recipe-code](docs/html-validation-add-recipe2.jpg)

- Edit Recipe - PASS

![html-validation-edit-recipe](docs/html-validation-edit-recipe.jpg)

- Delete Recipe - PASS

![html-validation-delete-recipe](docs/html-validation-delete-recipe.jpg)

- Contact - PASS

![html-validation-contact](docs/html-validation-contact.jpg)

- Error page - The errors I get are due to the curly braces

Since all the custom error pages (403, 404, 405, 500) are equivalent in style, I only validated one of them

![html-validation-error](docs/html-validation-error.jpg)
</details>

<details>
<summary>CSS</summary>

The CSS file was validated using the [W3C Jigsaw Validator Service](https://jigsaw.w3.org/css-validator/).
It passed the validation process without warnings or errors.

![css-validation](docs/macromeals-css-valid.jpg)

</details>

<details>
<summary>Python</summary>

The Python files were validated using the [Pep8 linter](https://pep8ci.herokuapp.com/#)

- models.py - PASS

![python-validation-models](docs/python-validation-models-py.jpg)

- forms.py - PASS

![python-validation-forms](docs/python-validation-forms-py.jpg)

- views.py - PASS

![python-validaton-views](docs/python-validation-views-py.jpg)

- admin.py - PASS

![python-validation-admin](docs/python-validation-admin-py.jpg)

</details>

## **Lighthouse**

<details>
<summary>Desktop</summary>

- Home

![lighthouse-home](docs/lighthouse-home-desktop.jpg)

- Sign Up

![lighthouse-signup](docs/lighthouse-signup-desktop.jpg)

- Sign In

![lighthouse-login](docs/lighthouse-login-desktop.jpg)

- Logout

![lighthouse-logout](docs/lighthouse-logout-desktop.jpg)

- Recipes

![lighthouse-recipes](docs/lighthouse-recipes-desktop.jpg)

- Recipe - logged in

![lighthouse-recipe-li](docs/lighthouse-recipe-logged-in-desktop.jpg)

- Recipe - logged out

![lighthouse-recipe-lo](docs/lighthouse-recipe-logged-out-desktop.jpg)

- Add recipe

![lighthouse-add-recipe](docs/lighthouse-add-recipe-desktop.jpg)

- Edit recipe

![lighthouse-edit-recipe](docs/lighthouse-edit-recipe-desktop.jpg)

- Delete recipe

![lighthouse-delete-recipe](docs/lighthouse-delete-recipe.desktop.jpg)

- Contact

![lighthouse-contact](docs/lighthouse-contact-desktop.jpg)

</details>

<details>
<summary>Mobile</summary>

- Home

![lighthouse-home-m](docs/lighthouse-home-mobile.jpg)

- Sign Up

![lighthouse-signup-m](docs/lighthouse-signup-mobile.jpg)

- Sign In

![lighthouse-signin-m](docs/lighthouse-login-mobile.jpg)

- Logout

![lighthouse-logout-m](docs/lighthouse-logout-mobile.jpg)

- Recipes

![lighthouse-recipes-m](docs/lighthouse-recipes-mobile.jpg)

- Recipe - logged in

![lighthouse-recipe-li-m](docs/lighthouse-recipe-logged-in-mobile.jpg)

- Recipe - logged out

![lighthouse-recipe-lo-m](docs/lighthouse-recipe-logged-out-mobile.jpg)

- Add recipe

![lighthouse-add-recipe-m](docs/lighthouse-add-recipe-mobile.jpg)

- Edit recipe

![lighthouse-edit-recipe-m](docs/lighthouse-edit-recipe-mobile.jpg)

- Delete recipe

![lighthouse-delete-recipe-m](docs/lighthouse-delete-recipe-mobile.jpg)

- Contact

![lighthouse-delete-recipe-m](docs/lighthouse-contact-mobile.jpg)

</details>

## **Manual Testing**

| Registration | Expected results |
| --- | ---|
| A username is required | If the cell is empty an error message is shown. |
| A password is required | An error message is shown if the password is invalid or missing. |
| An email is optional | Shouldn't be an error message shown if left empty and no verification required. |
| Sign up button | The signup button validates the form and the user is able to log in afterwards. |

| Login/Logout | Expected results |
| --- | --- |
| Login | Previous registration is required for the user to be able to log in. The log in fields are obligatory. When a user is logged in, they should have access to the commenting, rating, and recipe management features. If they are not logged in, navigating to those pages whould land them to a 403 or 404 page. |
| Logout | Logout option is only available for logged in users. Upon clicking the logout button, user should not have access to the previously available features and they should be able to navigate to the login form again. |

| Recipe management | Expected results |
| --- | --- |
| Recipe creation | The user should be logged in to create a recipe. Once that feature is available in the naviagion bar, they should be directed to a form which can be saved after filling in the required fields. There is no admin authorization needed. |
| Recipe modification | The user should be logged in and be the author of the recipe to be able to modify it. If they don't have the access but navigate to that page anyway, they should be redirected to a 404 or 403 page. |
| Recipe deletion | The user should be logged in and be the author of the recipe to be able to delete it. If they don't have access but navigate to that page anyway, they should be redirected to a 404 or 403 page. |

| Commenting/Rating | Expected results |
| --- | --- |
| See comments | Any user should be able to see the comments under a recipe. |
| Commenting | The user should be able to comment under a recipe if they are logged in. The admin has to approve the comment before it is visible on the page. The user should get informed about it on the page. |
| See ratings | Any user should be able to see the ratings on the recipe cards and under an individual recipe. |
| Rating | Logged in users should be able to choose from the different levels of rating and save it with a button below. Rating doesn't requre teh admin's approval. |

| Contact | Expected results |
| --- | --- |
| Send message | Any user, reistered or non-registered can send a message via the form. All fields are required, they should be given an error if a field is left empty. |

| Error pages | Expected results |
| --- | --- |
| Custom error pages | The user should be redirected to one of the custom error pages if their request is invalid or some other interference occurs. On the error page they should be able to navigate back to he home page via the button under the error message or via the navigation bar.

| Navigation | Expected results |
| --- | --- |
| Navbar | The navbar buttons are named conveniently so that the user can expect that upon clicking them they will get to the page the link indicates. Different navbar links are available for authenticated and non-authenticated users, detailed above. |
| Buttons | Save, Send, Edit, Submit, Delete buttons are indicative of the action they will lead to. The user is redirected to the page the action took place in the first place, or in the case of error pages, the home page.|

## **Bugs**

- Fixed bugs

    - Deployment didn't work at first due to collectstatic error and crispy forms error.
      Crispy forms was installed however, it wasn't saved into the requirements.txt file.
      When I corrected that, it worked fine.

    - I had image issues when I tried to edit a recipe in the frontend.
      I changed the request to request files, too, it worked fine.

    - When editing the form, the page didn't render the preexisting form.
      I rewrote the code in a way that it's not a request but an UpdateView and also changed the url path.
      I can't pinpoint one thing that made the difference, I just adjusted the code until it finally clicked.

- Unfixed bugs

    - The Django frameworks handles the registration process, I didn't create a custom registration.
      There is an issue with signup, where if the user creates a weak password, they get an error that the password is too weak,
      but then they can't sign up with the same email address anymore, so the user is created anyway, despite the issue.

    - There is a console error message regarding Bootstrap's close event functionality that is used for the time out of the success
      and error messages.

    - I can't make the entry model choices (macro_high, macro_low, meal_type) to render on the saved page
      in a proper way.
      So it is only displayed when adding a recipe but not rendered on the saved recipe page.

    - I couldn't figure out how to resize the summernote widget field to fit the mobile screen properly.

    - For some reason the toggle navigation is stuck in an 'in-between' state on Ipad Mini screen.

Return to [README.md](README.md#macromeals-pp4)