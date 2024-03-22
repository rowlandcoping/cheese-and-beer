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

});