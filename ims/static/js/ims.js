$(document).ready(function() {
	$("#guyoverlay").stop().animate({top:'671px'},{queue:false,duration:5000} );
	$("#dudeoverlay").stop().animate({top:'-665px'},{queue:false,duration:3500} );
        $('.messages').fadeOut(3000);

	$('.slideshow').cycle({
		fx: 'scrollLeft',
		speed: 500,
		timeout: 7000
	});
	
});	
