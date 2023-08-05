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
        }, function (error) {
            console.log('Failed', error);
        }
    );
};