/* Free Estimate Functions */

$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-base .modal-content").html("");
                $("#modal-base").modal("show");
            },
            success: function (data) {
                $("#modal-base .modal-content").html(data.html_form);
            }
        });
    };

    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#modal-base .modal-content").html(data.html_success_message);
                }
                else {
                    $("#modal-base .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    var homesaveForm = function (e) {
        e.preventDefault();
        var form = $(this);
        console.log("form submitted")
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $('#' + form.attr("id")).each(function () {
                        this.reset();
                    });
                    $("#modal-base .modal-content").html(data.html_success_message);
                    $("#modal-base").modal("show");
                }
                else {
                    $("#modal-base .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */


    // Update Employee Skill
    $(".js-estimate-request").on("click", loadForm);
    $("#modal-base").on("submit", ".js-estimate-request-form", saveForm);
    $("#contactUsForm").on("submit", homesaveForm);

});

