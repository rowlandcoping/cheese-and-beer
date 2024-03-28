/*jshint esversion: 6*/

document.addEventListener("DOMContentLoaded", function() {


    //MANY TO MANY FIELD SELECTOR
    //attach event listners to category buttons    
    const attachCategoryListners= Array.from(document.getElementsByClassName('category-selector'));
    attachCategoryListners.forEach(item => {
        item.addEventListener('click', function handleClick(event) {
            const itemId = item.getAttribute('id');                
            addSignupCategory(itemId);
        });
    });
    //clears categories on page refresh
    if (document.getElementById("id_pairings")) {
        document.getElementById("id_pairings").value="";
    }
    //ensures buttons on edit page have appropriate styling based on current pairings (do here by passing this field value to context and creating another hidden field in the form.py)
    if (document.getElementById("id_initial_pairings")) {
        const buttonsArray = Array.from(document.getElementsByClassName('category-selector'));
        const categoryButtons = buttonsArray.map(div => Number(div.id));
        const categorySelected = document.getElementById("id_initial_pairings").value;
        for (let i = 0; i < categoryButtons.length; i++) {
            for (let j = 0; j < categorySelected.length; j++) {
                if (categoryButtons[i] == categorySelected[j]) {
                    document.getElementById(categoryButtons[i]).style.backgroundColor = "green";
                    document.getElementById(categoryButtons[i]).style.color = "white";
                    document.getElementById(categoryButtons[i]).style.borderColor = "white";
                    document.getElementById("id_pairings").value += Number(categoryButtons[i]) + ",";
                }
            }
        }
    }
    //changes colour of category when clicked and adds the category to the pairings field
    function addSignupCategory(itemId) {        
        if (document.getElementById(itemId).style.color === "white") {
            document.getElementById(itemId).style.backgroundColor = "grey";
            document.getElementById(itemId).style.color = "black";
            document.getElementById(itemId).style.border = "2px solid rgb(53, 52, 52)";
            const oldText = document.getElementById("id_pairings").value;
            const newText = oldText.replace(itemId + "," ,'');
            document.getElementById("id_pairings").value = newText;
        } else {
            document.getElementById(itemId).style.backgroundColor = "green";
            document.getElementById(itemId).style.color = "white";
            document.getElementById(itemId).style.border = "2px solid white";
            document.getElementById("id_pairings").value += Number(itemId) + ",";
        }
        console.log(document.getElementById("id_pairings").value)
    }
    //mouseover effects for categories
    //NOT YET IMPLEMENTED

    function categoryMouseover(itemId) {        
        if (document.getElementById(itemId).style.backgroundColor === "green") {
            document.getElementById(itemId).style.backgroundColor = "rgb(49, 68, 49)";
            document.getElementById(itemId).style.color = "white";
            document.getElementById(itemId).style.border = "2px solid white";
        } else {
            document.getElementById(itemId).style.backgroundColor = "rgb(49, 68, 49)";
            document.getElementById(itemId).style.color = "black";
            document.getElementById(itemId).style.border = "2px solid rgb(53, 52, 52)";
        }
    }
    function categoryMouseout(itemId) {        
        if (document.getElementById(itemId).style.color === "white") {
            document.getElementById(itemId).style.backgroundColor = "green";
            document.getElementById(itemId).style.color = "white";
            document.getElementById(itemId).style.border = "2px solid white";
        } else {
            document.getElementById(itemId).style.backgroundColor = "grey";
            document.getElementById(itemId).style.color = "black";
            document.getElementById(itemId).style.border = "2px solid border:rgb(53, 52, 52)";
        }
    }


    //NAV MENU

    document.addEventListener("mouseover", function(e){
        const target = e.target.closest("#beer-nav");
        if(target){
            document.getElementById('beer-desktop-mouseout').style.display = "none";
            document.getElementById('beer-desktop-mouseover').style.display = "block";
        }
    });
    document.addEventListener("mouseout", function(e){
        const target = e.target.closest("#beer-nav");
        if(target){
            document.getElementById('beer-desktop-mouseout').style.display = "block";
            document.getElementById('beer-desktop-mouseover').style.display = "none";
        }
    });
    document.addEventListener("mouseover", function(e){
        const target = e.target.closest("#cheese-nav");
        if(target){
            document.getElementById('cheese-desktop-mouseout').style.display = "none";
            document.getElementById('cheese-desktop-mouseover').style.display = "block";
        }
    });
    document.addEventListener("mouseout", function(e){
        const target = e.target.closest("#cheese-nav");
        if(target){
            document.getElementById('cheese-desktop-mouseout').style.display = "block";
            document.getElementById('cheese-desktop-mouseover').style.display = "none";
        }
    });
    document.addEventListener("mouseover", function(e){
        const target = e.target.closest("#account-nav");
        if(target){
            document.getElementById('account-mouseout').style.display = "none";
            document.getElementById('account-mouseover').style.display = "block";
        }
    });
    document.addEventListener("mouseout", function(e){
        const target = e.target.closest("#account-nav");
        if(target){
            document.getElementById('account-mouseout').style.display = "block";
            document.getElementById('account-mouseover').style.display = "none";
        }
    });

    document.addEventListener("mouseover", function(e){
        const target = e.target.closest(".nav-menu-link");
        if(target){
            target.style.backgroundColor = "black";
            target.style.Color = "white";
        }
    });
    document.addEventListener("mouseout", function(e){
        const target = e.target.closest(".nav-menu-link");
        if(target){
            target.style.backgroundColor = "white";
            target.style.Color = "black";
        }
    });
    













    //IMAGE HANDLING (NOT YET IMPLEMENTED)
    //previews images due for upload
    const imageUpload= document.getElementById('uploaded-image');
    const previewPhoto = () => {
        const previewPic = imageUpload.files;
        if (previewPic) {
            const fileReader = new FileReader();
            const preview = document.getElementById('image-preview');
            fileReader.onload = function (event) {
                preview.setAttribute('src', event.target.result);
            };
            fileReader.readAsDataURL(previewPic[0]);
            if (document.getElementById('current-edit-image')) {
                document.getElementById('current-edit-image').style.display="none";
            }
            document.getElementById('image-preview').style.display="inline-block";
            if (document.getElementById('info-update')) {
                document.getElementById('info-update').style.display = "block";
            }
            document.getElementById('profile-pic-cancel').style.display = "inline-block";
            if (document.getElementById('image-submit')) {
                document.getElementById('image-submit').style.display = "inline-block";
            }
            if (document.getElementById('remove-picture')) {
                document.getElementById('remove-picture').style.display = "none";
            }
        }
    };
    if (imageUpload) {
        imageUpload.addEventListener("change", previewPhoto);
    }


    // STRIPE JS (needs converting from jQuery and whatever other stuff it uses)

    // Adds Card element to checkout page

    if (document.getElementById('id_stripe_public_key')) {
        const stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);
        const clientSecret = document.getElementById('id_client_secret').textContent.slice(1, -1);
        const stripe = Stripe(stripePublicKey);
        const elements = stripe.elements();
        console.log(elements);
        const style = {
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
        const card = elements.create('card',  { hidePostalCode: true, style: style});
        card.mount('#card-element');
    }
    /*
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
    var form = document.getElementById('payment-form');

    form.addEventListener('submit', function(ev) {
        ev.preventDefault();
        card.update({ 'disabled': true});
        $('#submit-button').attr('disabled', true);
        $('#payment-form').fadeToggle(100);
        $('#loading-overlay').fadeToggle(100);

        var saveInfo = Boolean($('#id-save-info').attr('checked'));
        // From using {% csrf_token %} in the form
        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        var postData = {
            'csrfmiddlewaretoken': csrfToken,
            'client_secret': clientSecret,
            'save_info': saveInfo,
        };
        var url = '/checkout/cache_checkout_data/';

        $.post(url, postData).done(function () {
            stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        name: $.trim(form.full_name.value),
                        phone: $.trim(form.phone_number.value),
                        email: $.trim(form.email.value),
                        address:{
                            line1: $.trim(form.street_address1.value),
                            line2: $.trim(form.street_address2.value),
                            city: $.trim(form.town_or_city.value),
                            country: $.trim(form.country.value),
                            state: $.trim(form.county.value),
                        }
                    }
                },
                shipping: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        postal_code: $.trim(form.postcode.value),
                        state: $.trim(form.county.value),
                    }
                },
            }).then(function(result) {
                if (result.error) {
                    var errorDiv = document.getElementById('card-errors');
                    var html = `
                        <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                        </span>
                        <span>${result.error.message}</span>`;
                    $(errorDiv).html(html);
                    $('#payment-form').fadeToggle(100);
                    $('#loading-overlay').fadeToggle(100);
                    card.update({ 'disabled': false});
                    $('#submit-button').attr('disabled', false);
                } else {
                    if (result.paymentIntent.status === 'succeeded') {
                        form.submit();
                    }
                }
            });
        }).fail(function () {
            // just reload the page, the error will be in django messages
            location.reload();
        })
    });
    */

});



