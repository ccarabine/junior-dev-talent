# Code Validators and Website Analysis

[Click here to go to the Readme file ](https://github.com/ccarabine/junior-dev-talent/blob/main/readme.md#validation-testing)

The website's pages was tested against the following validators:

## HTML Markup Validation Service
I used https://validator.w3.org/ to validate the html files

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
index.html                       |0 errors | [Results](../images/testing/html_testing/index.png)
privacy_policy.html              |0 errors | [Results](../images/testing/html_testing/privacy_policy.png)
forum - forum.html               |0 errors | [Results](../images/testing/html_testing/forum.png)
profiles- subscription.html      |0 errors | [Results](../images/testing/html_testing/subscription.png)
profiles- profile_type.html      |0 errors | [Results](../images/testing/html_testing/profile_type.png)
profiles- register_user_type.html|0 errors | [Results](../images/testing/html_testing/register_user_type.png)
products- products.html          |0 errors | [Results](../images/testing/html_testing/products.png)
products- product_detail.html    |0 errors | [Results](../images/testing/html_testing/product_detail.png)
checkout- checkout.html          |0 errors | [Results](../images/testing/html_testing/checkout.png)
checkout -checkout_success.html  |0 errors | [Results](../images/testing/html_testing/checkout_success.png)
checkout- basket.html          |0 errors | [Results](../images/testing/html_testing/basket.png)
404errors.html          |0 errors | [Results](../images/testing/html_testing/404.png)
500errors.html          |0 errors | [Results](../images/testing/html_testing/500.png)

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

all css files
Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
static/css/style.css | Passed, No errors found | [Results](../images/testing/
css_testing/css_validator_result.png) 
static/css/style.css | Passed, No errors found | [Results](../images/testing/css_testing/css_validator_result.png)
static/css/style.css | Passed, No errors found | [Results](../images/testing/css_testing/css_validator_result.png) 
<br>

## Wave Accessibility
- Wave accessibility(https://wave.webaim.org/) was used to test the websites accessibility

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
index.html                       |0 errors | [Results](../images/testing/wave_testing/index.png)
privacy_policy.html              |0 errors | [Results](../images/testing/wave_testing/privacy_policy.png)
forum - forum.html               |0 errors | [Results](../images/testing/wave_testing/forum.png)
profiles- subscription.html      |0 errors | [Results](../images/testing/wave_testing/subscription.png)
profiles- profile_type.html      |0 errors | [Results](../images/testing/wave_testing/profile_type.png)
profiles- register_user_type.html|0 errors | [Results](../images/testing/wave_testing/register_user_type.png)
products- products.html          |0 errors | [Results](../images/testing/wave_testing/products.png)
products- product_detail.html    |0 errors | [Results](../images/testing/wave_testing/product_detail.png)
checkout- checkout.html          |0 errors | [Results](../images/testing/wave_testing/checkout.png)
checkout -checkout_success.html  |0 errors | [Results](../images/testing/wave_testing/checkout_success.png)
checkout- basket.html          |0 errors | [Results](../images/testing/wave_testing/basket.png)
404errors.html          |0 errors | [Results](../images/testing/hwave_testing/404.png)
500errors.html          |0 errors | [Results](../images/testing/wave_testing/500.png)


___

## JSHint
- JSHint(https://jshint.com/) was used to analyse the Javascript files

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
static/js/script.js | 0 errors and 1 warning | [Results](../images/testing/jshint_testing/jshint.png)

Warning -redefinition of alert
<br>


## PEP8online
- PEP8online was used to analyse the Python files (https://pep8online.com/)

Page | Errors|Results
------------ | -------------  | ------------- 
Forum
forum/admin.py | No errors/warnings| [Results](../images/testing/pep8_testing/for_admin.png)
forum/apps.py | No errors/warnings | [Results](../images/testing/pep8_testing/for_apps.png)
forum/forms.py | No errors/warnings | [Results](../images/testing/pep8_testing/for_forms.png)
forum/models.py | No errors/warnings | [Results](../images/testing/pep8_testing/for_models.png)
forum/urls.py | No errors/warnings | [Results](../images/testing/pep8_testing/for_urls.png)
forum/views.py | No errors/warnings | [Results](../images/testing/pep8_testing/for_views.png)
forum/widgets.py | No errors/warnings | [Results](../images/testing/pep8_testing/widgets.png)
forum/test_models.py | No errors/warnings | [Results](../images/testing/pep8_testing/for_test_models.png)
forum/test_views.py | No errors/warnings | [Results](../images/testing/pep8_testing/for_test_views.png)

Page | Errors|Results
------------ | -------------  | ------------- 
products/admin.py | No errors/warnings| [Results](../images/testing/pep8_testing/pdt_admin.png)
products/apps.py | No errors/warnings | [Results](../images/testing/pep8_testing/pdt_apps.png)
products/forms.py | No errors/warnings | [Results](../images/testing/pep8_testing/pdt_forms.png)
products/models.py | No errors/warnings | [Results](../images/testing/pep8_testing/pdt_models.png)
products/urls.py | No errors/warnings | [Results](../images/testing/pep8_testing/pdt_urls.png)
products/widgets.py | No errors/warnings | [Results](../images/testing/pep8_testing/pdt_widgets.png)
products/test_forms.py | No errors/warnings | [Results](../images/testing/pep8_testing/pdt_test_forms.png)
products/test_models.py | No errors/warnings | [Results](../images/testing/pep8_testing/pdt_test_models.png)
products/test_views.py | No errors/warnings | [Results](../images/testing/pep8_testing/pdt_test_views.png)

Page | Errors|Results
------------ | -------------  | ------------- 
basket/apps.py | No errors/warnings | [Results](../images/testing/pep8_testing/bkt_apps.png)
basket/contexts.py | No errors/warnings| [Results](../images/testing/pep8_testing/bkt_contexts.png)
basket/urls.py | No errors/warnings | [Results](../images/testing/pep8_testing/bkt_urls.png)
basket/widgets.py | No errors/warnings | [Results](../images/testing/pep8_testing/bkt_widgets.png)
basket/views.py | No errors/warnings | [Results](../images/testing/pep8_testing/bkt_views.png)
basket/test_views.py | No errors/warnings | [Results](../images/testing/pep8_testing/bkt_test_views.png)

Page | Errors|Results
------------ | -------------  | ------------- 
checkout/admin.py | No errors/warnings| [Results](../images/testing/pep8_testing/ch_admin.png)
checkout/apps.py | No errors/warnings | [Results](../images/testing/pep8_testing/ch_apps.png)
checkout/forms.py | No errors/warnings | [Results](../images/testing/pep8_testing/ch_forms.png)
checkout/models.py | No errors/warnings | [Results](../images/testing/pep8_testing/ch_models.png)
checkout/signals.py | No errors/warnings | [Results](../images/testing/pep8_testing/ch_signals.png)
checkout/urls.py | No errors/warnings | [Results](../images/testing/pep8_testing/ch_urls.png)
checkout/views.py | No errors/warnings | [Results](../images/testing/pep8_testing/ch_views.png)
checkout/webhook_handler.py | No errors/warnings | [Results](../images/testing/pep8_testing/ch_webhook_handler.png)
checkout/webhooks.py | No errors/warnings | [Results](../images/testing/pep8_testing/ch_test_webhooks.png)
checkout/test_forms.py | No errors/warnings | [Results](../images/testing/pep8_testing/ch_test_forms.png)
checkout/test_models.py | No errors/warnings | [Results](../images/testing/pep8_testing/ch_test_models.png)
checkout/test_views.py | No errors/warnings | [Results](../images/testing/pep8_testing/ch_test_views.png)

Page | Errors|Results
------------ | -------------  | ------------- 
home/apps.py | No errors/warnings | [Results](../images/testing/pep8_testing/hom_apps.png)
home/urls.py | No errors/warnings | [Results](../images/testing/pep8_testing/hom_urls.png)
home/views.py | No errors/warnings | [Results](../images/testing/pep8_testing/hom_views.png)
home/test_views.py | No errors/warnings | [Results](../images/testing/pep8_testing/hom_test_views.png)

Page | Errors|Results
------------ | -------------  | ------------- 
profiles/admin.py | No errors/warnings| [Results](../images/testing/pep8_testing/pr_admin.png)
profiles/apps.py | No errors/warnings | [Results](../images/testing/pep8_testing/pr_apps.png)
profiles/forms.py | No errors/warnings | [Results](../images/testing/pep8_testing/pr_forms.png)
profiles/models.py | No errors/warnings | [Results](../images/testing/pep8_testing/pr_models.png)
profiles/signals.py | No errors/warnings | [Results](../images/testing/pep8_testing/pr_signals.png)
profiles/urls.py | No errors/warnings | [Results](../images/testing/pep8_testing/pr_urls.png)
profiles/views.py | No errors/warnings | [Results](../images/testing/pep8_testing/pr_views.png)
profiles/widgets.py | No errors/warnings | [Results](../images/testing/pep8_testing/pr_widgets.png)
profiles/test_forms.py | No errors/warnings | [Results](../images/testing/pep8_testing/pr_test_forms.png)
profiles/test_models.py | No errors/warnings | [Results](../images/testing/pep8_testing/pr_test_models.png)
profiles/test_views.py | No errors/warnings | [Results](../images/testing/pep8_testing/pr_test_views.png)

Page | Errors|Results
------------ | -------------  | ------------- 
custom_storages.py | No errors/warnings| [Results](docs/images/testing/pep8_testing/custom_storages.png)
eny.py | No errors/warnings| [Results](docs/images/testing/pep8_testing/env.png)
manage.py | No errors/warnings| [Results](docs/images/testing/pep8_testing/manage.png)
util.py | No errors/warnings| [Results](docs/images/testing/pep8_testing/util.png)

___

## a11y Color Contrast Accessibility Validator

- Color accessibility(https://color.a11y.com/) was used to test the websites accessibility

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
index.html                       |0 automated color contrast issues | [Results](../images/testing/a11y/index.png)
privacy_policy.html              |0 automated color contrast issues | [Results](../images/testing/a11y/privacy_policy.png)
forum - forum.html               |0 automated color contrast issues | [Results](../images/testing/a11y/forum.png)
profiles- subscription.html      |0 automated color contrast issues| [Results](../images/testing/a11y/subscription.png)
profiles- profile_type.html      |0 automated color contrast issues | [Results](../images/testing/a11y/profile_type.png)
profiles- register_user_type.html|0 automated color contrast issues | [Results](../images/testing/a11y/register_user_type.png)
products- products.html          |0 automated color contrast issues | [Results](../images/testing/a11y/products.png)
products- product_detail.html    |0 automated color contrast issues | [Results](../images/testing/a11y/product_detail.png)
checkout- checkout.html          |0 automated color contrast issues | [Results](../images/testing/a11y/checkout.png)
checkout -checkout_success.html  |0 automated color contrast issues | [Results](../images/testing/a11y/checkout_success.png)
checkout- basket.html          |0 automated color contrast issues | [Results](../images/testing/a11y/basket.png)
404errors.html          |0 automated color contrast issues | [Results](../images/testing/a11y/404.png)
500errors.html          |0 automated color contrast issues | [Results](../images/testing/a11y/500.png)
