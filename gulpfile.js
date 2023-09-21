var gulp = require("gulp");
var browserify = require("browserify");
var babelify = require("babelify");
var source = require("vinyl-source-stream");

gulp.task("default", async () => 
{
    return browserify("./source/app.js")
        .transform(babelify)
        .bundle()
        .pipe(source("main.js"))
        .pipe(gulp.dest("/var/www/html/js"));
})