// Copyright (c) 2016, MN Technique and contributors
// For license information, please see license.txt

frappe.ui.form.on('Forum Category', {
	refresh: function(frm) {
		
	},

	category_color: function(frm) {
		var category_text_color = invertColor(frm.doc.category_color);
		frm.set_value("category_text_color", category_text_color);
		//frappe.msgprint('FG '+ category_text_color + ', BG ' + frm.doc.category_color);
	}
});

frappe.ui.form.on("Forum Category", "onload_post_render", function(frm) {
  frappe.require('assets/frappe/js/lib/jscolor/jscolor.js', function() {
    $(frm.fields_dict["category_color"].input).addClass('color {required:false,hash:true}');
    jscolor.bind();
  });
});


function invertColor(hexTripletColor) {
    var color = hexTripletColor;
    color = color.substring(1);
    color = parseInt(color, 16);
    color = 0xFFFFFF ^ color;
    if (color < 8388607) {
      color = "000000";
    } else {
      color = "FFFFFF"
    }
    var out = "#" + color;
    return out;
}
// function invertColor(hexTripletColor) {
//     var color = hexTripletColor;
//     color = color.substring(1);           // remove #
//     color = parseInt(color, 16);          // convert to integer
//     color = 0xFFFFFF ^ color;             // invert three bytes
//     color = color.toString(16);           // convert to hex
//     color = ("000000" + color).slice(-6); // pad with leading zeros
//     color = "#" + color;                  // prepend #
//     return color;
// }

// function invertColor(hexTripletColor) {
//     var color = hexTripletColor;
//     color = color.substring(1);           // remove #
//     color = parseInt(color, 16);          // convert to integer
//     color = 0xFFFFFF ^ color;             // invert three bytes
//     color = color.toString(16);           // convert to hex
//     color = ("000000" + color).slice(-6); // pad with leading zeros
//     color = "#" + color;                  // prepend #
//     return color;
// }