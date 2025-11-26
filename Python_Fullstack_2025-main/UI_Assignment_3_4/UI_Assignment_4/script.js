const video = document.getElementById("video");
const playPauseBtn = document.getElementById("playPause");
const progressContainer = document.getElementById("progressContainer");
const progressBar = document.getElementById("progressBar");
const currentTimeEl = document.getElementById("currentTime");
const durationEl = document.getElementById("duration");
const muteBtn = document.getElementById("muteBtn");
const volumeSlider = document.getElementById("volumeSlider");
const fullscreenBtn = document.getElementById("fullscreenBtn");

// Format seconds -> m:ss
function formatTime(seconds) {
  const mins = Math.floor(seconds / 60) || 0;
  const secs = Math.floor(seconds % 60) || 0;
  return `${mins}:${secs < 10 ? "0" + secs : secs}`;
}

// Play / Pause toggle
function togglePlay() {
  if (video.paused || video.ended) {
    video.play();
  } else {
    video.pause();
  }
}

function updatePlayIcon() {
  if (video.paused || video.ended) {
    playPauseBtn.innerHTML = "&#9658;"; // play
    playPauseBtn.setAttribute("aria-label", "Play");
  } else {
    playPauseBtn.innerHTML = "&#10074;&#10074;"; // pause
    playPauseBtn.setAttribute("aria-label", "Pause");
  }
}

// Progress bar & time
function updateProgress() {
  if (!isNaN(video.duration)) {
    const percent = (video.currentTime / video.duration) * 100;
    progressBar.style.width = `${percent}%`;
    currentTimeEl.textContent = formatTime(video.currentTime);
    durationEl.textContent = formatTime(video.duration);
  }
}

function setProgress(e) {
  const rect = progressContainer.getBoundingClientRect();
  const clickX = e.clientX - rect.left;
  const width = rect.width;
  const percent = clickX / width;
  video.currentTime = percent * video.duration;
}

// Volume & mute
function updateVolume() {
  video.volume = volumeSlider.value;
  if (video.volume === 0) {
    video.muted = true;
  } else {
    video.muted = false;
  }
  updateMuteIcon();
}

function toggleMute() {
  video.muted = !video.muted;
  if (video.muted) {
    volumeSlider.dataset.prev = volumeSlider.value;
    volumeSlider.value = 0;
  } else {
    const prev = volumeSlider.dataset.prev || 0.7;
    volumeSlider.value = prev;
    video.volume = prev;
  }
  updateMuteIcon();
}

function updateMuteIcon() {
  if (video.muted || video.volume === 0) {
    muteBtn.textContent = "🔇";
  } else if (video.volume < 0.5) {
    muteBtn.textContent = "🔉";
  } else {
    muteBtn.textContent = "🔊";
  }
}

// Fullscreen
function toggleFullscreen() {
  if (!document.fullscreenElement) {
    if (video.parentElement.requestFullscreen) {
      video.parentElement.requestFullscreen();
    }
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    }
  }
}

// Event listeners
playPauseBtn.addEventListener("click", togglePlay);
video.addEventListener("click", togglePlay);
video.addEventListener("play", updatePlayIcon);
video.addEventListener("pause", updatePlayIcon);
video.addEventListener("timeupdate", updateProgress);
video.addEventListener("loadedmetadata", updateProgress);

progressContainer.addEventListener("click", setProgress);

muteBtn.addEventListener("click", toggleMute);
volumeSlider.addEventListener("input", updateVolume);

fullscreenBtn.addEventListener("click", toggleFullscreen);

// Keyboard shortcuts for accessibility
document.addEventListener("keydown", (e) => {
  if (e.target.tagName === "INPUT") return;

  switch (e.key.toLowerCase()) {
    case " ":
    case "k":
      e.preventDefault();
      togglePlay();
      break;
    case "m":
      toggleMute();
      break;
    case "f":
      toggleFullscreen();
      break;
    case "arrowright":
      video.currentTime = Math.min(video.currentTime + 5, video.duration || 0);
      break;
    case "arrowleft":
      video.currentTime = Math.max(video.currentTime - 5, 0);
      break;
    default:
      break;
  }
});

// Initial state
updateMuteIcon();


