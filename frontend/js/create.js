$( document ).ready(function() {
    function ajaxPost(endp, body) {
      url = baseURL + endp;
      return axios.post(url, body);
    }

    $('#createPersonForm').submit(function (e) {
        console.log('here');
        let firstName= $('#createPersonForm [name="firstName"]').val();
        let lastName = $('#createPersonForm [name="lastName"]').val();
        let isGay = $('#createPersonForm [name="isGay"]').val();
        ajaxPost('/persons', {
            first_name: firstName,
            last_name: lastName,
            is_gay: isGay
        }).then((response) => {
            console.log(response);
            // if (response.statusCode === '201') {
        //         $('.create_response').html("Person successfully created!")
        //     } else {
        //         $('.create_response').html("Error saving person.")
        //     }
        }).catch((err) => {
            console.log(err);
        });

    });
});
