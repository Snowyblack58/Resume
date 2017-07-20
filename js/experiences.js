define([
    'jquery',
    'underscore',
    'text!../../json/education.json',
    'text!../../json/work.json',
    'text!../../json/extracurricular.json',
    'text!../../partials/experience.html'
], function($, _, educationText, workText, extracurricularText, Experience){
    $(document).ready(function(){
        loadEducationExperiences();
        loadWorkExperiences();
        loadExtracurricularExperiences();
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

    function loadWorkExperiences(){
        var workJSON = JSON.parse(workText);
        var newExperienceTemplate = _.template(Experience);
        for(var cnt = 0; cnt < workJSON.length; cnt++){
            var newExperienceHTML = newExperienceTemplate(workJSON[cnt]);
            $('#work').append(newExperienceHTML);
        }
    }

    function loadExtracurricularExperiences(){
        var extracurricularJSON = JSON.parse(extracurricularText);
        var newExperienceTemplate = _.template(Experience);
        for(var cnt = 0; cnt < extracurricularJSON.length; cnt++){
            var newExperienceHTML = newExperienceTemplate(extracurricularJSON[cnt]);
            $('#extracurricular').append(newExperienceHTML);
        }
    }
});