document.addEventListener("DOMContentLoaded", function() {
  const audio = document.getElementById('shatakam-audio');
  const verses = document.querySelectorAll('.verse-card');

  if (!audio) return;

  audio.addEventListener('timeupdate', () => {
    let currentTime = audio.currentTime;

    verses.forEach(verse => {
      // Parse the start and end times from the HTML data attributes
      let start = parseFloat(verse.dataset.start);
      let end = parseFloat(verse.dataset.end);

      // If the current audio time is within this verse's timeframe, highlight it
      if (currentTime >= start && currentTime <= end) {
        verse.classList.add('highlight');
      } else {
        verse.classList.remove('highlight');
      }
    });
  });
});
