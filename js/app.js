require.config({
    baseUrl: 'js',
    paths: {
        jquery: 'libs/jquery-1.11.3.min',
        bootstrap: 'libs/bootstrap.min',
    },
    waitSeconds: 30
})

require([
    'js/scroll.js',
    'js/projects.js',
    'js/links.js'
]);

console.log("Hi there :) If you want to check out the code, go to https://github.com/davidbzhao/Resume")