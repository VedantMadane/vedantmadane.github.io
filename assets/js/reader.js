document.addEventListener("DOMContentLoaded", function () {
  var audio = document.getElementById("shatakam-audio");
  var verses = document.querySelectorAll(".verse-card");

  if (!audio) return;

  var lastHighlighted = null;

  audio.addEventListener("timeupdate", function () {
    var t = audio.currentTime;
    verses.forEach(function (verse) {
      var start = parseFloat(verse.dataset.start) || 0;
      var end = parseFloat(verse.dataset.end) || 0;
      if (start === 0 && end === 0) return;

      if (t >= start && t < end) {
        if (!verse.classList.contains("highlight")) {
          verse.classList.add("highlight");
          if (lastHighlighted !== verse) {
            verse.scrollIntoView({ behavior: "smooth", block: "center" });
            lastHighlighted = verse;
          }
        }
      } else {
        verse.classList.remove("highlight");
      }
    });
  });
});
