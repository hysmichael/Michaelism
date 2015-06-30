
function parseColor(color_string) {
    var m;
    m = color_string.match(/^#([0-9a-f]{6})$/i)[1];
    if (m) {
        return [
            parseInt(m.substr(0,2),16),
            parseInt(m.substr(2,2),16),
            parseInt(m.substr(4,2),16)
        ];
    }
}

function colorRGBA(RGB, alpha) {
    return 'rgba(' + RGB[0] + ',' + RGB[1] + ',' + RGB[2] + ',' + alpha +')';
}
