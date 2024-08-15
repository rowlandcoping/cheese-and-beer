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
                    document.getElementById(categoryButtons[i]).style.backgroundColor = "rgb(255, 255, 140)";
                    document.getElementById(categoryButtons[i]).style.color = "rgb(0, 51, 0)";
                    document.getElementById(categoryButtons[i]).style.borderColor = "rgb(0, 15, 0)";
                    document.getElementById("id_pairings").value += Number(categoryButtons[i]) + ",";
                }
            }
        }
    }
    //changes colour of category when clicked and adds the category to the pairings field
    function addSignupCategory(itemId) {        
        if (document.getElementById(itemId).style.color === "rgb(0, 51, 0)") {
            document.getElementById(itemId).style.backgroundColor = "grey";
            document.getElementById(itemId).style.color = "black";
            document.getElementById(itemId).style.border = "2px solid rgb(53, 52, 52)";
            const oldText = document.getElementById("id_pairings").value;
            const newText = oldText.replace(itemId + "," ,'');
            document.getElementById("id_pairings").value = newText;
        } else {
            document.getElementById(itemId).style.backgroundColor = "rgb(255, 255, 140)";
            document.getElementById(itemId).style.color = "rgb(0, 51, 0)";
            document.getElementById(itemId).style.border = "2px solid rgb(0, 15, 0)";
            document.getElementById("id_pairings").value += Number(itemId) + ",";
        }
    }
    //mouseover effects for categories
    const attachMouseoverListners= Array.from(document.getElementsByClassName('category-selector'));
    attachMouseoverListners.forEach(item => {
        item.addEventListener('mouseover', function handleClick(event) {
            const itemId = item.getAttribute('id');                
            categoryMouseover(itemId);
        });
    });
    //add mouseout effects
    const attachMouseoutListners= Array.from(document.getElementsByClassName('category-selector'));
    attachMouseoutListners.forEach(item => {
        item.addEventListener('mouseout', function handleClick(event) {
            const itemId = item.getAttribute('id');                
            categoryMouseout(itemId);
        });
    });
    function categoryMouseover(itemId) {        
        if (document.getElementById(itemId).style.backgroundColor === "rgb(255, 255, 140)") {
            document.getElementById(itemId).style.backgroundColor = "rgb(134, 134, 53)";
            document.getElementById(itemId).style.color = "rgb(0, 51, 0)";
            document.getElementById(itemId).style.border = "2px solid rgb(0, 15, 0)";
        } else {
            document.getElementById(itemId).style.backgroundColor = "rgb(134, 134, 53)";
            document.getElementById(itemId).style.color = "black";
            document.getElementById(itemId).style.border = "2px solid rgb(53, 52, 52)";
        }
    }
    function categoryMouseout(itemId) {        
        if (document.getElementById(itemId).style.color === "rgb(0, 51, 0)") {
            document.getElementById(itemId).style.backgroundColor = "rgb(255, 255, 140)";
            document.getElementById(itemId).style.color = "rgb(0, 51, 0)";
            document.getElementById(itemId).style.border = "2px solid rgb(0, 15, 0)";
        } else {
            document.getElementById(itemId).style.backgroundColor = "grey";
            document.getElementById(itemId).style.color = "black";
            document.getElementById(itemId).style.border = "2px solid border:rgb(53, 52, 52)";
        }
    }

    //NAV MENU FOR DESKTOP SCREEN SIZES
    document.addEventListener("mouseout", function(e){
        const target = e.target.closest(".menu-header");
        if(target){
            target.style.backgroundColor = "rgb(1, 70, 1)";
            target.style.color = "rgb(255, 255, 140)";
        }
    });
    document.addEventListener("mouseover", function(e){
        const target = e.target.closest(".menu-header");
        if(target){
            target.style.backgroundColor = "rgb(255, 255, 140)";
            target.style.color = "rgb(1, 70, 1)";
        }
    });
    document.addEventListener("mouseover", function(e){
        const target = e.target.closest("#beer-nav");
        if(target){
            document.getElementById('beer-desktop-mouseover').style.display = "block";
        }
    });
    document.addEventListener("mouseout", function(e){
        const target = e.target.closest("#beer-nav");
        if(target){
            document.getElementById('beer-desktop-mouseover').style.display = "none";
        }
    });
    document.addEventListener("mouseover", function(e){
        const target = e.target.closest("#cheese-nav");
        if(target){
            document.getElementById('cheese-desktop-mouseover').style.display = "block";
        }
    });
    document.addEventListener("mouseout", function(e){
        const target = e.target.closest("#cheese-nav");
        if(target){
            document.getElementById('cheese-desktop-mouseover').style.display = "none";
        }
    });
    document.addEventListener("mouseover", function(e){
        const target = e.target.closest("#account-nav");
        if(target){
            document.getElementById('account-mouseover').style.display = "block";
        }
    });
    document.addEventListener("mouseout", function(e){
        const target = e.target.closest("#account-nav");
        if(target){
            document.getElementById('account-mouseover').style.display = "none";
        }
    });
    document.addEventListener("mouseover", function(e){
        const target = e.target.closest(".nav-menu-link");
        if(target){
            target.style.backgroundColor = "rgb(255, 255, 140)";
            target.style.color = "rgb(1, 70, 1)";
        }
    });
    document.addEventListener("mouseout", function(e){
        const target = e.target.closest(".nav-menu-link");
        if(target){
            target.style.backgroundColor = "rgb(1, 70, 1)";
            target.style.color = "rgb(255, 255, 140)";
        }
    });

    //NAV MENU FOR MOBILE SCREEN SIZES
    window.addEventListener('click', function(e){   
        if (document.getElementById('cheese-click').contains(e.target)){
            document.getElementById('cheese-clickout').style.display = "block";
            document.getElementById('cheese-click').style.backgroundColor = "rgb(255, 255, 140)";
            document.getElementById('cheese-click').style.color = "rgb(1, 70, 1)";
            document.getElementById('cheese-clickout').style.color = "rgb(255, 255, 140)";
        } else{
            document.getElementById('cheese-clickout').style.display = "none";
            document.getElementById('cheese-click').style.backgroundColor = "rgb(1, 70, 1)";
            document.getElementById('cheese-click').style.color = "rgb(255, 255, 140)";
        }
    });
    window.addEventListener('click', function(e){   
        if (document.getElementById('beer-click').contains(e.target)){
            document.getElementById('beer-clickout').style.display = "block";
            document.getElementById('beer-click').style.backgroundColor = "rgb(255, 255, 140)";
            document.getElementById('beer-click').style.color = "rgb(1, 70, 1)";
            document.getElementById('beer-clickout').style.color = "rgb(255, 255, 140)";
        } else{
            document.getElementById('beer-clickout').style.display = "none";
            document.getElementById('beer-click').style.backgroundColor = "rgb(1, 70, 1)";
            document.getElementById('beer-click').style.color = "rgb(255, 255, 140)";
        }
    });
    window.addEventListener('click', function(e){   
        if (document.getElementById('account-click').contains(e.target)){
            document.getElementById('account-clickout').style.display = "block";
            document.getElementById('account-click').style.backgroundColor = "rgb(255, 255, 140)";
            document.getElementById('account-click').style.color = "rgb(1, 70, 1)";
            document.getElementById('account-clickout').style.color = "rgb(255, 255, 140)";
        } else{
            document.getElementById('account-clickout').style.display = "none";
            document.getElementById('account-click').style.backgroundColor = "rgb(1, 70, 1)";
            document.getElementById('account-click').style.color = "rgb(255, 255, 140)";
        }
    });
    
    //IMAGE HANDLING
    //clears files on page reload
    if (document.getElementById('id_image')) {
        window.onload=document.getElementById('id_image').value = "";
    }
    //previews images due for upload
    const imageUpload= document.getElementById('id_image');
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
    // cancel image update/add
    document.addEventListener("click", function(e){
        const target = e.target.closest("#profile-pic-cancel"); 
        if(target){
            if (document.getElementById('current-edit-image')) {
                document.getElementById('current-edit-image').style.display="inline-block";
            }
            document.getElementById('image-preview').style.display="none";
            document.getElementById('id_image').value = "";
            document.getElementById('profile-pic-cancel').style.display = "none";
            if (document.getElementById('image-submit')) {
                document.getElementById('image-submit').style.display = "none";
            }
            if (document.getElementById('remove-picture')) {
                document.getElementById('remove-picture').style.display = "flex";
            }
        }
    });

    // STRIPE PAYMENT CHECKOUT
    // Adds Card element to checkout page(if element exists).  Also adds event listeners and actions to be taken on card submit.
    // NB this section comes directly from Boutique Ado (converted from JQuery)   
    if (document.getElementById('id_stripe_public_key')) {
        const stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);
        const clientSecret = document.getElementById('id_client_secret').textContent.slice(1, -1);
        const stripe = Stripe(stripePublicKey);
        const elements = stripe.elements();
        const style = {
            base: {
                color: '#000',
                fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
                fontSmoothing: 'antialiased',
                fontSize: '14px',
                '::placeholder': {
                    color: 'grey'
                }
            },
            invalid: {
                color: 'red',
                iconColor: 'red'
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
        // end section from Boutique Ado

        // this function prevents the form from submitting when the button is activated
        const form = document.getElementById('payment-form');
        document.addEventListener("submit", function(e){
            const target = e.target.closest("#payment-form");
            if(target){
                e.preventDefault();
            }
        });    
        // Validates form with Javascript to avoid errors or premature submission
        const paymentSubmitButtons = Array.from(document.getElementsByClassName('payment-button'));
        paymentSubmitButtons.forEach(item => {
            item.addEventListener('click', function handleClick(event) {
                let takePayment = false;
                const addressFields = Array.from(document.getElementsByClassName('address-field'));
                for (let i = 0; i < addressFields.length; i++) {                  
                    if (addressFields[i].required) {
                        if (addressFields[i].value) {   
                            if (addressFields[i].name === "order_email") {
                                const email = addressFields[i].value;
                                const emailFormat = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
                                if (email.match(emailFormat)) {
                                    takePayment=true;
                                    document.getElementById('error-container').style.display="none";
                                } else {
                                    document.getElementById('error-container').style.display="block";
                                    document.getElementById('form-error-message').textContent = "email address is not in the correct format";
                                    takePayment=false;
                                    break;
                                }
                            } else {
                                takePayment=true;
                                document.getElementById('error-container').style.display="none";
                            }                     
                        } else {
                            document.getElementById('error-container').style.display="block";
                            document.getElementById('form-error-message').textContent = addressFields[i].placeholder + " has not been filled out";
                            takePayment=false;
                            break;
                        }
                    }
                }
                // submits payment intent if form validates                               
                if (takePayment === true) {
                    document.getElementById('form-submit-button').click();
                    // disables form input etc to prevent multiple submissions
                    card.update({ 'disabled': true});
                    const formButtons = Array.from(document.getElementsByClassName('form-button'));
                    for (let i = 0; i < formButtons.length; i++) {
                        formButtons[i].style.pointerEvents = "none";
                    }
                    if (document.getElementById('add-user-address')) {
                        document.getElementById('add-user-address').setAttribute('disabled', true);
                    }            
                    stripe.confirmCardPayment(clientSecret, {
                        //sends the data to stripe, 
                        payment_method: {
                            card: card,
                            billing_details: {
                                email: document.getElementById('order-email').value.trim(),
                            }
                        },
                        shipping: {
                            name: form.full_name.value,
                            address: {
                                line1: form.address_line_one.value.trim(),
                                line2: form.address_line_two.value.trim(),
                                city: form.town_or_city.value.trim(),
                                state: form.county.value.trim(),
                                postal_code: form.postcode.value.trim(),
                                country: form.country.value.trim(),
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
                                //this acts like the submit button and submits the form to the checkout view.
                                form.submit();
                            }
                        }
                    });
                }
            });
        });
    }

    //QUANTITY CONTROL BASKET/CHECKOUT
    // Prevents activation of decrement button if product quantity is 1
    const decrementButtons = Array.from(document.getElementsByClassName('zero-prevent'));
    decrementButtons.forEach(item => {
        const itemId = item.getAttribute('id');
        const id = itemId.split('-')[1];
        let quantity = document.getElementById('quantity-' + id).innerHTML;
        if (quantity == 1) {
            document.getElementById(itemId).style.pointerEvents = "none";
            document.getElementById(itemId).style.opacity = "0.5";
        } else {
            document.getElementById(itemId).style.pointerEvents = "auto";
            document.getElementById(itemId).style.opacity = "1";
        }
    });

    // QUANTITY CONTROL IN PRODUCT VIEW.
    if (document.getElementById('decrement-amount')) {
        document.addEventListener("click", function(e){
            const target = e.target.closest("#decrement-amount");
            if(target){
                if (document.getElementById('quantity').value > -1 && document.getElementById('quantity').value < 202) {
                    const disabledSections = Array.from(document.getElementsByClassName('product-action-button'));
                    for (let i = 0; i < disabledSections.length; i++) {
                        disabledSections[i].style.pointerEvents = "auto";
                        disabledSections[i].style.opacity = "1";
                        document.getElementById('quantity-alert').style.display="none";
                    }
                }
                if (document.getElementById('quantity').value > 1) {
                    let initial_price = document.getElementById('product-price').innerHTML;
                    initial_price = Number(initial_price);
                    let quantity = document.getElementById('quantity').value;
                    quantity = Number(quantity);
                    quantity = Math.ceil(quantity);
                    quantity -= 1;                    
                    document.getElementById('quantity').value = quantity;
                    document.getElementById('product-view-total').innerHTML = (Math.round((initial_price * quantity) * 100) / 100).toFixed(2); 
                }
            }
        });
        document.addEventListener("click", function(e){
            const target = e.target.closest("#increment-amount");
            if(target){
                if (document.getElementById('quantity').value > -1 && document.getElementById('quantity').value < 202) {
                    const disabledSections = Array.from(document.getElementsByClassName('product-action-button'));
                    for (let i = 0; i < disabledSections.length; i++) {
                        disabledSections[i].style.pointerEvents = "auto";
                        disabledSections[i].style.opacity = "1";
                        document.getElementById('quantity-alert').style.display="none";
                    }
                }
                if (document.getElementById('quantity').value < 200) {
                    let initial_price = document.getElementById('product-price').innerHTML;
                    initial_price = Number(initial_price);
                    let quantity = document.getElementById('quantity').value;
                    quantity = Number(quantity);
                    quantity = Math.ceil(quantity);
                    quantity += 1;
                    document.getElementById('quantity').value = quantity;
                    document.getElementById('product-view-total').innerHTML = (Math.round((initial_price * quantity) * 100) / 100).toFixed(2);
                }               
            }
        });
        document.addEventListener("input", function(e){
            const target = e.target.closest("#quantity");
            if(target){
                let initial_price = document.getElementById('product-price').innerHTML;
                initial_price = Number(initial_price);
                let initial_quantity = document.getElementById('quantity').value;
                initial_quantity = Number(initial_quantity);
                const enableSections = Array.from(document.getElementsByClassName('product-action-button'));
                    for (let i = 0; i < enableSections.length; i++) {
                        enableSections[i].style.pointerEvents = "auto";
                        enableSections[i].style.opacity = "1";
                    }
                    document.getElementById('quantity-alert').style.display="none";
                if (initial_quantity > 200 || initial_quantity < 1 || Number.isInteger(initial_quantity) === false) {
                    const disabledSections = Array.from(document.getElementsByClassName('product-action-button'));
                    for (let i = 0; i < disabledSections.length; i++) {
                        disabledSections[i].style.pointerEvents = "none";
                        disabledSections[i].style.opacity = "0.5";
                    }
                    document.getElementById('quantity-alert').style.display="inline-block";
                }
                document.getElementById('product-view-total').innerHTML = (Math.round((initial_price * initial_quantity) * 100) / 100).toFixed(2);                
            }
        });
    }
    // set initial status of buttons if outside boundaries on page refresh
    if (document.getElementById('decrement-amount')) {
        let quantity = document.getElementById('quantity').value;
        if (quantity > 200 || quantity < 1 || Number.isInteger(quantity) === false) {
            const disabledSections = Array.from(document.getElementsByClassName('product-action-button'));
            for (let i = 0; i < disabledSections.length; i++) {
                disabledSections[i].style.pointerEvents = "none";
                disabledSections[i].style.opacity = "0.5";
            }
            document.getElementById('quantity-alert').style.display="inline-block";
        }
    }

    // BUY IT NOW ALERTS
    if (document.getElementById('buynow-alert')) {
        const buyNowButtons = Array.from(document.getElementsByClassName('buy-now'));
        buyNowButtons.forEach(item => {
            item.addEventListener('click', function handleClick(event) {
                const itemId = item.getAttribute('id'); 
                const productId = itemId.split("-")[1];
                const productScenario = itemId.split("-")[0];
                document.getElementById('buy-now-name').textContent = document.getElementById('buyname-' + productId).textContent;
                let quantity = 1;
                if (document.getElementById('product-page')) {
                    quantity = document.getElementById('quantity').value;
                    quantity = Number(quantity);
                }
                // adds url for correct quantity, view-product view only where basket is empty
                if (productScenario === "single") {
                    const url = "/basket/buy-now/?single=" + productId + "," + quantity;
                    window.location.href = url;
                }
                // triggers buy-now alert if items in basket
                if (productScenario === "basket") {
                    document.getElementById('buynow-alert').style.display="block";
                    const disabledSections = Array.from(document.getElementsByClassName('alert-disable'));
                    for (let i = 0; i < disabledSections.length; i++) {
                        disabledSections[i].style.pointerEvents = "none";
                        disabledSections[i].style.opacity = "0.5";
                    }
                    document.getElementById('remove-products').href = "/basket/buy-now/?remove=" + productId + "," + quantity;
                    document.getElementById('keep-products').href = "/basket/buy-now/?addon=" + productId + "," + quantity;
                    document.addEventListener("click", function(e){
                        const target = e.target.closest(".cancel-alert");
                        if(target){
                            document.getElementById('buynow-alert').style.display="none";
                            const disabledSections = Array.from(document.getElementsByClassName('alert-disable'));
                            for (let i = 0; i < disabledSections.length; i++) {
                                disabledSections[i].style.pointerEvents = "auto";
                                disabledSections[i].style.opacity = "1";
                            }
                        }
                    });   
                }
            });    
        });
    }

    // ADDRESS REMOVAL ALERTS
    if (document.getElementById('address-alert')) {
        const removeAddressButtons = Array.from(document.getElementsByClassName('remove-address'));
        removeAddressButtons.forEach(item => {
            item.addEventListener('click', function handleClick(event) {
                const itemId = item.getAttribute('id');
                const id=itemId.split("-")[1];
                document.getElementById('alert-full-name').textContent = document.getElementById('name-' + id).textContent;
                document.getElementById('alert-line-one').textContent = document.getElementById('one-' + id).textContent;
                if (document.getElementById('two-' + id)) {
                    document.getElementById('alert-line-two').textContent = document.getElementById('two-' + id).textContent;
                }
                document.getElementById('alert-city').textContent = document.getElementById('city-' + id).textContent;
                document.getElementById('alert-county').textContent = document.getElementById('county-' + id).textContent;
                document.getElementById('alert-postcode').textContent = document.getElementById('postcode-' + id).textContent;
                document.getElementById('remove-address').href = "/addresses/remove-address/" + id + "/";
                const disabledSections = Array.from(document.getElementsByClassName('alert-disable'));
                    for (let i = 0; i < disabledSections.length; i++) {
                        disabledSections[i].style.pointerEvents = "none";
                        disabledSections[i].style.opacity = "0.5";
                    }
                document.getElementById('address-alert').style.display="block";
                document.addEventListener("click", function(e){
                    const target = e.target.closest(".cancel-alert");
                    if(target){
                        document.getElementById('address-alert').style.display="none";
                        const disabledSections = Array.from(document.getElementsByClassName('alert-disable'));
                        for (let i = 0; i < disabledSections.length; i++) {
                            disabledSections[i].style.pointerEvents = "auto";
                            disabledSections[i].style.opacity = "1";
                        }
                    }
                });
            });
        });
    }

    // MESSAGE REMOVAL ALERTS
    if (document.getElementById('message-alert')) {
        const removeAddressButtons = Array.from(document.getElementsByClassName('remove-message'));
        removeAddressButtons.forEach(item => {
            item.addEventListener('click', function handleClick(event) {
                const itemId = item.getAttribute('id');
                const id = itemId.split("-")[1];
                document.getElementById('remove-message').href = "/admin-console/remove-message/" + id + "/";
                const disabledSections = Array.from(document.getElementsByClassName('alert-disable'));
                    for (let i = 0; i < disabledSections.length; i++) {
                        disabledSections[i].style.pointerEvents = "none";
                        disabledSections[i].style.opacity = "0.5";
                    }
                document.getElementById('message-alert').style.display="block";
                document.addEventListener("click", function(e){
                    const target = e.target.closest(".cancel-alert");
                    if(target){
                        document.getElementById('message-alert').style.display="none";
                        const disabledSections = Array.from(document.getElementsByClassName('alert-disable'));
                        for (let i = 0; i < disabledSections.length; i++) {
                            disabledSections[i].style.pointerEvents = "auto";
                            disabledSections[i].style.opacity = "1";
                        }
                    }
                });
            });
        });
    }
    
    // PRODUCT DELETION ALERTS
    if (document.getElementById('product-alert')) {
        const removeAddressButtons = Array.from(document.getElementsByClassName('delete-product'));
        removeAddressButtons.forEach(item => {
            item.addEventListener('click', function handleClick(event) {
                const itemId = item.getAttribute('id');
                const id=itemId.split("-")[1];
                document.getElementById('alert-name').textContent = document.getElementById('name-' + id).textContent;
                document.getElementById('remove-product').href = "/products/delete-product/" + id + "/";
                const disabledSections = Array.from(document.getElementsByClassName('alert-disable'));
                    for (let i = 0; i < disabledSections.length; i++) {
                        disabledSections[i].style.pointerEvents = "none";
                        disabledSections[i].style.opacity = "0.5";
                    }
                document.getElementById('product-alert').style.display="block";
                document.addEventListener("click", function(e){
                    const target = e.target.closest(".cancel-alert");
                    if(target){
                        document.getElementById('product-alert').style.display="none";
                        const disabledSections = Array.from(document.getElementsByClassName('alert-disable'));
                        for (let i = 0; i < disabledSections.length; i++) {
                            disabledSections[i].style.pointerEvents = "auto";
                            disabledSections[i].style.opacity = "1";
                        }
                    }
                });
            });
        });
    }

    // ADD OR SELECT ADDRESSES FROM CHECKOUT FOR LOGGED IN USERS
    if (document.getElementById('add-new-address')) {
        document.addEventListener("click", function(e){
            const target = e.target.closest("#add-new-address");
            if(target){
                document.getElementById('add-new-address-form').style.display="block";
                document.getElementById('existing-address-section').style.display="none";
                const formButtons = Array.from(document.getElementsByClassName('form-button'));
                for (let i = 0; i < formButtons.length; i++) {
                    formButtons[i].style.pointerEvents = "none";
                }
                const addressFields = Array.from(document.getElementsByClassName('address-field'));
                for (let i = 0; i < addressFields.length; i++) {
                    addressFields[i].value = "";
                }
            }
        });
        document.addEventListener("click", function(e){
            const target = e.target.closest("#select-address");
            if(target){
                document.getElementById('address-selection').style.display="block";
                document.getElementById('existing-address-section').style.display="none";
                const formButtons = Array.from(document.getElementsByClassName('form-button'));
                for (let i = 0; i < formButtons.length; i++) {
                    formButtons[i].style.pointerEvents = "none";
                }
            }
        });
        //styling for address selector
        document.addEventListener("click", function(e){
            const target = e.target.closest(".address-bar");
            if(target){
                const itemId = target.getAttribute('id');
                const selectorId = itemId.split('-')[1];
                const allAddresses = Array.from(document.getElementsByClassName('address-bar'));
                for (let i = 0; i < allAddresses.length; i++) {
                    allAddresses[i].style.backgroundColor = "white";
                }
                document.querySelector('input[name="address_selector"]:checked').checked = false;
                document.getElementById(selectorId).checked = true;
                document.getElementById(itemId).style.backgroundColor = "rgb(255, 255, 140)";
                const formButtons = Array.from(document.getElementsByClassName('form-button'));
                for (let i = 0; i < formButtons.length; i++) {
                    formButtons[i].style.pointerEvents = "none";
                }
            }
        });        
    }

    // SORT FILTER, PRODUCT VIEW PAGE
    // NB this code is converted from the Boutique Ado project    
    document.addEventListener("change", function(e){
        const target = e.target.closest("#sort-selector");
        if(target){
            const selector = document.querySelector('#sort-selector');
            const currentUrl = new URL(window.location);
            const selectedVal = selector.value;
            if(selectedVal != "reset"){
                const sort = selectedVal.split("_")[0];
                const direction = selectedVal.split("_")[1];                
                currentUrl.searchParams.set("sort", sort);
                currentUrl.searchParams.set("direction", direction);
                window.location.replace(currentUrl);
            } else {
                currentUrl.searchParams.delete("sort");
                currentUrl.searchParams.delete("direction");
                window.location.replace(currentUrl);
            }
        }
    });


    // FADE EFFECT FOR BASKET ADJUSTMENT MESSAGES
    // Please note this code is adapded from a snipped found on the geeksforgeeks.org website as mentioned in README.md
    function hide(){
        let opacity=0; 
        let intervalID=0;
        let bmessage=document.getElementById("basket-message"); 
        opacity = Number(window.getComputedStyle(bmessage).getPropertyValue("opacity"));
        if(opacity>0){ 
            opacity=opacity-0.01; 
            bmessage.style.opacity=opacity;
        } 
        else{ 
            clearInterval(intervalID);
            document.getElementById("basket-message").style.display="none";
        } 
    }
    window.onload=setTimeout(function(){
        if (document.getElementById("basket-message")) {
            setInterval(hide, 40); 
        }
    }, 500);

    // ENSURES CORRECT RADIAL BUTTON CHECKED ON BEER EDIT FORM
    if (document.getElementById("container-selected")) {
        const container = document.getElementById("container-selected").value;
        if (container ==="can") {
            document.getElementById("id_container_1").checked = true;
        } else {
            document.getElementById("id_container_0").checked = true;
        }
    }

});



