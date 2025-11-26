# UI Assignment 3 - Music Player (OMusic)

A modern, minimal music player built with HTML, CSS, and JavaScript. This application provides a sleek interface for playing audio tracks with full playback controls.

## Features

- 🎵 **Playlist Management**: Display and manage a list of tracks in a table format
- ▶️ **Playback Controls**: Play, pause, previous, and next track navigation
- 📊 **Progress Tracking**: Visual progress bar with current time and duration display
- 🔊 **Volume Control**: Adjustable volume with up/down buttons and percentage display
- 🎨 **Modern UI**: Clean, minimal design with sidebar navigation
- 📱 **Responsive Design**: Works on different screen sizes

## File Structure

```
UI_assignment_3/
├── index.html          # Main HTML structure
├── style.css           # Styling and layout
├── script.js           # JavaScript functionality
├── audio files/        # Directory containing MP3 audio files
│   ├── Chappell_Roan_-_HOT_TO_GO_(mp3.pm).mp3
│   ├── Chappell_Roan_-_Pink_Pony_Club_(mp3.pm).mp3
│   ├── Chappell_Roan_-_Red_Wine_Supernova_2023_(mp3.pm).mp3
│   └── Lana_DelRey_-_Million_Dollar_Man_(mp3.pm).mp3
└── music cover/        # Album cover images
    ├── Lana.jpg
    └── Roan.jpg
```

## How to Use

1. **Open the Application**
   - Open `index.html` in a modern web browser (Chrome, Firefox, Edge, etc.)

2. **Play Music**
   - Click on any track in the "Global Top 50" table to start playing
   - Use the play/pause button in the bottom player bar
   - Use previous (⏮) and next (⏭) buttons to navigate between tracks

3. **Control Playback**
   - Drag the progress slider to seek to different positions in the track
   - View current time and total duration below the progress bar

4. **Adjust Volume**
   - Click the volume up (+) or volume down (−) buttons
   - Volume percentage is displayed next to the controls

5. **Navigation**
   - Use the sidebar menu to navigate between sections (Home, Discover, Radio, Podcast)
   - Browse your library (Albums, Songs, Artists)

## Technical Details

### HTML Structure
- Sidebar navigation with menu items
- Main content area with hero section and track table
- Bottom player bar with controls
- HTML5 `<audio>` element for playback

### CSS Features
- Modern card-based design
- Smooth transitions and hover effects
- Responsive layout
- Custom styling for controls and progress bars

### JavaScript Functionality
- Track management and playlist handling
- Audio playback control
- Progress bar updates
- Volume management
- Track switching (previous/next)
- Dynamic UI updates

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Edge
- Safari
- Opera

## Notes

- Make sure all audio files are in the `audio files/` directory
- Cover images should be placed in the `music cover/` directory
- The player uses HTML5 audio API for cross-browser compatibility
- All tracks are loaded from the local `audio files/` folder

## Customization

To add your own tracks:
1. Place MP3 files in the `audio files/` directory
2. Update the track list in `script.js` with your track information
3. Add corresponding cover images to the `music cover/` directory

---

**Assignment**: UI Assignment 3  
**Technologies**: HTML5, CSS3, JavaScript (Vanilla)  
**Author**: Python Fullstack 2025

