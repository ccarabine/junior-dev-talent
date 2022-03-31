/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js

    Stripe works with what are called payment intents.
    The process - when a user hits the checkout page
    the checkout view will call out to stripe and create a payment intent
    for the current amount of the shopping bag.
    When stripe creates it. it'll also have a secret that identifies it.
    Which will be returned to us and we'll send it to the template as the 
    client secret variable.
    Then in the JavaScript on the client side.
    We'll call the confirm card payment method from stripe js.
    Using the client secret which will verify the card number.
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
// Get the form element 
// the first thing the listener does is prevent its default action which is to post.

// It uses the stripe.confirm card payment method to send the card information
// securely to stripe.

// Before the call to stripe. Disable both the card element and the submit button to prevent multiple submissions.

// Call the confirm card payment method.
// Provide the card to stripe (line 79) and then execute this function (.then(function(result) )on the result.
// If there's an error put the error right into the card error div.
// And otherwise If the status of the payment intent comes back is succeeded we'll submit the form.
// if there's an error.
// re-enable the card element and the submit button to allow the user to fix it.

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});