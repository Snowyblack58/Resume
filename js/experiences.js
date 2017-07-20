define([
    'jquery',
    'underscore',
    'text!../../json/education.json',
    'text!../../partials/experience.html'
], function($, _, educationText, Experience){
    $(document).ready(function(){
        loadEducationExperiences();
        $(window).scrollTop(sessionStorage.getItem("preRefreshPosition"));
        initCheckpoints();
    })

    $(window).unload(function() {
        sessionStorage.setItem("preRefreshPosition", $(window).scrollTop());
    });

    function loadEducationExperiences(){
        var educationJSON = JSON.parse(educationText);
        var newExperienceTemplate = _.template(Experience);
        for(var cnt = 0; cnt < educationJSON.length; cnt++){
            var newExperienceHTML = newExperienceTemplate(educationJSON[cnt]);
            $('#education').append(newExperienceHTML);
        }
    }
});