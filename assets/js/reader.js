document.addEventListener("DOMContentLoaded", function() {
  const audio = document.getElementById('shatakam-audio');
  const verses = document.querySelectorAll('.verse-card');

  // THE FIX: If there is no audio element, exit silently. The text will still render perfectly.
  if (!audio) {
      console.log("Running in text-only mode.");
      return; 
  }

  audio.addEventListener('timeupdate', () => {
    let currentTime = audio.currentTime;
    verses.forEach(verse => {
      let start = parseFloat(verse.dataset.start) || 0;
      let end = parseFloat(verse.dataset.end) || 0;
      if (currentTime >= start && currentTime <= end) {
        verse.classList.add('highlight');
      } else {
        verse.classList.remove('highlight');
      }
    });
  });
});
