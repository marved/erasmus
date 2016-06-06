app.filter('htmlEscape', function() {
    return function(input) {
        if (!input) {
            return '';
        }
        return input.
            replace(/&/g, '&amp;').
            replace(/</g, '&lt;').
            replace(/>/g, '&gt;').
            replace(/'/g, '&#39;').
            replace(/"/g, '&quot;')
        ;
    };
});
app.filter('textToHtml', ['$sce', 'htmlEscapeFilter', function($sce, htmlEscapeFilter) {
    return function(input) {
        if (!input) {
            return '';
        }
        input = htmlEscapeFilter(input);

        var output = '';
        $.each(input.split("\n"), function(key, paragraph) {
            output += '<p>- ' + paragraph + '</p>';
        });

        return $sce.trustAsHtml(output);
    };
}])