function ConfirmDelete(elem) {
    var deleteId = $(elem).attr('data-id')
    localStorage.setItem('deleteId', deleteId);
    //$('#deleteModal').modal();
    var txt;
    if (confirm("Are you sure you want to delete?")) {
        var url = "/admin/users/delete/" + deleteId;
        alert(url);
        $.ajax({
            url: url,
            data: {
                id: deleteId
            },
            type: 'GET',
            success: function(res) {
                var result = JSON.parse(res);
                if (result.status == 'OK') {
                    $('#deleteModal').modal('hide');
                } else {
                    alert(result.status);
                }
            },
            error: function(error) {
                console.log(error);
            }
        });
    }
}

/*
function ConfirmDelete(elem) {
    var deleteId = $(elem).attr('data-id');
    alert(deleteId);
    var confirm_ret = window.confirm('Are you sure you want to delete?');
    if ( confirm_ret == true ) {
        $.ajax({
            url: '/admin/users/delete/' + deleteId,
            data: {
                id: deleteId
            },
            type: 'POST',
            success: function(response){
                console.log(response);
            },
            error: function(error){
                console.log(error);
            }
        }
    }
}
*/

function Delete() {
    var deleteId = localStorage.getItem('deleteId')
    alert(deleteId)
    $.ajax({
        url: '/admin/users/delete/' + deleteId,
        data: {
            id: deleteId
        },
        type: 'POST',
        success: function(res) {
            console.log(res)
            var result = JSON.parse(res);
            if (result.status == 'OK') {
                $('#deleteModal').modal('hide');
            } else {
                alert(result.status);
            }
        },
        error: function(error) {
            console.log(error);
        }
    });
}
