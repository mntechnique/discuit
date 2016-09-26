// Copyright (c) 2016, MN Technique and contributors
// For license information, please see license.txt

frappe.ui.form.on('Forum Category', {
	refresh: function(frm) {

	}
});

frappe.ui.form.on("Forum Category", "onload_post_render", function(frm) {
  frappe.require('assets/frappe/js/lib/jscolor/jscolor.js', function() {
    $(frm.fields_dict["category_color"].input).addClass('color {required:false,hash:true}');
    jscolor.bind();
  });
});
