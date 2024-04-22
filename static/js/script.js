$(document).ready(function () {
    // owl_carousel
    $(document).ready(function () {
        $(".owl-carousel").owlCarousel({
            loop: true,
            margin: 10,
            nav: true,
            dots: false,
            autoplay: true,
            autoplayTimeout: 3000,
            autoplayHoverPause: true,
            center: true,
            navText: [
                "<i class='fa fa-angle-left'></i>",
                "<i class='fa fa-angle-right'></i>",
            ],
            responsive: {
                0: {
                    items: 1,
                },
                600: {
                    items: 1,
                },
                1000: {
                    items: 3,
                },
            },
        });
        $(".owl-carousel").find(".owl-nav").removeClass("disabled");
        $(".owl-carousel").on("changed.owl.carousel", function (event) {
            $(this).find(".owl-nav").removeClass("disabled");
        });
    });

    const dropdownTtiles = document.querySelectorAll(".mobile-menu-dropdown");
    let clickedIndex = null;

    const dropdowns = document.querySelectorAll(".drop-down-sub-nav");
    dropdownTtiles?.forEach((title, index) => {
        title.addEventListener("click", function () {
            if (clickedIndex === index) {
                // If the clicked dropdown title is already active, remove the active class
                title.classList.remove("active");
                dropdowns[index].classList.remove("active");
                clickedIndex = null; // Reset clickedIndex to null, as the dropdown is closed now.
            } else {
                if (clickedIndex !== null) {
                    dropdownTtiles[clickedIndex].classList.remove("active");
                    dropdowns[clickedIndex].classList.remove("active");
                }
                clickedIndex = index;

                dropdowns.forEach((dropdown) => {
                    dropdown?.classList.remove("active");
                });

                dropdowns[index].classList.add("active");
                dropdownTtiles[index]?.classList.add("active");
            }
        });
    });

    //HIGHLIGHTING ACTIVE MENU
    $(function () {
        const currentPath = window.location.pathname;

        $(".nav-link").each(function () {
            if ($(this).prop("pathname") == currentPath) {
                $(this).addClass("active");
            }
        });
    });
    // mobileMenu
    let one = document.getElementById("menu-icon");
    one.addEventListener("click", function () {
        document.getElementById("mobile-menu").classList.add("active");
        for (x of document.getElementsByClassName("overlay")) {
            x.classList.add("active");
        }
    });

    $(".overlay").on("click", function () {
        $(this).removeClass("active");
        $("#mobile-menu").removeClass("active");
    });
    let two = document.getElementsByClassName("close");
    for (x of two) {
        x.addEventListener("click", () => {
            for (x of document.getElementsByClassName("overlay")) {
                x.classList.remove("active");
            }
            document.getElementById("mobile-menu").classList.remove("active");
        });
    }

    //   alumni-activites-detailed page

    const cards = document.querySelectorAll(".detailed-page");
    const details = document.querySelectorAll(".main-card");

    cards.forEach((card) => {
        const topic = card.getAttribute("data-topic");
        card.addEventListener("click", () => { });
    });
    details?.forEach((detail) => {
        const topic = detail.getAttribute("data-topic");
        const queryParams = new URLSearchParams(window.location.search);
        const currentTopic = queryParams.get("topic");

        if (topic === currentTopic) {
            detail.style.display = "block";
        }
    });

    // Scroll to top

    $(".sidebar").click(function () {
        $(".sidebar .left-box").toggle("slide");
    });

    $(".backtotop").click(function () {
        $(window).scrollTop(0);
    });

    $(".spotlight-slide,.listcard,.card-slider").slick({
        dots: true,
        arrows: false,
        autoplay: true,
        autoplaySpeed: 4000,
        slidesToShow: 1,
    });

    $(".slick-prev").click(function () {
        $(".spotlight-slide, .card-slider").slick("slickPrev");
    });
    $(".slick-next").click(function () {
        $(".spotlight-slide, .card-slider").slick("slickNext");
    });
});
// image slider

$(function () {
    $(".slider").slick({
        speed: 900,
        dots: true,
        arrows: true,
    });
});

// card slider

$(".listcard").slick({
    dots: false,
    slidesToShow: 3,
    autoplay: false,
    speed: 900,
    autoplaySpeed: 700,
    prevArrow: ".slick-preve",
    nextArrow: ".slick-nexte",
    responsive: [
        {
            breakpoint: 768,
            settings: {
                slidesToShow: 2,
            },
        },
        {
            breakpoint: 550,
            settings: {
                slidesToShow: 1,
            },
        },
    ],
});

$(document).ready(function () {
    // home page gallery moment play button Handle
    $("#play-btn")?.click(() => {
        $("video")[0].play();
        $("video")[0].controls = true;
        $("#play-btn").hide();
    });

    // gallery page
    // get index of click card
    index = 0

    // Get all card elements
    const showcases = document.querySelectorAll(".showcase");
    // Get all details elements
    const collashes = document.querySelectorAll(".gallery-details");

    // Show details of the first card by default
    if (collashes[index]) {
        collashes[index].style.display = "block";
    }
    if (showcases[index]) {
        showcases[index].classList.add("active");
    }

    // Add click event listeners to each card
    showcases.forEach((showcase, index) => {
        showcase.addEventListener("click", () => {
            // Hide all details
            collashes.forEach((collashe) => {
                collashe.style.display = "none";
            });
            // Remove active class from all cards
            showcases.forEach((showcase) => {
                showcase.classList.remove("active");
            });
            // Show details of the clicked card
            collashes[index].style.display = "block";
            // Add active class to the clicked card
            showcase.classList.add("active");
        });
    });
});

// Adding image-name
$("input:file").change(function () {
    var filepath = this.value;
    var m = filepath.match(/([^\/\\]+)$/);
    var filename = m[1];
    $(".file-name").html(filename);
});

// file input preview

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $(".logoContainer img").attr("src", e.target.result);
        };
        reader.readAsDataURL(input.files[0]);
    }
}
$("input:file").change(function () {
    readURL(this);
});

// IQAC drop-down animation

(function (w, d) {
    var titles = d.querySelectorAll(".title"),
        i = 0,
        len = titles.length;

    for (; i < len; i++)
        titles[i].onclick = function (e) {
            for (var j = 0; j < len; j++)
                if (this != titles[j])
                    titles[j].parentNode.className = titles[
                        j
                    ].parentNode.className.replace(/ open/i, "");

            var cn = this.parentNode.className;

            this.parentNode.className = ~cn.search(/open/i)
                ? cn.replace(/ open/i, "")
                : cn + " open";
        };
})(this, document);

// iqac report page calender

$(function () {
    $(".taco").after("");
    var rowElement = document.getElementById("row");
    if (rowElement) {
        rowElement.onclick = function (e) {
            document.getElementById("calendar").focus();
        };
    }
});
// set current date in an input field
let current_date = new Date().toJSON().slice(0, 10);
$("#calender").text(moment(current_date).format("DD MMM YYYY"));

// Report-complaint-page clear form

document.querySelector(".reset_report")?.addEventListener("click", (event) => {
    document.querySelector(".report_form").reset();
    event.preventDefault();
});

//iqac complaint form submit handling
complaint_form = document.getElementById("complaint_form");
// Add a submit event listener to the form
$("#iqac-submit")?.click(function (event) {
    event.preventDefault(); // Prevent the default form submission
    const fields = [
        "first_name",
        "last_name",
        "year_of_batch",
        "subject",
        "complaint",
    ];
    let error_message = {};
    for (const field of fields) {
        const value = $("#" + field)
            .val()
            .trim();
        const labelName = $("#" + field)
            .prev("label")
            .text()
            .slice(0, -1);

        if (value === "") {
            error_message[field] = [`Please fill in the ${labelName} field.`];
        }
    }
    if (Object.keys(error_message).length !== 0) {
        displayErrors(error_message);
        return false; // Prevent form submission
    }

    // Get the form data
    const formData = new FormData(complaint_form);
    // Make an AJAX request using Axios
    axios
        .post("/iqac/complaint-report/", formData)
        .then((response) => {
            console.log(response);
            // Handle the successful response
            if (response.data.success) {
                $(".modal_wrapper_two")[0].classList.add("active");
            }
        })
        .catch((error) => {
            console.log(error);
            // Handle the error
            if (error.response.data.error) {
                const errors = error.response.data.message;
                displayErrors(errors);
            }
        });
});

// Registrtion alumni form

let form_1 = document.querySelector(".form_1");
let form_2 = document.querySelector(".form_2");
let form_3 = document.querySelector(".form_3");

let form_1_btns = document.querySelector(".form_1_btns");
let form_2_btns = document.querySelector(".form_2_btns");
let form_3_btns = document.querySelector(".form_3_btns");

let form_1_next_btn = document.querySelector(".form_1_btns .btn_next");
let form_2_back_btn = document.querySelector(".form_2_btns .btn_back");
let form_2_next_btn = document.querySelector(".form_2_btns .btn_next");
let form_3_back_btn = document.querySelector(".form_3_btns .btn_back");

let form_2_progessbar = document.querySelector(".form_2_progessbar");
let form_3_progessbar = document.querySelector(".form_3_progessbar");

let btn_done = document.querySelector(".btn_done");
let modal_wrapper = document.querySelector(".modal_wrapper");
let shadow = document.querySelector(".shadow");

let progressCheck = document.querySelector(".step .check");
let progressCheck_two = document.querySelector(".step .check_two");
let progressCheck_three = document.querySelector(".step .check_three");

let spanRemove = document.querySelector(".step .bullet .remove");
let spanRemove_two = document.querySelector(".step .bullet .remove_two");
let spanRemove_three = document.querySelector(".step .bullet .remove_three");

function removeSpecialCharacters(inputField) {
    // Get the current value of the input field
    let currentValue = inputField.value;

    // Remove special characters, numbers, and spaces using a regular expression
    let cleanedValue = currentValue.replace(/[^a-zA-Z]/g, "");

    // Update the input field value with the cleaned value
    inputField.value = cleanedValue;
}

$("#phone_number")?.on("input", function () {
    // Get the current value of the input field
    let currentValue = $(this).val();

    // Check if the input field has a value
    if (currentValue) {
        // Remove special characters, letters, and spaces using a regular expression
        let cleanedValue = currentValue.replace(/[^0-9]/g, "");
        // Update the input field value with the cleaned value
        $(this).val(cleanedValue);
    }
});
function isValidEmail(email) {
    // Regular expression pattern for email validation
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    // Use the test() method of the RegExp object to check if the email matches the pattern
    return emailPattern.test(email);
}

form_1_next_btn?.addEventListener("click", function (e) {
    e.preventDefault();

    const fields = [
        "first_name",
        "last_name",
        "gender",
        "marital_status",
        "phone_number",
        "email",
        "address",
    ];
    let error_message = {};
    for (const field of fields) {
        const value = $("#" + field)
            .val()
            .trim();
        const labelName = $("#" + field)
            .prev("label")
            .text()
            .slice(0, -1);

        if (value === "") {
            error_message[field] = [`Please fill in the ${labelName} field.`];
        }
        if (field === "phone_number" && value.length != 10) {
            error_message[field] = [`${labelName} field should be in 10 digit.`];
        }
        if (field === "email" && !isValidEmail(value) && value !== "") {
            error_message[field] = [`${labelName} field is not valid.`];
        }
    }
    if (Object.keys(error_message).length !== 0) {
        displayErrors(error_message);
        return false; // Prevent form submission
    }

    form_1.style.display = "none";
    form_2.style.display = "block";

    form_1_btns.style.display = "none";
    form_2_btns.style.display = "flex";

    form_2_progessbar.classList.add("active");

    progressCheck.style.display = "block";
    spanRemove.style.display = "none";
});

form_2_back_btn?.addEventListener("click", function () {
    form_1.style.display = "block";
    form_2.style.display = "none";

    form_1_btns.style.display = "flex";
    form_2_btns.style.display = "none";

    form_2_progessbar.classList.remove("active");

    progressCheck.style.display = "none";
    spanRemove.style.display = "block";
});

form_2_next_btn?.addEventListener("click", function () {
    const fields = ["b_ed_subject", "year_of_study", "educational_status"];
    let error_message = {};
    for (const field of fields) {
        const value = $("#" + field)
            .val()
            .trim();
        const labelName = $("#" + field)
            .prev("label")
            .text()
            .slice(0, -1);

        if (value === "") {
            error_message[field] = [`Please fill in the ${labelName} field.`];
        }
    }
    if (Object.keys(error_message).length !== 0) {
        displayErrors(error_message);
        return false; // Prevent form submission
    }

    form_2.style.display = "none";
    form_3.style.display = "block";

    form_3_btns.style.display = "flex";
    form_2_btns.style.display = "none";

    form_3_progessbar.classList.add("active");

    progressCheck_two.style.display = "block";
    spanRemove_two.style.display = "none";
});

form_3_back_btn?.addEventListener("click", function () {
    form_2.style.display = "block";
    form_3.style.display = "none";

    form_3_btns.style.display = "none";
    form_2_btns.style.display = "flex";

    form_3_progessbar.classList.remove("active");

    progressCheck_two.style.display = "none";
    spanRemove_two.style.display = "block";
});

shadow?.addEventListener("click", function () {
    modal_wrapper.classList.remove("active");
});

document.querySelector(".resetFirst")?.addEventListener("click", (event) => {
    document.querySelector(".first_form").reset();
    event.preventDefault();
});

document.querySelector(".resetSecond")?.addEventListener("click", (event) => {
    document.querySelector(".second_form").reset();
    event.preventDefault();
});
document.querySelector(".resetThird")?.addEventListener("click", (event) => {
    document.querySelector(".third_form").reset();
    event.preventDefault();
});

document.getElementById("submit")?.addEventListener("click", function () {
    // clearing all errors message in forms
    const errorMessages = document.querySelectorAll(".error");

    errorMessages?.forEach(function (element) {
        element.textContent = "";
    });

    // Get form field values
    let csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    let firstName = document.getElementById("first_name").value;
    let lastName = document.getElementById("last_name").value;
    let gender = document.getElementById("gender").value;
    let maritalStatus = document.getElementById("marital_status").value;
    let phoneNumber = document.getElementById("phone_number").value;
    let email = document.getElementById("email").value;
    let address = document.getElementById("address").value;
    let bEdSubject = document.getElementById("b_ed_subject").value;
    let yearOfStudy = document.getElementById("year_of_study").value;
    let educationalStatus = document.getElementById("educational_status").value;
    let jntcPeriod = document.getElementById("jntc_period").value;
    let suggestion = document.getElementById("suggestion").value;
    let image = document.getElementById("image").files[0];

    // Create FormData object and append form field values
    let formData = new FormData();
    formData.append("csrfmiddlewaretoken", csrfToken);
    formData.append("first_name", firstName);
    formData.append("last_name", lastName);
    formData.append("gender", gender);
    formData.append("marital_status", maritalStatus);
    formData.append("phone_number", phoneNumber);
    formData.append("email", email);
    formData.append("address", address);
    formData.append("b_ed_subject", bEdSubject);
    formData.append("year_of_study", yearOfStudy);
    formData.append("educational_status", educationalStatus);
    formData.append("jntc_period", jntcPeriod);
    formData.append("suggestion", suggestion);
    formData.append("image", image);

    axios
        .post("/alumni/alumni-network-registration/", formData)
        .then(function (response) {
            // Handle success response

            if (response.data.success) {
                $(".modal_wrapper")[0].classList.add("active");
            }
            // Perform any further actions, such as showing a success message
        })
        .catch(function (error) {
            // Handle error response
            
            if (error.response.data.error) {
                let { form1 } = error.response.data.messages;
                if (Object.keys(form1).length !== 0) {
                    form_1.style.display = "block";
                    form_3.style.display = "none";

                    form_1_btns.style.display = "flex";
                    form_3_btns.style.display = "none";

                    form_3_progessbar.classList.remove("active");
                    form_2_progessbar.classList.remove("active");

                    progressCheck_two.style.display = "none";
                    spanRemove_two.style.display = "block";

                    progressCheck.style.display = "none";
                    spanRemove.style.display = "block";

                    displayErrors(form1);
                }
            }
            // Perform any further actions, such as showing an error message
        });
});

//contact us form submit handling

// Get the form element
const submit_button = document.getElementById("contact-submit");

// Add a submit event listener to the form
submit_button?.addEventListener("click", function (event) {
    event.preventDefault(); // Prevent the default form submission

    const fields = [
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "message",
    ];
    let error_message = {};
    for (const field of fields) {
        const value = $("#" + field)
            .val()
            .trim();
        const name = $("#" + field).attr("placeholder");

        if (value === "") {
            error_message[field] = [`Please fill in the ${name} field.`];
        }

        if (field === "phone_number" && value.length > 0 && value.length != 10) {
            error_message[field] = [`Phone number field should be in 10 digit.`];
        }

        if (field === "email" && !isValidEmail(value) && value !== "") {
            error_message[field] = [`${name} field is not valid.`];
        }
    }
    if (Object.keys(error_message).length !== 0) {
        displayErrors(error_message);
        return false; // Prevent form submission
    }
    // Get the form data
    const formData = new FormData(contact_form);
    // Make an AJAX request using Axios
    axios
        .post("/contact_us/", formData)
        .then((response) => {
            // Handle the successful response
            if (response.data.success) {
                $(".modal_wrapper")[0].classList.add("active");
            }
        })
        .catch((error) => {
            // Handle the error
            if (error.response.data.error) {
                const errors = error.response.data.message;
                displayErrors(errors);
            }
        });
});

//form errors handling
function displayErrors(errors) {
    const errorMessages = document.querySelectorAll(".error");

    errorMessages.forEach(function (element) {
        element.textContent = "";
    });

    Object.keys(errors).forEach(function (fieldName) {
        const field = document.getElementById(fieldName);
        let parent = field.parentElement;

        if (field) {
            const errorElement = parent.querySelector("p");
            if (errorElement && errorElement?.classList.contains("error")) {
                errorElement?.classList.add("active");
                errorElement.textContent = errors[fieldName][0];
            }
        }
    });
}
