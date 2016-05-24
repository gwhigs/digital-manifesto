"use strict";

/* See http://stackoverflow.com/questions/5379120/get-the-highlighted-selected-text */
function msieversion() {
    var ua = window.navigator.userAgent;

    var msie = ua.indexOf('MSIE ');
    if (msie > 0) {
        // IE 10 or older => return version number
        return parseInt(ua.substring(msie + 5, ua.indexOf('.', msie)), 10);
    }

    var trident = ua.indexOf('Trident/');
    if (trident > 0) {
        // IE 11 => return version number
        var rv = ua.indexOf('rv:');
        return parseInt(ua.substring(rv + 3, ua.indexOf('.', rv)), 10);
    }

    var edge = ua.indexOf('Edge/');
    if (edge > 0) {
       // Edge (IE 12+) => return version number
       return parseInt(ua.substring(edge + 5, ua.indexOf('.', edge)), 10);
    }

    // other browser
    return false;
}

var msie = msieversion();

// selection objects will differ between browsers
function getSelection () {
  return ( msie )
    ? document.selection
    : ( window.getSelection || document.getSelection )();
}

// range objects will differ between browsers
function getRange () {
  return ( msie )
      ? getSelection().createRange()
      : getSelection().getRangeAt( 0 )
}

// abstract getting a parent container from a range
function parentContainer ( range ) {
  return ( msie )
      ? range.parentElement()
      : range.commonAncestorContainer;
}

function updateTextSelect ( text_div, start_index_input, end_index_input ) {
    var range = getRange();
    var check_next = true;
    while( check_next ) {
        var parent = parentContainer(range)
    }
}

/* http://stackoverflow.com/questions/4811822/get-a-ranges-start-and-end-offsets-relative-to-its-parent-container */

function getCaretCharacterOffsetWithin(element) {
    var caretOffset = 0;
    var doc = element.ownerDocument || element.document;
    var win = doc.defaultView || doc.parentWindow;
    var sel;
    if (typeof win.getSelection != "undefined") {
        sel = win.getSelection();
        if (sel.rangeCount > 0) {
            var range = win.getSelection().getRangeAt(0);
            var preCaretRange = range.cloneRange();
            preCaretRange.selectNodeContents(element);
            preCaretRange.setEnd(range.endContainer, range.endOffset);
            caretOffset = preCaretRange.toString().length;
        }
    } else if ( (sel = doc.selection) && sel.type != "Control") {
        var textRange = sel.createRange();
        var preCaretTextRange = doc.body.createTextRange();
        preCaretTextRange.moveToElementText(element);
        preCaretTextRange.setEndPoint("EndToEnd", textRange);
        caretOffset = preCaretTextRange.text.length;
    }
    return caretOffset;
}