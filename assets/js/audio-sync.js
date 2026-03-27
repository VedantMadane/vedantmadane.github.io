document.addEventListener("DOMContentLoaded", function () {
  var players = document.querySelectorAll("[data-audio-sync-player]");

  players.forEach(function (audio) {
    var root = audio.closest(".audio-sync-root") || document;
    var markers = Array.prototype.slice.call(root.querySelectorAll("[data-start][data-end]"));
    var lastTarget = null;

    if (markers.length === 0) return;

    function getTarget(marker) {
      if (marker.classList.contains("sync-anchor")) {
        return marker.nextElementSibling;
      }
      return marker;
    }

    audio.addEventListener("timeupdate", function () {
      var t = audio.currentTime;
      var activeMarker = null;

      markers.forEach(function (marker) {
        var start = parseFloat(marker.dataset.start || "0");
        var end = parseFloat(marker.dataset.end || "0");
        if (t >= start && t < end) {
          activeMarker = marker;
        }
      });

      var nextTarget = activeMarker ? getTarget(activeMarker) : null;

      if (lastTarget && lastTarget !== nextTarget) {
        lastTarget.classList.remove("sync-current");
      }

      if (!nextTarget) {
        lastTarget = null;
        return;
      }

      if (lastTarget !== nextTarget) {
        nextTarget.classList.add("sync-current");
        nextTarget.scrollIntoView({ behavior: "smooth", block: "center" });
        lastTarget = nextTarget;
      }
    });
  });
});
