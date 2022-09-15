$('#select-client').change((e)=>{
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');
    var client_id = e.target.value;
    console.log(typeof(client_id));
    $.ajax({
        type: 'POST',
        url:"/coordinator/get_client/",
        data:{
            id:client_id,
            csrfmiddlewaretoken:csrftoken,
        },
        success: function(response){
            console.log('ajax is wordking done');
            const client = JSON.parse(response)
            console.log(client);
            $('#client-name').text(client.name);
            $('#client-serial').text(client.serial_number);
            $('#client-location').text(client.location);
        }
    })
})