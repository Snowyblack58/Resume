define([
    'jquery',
    'underscore',
    'text!../../json/education.json',
    'text!../../partials/experience.html'
], function($, _, educationJSON, Experience){
    console.log(educationJSON);
    console.log(typeof(educationJSON));
    var newExperienceTemplate = _.template(Experience);
});