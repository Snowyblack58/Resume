// Project links
$('.project-card').click(function(event){
	var link = $(this).parent().attr('data-href');
	window.open(link, '_blank');
})

//Contact Links

$(".icon-github").click(function(){
	window.open("https://github.com/davidbzhao","_blank");
});

$(".icon-linkedin").click(function(){
	window.open("https://www.linkedin.com/in/davidbzhao","_blank");
});

