var gulp = require('gulp');

var gulp = require('gulp');
var browserify = require('browserify');
var babelify = require('babelify');
var source = require('vinyl-source-stream');

gulp.task('default', function () {
	return browserify('./source/main.js')
	.transform(babelify, {presets: ["es2015", "react"]})
	.bundle()
	.pipe(source('app.js'))
	.pipe(gulp.dest('./static/'));
});

// Watch listeners
gulp.task('watch', function() {
    gulp.watch('./templates/*.html', ['templates']);
});