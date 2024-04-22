$(document).ready(function () {
    // Iterate over each card-slider element
    $(".card-slider").each(function () {
        var $currentSlider = $(this);

        // Initialize the slider
        $currentSlider.slick({
            dots: true,
            arrows: false,
            autoplay: true,
            autoplaySpeed: 4000,
            slidesToShow: 1,
        });

        // Find the corresponding prev and next buttons
        var $prevButton = $currentSlider.closest(".card").find(".slick-prev");
        var $nextButton = $currentSlider.closest(".card").find(".slick-next");

        // Add click event handlers to the buttons
        $prevButton.click(function () {
            $currentSlider.slick("slickPrev");
        });

        $nextButton.click(function () {
            $currentSlider.slick("slickNext");
        });
    });
});

// events FeaturedDataSection
$(document).ready(function () {
    // Iterate over each card-slider element
    $(".card-slider-featured").each(function () {
        var $currentSlider = $(this);

        // Initialize the slider
        $currentSlider.slick({
            dots: true,
            arrows: false,
            autoplay: true,
            autoplaySpeed: 4000,
            slidesToShow: 1,
        });

        // Find the corresponding prev and next buttons
        var $prevButton = $currentSlider.closest(".card").find(".slick-prev");
        var $nextButton = $currentSlider.closest(".card").find(".slick-next");

        // Add click event handlers to the buttons
        $prevButton.click(function () {
            $currentSlider.slick("slickPrev");
        });

        $nextButton.click(function () {
            $currentSlider.slick("slickNext");
        });
    });
});

//events Upcoming Section data
$(document).ready(function () {
    // Iterate over each card-slider element
    $(".card-slider-upcoming").each(function () {
        var $currentSlider = $(this);

        // Initialize the slider
        $currentSlider.slick({
            dots: true,
            arrows: false,
            autoplay: true,
            autoplaySpeed: 4000,
            slidesToShow: 1,
        });

        // Find the corresponding prev and next buttons
        var $prevButton = $currentSlider.closest(".card").find(".slick-prev");
        var $nextButton = $currentSlider.closest(".card").find(".slick-next");

        // Add click event handlers to the buttons
        $prevButton.click(function () {
            $currentSlider.slick("slickPrev");
        });

        $nextButton.click(function () {
            $currentSlider.slick("slickNext");
        });
    });
});


//results page => modal

// Initialize Flatpickr
const dateInput = document.getElementById("date_of_birth");
if (dateInput) {
    flatpickr(dateInput, {
        dateFormat: "d/m/Y", // Set the desired date format
    });  
}

// only allowing number in register number input
$("#register_no")?.on("input", function () {
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

const resultModal = document.getElementById("result-modal");
const resultTab = document.querySelectorAll(".result-box");
const closeButton = document.getElementById("result-modal-close-btn");
const form = document.getElementById("form-result");
    
    //form submit handling
    form?.addEventListener("submit", function(event) {
        event.preventDefault();

        // Get form field values
        let csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
        let exam_id = document.getElementById('exam_id').value;
        let register_no = document.getElementById('register_no').value;
        let date_of_birth = document.getElementById('date_of_birth').value;

        // Split the input date by '/'
        let parts = date_of_birth.split('/');

        // Reorder the parts in the desired format
        let formattedDate = parts[2] + '-' + parts[1] + '-' + parts[0];

        // Get the form data
        let formData = new FormData();
        formData.append('csrfmiddlewaretoken', csrfToken);
        formData.append('exam_id', exam_id);
        formData.append('register_no', register_no);
        formData.append('date_of_birth', formattedDate);

        // Send the form data using Axios
        axios.post("/student-zone/b-ed-examination/results/", formData)
            .then(function(response) {
                    // Handle the success case
                    if (response.data.success) {
                        window.location.href = response.data.redirect
                    }
            })
            .catch(function(error) {
                if (error.response.data.error) {
                    const errors = error.response.data.message;
                    displayErrors(errors);
                }
            });
    });
   

$(document).ready(function () {
    $('label[for="exam_id"]').hide();
    // result title click handling
    resultTab.forEach((res)=>{
        res?.addEventListener("click", function (e) {
            e.stopPropagation();

            resultModal.style.display = "block";
            document.body.style.overflow = "hidden";

            const dataResult = res.getAttribute("data-result");
            const [title, id] = dataResult.split(",");
            const formattedTitle = title.replace("(", "<br>(");

            $("#exam_id")[0].value = id;
            $("#result-modal-title")[0].innerHTML = formattedTitle;
        });
    })
    // result modal close button handling
    closeButton?.addEventListener("click", function () {
        const errorMessages = document.querySelectorAll('.error');

        errorMessages.forEach(function(element) {
            element.textContent = '';
        });
        resultModal.style.display = "none";
        document.body.style.overflow = "unset";
        document.getElementById("form-result").reset();
    });
});

// result page search handling
$(document).ready(function(){
    $("#result-search input").on("input", (e) => {
        if (!e.target.value) {
            e.target.value=""
            $('#result-search').submit()
        }
    });
})

// gallery
document?.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll(".image-gallery .major");

    const gallery = document.querySelectorAll(".gallery-details");
    const showcases = document.querySelectorAll(".showcase");

    if (cards) {
        cards.forEach((card, index) => {
            card?.addEventListener("click", (e) => {
                e.preventDefault();
                console.log(card.getAttribute("gallery-index"),"card")
                let index = card.getAttribute("gallery-index")
                
                window.location.href= "/resources/gallery/?index="+index;

                
                gallery.forEach((collashe) => {
                    collashe.style.display = "none";
                });
                
                showcases.forEach((showcase) => {
                    showcase?.classList.remove("active");
                });

                // Add active class to the clicked card
                card?.classList.add("active");
            });
        });
    }
});


$(document).ready(function () {
    // All events page => featured, upcoming buttons
    const featuredButton = document.getElementById("featured-btn");
    const upcomingButton = document.getElementById("upcoming-btn");

    // All events page => featured, upcoming sections
    const featuredDataSection = document.getElementById("featured-data-container");
    const upcomingDataSection = document.getElementById("upcoming-data-container");

    // All events page => featured, upcoming pagination
    const featuredPagination = document.getElementById("featured_pagination");
    const upcomingPagination = document.getElementById("upcoming_pagination");


        if(localStorage.getItem("filter_events")== "upcoming"){
            upcomingButton?.classList.add("active-button");
            upcomingDataSection?.classList.add("active");
            upcomingPagination?.classList.add("active");
        }else{
            featuredButton?.classList.add("active-button");
            featuredDataSection?.classList.add("active");
            featuredPagination?.classList.add("active");
        }
    
    
    // All events page => switching featured, upcoming section on button clicks
    featuredButton?.addEventListener("click", function () {
        localStorage.setItem("filter_events","featured")

        featuredButton?.classList.add("active-button");
        upcomingButton?.classList.remove("active-button");
        
        featuredDataSection?.classList.add("active");
        featuredPagination?.classList.add("active");
        upcomingDataSection?.classList.remove("active");
        upcomingPagination?.classList.remove("active");

    });

    upcomingButton?.addEventListener("click", function () {
        localStorage.setItem("filter_events","upcoming")

        upcomingButton?.classList.add("active-button");
        featuredButton?.classList.remove("active-button");

        featuredDataSection?.classList.remove("active");
        featuredPagination?.classList.remove("active");
        upcomingDataSection?.classList.add("active");
        upcomingPagination?.classList.add("active");

    });
});

//Downloads page => magazine slider
$(document).ready(function () {
    // Initialize the slider
    $(".all-magazines")?.slick({
        dots: false,
        arrows: true,
        autoplay: false,
        autoplaySpeed: 1500,
        slidesToShow: 4,
        responsive: [
            {
                breakpoint: 920,
                settings: {
                    slidesToShow: 3,
                },
            },
            {
                breakpoint: 640,
                settings: {
                    slidesToShow: 2,
                },
            },
            {
                breakpoint: 380,
                settings: {
                    slidesToShow: 1,
                },
            },
        ],
    });

    $("#magazine .slick-prev").click(function () {
        $(".all-magazines").slick("slickPrev");
    });

    $("#magazine .slick-next").click(function () {
        $(".all-magazines").slick("slickNext");
    });
});

//downloads page => view type selection [card/list view selection]
$(document).ready(function () {
    const cardIcon = document.querySelector("#download .card-icon");
    const listIcon = document.querySelector("#download .list-icon");
    const cardViewContainer = document.querySelector("#download .card-view-box");
    const listViewContainer = document.querySelector("#download .list-view-box");

    //initial state
    if (localStorage.getItem("download") == "list") {
        listIcon?.classList.add("active");
        cardIcon?.classList.remove("active");
        cardViewContainer?.classList.remove("active");
        listViewContainer?.classList.add("active");
    }else{
        cardIcon?.classList.add("active");
        listIcon?.classList.remove("active");
        cardViewContainer?.classList.add("active");
        listViewContainer?.classList.remove("active");
    }

    cardIcon?.addEventListener("click", () => {
        localStorage.setItem("download","card")
        cardIcon?.classList.add("active");
        listIcon?.classList.remove("active");
        cardViewContainer?.classList.add("active");
        listViewContainer?.classList.remove("active");
    });

    listIcon?.addEventListener("click", () => {
        localStorage.setItem("download","list")
        listIcon?.classList.add("active");
        cardIcon?.classList.remove("active");
        cardViewContainer?.classList.remove("active");
        listViewContainer?.classList.add("active");
    });
});

//evalution policies page => view type selection [card/list view selection]
$(document).ready(function () {
    const cardIcon = document.querySelector("#evalution-policy .card-icon");
    const listIcon = document.querySelector("#evalution-policy .list-icon");
    const cardViewContainer = document.querySelector("#evalution-policy .card-view-box");
    const listViewContainer = document.querySelector("#evalution-policy .list-view-box");

    // initial setting
    if (localStorage.getItem("evaluation")=="list") {
        listIcon?.classList.add("active");
        cardIcon?.classList.remove("active");
        cardViewContainer?.classList.remove("active");
        listViewContainer?.classList.add("active");
    }else{
        cardIcon?.classList.add("active");
        listIcon?.classList.remove("active");
        cardViewContainer?.classList.add("active");
        listViewContainer?.classList.remove("active");
    }

    cardIcon?.addEventListener("click", () => {
        localStorage.setItem("evaluation","card")
        cardIcon?.classList.add("active");
        listIcon?.classList.remove("active");
        cardViewContainer?.classList.add("active");
        listViewContainer?.classList.remove("active");
    });

    listIcon?.addEventListener("click", () => {
        localStorage.setItem("evaluation","list")
        listIcon?.classList.add("active");
        cardIcon?.classList.remove("active");
        cardViewContainer?.classList.remove("active");
        listViewContainer?.classList.add("active");
    });
});


//accounts page => view type selection [card/list view selection]
$(document).ready(function () {
    const cardIcon = document.querySelector("#accounts .card-icon");
    const listIcon = document.querySelector("#accounts .list-icon");
    const cardViewContainer = document.querySelector("#accounts .card-view-box");
    const listViewContainer = document.querySelector("#accounts .list-view-box");

    if (localStorage.getItem("accounts")== "list") {
        listIcon?.classList.add("active");
        cardIcon?.classList.remove("active");
        cardViewContainer?.classList.remove("active");
        listViewContainer?.classList.add("active");
    }else{
        cardIcon?.classList.add("active");
        listIcon?.classList.remove("active");
        cardViewContainer?.classList.add("active");
        listViewContainer?.classList.remove("active");
    }

    cardIcon?.addEventListener("click", () => {
        localStorage.setItem("accounts","card")
        cardIcon?.classList.add("active");
        listIcon?.classList.remove("active");
        cardViewContainer?.classList.add("active");
        listViewContainer?.classList.remove("active");
    });

    listIcon?.addEventListener("click", () => {
        localStorage.setItem("accounts","list")
        listIcon?.classList.add("active");
        cardIcon?.classList.remove("active");
        cardViewContainer?.classList.remove("active");
        listViewContainer?.classList.add("active");
    });
});

//academic calendar section
$(document).ready(function () {
    const topSection = document.querySelectorAll("#academic-calendar .top-card");
    const bottomSection = document.querySelectorAll("#academic-calendar .bottom-card");

    const yearButtons = document.querySelectorAll("#academic-calendar .year");

    // initial state
    yearButtons[0]?.classList.add("active");
    topSection[0]?.classList.add("active");
    bottomSection[0]?.classList.add("active");
    
    yearButtons.forEach((button, index) => {
        button?.addEventListener("click", () => {
            yearButtons.forEach((button) => {
                button?.classList.remove("active");
            });
            button?.classList.add("active");
            topSection.forEach((section) => {
                section?.classList.remove("active");
            });
            bottomSection.forEach((section) => {
                section?.classList.remove("active");
            });

            topSection[index]?.classList.add("active");
            bottomSection[index]?.classList.add("active");
        });
    });
});

//year and semester wise results page
$(document).ready(function () {
    const topSection = document.querySelectorAll("#all-result .top-card");
    const bottomSection = document.querySelectorAll("#all-result .bottom-card");

    const yearButtons = document.querySelectorAll("#all-result .year");

        // initial state
        yearButtons[0]?.classList.add("active");
        topSection[0]?.classList.add("active");
        bottomSection[0]?.classList.add("active");

    yearButtons.forEach((button, index) => {
        button?.addEventListener("click", () => {
            yearButtons.forEach((button) => {
                button?.classList.remove("active");
            });
            button?.classList.add("active");
            topSection.forEach((section) => {
                section?.classList.remove("active");
            });
            bottomSection.forEach((section) => {
                section?.classList.remove("active");
            });

            topSection[index]?.classList.add("active");
            bottomSection[index]?.classList.add("active");
        });
    });
});



