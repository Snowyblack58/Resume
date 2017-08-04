define([
	'jquery',
], function($){
	$(document).ready(function(){
		initContactIconLinks();
		initFlyoutLink();
		backButton();
	});
	
	function initContactIconLinks(){
		$(".icon-github").click(function(){
			window.open("https://github.com/davidbzhao","_blank");
		});
		$(".icon-linkedin").click(function(){
			window.open("https://www.linkedin.com/in/davidbzhao","_blank");
		});
	}

	function initFlyoutLink(){
		$('#toCurrent').click(function(){
			window.open('http://davidzhao.me/Current/', '_self');
		});
	}

	function backButton(){
		$('#backButton').click(function(){
			window.open('http://davidzhao.me/', '_self');
		})
	}
})