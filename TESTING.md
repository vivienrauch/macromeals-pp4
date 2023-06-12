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

    - I can't make the entry model choices (macro_high, macro_low, meal_type) to render on the saved page
      in a proper way.
      So it is only displayed when adding a recipe but not rendered on the saved recipe page.

    - I couldn't figure out how to resize the summernote widget field to fit the mobile screen properly.

    - For some reason the toggle navigation is stuck in an 'in-between' state on Ipad Mini screen.

Return to [README.md](README.md#macromeals-pp4)