# UI Assignment 4 - Custom Video Player

A fully functional custom video player built with HTML, CSS, and JavaScript. This player provides a complete set of video playback controls with a modern, user-friendly interface.

## Features

- ▶️ **Play/Pause Control**: Start and pause video playback
- ⏱️ **Time Display**: Shows current playback time and total duration
- 📊 **Progress Bar**: Visual progress indicator with clickable seeking
- 🔊 **Volume Control**: Adjustable volume slider with mute/unmute functionality
- 🖥️ **Fullscreen Mode**: Toggle fullscreen viewing experience
- ⌨️ **Keyboard Shortcuts**: 
  - `Space` or `K` - Play/Pause
  - `M` - Mute/Unmute
  - `F` - Toggle Fullscreen
  - `←` / `→` - Seek backward/forward (10 seconds)
- 🎨 **Modern UI**: Clean, centered design with smooth animations
- 📱 **Responsive Design**: Adapts to different screen sizes

## File Structure

```
UI_Assignment_4/
├── index.html          # Main HTML structure
├── style.css           # Styling and layout
├── script.js           # JavaScript functionality
└── sample-video.mp4    # Video file (replace with your own)
```

## How to Use

1. **Setup**
   - Place your video file in the `UI_Assignment_4/` directory
   - Update the `src` attribute in `index.html` (line 22) to point to your video file:
     ```html
     <video id="video" class="video" src="your-video.mp4" preload="metadata">
     ```

2. **Open the Application**
   - Open `index.html` in a modern web browser

3. **Playback Controls**
   - **Play/Pause**: Click the play button (▶) or press `Space`/`K`
   - **Seek**: Click anywhere on the progress bar to jump to that position
   - **Volume**: Use the volume slider or press `M` to mute/unmute
   - **Fullscreen**: Click the fullscreen button (⛶) or press `F`

4. **Keyboard Shortcuts**
   - `Space` or `K` - Toggle play/pause
   - `M` - Toggle mute
   - `F` - Toggle fullscreen
   - `←` (Left Arrow) - Seek backward 10 seconds
   - `→` (Right Arrow) - Seek forward 10 seconds

## Technical Details

### HTML Structure
- HTML5 `<video>` element for video playback
- Custom control bar with all playback controls
- Semantic HTML5 elements for accessibility

### CSS Features
- Modern card-based video player design
- Smooth transitions and hover effects
- Gradient progress bar
- Responsive layout that centers on the page
- Custom-styled buttons and controls

### JavaScript Functionality
- Video playback control (play/pause)
- Progress bar updates in real-time
- Clickable progress bar for seeking
- Volume control with slider and mute button
- Fullscreen API integration
- Keyboard event handling
- Time formatting (MM:SS)
- Dynamic button icon updates

## Supported Video Formats

The player supports all formats supported by the HTML5 `<video>` element:
- MP4 (H.264)
- WebM
- OGG

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Edge
- Safari
- Opera

## Customization

### Changing Video Source
Edit `index.html` and update the video `src` attribute:
```html
<video id="video" class="video" src="path/to/your/video.mp4" preload="metadata">
```

### Styling
Modify `style.css` to customize:
- Colors and themes
- Player dimensions
- Control button styles
- Progress bar appearance

### Functionality
Extend `script.js` to add:
- Playback speed control
- Subtitle support
- Picture-in-picture mode
- Additional keyboard shortcuts

## Code Structure

### Main Functions
- `togglePlay()` - Handles play/pause functionality
- `updateProgress()` - Updates progress bar and time display
- `setProgress()` - Seeks video to clicked position
- `toggleMute()` - Mutes/unmutes audio
- `setVolume()` - Adjusts volume level
- `toggleFullscreen()` - Enters/exits fullscreen mode
- `formatTime()` - Formats seconds to MM:SS format

## Notes

- The video file must be in a supported format (MP4 recommended)
- For best performance, use videos with appropriate encoding
- The player uses HTML5 Video API for cross-browser compatibility
- Preload is set to "metadata" for faster initial load

---

**Assignment**: UI Assignment 4  
**Technologies**: HTML5, CSS3, JavaScript (Vanilla)  
**Author**: Python Fullstack 2025

