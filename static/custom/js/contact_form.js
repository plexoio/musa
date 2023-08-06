function sendMail(contactForm, event) { // as 'this' on the form tag
    event.preventDefault();
    emailjs.send("service_at381m9", "template_ba0oxqh", {
        "musa_name": contactForm.name.value,
        "musa_email": contactForm.emailaddress.value,
        "musa_subject": contactForm.subject.value,
        "musa_message": contactForm.issue.value
    }).then(
        function (response) {
            console.log('Success', response);
            $('#email_sent').html(`
            <div class="alert alert-success alert-dismissible text-center" role="alert" tabindex="-1">
                <div>Your email has been sent successfully we'll be in touch with you shortly!</div>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>`);
            $('#email_sent .alert').focus()
        },
        function (error) {
            console.log('Failed', error);
            $('#email_sent').html(`
            <div class="alert alert-danger alert-dismissible text-center" role="alert" tabindex="-1">
           <div>STATUS: ${error.status} and ERROR: ${error.text}</div>
           <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
           </div>`);
            $('#email_sent .alert').focus()
        }
    );
};