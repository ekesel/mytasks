// $( '#topheader .navbar-nav a' ).on( 'click', function () {
// 	$( '#topheader .navbar-nav' ).find( 'li.active' ).removeClass( 'active' );
// 	$( this ).parent( 'li' ).addClass( 'active' );
// });

jQuery(function($) {
	var path = window.location.href; 
	// because the 'href' property of the DOM element is the absolute path
	$('ul a').each(function() {
	  if (this.href === path) {
		// $(this).addClass('active');
		$( this ).parent( 'li' ).addClass( 'active' );
	  }
	  else{
		$( this ).parent( 'li' ).removeClass( 'active' );
	  }
	});
  });

jQuery(function($) {
  var path = window.location.href; 
  // because the 'href' property of the DOM element is the absolute path
  $('ol a').each(function() {
    if (this.href === path) {
      // $(this).addClass('active');
      $( this ).addClass( 'p-active' );
    }
    else{
      $( this ).removeClass( 'p-active' );
    }
  });
});

