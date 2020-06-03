function completeRequest(result) {
    console.log('Response received from API: ', result);
}

$(document).ready(function () {
    console.log('ready');
    $('#createPerson').click(function () {
        console.log('here');
        let firstName = $('#createPersonForm [name="firstName"]').val();
        let lastName = $('#createPersonForm [name="lastName"]').val();
        let isGay = $('#createPersonForm [name="isGay"]').val();
        let person = new Person(firstName, lastName, isGay);
        let payload = JSON.stringify({
                first_name: person.firstName,
                last_name: person.lastName,
                is_gay: person.isGay
            });
        payload = "'" + payload + "'";
        $.ajax({
            type: 'POST',
            // url: _config.api.invokeUrl + '/persons',
            url: 'https://aretheygay.org/api/persons',
            data: payload,
            contentType: "application/json; charset=utf-8",
            async: false,
            success: function (result) {
                if (result.statusCode === 201){
                    $('#submit_message').html("Person created.")
                }
                console.log('success');
                console.log(result);
            },
            error: function (req, err) {
                console.error('Error: ', err);
                console.error('Response: ', req);
            },
        });

    });

    $.get("https://aretheygay.org/api/persons", function (data) {
        console.log('successful get');
        console.log(data)
    });


});

class Person {
    constructor(firstName, lastName, isGay) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.isGay = isGay;
    }
}