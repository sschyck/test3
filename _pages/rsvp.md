---
layout: page
permalink: /rsvp/
title: Defense RSVP
description: RSVP page for Sarah's PhD Defense.
nav: true
nav_order: 5
---

## RSVP Defense Form

Please fill out the form below to RSVP for the event:

<form id="rsvp-form" class="rsvp-form" action="https://script.google.com/macros/s/AKfycby_KcILhOhdLySQY2lnJmg_EbNnGfK9Ums3cxN5UwozH9npUlQWzhbWZUg1bf262HQr/exec" method="POST">
    <div class="row">
        <div class="col-md-6 col-sm-6">
            <div class="form-input-group">
                <i class="fa fa-envelope"></i>
                <input type="email" name="email" class="" placeholder="Your email" required>
            </div>
        </div>
        <div class="col-md-6 col-sm-6">
            <div class="form-input-group">
                <i class="fa fa-user"></i>
                <input name="name" class="" placeholder="Your name" required>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-md-6 col-sm-6">
            <div class="form-input-group">
                <i class="fa fa-users"></i>
                <input type="number" name="extras" class="" min="0" max="4" placeholder="# of people" required>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-md-12" id="alert-wrapper"></div>
    </div>
    <button class="btn-fill rsvp-btn">
        Yes, that's me!
    </button>
</form>

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
  $(document).ready(function() {
    function alert_markup(type, message) {
      return '<div class="alert alert-' + type + ' alert-dismissible fade show" role="alert">' +
        '<button type="button" class="close" data-dismiss="alert" aria-label="Close">' +
        '<span aria-hidden="true">&times;</span></button>' +
        message + '</div>';
    }

    $('#rsvp-form').on('submit', function(e) {
      e.preventDefault();
      var data = $(this).serialize();

      $('#alert-wrapper').html(alert_markup('info', '<strong>Just a sec!</strong> We are saving your details.'));

      $.post('https://script.google.com/macros/s/AKfycby_KcILhOhdLySQY2lnJmg_EbNnGfK9Ums3cxN5UwozH9npUlQWzhbWZUg1bf262HQr/exec', data)
        .done(function(data) {
          console.log(data);
          if (data.result === 'error') {
            $('#alert-wrapper').html(alert_markup('danger', data.message));
          } else {
            $('#alert-wrapper').html('');
            $('#rsvp-modal').modal('show');
          }
        })
        .fail(function (data) {
          console.log(data);
          $('#alert-wrapper').html(alert_markup('danger', '<strong>Sorry!</strong> There is some issue with the server. '));
        });
    });
  });
</script>
