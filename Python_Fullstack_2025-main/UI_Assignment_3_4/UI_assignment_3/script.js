/* Updated playlist + fixed volume logic */
(function(){
  const audio = document.getElementById('audio');

  const playBtn = document.getElementById('play');
  const prevBtn = document.getElementById('prev');
  const nextBtn = document.getElementById('next');
  const playIcon = document.getElementById('playIcon');
  const pauseIcon = document.getElementById('pauseIcon');

  const heroPlay = document.getElementById('heroPlay');

  const progress = document.getElementById('progress');
  const curLabel = document.getElementById('cur');
  const durLabel = document.getElementById('dur');

  const miniTitle = document.getElementById('miniTitle');
  const miniArtist = document.getElementById('miniArtist');
  const miniCover = document.getElementById('miniCover');
  const heroCover = document.getElementById('heroCover');

  const volDown = document.getElementById('volDown');
  const volUp = document.getElementById('volUp');
  const volLabel = document.getElementById('volLabel');

  const trackTableBody = document.querySelector('#trackTable tbody');

  // ----- playlist -----
  const playlist = [
    {
      title: "HOT TO GO",
      artist: "Chappell Roan",
      src: "audio files/Chappell_Roan_-_HOT_TO_GO_(mp3.pm).mp3",
      cover: "music cover/Roan.jpg",
      time: null
    },
    {
      title: "Red Wine Supernova (2023)",
      artist: "Chappell Roan",
      src: "audio files/Chappell_Roan_-_Red_Wine_Supernova_2023_(mp3.pm).mp3",
      cover: "music cover/Roan.jpg",
      time: null
    },
    {
      title: "Pink Pony Club",
      artist: "Chappell Roan",
      src: "audio files/Chappell_Roan_-_Pink_Pony_Club_(mp3.pm).mp3",
      cover: "music cover/Roan.jpg",
      time: null
    },
    {
      title: "Million Dollar Man",
      artist: "Lana Del Rey",
      src: "audio files/Lana_DelRey_-_Million_Dollar_Man_(mp3.pm).mp3",
      cover: "music cover/Lana.jpg",
      time: null
    }
  ];

  let idx = 0;
  let isSeeking = false;

  // render playlist table
  function renderTable(){
    trackTableBody.innerHTML = '';
    playlist.forEach((t,i)=>{
      const tr = document.createElement('tr');

      const tdIndex = document.createElement('td');
      tdIndex.className = 'small';
      tdIndex.textContent = String(i+1).padStart(2,'0');

      const tdTitle = document.createElement('td');
      tdTitle.textContent = t.title;

      const tdArtist = document.createElement('td');
      tdArtist.className = 'small';
      tdArtist.textContent = t.artist;

      const tdTime = document.createElement('td');
      tdTime.className = 'small';
      tdTime.textContent = t.time || '—';
      t._timeCell = tdTime;

      tr.appendChild(tdIndex);
      tr.appendChild(tdTitle);
      tr.appendChild(tdArtist);
      tr.appendChild(tdTime);

      tr.addEventListener('click', ()=>{ loadTrack(i); play(); });
      trackTableBody.appendChild(tr);
    });
  }

  // load a track
  function loadTrack(i){
    idx = i;
    const t = playlist[idx];
    audio.src = t.src;

    miniTitle.textContent = t.title;
    miniArtist.textContent = t.artist;
    miniCover.src = t.cover || '';
    heroCover.src = t.cover || '';

    curLabel.textContent = '0:00';
    durLabel.textContent = t.time || '0:00';
    progress.value = 0;
  }

  // play/pause
  function play(){
    if(!audio.src){
      loadTrack(0);
    }
    audio.play().then(()=>{
      playIcon.style.display = 'none';
      pauseIcon.style.display = '';
      playBtn.setAttribute('aria-label','Pause');
    }).catch((e)=>console.warn('Playback error', e));
  }

  function pause(){
    audio.pause();
    playIcon.style.display = '';
    pauseIcon.style.display = 'none';
    playBtn.setAttribute('aria-label','Play');
  }

  playBtn.addEventListener('click', ()=>{
    if(!audio.src) return;
    if(audio.paused) play(); else pause();
  });

  prevBtn.addEventListener('click', ()=>{
    idx = (idx - 1 + playlist.length) % playlist.length;
    loadTrack(idx);
    play();
  });

  nextBtn.addEventListener('click', ()=>{
    idx = (idx + 1) % playlist.length;
    loadTrack(idx);
    play();
  });

  heroPlay.addEventListener('click', ()=>{
    if(!audio.src) loadTrack(0);
    play();
  });

  // ---- VOLUME CONTROL ----
  const VOLUME_STEP = 0.05; // 5% steps so change is clearly audible

  function setVolume(v){
    const clamped = Math.min(1, Math.max(0, Math.round(v * 100) / 100));
    audio.volume = clamped;
    if (volLabel) volLabel.textContent = `${Math.round(audio.volume * 100)}%`;
  }

  // initialize UI
  setVolume(audio.volume ?? 1);

  if (volDown && volUp) {
    volDown.addEventListener('click', () => setVolume(audio.volume - VOLUME_STEP));
    volUp.addEventListener('click', () => setVolume(audio.volume + VOLUME_STEP));
  }

  // time + progress
  audio.addEventListener('loadedmetadata', ()=>{
    const dur = Math.floor(audio.duration || 0);
    progress.max = dur;
    durLabel.textContent = formatTime(dur);

    const t = playlist[idx];
    t.time = formatTime(dur);
    if (t._timeCell) t._timeCell.textContent = t.time;
  });

  audio.addEventListener('timeupdate', ()=>{
    if(isSeeking) return;
    progress.value = Math.floor(audio.currentTime);
    curLabel.textContent = formatTime(Math.floor(audio.currentTime));
  });

  audio.addEventListener('ended', ()=>{
    idx = (idx + 1) % playlist.length;
    loadTrack(idx);
    play();
  });

  progress.addEventListener('input', ()=>{
    isSeeking = true;
    curLabel.textContent = formatTime(Number(progress.value));
  });

  progress.addEventListener('change', ()=>{
    audio.currentTime = Number(progress.value);
    isSeeking = false;
  });

  function formatTime(s){
    if (!Number.isFinite(s)) return '0:00';
    const m = Math.floor(s / 60);
    const r = s % 60;
    return `${m}:${String(r).padStart(2,'0')}`;
  }

  // preload durations for table
  function preloadDurations(){
    playlist.forEach((t)=>{
      if (t.time) return;
      const temp = new Audio();
      temp.src = t.src;
      temp.addEventListener('loadedmetadata', ()=>{
        const d = Math.floor(temp.duration || 0);
        t.time = formatTime(d);
        if (t._timeCell) t._timeCell.textContent = t.time;
      });
    });
  }

  // init
  renderTable();
  loadTrack(0);
  preloadDurations();

})();
