//Snackbar.
var mnt = {}


//frappe.require("assets/frappe/js/lib/jquery/jquery-ui.min.js");
frappe.require("assets/frappe/js/lib/jquery/bootstrap_theme/jquery-ui.selected.css");
frappe.require("assets/frappe/js/lib/jquery/jquery.ui.slider.min.js");
frappe.require("assets/frappe/js/lib/jquery/jquery.ui.sliderAccess.js");
frappe.require("assets/frappe/js/lib/jquery/jquery.ui.timepicker-addon.css");
frappe.require("assets/frappe/js/lib/jquery/jquery.ui.timepicker-addon.js");

mnt.summernotize = function(inputcontrol, destroy = false) {
  if (!destroy) {
    inputcontrol.summernote({ height: 300, focus: true }); 
    //$('.note-btn').attr('title', ''); //Disable tooltip on summernote. Malformed due to sequence of inclusion jquery, bootstrap.
  } else {
    inputcontrol.summernote('destroy');
  }
}

mnt.show_alert = function(txt, seconds) {
  if(!$('#dialog-container').length) {
    $('<div id="dialog-container"><div id="alert-container"></div></div>').appendTo('body');
  }

  var div = $(repl('<div class="alert desk-alert" style="display: none;">'
      + '<a class="close">&times;</a><span class="alert-message">%(txt)s</span>'
    + '</div>', {txt: txt}))
    .appendTo("#alert-container")
    .fadeIn(300);

  div.find('.close').click(function() {
    $(this).parent().remove();
    return false;
  });

  div.delay(seconds ? seconds * 1000 : 7000).fadeOut(300);
  return div;
}

mnt.init_datepicker = function(datepickerinput) {
  // frappe.datepicker_format = "{{ frappe.date_format.replace('yyyy', 'yy') }}";
  frappe.call({
    method: "discuit.api.get_frappe_date_format",
    callback: function(r) {
      if (!r.exc) {
       $(datepickerinput).datepicker({
          altFormat:'yy-mm-dd',
          changeYear: true,
          yearRange: "-70Y:+10Y",
          dateFormat: r.message,
        });
      }
    }
  });
}

mnt.refresh_page_element = function(element_name, refresh_within_parent=1, after_refresh_callback=undefined) {
  if (after_refresh_callback === undefined) {
    after_refresh_callback = function () {
      // pass...
    };
  } 

  $(element_name).fadeOut();

  if (refresh_within_parent == 1) {
    $(element_name).parent().load(document.URL + element_name, function() {
      $(element_name).fadeIn();
      after_refresh_callback();
      console.log('Refreshed "' + element_name + '" within parent');
    });
  } else {
    $(element_name).load(document.URL + ' ' + element_name, function() {
      $(element_name).fadeIn();
      after_refresh_callback();
      console.log('Refreshed "' + element_name + '" directly.');
    });
  }
}

mnt.invert_color = function(hexTripletColor) {
    var color = hexTripletColor;
    color = color.substring(1);
    color = parseInt(color, 16);
    color = 0xFFFFFF ^ color;
    if (color < 126) {
      color = "000000";
    } else {
      color = "FFFFFF"
    }
    color = "#" + color;
    return color;
}

mnt.get_url_param = function(param="", param_value_delimiter="+") {
    var params = document.URL.split('?')[1];
    var params_json = JSON.parse('{"' + decodeURI(params).replace(/"/g, '\\"').replace(/&/g, '","').replace(/=/g,'":"') + '"}');
    if (params_json[param]!=null) {
      return params_json[param].split(param_value_delimiter);
    } else {
      return [];
    }
}

mnt.get_url_location = function() {
  return document.URL.split('?')[0];
} 