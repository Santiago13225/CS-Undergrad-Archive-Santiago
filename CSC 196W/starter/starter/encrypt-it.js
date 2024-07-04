/*
 * Starter file 
 */
alert("Hello, world!");
console.log("Window loaded!");

function handleClick() {
  alert("Hello, world!");
  console.log("Button clicked!");
}

(function() {
  "use strict";
  /**
   * The starting point in our program, setting up a listener
   * for the "load" event on the window, signalling the HTML DOM has been constructed
   * on the page. When this event occurs, the attached function (init) will be called.
   */
  window.addEventListener("load", init);

  /* Helper Functions */
  function $(id) {
    return document.getElementById(id);
  }
  
  function $$(clazz) {
    return document.querySelectorAll(clazz);
  }

  function isLowerCaseLetter(c) {
    return c >= 'a' && c <= 'z';
  }

  /**
   * TODO: Write a function comment using JSDoc.
   */
  function init() {
    // Note: In this function, we usually want to set up our event handlers
    // for UI elements on the page.
    $("encrypt-it").addEventListener("click", generateCipher);
    $("reset").addEventListener("click", function() { // example of anonymous function
      $("result").innerText = "";
    });

    let fontSizeOptions = $$("input[name=text-size]");
    for (let i = 0; i < fontSizeOptions.length; i++) {
      fontSizeOptions[i].addEventListener("change", function() {
        $("result").style.fontSize = this.value;
      });
    }
  }
 
  // Add any other functions in this area (you should not implement your
  // entire program in the init function, for similar reasons that
  // you shouldn't write an entire Java program in the main method).
  function generateCipher() {
    if ($("cipher-type").value == "shift") {
      $("result").innerText = shiftCipher($("input-text").value.toLowerCase());
    } else {
      $("result").innerText = randomCipher($("input-text").value.toLowerCase());
    }
  }

  /**
   * Returns an encrypted version of the given text, where
   * each letter is shifted alphabetically ahead by 1 letter,
   * and 'z' is shifted to 'a' (creating an alphabetical cycle).
   */
  function shiftCipher(text) {
    text = text.toLowerCase();
    let result = "";
    for (let i = 0; i < text.length; i++) {
      if (!isLowerCaseLetter(text[i])) { // keep non-letter characters the same 
        result += text[i];
      } else if (text[i] == 'z') {
        result += 'a';
      } else { // letter is between 'a' and 'y'
        let letter = text.charCodeAt(i); 
        let resultLetter = String.fromCharCode(letter + 1);
        result += resultLetter;
      }
    }
    if ($("all-caps").checked) {
      result = result.toUpperCase();
    }
    return result;
  }
  
})();