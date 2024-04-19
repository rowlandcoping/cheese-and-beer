const paymentSubmitButtons = Array.from(document.getElementsByClassName('payment-button'));
        paymentSubmitButtons.forEach(item => {
            item.addEventListener('click', function handleClick(event) {
                const addressFields = Array.from(document.getElementsByClassName('address-field'));
                for (let i = 0; i < addressFields.length; i++) {                    
                    if (addressFields[i].required) {
                        if (addressFields[i].value) {
                            if (addressFields[i].name === "order_email") {
                                email = addressFields[i].value
                                emailFormat = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
                                if (email.match(emailFormat)){
                                    takePayment=true;
                                } else {
                                    document.getElementById('error-container').style.display="block"
                                    document.getElementById('form-error-message').textContent = "email address is not in the correct format"
                                    takePayment=false;
                                    break;
                                }
                            } else {
                                takePayment=true;
                            }                      
                        } else {
                            document.getElementById('form-error-message').style.display="block"
                            document.getElementById('form-error-message').textContent = addressFields[i].placeholder + " has not been filled out"
                            takePayment=false;
                            break;
                        }
                    }
                }
                if (takePayment) {
                    document.getElementById('form-submit-button').click();
                }
            })
        })