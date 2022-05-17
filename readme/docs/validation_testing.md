# Code Validators and Website Analysis

[Click here to go to the Readme file ](https://github.com/ccarabine/coronavirusforum/blob/main/readme.md#validation-testing)

The website's pages was tested against the following validators:

## HTML Markup Validation Service
I used https://validator.w3.org/ to validate the html files

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
index.html                       |0 errors | [Results](../images/testing/html_validation/homepage.png)

<br>

## CSS Validation Service
I used https://jigsaw.w3.org/css-validator/ to validate the css(style.css)
<p>
    <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
static/css/style.css | Passed, No errors found | [Results]
(../images/testing/css_testing/css_validator_result.png) 

<br>

## Wave Accessibility
- Wave accessibility(https://wave.webaim.org/) was used to test the websites accessibility

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
index.html                        |0 errors and 0 contrast errors| [Results](../images/testing/wave_testing/home_page.png) 

postform.html(see below)       |2 errors and 0 contrast errors| [Results](docs/images/testing/wave_testing/issues/postform.png)
postlist.html                     |0 errors and 0 contrast errors| [Results](docs/images/testing/wave_testing/postlist.png)
postdetail.html                   |0 errors and 0 contrast errors| [Results](docs/images/testing/wave_testing/postdetail.png)
updatepost.html                   |0 errors and 0 contrast errors| [Results](docs/images/testing/wave_testing/updatepost.png) 
deletepost.html                   |0 errors and 0 contrast errors| [Results](docs/images/testing/wave_testing/deletepost.png)
commentform.html                  |0 errors and 0 contrast errors| [Results](docs/images/testing/wave_testing/commentform.png)
govukdata.html                    |0 errors and 0 contrast errors| [Results](docs/images/testing/wave_testing/govukdata.png) 
talkguidelines.html               |0 errors and 0 contrast errors| [Results](docs/images/testing/wave_testing/talkguidelines.png)
privacypolicy.html                |0 errors and 0 contrast errors| [Results](docs/images/testing/wave_testing/privacy_policy.png)
contactus.html                    |0 errors and 0 contrast errors| [Results](docs/images/testing/wave_testing/contact_us.png) 
aboutus.html                      |0 errors and 0 contrast errors| [Results](docs/images/testing/wave_testing/about_us.png)

Postform warning
- page title is missing or not descriptive, document language using the `<html lang>` attribute with a valid value (e.g., <html lang="en">).

- In  base.html this is included 
    `<html lang="en">`
    `<title>Corona Virus Forum</title>`

Some of the pages did not load correctly due to not being signed in
___

## JSHint
- JSHint(https://jshint.com/) was used to analyse the Javascript files

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
static/js/script.js | 0 errors and 1 warning | [Results](../images/testing/jshint_testing/jshint.png)

Warning -redefinition of alert
<br>

___

## PEP8online
- PEP8online was used to analyse the Python files (https://pep8online.com/)

Page | Errors|Results
------------ | -------------  | ------------- 
forum/admin.py | No errors/warnings| [Results](../images/testing/pep8_testing/admin.png)

forum/apps.py | No errors/warnings | [Results](docs/images/testing/pep8_testing/apps.png)
forum/forms.py | No errors/warnings | [Results](docs/images/testing/pep8_testing/forms.png)
forum/models.py | No errors/warnings | [Results](docs/images/testing/pep8_testing/models.png)
forum/signals.py | No errors/warnings | [Results](docs/images/testing/pep8_testing/signals.png)
forum/test_forms.py | No errors/warnings | [Results](docs/images/testing/pep8_testing/test_forms.png)
forum/test_models.py | No errors/warnings | [Results](docs/images/testing/pep8_testing/test_models.png)
forum/test_views.py | No errors/warnings | [Results](docs/images/testing/pep8_testing/test_views.png)
forum/urls.py | No errors/warnings | [Results](docs/images/testing/pep8_testing/urls.png)
forum/views.py | No errors/warnings | [Results](docs/images/testing/pep8_testing/views.png)
custom_storages.py | No errors/warnings| [Results](docs/images/testing/pep8_testing/custom_storages.png)
eny.py | No errors/warnings| [Results](docs/images/testing/pep8_testing/env.png)
manage.py | No errors/warnings| [Results](docs/images/testing/pep8_testing/manage.png)
___

## a11y Color Contrast Accessibility Validator

- Color accessibility(https://color.a11y.com/) was used to test the websites accessibility

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
index.html                        |0 automated color contrast issues| 
[Results](../images/testing/a11y/home_page.png)

postform.html                     |0 automated color contrast issues| [Results](docs/images/testing/a11y/postform.png)
postlist.html                     |0 automated color contrast issues| [Results](docs/images/testing/a11y/postlist.png)
postdetail.html                   |0 automated color contrast issues| [Results](docs/images/testing/a11y/postdetail.png)
updatepost.html                   |0 automated color contrast issues| [Results](docs/images/testing/a11y/updatepost.png) 
deletepost.html                   |0 automated color contrast issues| [Results](docs/images/testing/a11y/deletepost.png)
commentform.html                  |0 automated color contrast issues| [Results](docs/images/testing/a11y/commentform.png)
govukdata.html                    |0 automated color contrast issues| [Results](docs/images/testing/a11y/govukdata.png) 
talkguidelines.html               |0 automated color contrast issues| [Results](docs/images/testing/a11y/talkguidelines.png)
privacypolicy.html                |0 automated color contrast issues| [Results](docs/images/testing/a11y/privacy_policy.png)
contactus.html                    |0 automated color contrast issues| [Results](docs/images/testing/a11y/contact_us.png) 
aboutus.html                      |0 automated color contrast issues| [Results](docs/images/testing/a11y/about_us.png)

Some of the pages did not load correctly due to not being signed in such as create, update, delete post, create comment