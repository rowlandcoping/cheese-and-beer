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

    // Adds Card element to checkout page(if element exists).  Also adds event listeners and actions to be taken on card submit.
    if (document.getElementById('id_stripe_public_key')) {
        const stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);
        const clientSecret = document.getElementById('id_client_secret').textContent.slice(1, -1);
        const stripe = Stripe(stripePublicKey);
        const elements = stripe.elements();
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
        // Handle realtime validation errors on the card element
        card.addEventListener('change', function (event) {
            var errorDiv = document.getElementById('card-errors');
            if (event.error) {
                let html = `
                    <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                    </span>
                    <span>${event.error.message}</span>
                `;
                errorDiv.innerHTML = html;
            } else {
                errorDiv.textContent = '';
            }
        });        
        // HANDLE FORM SUBMISSION
        const form = document.getElementById('payment-form');
        // adds event listeners to all the payment buttons.       
        const paymentSubmitButtons = Array.from(document.getElementsByClassName('payment-button'));
        paymentSubmitButtons.forEach(item => {
            item.addEventListener('click', function handleClick(event) {
                //disables form input etc to prevent multiple submissions
                card.update({ 'disabled': true});
                formButtons = Array.from(document.getElementsByClassName('form-button'));
                for (let i = 0; i < formButtons.length; i++) {
                    formButtons[i].style.pointerEvents = "none";
                }
                if (document.getElementById('add-user-address')) {
                    document.getElementById('add-user-address').setAttribute('disabled', true);
                }

                /*this is for the loading circle thing.  Fade toggle is just an opacity type toggle thing in jquery.
                given I don't have a loady circle thing yet I'll park this for now.  Maybe replace with a spinning cheese or whatever*/
                //document.getElementById('payment-form').fadeToggle(100);
                //document.getElementById('loading-overlay').fadeToggle(100);

                // From using {% csrf_token %} in the form, in order to use in the header of the POST request
                const csrfToken = document.querySelector("[name='csrfmiddlewaretoken']").value;
                const postData = JSON.stringify({
                    'csrfmiddlewaretoken': csrfToken,
                    'client_secret': clientSecret,
                });
                const url = 'cache_checkout_data/';
                /*don't forget to trim whitespace from the user supplied fields.
                This fetch statement adds the current info to the webhook and confirms card info with stripe,
                as well as updating payment intent with order details (useful later)*/
                fetch(url, {
                    method: 'POST',
                    body: postData,
                    mode: "no-cors",
                    headers: { 
                        "X-CSRFToken": csrfToken, 
                        'Content-Type': 'application/json',
                     },
                    credentials: 'same-origin',
                }).then(
                    stripe.confirmCardPayment(clientSecret, {
                        //sends the data to stripe, 
                        payment_method: {
                            card: card,
                            //may well be worth adding billing data to this section later on, along with billing e-mail.  Not essential functionality though.
                        },
                        shipping: {
                            name: form.full_name.value,
                            address: {
                                line1: form.address_line_one.value,
                                line2: form.address_line_two.value,
                                city: form.town_or_city.value,
                                state: form.county.value,
                                postal_code: form.postcode.value,
                                country: form.country.value,
                            }
                        },
                    }).then(function(result) {
                        // if stripe throws an error
                        if (result.error) {
                            var errorDiv = document.getElementById('card-errors');
                            var html = `
                                <span class="icon" role="alert">
                                <i class="fas fa-times"></i>
                                </span>
                                <span>${result.error.message}</span>`;
                                errorDiv.innerHTML = html;
                            console.log(result.error.message)
                            /*spinny wheel stuff again
                            $('#payment-form').fadeToggle(100);
                            $('#loading-overlay').fadeToggle(100);
                            */
                            // re-enable buttons
                            card.update({ 'disabled': false});
                            for (let i = 0; i < formButtons.length; i++) {
                                formButtons[i].style.pointerEvents = "auto";
                            }
                            if (document.getElementById('add-user-address')) {
                                document.getElementById('add-user-address').removeAttribute('disabled');
                            }
                        } else {
                            if (result.paymentIntent.status === 'succeeded') {
                                console.log("it worked")
                                //this acts like the submit button and submits the form to the checkout view.
                                form.submit();
                            }
                        }
                    })  
                )
            })       
        });    
    }
    //Quantity form control icons.
    if (document.getElementById('decrement-amount')) {
        document.addEventListener("click", function(e){
            const target = e.target.closest("#decrement-amount");
            if(target){
                if (document.getElementById('quantity').value > 1) {
                    document.getElementById('quantity').value -= 1
                }
            }
        });
        document.addEventListener("click", function(e){
            const target = e.target.closest("#increment-amount");
            if(target){
                quantity = document.getElementById('quantity').value;
                quantity = Number(quantity);
                quantity += 1;
                document.getElementById('quantity').value = quantity;                    
            }
        });

    }
    




});



