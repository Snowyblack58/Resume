# Resume

Live @ [http://davidzhao.me/Resume/](http://davidzhao.me/Resume/)

## How it works

Note: There was a major update to this page in Aug 2018.

Currently, this page is developed using Django, SASS, JavaScript, HTML. The site is served off of an Amazon EC2 instance.

Previously, the site used basic HTML, JavaScript, and CSS with a few libraries like JQuery (for convenience), Underscore (for templates), and Require (for fun), as well as Bootstrap (for design). Because this site was originally on Github Pages, there was no opportunity to use an actual backend like Django. All the templates had to be combined locally and then pushed up to the repo.

## Optimizations

At the start of the optimization process, the site loaded in around 1.1s with 1.1 MB data transferred. Compressing and moving images to AWS Cloudfront reduced the data transferred to 222 KB, resulting in a load time of around 0.6s.