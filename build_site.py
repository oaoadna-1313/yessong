# -*- coding: utf-8 -*-
import json, os

script_dir = os.path.dirname(os.path.abspath(__file__))
output_dirs = [
    os.path.join(script_dir, "taipei"),
    os.path.join(script_dir, "成品")
]
for d in output_dirs:
    os.makedirs(d, exist_ok=True)

with open(os.path.join(script_dir, "songs_data.json"), "r", encoding="utf-8") as f:
    songs = json.load(f)

# Helper to render JSON into HTML script tag
songs_json_str = json.dumps(songs, ensure_ascii=False)

def generate_html(current_song_id=None, is_index=True):
    # If is_index, it has dynamic song switcher. If single song page, it can default to that song.
    default_id = current_song_id if current_song_id else songs[0]["id"]
    
    html = f"""<!DOCTYPE html>
<html lang="zh-TW" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>【八上閱思龍門】歌SONG臺北・音樂地誌互動教學平台</title>
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <!-- Google Fonts: Noto Serif TC & Noto Sans TC -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;600;700&family=Noto+Serif+TC:wght@400;600;700;900&display=swap" rel="stylesheet">
  
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            serif: ['"Noto Serif TC"', 'serif'],
            sans: ['"Noto Sans TC"', 'sans-serif'],
            kaiti: ['"DFKai-SB"', '"BiauKai"', '"KaiTi"', 'serif']
          }},
          keyframes: {{
            spin_slow: {{
              '0%': {{ transform: 'rotate(0deg)' }},
              '100%': {{ transform: 'rotate(360deg)' }}
            }},
            pulse_soft: {{
              '0%, 100%': {{ opacity: 1, transform: 'scale(1)' }},
              '50%': {{ opacity: 0.85, transform: 'scale(1.03)' }}
            }}
          }},
          animation: {{
            'spin-slow': 'spin_slow 18s linear infinite',
            'pulse-soft': 'pulse_soft 2s ease-in-out infinite'
          }}
        }}
      }}
    }}
  </script>
  <style>
    /* Custom handwriting font style for teacher answers */
    .font-handwriting {{
      font-family: "DFKai-SB", "BiauKai", "KaiTi", "Noto Serif TC", serif;
      letter-spacing: 0.08em;
    }}
    /* Custom scrollbars */
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: #f1f5f9;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #cbd5e1;
      border-radius: 9999px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #94a3b8;
    }}
    
    /* Blank box styles */
    .blank-box {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 4rem;
      min-height: 2.1rem;
      padding: 0.15rem 0.6rem;
      margin: 0.15rem 0.25rem;
      background-color: #ffffff;
      border: 1.5px solid #94a3b8;
      border-radius: 0.375rem;
      vertical-align: middle;
      cursor: pointer;
      user-select: none;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      position: relative;
    }}
    .blank-box:hover {{
      border-color: #8b5cf6;
      background-color: #f5f3ff;
      transform: translateY(-1px);
      box-shadow: 0 4px 6px -1px rgba(139, 92, 246, 0.15);
    }}
    .blank-box.revealed {{
      border-color: #fca5a5;
      background-color: #fff1f2;
      box-shadow: 0 1px 3px 0 rgba(225, 29, 72, 0.1);
    }}
    .blank-box.revealed:hover {{
      border-color: #f87171;
      background-color: #ffe4e6;
    }}
    
    /* Print optimizations */
    @media print {{
      header, footer, .no-print {{
        display: none !important;
      }}
      body {{
        background: #ffffff !important;
        color: #000000 !important;
      }}
      .worksheet-card {{
        border: 2px solid #000000 !important;
        box-shadow: none !important;
        page-break-inside: avoid;
      }}
      .blank-box {{
        border: 1.5px solid #000000 !important;
        background: transparent !important;
      }}
      .blank-box.revealed .revealed-text {{
        color: #dc2626 !important;
      }}
    }}
    
    /* Vinyl arm pivot */
    .vinyl-arm {{
      transform-origin: 85% 15%;
      transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .vinyl-arm.playing {{
      transform: rotate(26deg);
    }}
  </style>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased min-h-screen flex flex-col selection:bg-purple-100 selection:text-purple-900">

  <!-- ==================== STICKY HEADER (yuesilongmen-web-title-spec) ==================== -->
  <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-sm transition-all duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      <!-- Brand & Title (閱思龍門標準品牌標題) -->
      <div class="flex items-center space-x-3">
        <a href="index.html" class="flex items-center space-x-2 group" title="返回歌SONG臺北教學首頁">
          <img src="assets/badge-yuesilongmen.png" alt="閱思龍門" class="w-10 h-10 object-contain rounded-full shadow-sm group-hover:rotate-12 transition-transform duration-300">
          <div>
            <div class="flex items-center space-x-2">
              <span class="font-serif font-bold text-lg sm:text-xl text-slate-900 tracking-wide">歌SONG臺北</span>
              <span class="hidden sm:inline-flex items-center px-2 py-0.5 rounded-full text-xs font-semibold bg-purple-100 text-purple-800 border border-purple-200">八上閱思龍門・音樂地誌</span>
            </div>
            <p class="text-[11px] text-slate-500 font-medium hidden md:block">聆聽城市心跳・穿梭流行金曲與臺北地誌記憶</p>
          </div>
        </a>
      </div>

      <!-- Quick Action Controls -->
      <div class="flex items-center space-x-2 sm:space-x-3">
        <!-- Reveal All Toggle -->
        <button id="toggleAllBtn" onclick="toggleAllBlanks()" class="px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 bg-rose-50 text-rose-700 hover:bg-rose-100 border border-rose-200 shadow-xs cursor-pointer active:scale-95">
          <i class="fa-solid fa-graduation-cap"></i>
          <span id="toggleAllBtnText">一鍵揭曉教師版</span>
        </button>
        <!-- Reset Blanks -->
        <button onclick="resetAllBlanks()" class="px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 bg-slate-100 text-slate-700 hover:bg-slate-200 border border-slate-200 shadow-xs cursor-pointer active:scale-95">
          <i class="fa-solid fa-rotate-left"></i>
          <span class="hidden sm:inline">重置空白</span>
        </button>
      </div>
    </div>
  </header>

  <!-- ==================== MAIN CONTENT ==================== -->
  <main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 w-full space-y-6">

    <!-- Top Banner & Song Carousel Selector -->
    <div class="bg-gradient-to-r from-purple-900 via-indigo-900 to-slate-900 rounded-2xl p-5 sm:p-6 text-white shadow-xl relative overflow-hidden">
      <!-- Background Decorative Lights -->
      <div class="absolute -right-10 -bottom-10 w-64 h-64 bg-purple-500/20 rounded-full blur-3xl pointer-events-none"></div>
      <div class="absolute right-1/3 -top-10 w-48 h-48 bg-pink-500/20 rounded-full blur-2xl pointer-events-none"></div>

      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5 relative z-10">
        <!-- Left: Logo Banner -->
        <div class="flex items-center gap-4">
          <img src="assets/logo-gesong-taipei.png" alt="歌SONG臺北" class="h-12 sm:h-16 w-auto object-contain filter drop-shadow-md">
          <div class="hidden sm:block border-l border-white/20 pl-4">
            <h1 class="text-sm sm:text-base font-serif font-bold text-purple-200 tracking-wide">臺北城市聲響與地誌文學</h1>
            <p class="text-xs text-slate-300 mt-0.5">點選下方歌曲卡片，邊聽音樂邊完成歌詞填空與深度鑑賞</p>
          </div>
        </div>

        <!-- Right: Status / Teacher Mode Badge -->
        <div class="flex items-center gap-3">
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-white/15 text-xs text-purple-200">
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
            <span id="currentModeLabel">學生自修填空模式</span>
          </div>
          <a href="#reflectionSec" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-purple-600/80 hover:bg-purple-600 text-xs font-semibold text-white transition-all">
            <i class="fa-solid fa-pen-to-square"></i>
            <span>心得探究區</span>
          </a>
        </div>
      </div>

      <!-- Song Navigation Pills / Tabs -->
      <div class="mt-5 pt-4 border-t border-white/15 flex items-center gap-2 overflow-x-auto pb-1 scrollbar-none" id="songTabsContainer">
        <!-- Rendered via JS -->
      </div>
    </div>

    <!-- Active Song Hero & Core Teaching Board (Grid Layout) -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">

      <!-- Left Column: Audio Player & Song Info Card (Sticky on desktop, 4 cols) -->
      <div class="lg:col-span-5 space-y-5 lg:sticky lg:top-24">

        <!-- ==================== PLAYER CARD ==================== -->
        <div class="bg-white rounded-2xl border border-slate-200 shadow-md overflow-hidden transition-all duration-300 hover:shadow-lg">
          <!-- Card Header & Mood Badge -->
          <div class="px-5 py-4 border-b border-slate-100 flex items-center justify-between bg-slate-50/60">
            <div class="flex items-center space-x-2">
              <span id="playerOrderBadge" class="px-2 py-0.5 text-xs font-bold rounded-md bg-purple-100 text-purple-800 border border-purple-200">第一曲</span>
            </div>
            <div class="flex items-center gap-2">
              <span id="playerTagBadge" class="px-2.5 py-0.5 text-xs font-medium rounded-full bg-amber-100 text-amber-800">治癒系</span>
              <!-- MV Switch Button if video available -->
              <button id="videoToggleBtn" onclick="toggleVideoMode()" class="hidden px-2 py-0.5 text-xs font-bold rounded-md bg-rose-600 hover:bg-rose-700 text-white transition-colors cursor-pointer flex items-center gap-1 shadow-xs" title="切換MV視頻播放">
                <i class="fa-solid fa-video"></i>
                <span id="videoToggleText">MV</span>
              </button>
            </div>
          </div>

          <!-- Player Body: Visualizer / Vinyl Record -->
          <div class="p-6 flex flex-col items-center justify-center bg-gradient-to-b from-slate-900 to-slate-950 text-white relative overflow-hidden">
            <!-- Background Glow -->
            <div id="playerGlow" class="absolute w-44 h-44 bg-purple-500/25 rounded-full blur-3xl transition-all duration-500 pointer-events-none"></div>

            <!-- Video Player Container (Hidden by default) -->
            <div id="videoContainer" class="hidden w-full aspect-video rounded-xl overflow-hidden bg-black shadow-inner mb-4 relative z-10">
              <video id="videoPlayer" class="w-full h-full object-contain" controls>
                您的瀏覽器不支援影片播放。
              </video>
            </div>

            <!-- Vinyl Record Turntable Animation (Shown in audio mode) -->
            <div id="vinylContainer" class="relative w-48 h-48 sm:w-56 sm:h-56 flex items-center justify-center my-2 select-none z-10">
              <!-- Vinyl Disc -->
              <div id="vinylDisc" class="w-full h-full rounded-full bg-slate-950 border-4 border-slate-800 shadow-2xl flex items-center justify-center relative overflow-hidden transition-transform duration-500">
                <!-- Concentric Grooves -->
                <div class="absolute inset-2 rounded-full border border-slate-800/80"></div>
                <div class="absolute inset-5 rounded-full border border-slate-800/60"></div>
                <div class="absolute inset-8 rounded-full border border-slate-800/40"></div>
                <div class="absolute inset-12 rounded-full border border-slate-800/30"></div>
                <!-- Vinyl Label (Center) -->
                <div id="vinylLabel" class="w-20 h-20 sm:w-24 sm:h-24 rounded-full bg-gradient-to-tr from-amber-500 to-rose-500 flex flex-col items-center justify-center text-center p-2 shadow-inner border-2 border-white/20">
                  <i class="fa-solid fa-music text-white text-base drop-shadow"></i>
                  <span id="vinylSongTitle" class="text-[10px] font-bold text-white tracking-tight line-clamp-1 mt-0.5">台北天晴</span>
                </div>
                <!-- Center Hole -->
                <div class="absolute w-3.5 h-3.5 rounded-full bg-slate-950 border border-slate-700 shadow-inner"></div>
              </div>

              <!-- Turntable Needle Arm -->
              <div id="vinylArm" class="vinyl-arm absolute -top-4 right-2 w-14 h-32 pointer-events-none z-20">
                <div class="w-4 h-4 rounded-full bg-slate-400 border border-slate-300 shadow absolute top-0 right-0"></div>
                <div class="w-1.5 h-24 bg-gradient-to-b from-slate-300 to-slate-400 shadow rounded-full absolute top-2 right-1.5 transform rotate-6"></div>
                <div class="w-3 h-5 bg-rose-500 rounded-sm shadow absolute bottom-4 right-3.5 border border-white/20"></div>
              </div>
            </div>

            <!-- Song Title & Artist -->
            <div class="text-center mt-3 z-10">
              <h2 id="playerSongTitle" class="text-xl sm:text-2xl font-serif font-black text-white tracking-wide">台北天晴</h2>
              <p id="playerArtist" class="text-xs sm:text-sm text-purple-200 mt-1 font-medium">演唱：嚴正嵐・2014</p>
            </div>

            <!-- Progress Bar & Scrubber -->
            <div class="w-full mt-5 space-y-1.5 z-10">
              <div class="relative w-full h-2 bg-slate-800 rounded-full cursor-pointer group" id="progressBarContainer" onclick="seekAudio(event)">
                <div id="progressBar" class="h-full bg-gradient-to-r from-purple-500 to-pink-500 rounded-full w-0 transition-all duration-100 group-hover:brightness-110"></div>
                <!-- Scrubber Handle -->
                <div id="progressHandle" class="absolute top-1/2 -translate-y-1/2 -ml-1.5 w-3.5 h-3.5 bg-white rounded-full shadow-md border border-purple-300 opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none"></div>
              </div>
              <!-- Time Readout -->
              <div class="flex justify-between items-center text-[11px] font-mono text-slate-400">
                <span id="currentTime">00:00</span>
                <span id="totalDuration">--:--</span>
              </div>
            </div>

            <!-- Playback Control Buttons -->
            <div class="flex items-center justify-center gap-4 mt-4 z-10">
              <!-- Rewind 5s -->
              <button onclick="skipTime(-5)" class="w-9 h-9 rounded-full bg-white/10 hover:bg-white/20 text-slate-300 hover:text-white transition-all flex items-center justify-center text-xs cursor-pointer active:scale-90" title="倒退 5 秒">
                <i class="fa-solid fa-rotate-left"></i>
              </button>
              <!-- Prev Song -->
              <button onclick="prevSong()" class="w-9 h-9 rounded-full bg-white/10 hover:bg-white/20 text-slate-300 hover:text-white transition-all flex items-center justify-center text-xs cursor-pointer active:scale-90" title="上一首">
                <i class="fa-solid fa-backward-step"></i>
              </button>
              <!-- Play / Pause Main Button -->
              <button id="playPauseBtn" onclick="togglePlayPause()" class="w-14 h-14 rounded-full bg-gradient-to-tr from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600 text-white shadow-lg shadow-purple-500/30 transition-all transform hover:scale-105 active:scale-95 flex items-center justify-center text-xl cursor-pointer" title="播放 / 暫停">
                <i id="playIcon" class="fa-solid fa-play ml-1"></i>
              </button>
              <!-- Next Song -->
              <button onclick="nextSong()" class="w-9 h-9 rounded-full bg-white/10 hover:bg-white/20 text-slate-300 hover:text-white transition-all flex items-center justify-center text-xs cursor-pointer active:scale-90" title="下一首">
                <i class="fa-solid fa-forward-step"></i>
              </button>
              <!-- Forward 5s -->
              <button onclick="skipTime(5)" class="w-9 h-9 rounded-full bg-white/10 hover:bg-white/20 text-slate-300 hover:text-white transition-all flex items-center justify-center text-xs cursor-pointer active:scale-90" title="快進 5 秒">
                <i class="fa-solid fa-rotate-right"></i>
              </button>
            </div>

            <!-- Bottom Secondary Bar: Volume & Speed -->
            <div class="flex items-center justify-between w-full mt-4 pt-3 border-t border-white/10 text-xs text-slate-300 z-10">
              <!-- Volume Control -->
              <div class="flex items-center space-x-2">
                <button onclick="toggleMute()" class="text-slate-300 hover:text-white text-xs cursor-pointer" id="muteBtn" title="靜音切換">
                  <i id="volumeIcon" class="fa-solid fa-volume-high"></i>
                </button>
                <input id="volumeSlider" type="range" min="0" max="1" step="0.05" value="0.9" oninput="changeVolume(this.value)" class="w-16 sm:w-20 h-1.5 bg-slate-700 rounded-lg appearance-none cursor-pointer accent-purple-400">
              </div>

              <!-- Speed Selector -->
              <div class="flex items-center space-x-1">
                <span class="text-[11px] text-slate-400 mr-1">倍速:</span>
                <button onclick="setSpeed(0.8, this)" class="speed-btn px-1.5 py-0.5 rounded text-[10px] font-mono bg-white/10 hover:bg-white/20 text-slate-300">0.8x</button>
                <button onclick="setSpeed(1.0, this)" class="speed-btn px-1.5 py-0.5 rounded text-[10px] font-mono bg-purple-600 text-white font-bold">1.0x</button>
                <button onclick="setSpeed(1.2, this)" class="speed-btn px-1.5 py-0.5 rounded text-[10px] font-mono bg-white/10 hover:bg-white/20 text-slate-300">1.2x</button>
              </div>
            </div>

          </div>

          <!-- Song Meta & Geopoetic Background Description -->
          <div class="p-5 space-y-3 bg-white">
            <h3 class="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center gap-1.5">
              <i class="fa-solid fa-circle-info text-purple-600"></i>
              <span>歌曲背景與地誌導讀</span>
            </h3>
            <p id="playerSongIntro" class="text-xs sm:text-sm text-slate-600 leading-relaxed font-sans">
              這座城市有著吐不完的苦水，但也有著大好天空值得我們去積累。下過雨後的臺北，空氣洗去塵埃，張開雙臂迎向天晴，體現青春在挫折中尋覓希望的堅韌。
            </p>
            <div class="pt-2 border-t border-slate-100 flex flex-wrap gap-y-1 text-[11px] text-slate-500">
              <span class="w-1/2" id="metaLyricist">作詞：嚴正嵐</span>
              <span class="w-1/2" id="metaComposer">作曲：嚴正嵐</span>
              <span class="w-1/2" id="metaArtist">演唱：嚴正嵐</span>
              <span class="w-1/2" id="metaYear">發行：2014-11</span>
            </div>
          </div>
        </div>

        <!-- Quick Switch Checklist (7 Songs Grid) -->
        <div class="bg-white rounded-2xl border border-slate-200 p-4 shadow-xs">
          <h4 class="text-xs font-bold text-slate-600 mb-2.5 flex items-center justify-between">
            <span class="flex items-center gap-1.5">
              <i class="fa-solid fa-list-check text-indigo-600"></i>
              <span>全系列歌曲學習地圖 (7首)</span>
            </span>
            <span class="text-[11px] text-purple-600 font-semibold" id="overallCompletion">進度 0/7</span>
          </h4>
          <div class="space-y-1.5" id="songListMenu">
            <!-- Rendered by JS -->
          </div>
        </div>

      </div>

      <!-- Right Column: Interactive Worksheet (7 cols) -->
      <div class="lg:col-span-7 space-y-6">

        <!-- ==================== WORKSHEET CARD ==================== -->
        <div class="worksheet-card bg-white rounded-2xl border-2 border-slate-800 shadow-lg p-5 sm:p-8 relative transition-all duration-300">

          <!-- Worksheet Top Header -->
          <div class="flex items-center justify-between border-b-2 border-slate-800 pb-4 mb-6">
            <div class="flex items-center space-x-3">
              <div class="w-10 h-10 rounded-full bg-purple-600 text-white flex items-center justify-center font-serif font-black text-xl shadow-xs">
                <i class="fa-solid fa-folder-open text-base"></i>
              </div>
              <div>
                <h2 id="sheetTitle" class="text-xl sm:text-2xl font-serif font-black text-slate-900 tracking-wide">【台北天晴】</h2>
                <p id="sheetCredits" class="text-xs text-slate-600 mt-1">作詞：嚴正嵐  作曲：嚴正嵐  演唱：嚴正嵐  2014-11</p>
              </div>
            </div>
          </div>

          <!-- Lyrics Display Area -->
          <div class="space-y-4 text-base sm:text-lg leading-loose font-serif text-slate-800 tracking-wide" id="lyricsContainer">
            <!-- Rendered by JS -->
          </div>

          <!-- Vocabulary Section (查一查，下面的詞語是什麼意思？) -->
          <div id="vocabSection" class="mt-8 pt-6 border-t-2 border-dashed border-slate-300">
            <div class="flex items-center gap-2 mb-4">
              <span class="text-lg text-purple-700"><i class="fa-solid fa-book-open"></i></span>
              <h3 class="font-serif font-bold text-base sm:text-lg text-slate-900">查一查，下面的詞語是什麼意思？</h3>
            </div>
            <div class="space-y-4" id="vocabContainer">
              <!-- Rendered by JS -->
            </div>
          </div>

          <!-- Worksheet Thinking Questions Section (找一找、想一想、說一說) -->
          <div id="reflectionSec" class="mt-8 pt-6 border-t-2 border-slate-800 space-y-5">
            <!-- Header Row: Title on Left, Student Info on Right -->
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <h3 class="font-serif font-bold text-base sm:text-lg text-slate-900 flex items-center gap-2">
                <i class="fa-solid fa-comments text-indigo-600"></i>
                <span>課堂深層探究與回饋分享</span>
              </h3>

              <!-- Student Info Fields (班級、座號、姓名) -->
              <div class="flex items-center gap-2 sm:gap-3 text-xs font-medium text-slate-700 bg-slate-50 border border-slate-300 px-3 py-1.5 rounded-lg shadow-2xs self-start sm:self-auto">
                <div class="flex items-center">
                  <span>班級：</span>
                  <input type="text" id="stuClass" placeholder="如 801" oninput="saveStudentInfo('class', this.value)" class="w-14 px-1.5 py-0.5 text-xs bg-white border-b-2 border-slate-400 focus:border-purple-600 focus:outline-none text-center font-bold font-sans">
                </div>
                <div class="flex items-center">
                  <span>座號：</span>
                  <input type="text" id="stuSeat" placeholder="如 08" oninput="saveStudentInfo('seat', this.value)" class="w-12 px-1.5 py-0.5 text-xs bg-white border-b-2 border-slate-400 focus:border-purple-600 focus:outline-none text-center font-bold font-sans">
                </div>
                <div class="flex items-center">
                  <span>姓名：</span>
                  <input type="text" id="stuName" placeholder="如 王小明" oninput="saveStudentInfo('name', this.value)" class="w-20 px-1.5 py-0.5 text-xs bg-white border-b-2 border-slate-400 focus:border-purple-600 focus:outline-none text-center font-bold font-sans">
                </div>
              </div>
            </div>

            <!-- Question 1 & 2 Dual Columns -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- Q1 -->
              <div class="bg-slate-50 border border-slate-200 rounded-xl p-4 space-y-2">
                <label class="font-serif font-bold text-sm text-slate-800 flex items-center gap-1.5">
                  <i class="fa-regular fa-folder text-purple-600"></i>
                  <span>找一找，這首歌不錯的句子有哪些？</span>
                </label>
                <textarea id="q1Input" rows="3" placeholder="請在此記錄令你感動或寫作精妙的歌詞金句..." oninput="saveNote('q1', this.value)" class="w-full text-xs sm:text-sm bg-white border border-slate-300 rounded-lg p-2.5 focus:outline-none focus:ring-2 focus:ring-purple-400 resize-none font-sans"></textarea>
              </div>

              <!-- Q2 -->
              <div class="bg-slate-50 border border-slate-200 rounded-xl p-4 space-y-2">
                <label class="font-serif font-bold text-sm text-slate-800 flex items-center gap-1.5">
                  <i class="fa-regular fa-folder text-purple-600"></i>
                  <span>想一想，這首歌想表達什麼？</span>
                </label>
                <textarea id="q2Input" rows="3" placeholder="請寫下創作者透過旋律與歌詞傳遞的情感核心..." oninput="saveNote('q2', this.value)" class="w-full text-xs sm:text-sm bg-white border border-slate-300 rounded-lg p-2.5 focus:outline-none focus:ring-2 focus:ring-purple-400 resize-none font-sans"></textarea>
              </div>
            </div>

            <!-- Q3 -->
            <div class="bg-slate-50 border border-slate-200 rounded-xl p-4 space-y-2">
              <label class="font-serif font-bold text-sm text-slate-800 flex items-center gap-1.5">
                <i class="fa-regular fa-folder text-purple-600"></i>
                <span>說一說，聽完這首歌你有什麼感想？</span>
              </label>
              <textarea id="q3Input" rows="2" placeholder="談談你在旋律或歌詞裡看見了什麼樣的臺北？或是引發了你的何種生活共鳴？" oninput="saveNote('q3', this.value)" class="w-full text-xs sm:text-sm bg-white border border-slate-300 rounded-lg p-2.5 focus:outline-none focus:ring-2 focus:ring-purple-400 resize-none font-sans"></textarea>
            </div>

            <!-- Emotion Chips -->
            <div class="bg-slate-50 border border-slate-200 rounded-xl p-4 space-y-2.5">
              <label class="font-serif font-bold text-xs sm:text-sm text-slate-800 flex items-center gap-1.5">
                <i class="fa-regular fa-folder text-purple-600"></i>
                <span>這首歌讓我覺得：</span>
              </label>
              <div class="flex flex-wrap gap-2 text-xs" id="emotionContainer">
                <button onclick="toggleEmotion(this, '很開心')" class="emotion-chip px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-amber-50 text-slate-700 transition-all flex items-center gap-1.5 cursor-pointer">
                  <span>😊</span>
                  <span>很開心</span>
                </button>
                <button onclick="toggleEmotion(this, '溫馨感動')" class="emotion-chip px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-rose-50 text-slate-700 transition-all flex items-center gap-1.5 cursor-pointer">
                  <span>💖</span>
                  <span>溫馨感動</span>
                </button>
                <button onclick="toggleEmotion(this, '有啟發')" class="emotion-chip px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-emerald-50 text-slate-700 transition-all flex items-center gap-1.5 cursor-pointer">
                  <span>💡</span>
                  <span>有啟發</span>
                </button>
                <button onclick="toggleEmotion(this, '拍案叫絕')" class="emotion-chip px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-indigo-50 text-slate-700 transition-all flex items-center gap-1.5 cursor-pointer">
                  <span>👏</span>
                  <span>拍案叫絕</span>
                </button>
                <button onclick="toggleEmotion(this, '很感傷')" class="emotion-chip px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-blue-50 text-slate-700 transition-all flex items-center gap-1.5 cursor-pointer">
                  <span>😢</span>
                  <span>很感傷</span>
                </button>
              </div>
            </div>

            <!-- Action footer for worksheet -->
            <div class="flex items-center justify-between pt-3 text-xs text-slate-500 no-print">
              <span id="savedIndicator" class="text-emerald-600 font-medium opacity-0 transition-opacity">
                <i class="fa-solid fa-check mr-1"></i>筆記已自動儲存至本機
              </span>
              <div class="flex items-center gap-2 sm:gap-3">
                <button onclick="clearCurrentNotes()" class="text-slate-400 hover:text-slate-600 underline cursor-pointer">清空本曲筆記</button>
                <button id="copyAnswersBtn" onclick="copyCurrentAnswers()" class="px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 bg-purple-50 text-purple-700 hover:bg-purple-100 border border-purple-200 shadow-xs cursor-pointer active:scale-95" title="一鍵複製題目與回答內容">
                  <i id="copyBtnIcon" class="fa-solid fa-copy"></i>
                  <span id="copyBtnText">一鍵複製回答</span>
                </button>
              </div>
            </div>

          </div>

        </div>

      </div>

    </div>

  </main>

  <!-- ==================== FOOTER (yuesilongmen-web-title-spec) ==================== -->
  <footer class="bg-slate-100 text-slate-600 py-6 border-t border-slate-200 mt-16 print:hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4">
        <!-- Left: Logo, Title & Tagline -->
        <div class="flex flex-wrap items-center justify-center sm:justify-start gap-2 sm:gap-3 text-center sm:text-left">
          <div class="flex items-center space-x-2">
            <img src="assets/badge-yuesilongmen.png" alt="閱思龍門" class="w-8 h-8 rounded-full shadow-sm">
            <span class="font-serif font-bold text-slate-800 text-base">八上閱思龍門・歌SONG臺北</span>
          </div>
          <span class="hidden sm:inline text-slate-300">|</span>
          <span class="text-xs text-slate-500 font-medium">聆聽城市心跳・穿梭流行金曲與臺北地誌記憶</span>
        </div>

        <!-- Right: Copyright -->
        <div class="text-xs text-slate-500 font-medium">
          © 2026 學思軒
        </div>
      </div>
    </div>
  </footer>

  <!-- Invisible Audio Element -->
  <audio id="audioPlayer" preload="auto"></audio>

  <!-- ==================== CLIENT LOGIC SCRIPT ==================== -->
  <script>
    // All Songs Data
    const songsData = {songs_json_str};
    let currentSongIndex = 0;
    let isPlaying = false;
    let isTeacherMode = false;
    let isVideoMode = false;
    let revealedBlanks = new Set(); // Track revealed blank IDs
    let revealedVocab = new Set();  // Track revealed vocab indices

    // Find initial song index
    const initialSongId = "{default_id}";
    const foundIdx = songsData.findIndex(s => s.id === initialSongId);
    if (foundIdx !== -1) currentSongIndex = foundIdx;

    // DOM Elements
    const audio = document.getElementById('audioPlayer');
    const video = document.getElementById('videoPlayer');
    const videoContainer = document.getElementById('videoContainer');
    const vinylContainer = document.getElementById('vinylContainer');
    const videoToggleBtn = document.getElementById('videoToggleBtn');
    const videoToggleText = document.getElementById('videoToggleText');
    const playPauseBtn = document.getElementById('playPauseBtn');
    const playIcon = document.getElementById('playIcon');
    const vinylDisc = document.getElementById('vinylDisc');
    const vinylArm = document.getElementById('vinylArm');
    const progressBar = document.getElementById('progressBar');
    const progressHandle = document.getElementById('progressHandle');
    const currentTimeEl = document.getElementById('currentTime');
    const totalDurationEl = document.getElementById('totalDuration');
    const volumeSlider = document.getElementById('volumeSlider');
    const volumeIcon = document.getElementById('volumeIcon');

    // Initialize App
    window.addEventListener('DOMContentLoaded', () => {{
      renderTabs();
      renderSongListMenu();
      loadSong(currentSongIndex, false);
      setupAudioEvents();
      setupVideoEvents();
      loadSavedNotes();
    }});

    // Render Song Navigation Tabs
    function renderTabs() {{
      const container = document.getElementById('songTabsContainer');
      container.innerHTML = songsData.map((song, idx) => {{
        const isActive = idx === currentSongIndex;
        return `
          <button onclick="switchSong(${{idx}}, false)" class="song-tab px-3.5 py-1.5 rounded-lg text-xs font-semibold whitespace-nowrap transition-all flex items-center gap-1.5 cursor-pointer ${{isActive ? 'bg-white text-purple-950 shadow-md font-bold ring-2 ring-purple-300' : 'bg-white/10 text-slate-200 hover:bg-white/20 hover:text-white'}}">
            <span class="w-1.5 h-1.5 rounded-full ${{isActive ? 'bg-purple-600' : 'bg-slate-300'}}"></span>
            <span>${{song.title}}</span>
          </button>
        `;
      }}).join('');
    }}

    // Render Quick Switch Menu
    function renderSongListMenu() {{
      const container = document.getElementById('songListMenu');
      container.innerHTML = songsData.map((song, idx) => {{
        const isActive = idx === currentSongIndex;
        const isThisPlaying = isActive && isPlaying;
        return `
          <div onclick="switchSong(${{idx}}, false)" class="group p-2 rounded-lg text-xs flex items-center justify-between cursor-pointer transition-all ${{isActive ? 'bg-purple-50 text-purple-900 font-bold border border-purple-200 shadow-2xs' : 'hover:bg-slate-50 text-slate-700'}}">
            <div class="flex items-center gap-2 min-w-0">
              <!-- Dedicated Play / Pause Button in List -->
              <button onclick="event.stopPropagation(); toggleListPlay(${{idx}})" 
                      class="w-6 h-6 rounded-full flex items-center justify-center transition-all shrink-0 cursor-pointer ${{isThisPlaying ? 'bg-purple-600 text-white shadow-xs' : isActive ? 'bg-purple-200 text-purple-700 hover:bg-purple-600 hover:text-white' : 'bg-slate-100 text-slate-500 hover:bg-purple-600 hover:text-white group-hover:bg-purple-100 group-hover:text-purple-700'}}" 
                      title="${{isThisPlaying ? '暫停播放' : '立即播放《' + song.title + '》'}}">
                <i class="fa-solid ${{isThisPlaying ? 'fa-pause text-[10px]' : 'fa-play text-[9px] ml-0.5'}}"></i>
              </button>
              <span class="w-4 text-center font-mono text-[11px] ${{isActive ? 'text-purple-600 font-bold' : 'text-slate-400'}}">${{idx + 1}}</span>
              <span class="truncate">${{song.title}}</span>
            </div>
            <div class="flex items-center gap-2 text-[10px] shrink-0">
              <span class="text-slate-400">${{song.artist}}</span>
              ${{song.video ? '<i class="fa-solid fa-video text-rose-500" title="具備MV"></i>' : ''}}
            </div>
          </div>
        `;
      }}).join('');
    }}

    // Switch Song (defaults to autoPlay = false)
    function switchSong(index, autoPlay = false) {{
      if (index < 0 || index >= songsData.length) return;
      currentSongIndex = index;
      renderTabs();
      renderSongListMenu();
      loadSong(currentSongIndex, autoPlay);
    }}

    // Toggle Play from List Button
    function toggleListPlay(index) {{
      if (index === currentSongIndex) {{
        togglePlayPause();
      }} else {{
        switchSong(index, true);
      }}
    }}

    function prevSong() {{
      const newIdx = (currentSongIndex - 1 + songsData.length) % songsData.length;
      switchSong(newIdx, isPlaying);
    }}

    function nextSong() {{
      const newIdx = (currentSongIndex + 1) % songsData.length;
      switchSong(newIdx, isPlaying);
    }}

    // Load Song Data into View
    function loadSong(index, autoPlay = false) {{
      const song = songsData[index];
      
      // Reset blank trackers for this song unless in teacher mode
      if (!isTeacherMode) {{
        revealedBlanks.clear();
        revealedVocab.clear();
      }}

      // Stop any current playing media
      audio.pause();
      audio.currentTime = 0;
      video.pause();
      video.currentTime = 0;

      // Always reset back to Vinyl Audio Mode when loading a new song
      isVideoMode = false;
      videoContainer.classList.add('hidden');
      vinylContainer.classList.remove('hidden');
      videoToggleText.textContent = "MV";

      // Reset progress bar display
      progressBar.style.width = '0%';
      progressHandle.style.left = '0%';
      currentTimeEl.textContent = '00:00';
      totalDurationEl.textContent = '--:--';

      // Player Info
      document.getElementById('playerOrderBadge').textContent = song.order;
      document.getElementById('playerTagBadge').textContent = song.tag;
      document.getElementById('playerSongTitle').textContent = song.title;
      document.getElementById('vinylSongTitle').textContent = song.title;
      document.getElementById('playerArtist').textContent = `演唱：${{song.artist}}・${{song.year.split('-')[0]}}`;
      document.getElementById('playerSongIntro').textContent = song.intro;
      document.getElementById('metaLyricist').textContent = `作詞：${{song.lyricist}}`;
      document.getElementById('metaComposer').textContent = `作曲：${{song.composer}}`;
      document.getElementById('metaArtist').textContent = `演唱：${{song.artist}}`;
      document.getElementById('metaYear').textContent = `發行：${{song.year}}`;

      // Worksheet Info
      document.getElementById('sheetTitle').textContent = `【${{song.title}}】`;
      document.getElementById('sheetCredits').textContent = `作詞：${{song.lyricist}}  作曲：${{song.composer}}  演唱：${{song.artist}}  ${{song.year}}`;

      // Video Source & Toggle Button Visibility
      if (song.video) {{
        videoToggleBtn.classList.remove('hidden');
        video.src = song.video;
        video.load();
      }} else {{
        videoToggleBtn.classList.add('hidden');
        video.removeAttribute('src');
        video.load();
      }}

      // Update Audio Source
      audio.src = song.audio;
      audio.load();

      // Render Lyrics
      renderLyrics(song);

      // Render Vocabulary
      renderVocabulary(song);

      // Load Note Fields
      loadSavedNotes();

      // Update completion label
      document.getElementById('overallCompletion').textContent = `進行中 (${{index + 1}}/${{songsData.length}})`;

      if (autoPlay) {{
        playMedia();
      }} else {{
        pauseMedia();
      }}
    }}

    // Toggle Video vs Audio Mode
    function toggleVideoMode() {{
      const song = songsData[currentSongIndex];
      if (!song.video) return;

      isVideoMode = !isVideoMode;
      if (isVideoMode) {{
        // Switch to Video
        audio.pause();
        videoContainer.classList.remove('hidden');
        vinylContainer.classList.add('hidden');
        videoToggleText.textContent = "黑膠";
        video.currentTime = audio.currentTime;
        if (isPlaying) video.play();
      }} else {{
        // Switch to Vinyl Audio
        video.pause();
        videoContainer.classList.add('hidden');
        vinylContainer.classList.remove('hidden');
        videoToggleText.textContent = "MV";
        audio.currentTime = video.currentTime;
        if (isPlaying) audio.play();
      }}
    }}

    // Render Lyrics with Blank Boxes
    function renderLyrics(song) {{
      const container = document.getElementById('lyricsContainer');
      let html = '';
      let blankCounter = 0;

      // Special Legend Guide for dialect songs with Tai-lo (like 向前走)
      if (song.id === 'moving-forward') {{
        html += `
          <div class="mb-5 p-3.5 bg-gradient-to-r from-rose-50/90 via-sky-50/90 to-slate-50 border border-slate-300 rounded-xl flex flex-wrap items-center justify-between gap-3 text-xs shadow-2xs">
            <div class="flex items-center gap-2">
              <span class="w-6 h-6 rounded-full bg-purple-600 text-white flex items-center justify-center font-bold shadow-2xs">
                <i class="fa-solid fa-language text-xs"></i>
              </span>
              <span class="font-bold text-slate-900 text-sm font-serif">雙軌語文對照指南：</span>
            </div>
            <div class="flex flex-wrap items-center gap-2 sm:gap-3">
              <span class="inline-flex items-center gap-1.5 text-slate-700 font-serif font-medium">
                <span class="w-2.5 h-2.5 rounded-full bg-slate-700"></span>
                <span>華語意譯原意</span>
              </span>
              <span class="inline-flex items-center gap-1.5 text-rose-700 font-bold font-serif bg-white border border-rose-300 px-2 py-0.5 rounded shadow-2xs">
                <span class="w-2.5 h-2.5 rounded-full bg-rose-600"></span>
                <span>[ 台語正字 (紅框) ]</span>
              </span>
              <span class="inline-flex items-center gap-1.5 text-blue-700 font-medium font-sans bg-white border border-blue-300 px-2 py-0.5 rounded shadow-2xs">
                <span class="w-2.5 h-2.5 rounded-full bg-blue-600"></span>
                <span>台羅拼音 (藍框)</span>
              </span>
            </div>
          </div>
        `;
      }}

      song.lyrics.forEach((line) => {{
        if (line.type === 'space' || (Array.isArray(line) && line[0] && line[0].type === 'space')) {{
          html += '<div class="h-3.5 sm:h-4"></div>';
          return;
        }}

        const lineClass = (Array.isArray(line) && line[0] && line[0].lineCls)
          ? line[0].lineCls
          : 'lyric-line py-1 flex flex-wrap items-center leading-relaxed';

        html += `<div class="${{lineClass}}">`;
        line.forEach((chunk) => {{
          if (chunk.t) {{
            const cls = chunk.cls ? chunk.cls : 'inline-block';
            html += `<span class="${{cls}}">${{chunk.t}}</span>`;
          }} else if (chunk.b) {{
            blankCounter++;
            const blankId = `${{song.id}}-b-${{blankCounter}}`;
            const isRevealed = isTeacherMode || revealedBlanks.has(blankId);
            html += `
              <span id="${{blankId}}" onclick="toggleBlank('${{blankId}}', '${{chunk.b}}')" class="blank-box ${{isRevealed ? 'revealed' : ''}}" title="點擊翻開/隱藏答案">
                ${{isRevealed 
                  ? `<span class="revealed-text font-handwriting text-rose-600 font-bold text-lg sm:text-xl animate-in">${{chunk.b}}</span>` 
                  : `<span class="placeholder text-xs text-slate-400 font-sans tracking-normal">[ ${{chunk.h}} ]</span>`
                }}
              </span>
            `;
          }}
        }});
        html += '</div>';
      }});

      container.innerHTML = html;
    }}

    // Toggle Single Blank Box
    function toggleBlank(blankId, word) {{
      const el = document.getElementById(blankId);
      if (!el) return;

      if (revealedBlanks.has(blankId)) {{
        revealedBlanks.delete(blankId);
        el.classList.remove('revealed');
        // Find hint by searching the span
        el.innerHTML = `<span class="placeholder text-xs text-slate-400 font-sans tracking-normal">[ ${{word.length}}字 ]</span>`;
      }} else {{
        revealedBlanks.add(blankId);
        el.classList.add('revealed');
        el.innerHTML = `<span class="revealed-text font-handwriting text-rose-600 font-bold text-lg sm:text-xl animate-in">${{word}}</span>`;
      }}
    }}

    // Render Vocabulary (查一查)
    function renderVocabulary(song) {{
      const sec = document.getElementById('vocabSection');
      const container = document.getElementById('vocabContainer');

      if (!song.vocab || song.vocab.length === 0) {{
        sec.classList.add('hidden');
        return;
      }}
      sec.classList.remove('hidden');

      container.innerHTML = song.vocab.map((item, idx) => {{
        const vocabId = `${{song.id}}-v-${{idx}}`;
        const isRevealed = isTeacherMode || revealedVocab.has(vocabId);
        
        // Zhuyin character boxes
        const charBoxes = item.chars.map(c => `
          <div class="inline-flex flex-col items-center justify-center w-8 h-10 border border-slate-700 bg-white text-center rounded-xs shadow-2xs">
            <span class="text-sm font-serif font-black text-slate-900 leading-tight">${{c.c}}</span>
            <span class="text-[9px] text-slate-500 font-sans leading-none -mt-0.5">${{c.z}}</span>
          </div>
        `).join('');

        return `
          <div class="p-3.5 rounded-xl border border-slate-200 bg-slate-50/70 hover:bg-slate-50 transition-all">
            <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3">
              <!-- Characters with Phonetics -->
              <div class="flex items-center gap-1 shrink-0">
                ${{charBoxes}}
                <span class="font-serif font-bold text-slate-800 ml-1">：</span>
              </div>
              <!-- Meaning Definition Box -->
              <div id="${{vocabId}}" onclick="toggleVocab('${{vocabId}}')" class="flex-grow p-2.5 rounded-lg border-1.5 border-dashed ${{isRevealed ? 'border-rose-300 bg-rose-50/50' : 'border-slate-300 bg-white hover:border-purple-300'}} cursor-pointer transition-all">
                ${{isRevealed 
                  ? `<span class="font-handwriting text-rose-600 font-bold text-sm sm:text-base leading-relaxed">${{item.meaning}}</span>` 
                  : `<span class="text-xs text-slate-400 flex items-center gap-1.5"><i class="fa-solid fa-hand-pointer text-purple-400"></i>點擊查閱詞義注釋 (學生作答區)</span>`
                }}
              </div>
            </div>
          </div>
        `;
      }}).join('');
    }}

    // Toggle Single Vocabulary Meaning
    function toggleVocab(vocabId) {{
      const song = songsData[currentSongIndex];
      const idx = parseInt(vocabId.split('-v-')[1]);
      const item = song.vocab[idx];
      const el = document.getElementById(vocabId);
      if (!el || !item) return;

      if (revealedVocab.has(vocabId)) {{
        revealedVocab.delete(vocabId);
        el.className = "flex-grow p-2.5 rounded-lg border-1.5 border-dashed border-slate-300 bg-white hover:border-purple-300 cursor-pointer transition-all";
        el.innerHTML = `<span class="text-xs text-slate-400 flex items-center gap-1.5"><i class="fa-solid fa-hand-pointer text-purple-400"></i>點擊查閱詞義注釋 (學生作答區)</span>`;
      }} else {{
        revealedVocab.add(vocabId);
        el.className = "flex-grow p-2.5 rounded-lg border-1.5 border-dashed border-rose-300 bg-rose-50/50 cursor-pointer transition-all";
        el.innerHTML = `<span class="font-handwriting text-rose-600 font-bold text-sm sm:text-base leading-relaxed">${{item.meaning}}</span>`;
      }}
    }}

    // Reveal All Blanks for Current Song
    function revealCurrentSongAnswers() {{
      const song = songsData[currentSongIndex];
      let blankCounter = 0;
      song.lyrics.forEach(line => {{
        if (line.type !== 'space') {{
          line.forEach(chunk => {{
            if (chunk.b) {{
              blankCounter++;
              revealedBlanks.add(`${{song.id}}-b-${{blankCounter}}`);
            }}
          }});
        }}
      }});
      if (song.vocab) {{
        song.vocab.forEach((_, idx) => revealedVocab.add(`${{song.id}}-v-${{idx}}`));
      }}
      renderLyrics(song);
      renderVocabulary(song);
    }}

    // Toggle Global Teacher Mode (All blanks everywhere revealed)
    function toggleAllBlanks() {{
      isTeacherMode = !isTeacherMode;
      const btnText = document.getElementById('toggleAllBtnText');
      const modeLabel = document.getElementById('currentModeLabel');

      if (isTeacherMode) {{
        btnText.textContent = "切換回學生空白版";
        modeLabel.textContent = "教師解答全揭示模式";
        modeLabel.parentElement.classList.replace('bg-white/10', 'bg-rose-500/20');
        modeLabel.parentElement.classList.replace('text-purple-200', 'text-rose-200');
        revealCurrentSongAnswers();
      }} else {{
        btnText.textContent = "一鍵揭曉教師版";
        modeLabel.textContent = "學生自修填空模式";
        modeLabel.parentElement.classList.replace('bg-rose-500/20', 'bg-white/10');
        modeLabel.parentElement.classList.replace('text-rose-200', 'text-purple-200');
        resetAllBlanks();
      }}
    }}

    // Reset All Blanks
    function resetAllBlanks() {{
      revealedBlanks.clear();
      revealedVocab.clear();
      renderLyrics(songsData[currentSongIndex]);
      renderVocabulary(songsData[currentSongIndex]);
    }}

    // ==================== AUDIO & VIDEO PLAYBACK ====================
    function togglePlayPause() {{
      if (isPlaying) {{
        pauseMedia();
      }} else {{
        playMedia();
      }}
    }}

    function playMedia() {{
      const target = isVideoMode ? video : audio;
      const playPromise = target.play();
      if (playPromise !== undefined) {{
        playPromise.catch(err => {{
          console.warn('Playback deferred or error:', err);
          isPlaying = false;
          playIcon.className = 'fa-solid fa-play ml-1';
          vinylDisc.classList.remove('animate-spin-slow');
          vinylArm.classList.remove('playing');
          renderSongListMenu();
        }});
      }}
    }}

    function pauseMedia() {{
      if (isVideoMode) {{
        video.pause();
      }} else {{
        audio.pause();
      }}
      isPlaying = false;
      playIcon.className = 'fa-solid fa-play ml-1';
      vinylDisc.classList.remove('animate-spin-slow');
      vinylArm.classList.remove('playing');
      renderSongListMenu();
    }}

    function skipTime(seconds) {{
      const target = isVideoMode ? video : audio;
      target.currentTime = Math.max(0, Math.min(target.duration || 0, target.currentTime + seconds));
    }}

    function seekAudio(e) {{
      const target = isVideoMode ? video : audio;
      if (!target.duration) return;
      const rect = e.currentTarget.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const ratio = clickX / rect.width;
      target.currentTime = ratio * target.duration;
    }}

    function changeVolume(val) {{
      audio.volume = val;
      video.volume = val;
      if (val == 0) {{
        volumeIcon.className = 'fa-solid fa-volume-xmark';
      }} else if (val < 0.5) {{
        volumeIcon.className = 'fa-solid fa-volume-low';
      }} else {{
        volumeIcon.className = 'fa-solid fa-volume-high';
      }}
    }}

    function toggleMute() {{
      const target = isVideoMode ? video : audio;
      target.muted = !target.muted;
      if (target.muted) {{
        volumeIcon.className = 'fa-solid fa-volume-xmark text-rose-400';
      }} else {{
        changeVolume(volumeSlider.value);
      }}
    }}

    function setSpeed(rate, btn) {{
      audio.playbackRate = rate;
      video.playbackRate = rate;
      document.querySelectorAll('.speed-btn').forEach(b => {{
        b.className = 'speed-btn px-1.5 py-0.5 rounded text-[10px] font-mono bg-white/10 hover:bg-white/20 text-slate-300';
      }});
      btn.className = 'speed-btn px-1.5 py-0.5 rounded text-[10px] font-mono bg-purple-600 text-white font-bold';
    }}

    function setupAudioEvents() {{
      audio.addEventListener('play', () => {{
        isPlaying = true;
        playIcon.className = 'fa-solid fa-pause';
        vinylDisc.classList.add('animate-spin-slow');
        vinylArm.classList.add('playing');
        renderSongListMenu();
      }});
      audio.addEventListener('pause', () => {{
        if (!isVideoMode) {{
          isPlaying = false;
          playIcon.className = 'fa-solid fa-play ml-1';
          vinylDisc.classList.remove('animate-spin-slow');
          vinylArm.classList.remove('playing');
          renderSongListMenu();
        }}
      }});
      audio.addEventListener('timeupdate', () => {{
        if (!isVideoMode) updateProgress(audio.currentTime, audio.duration);
      }});
      audio.addEventListener('loadedmetadata', () => {{
        if (!isVideoMode) totalDurationEl.textContent = formatTime(audio.duration);
      }});
      audio.addEventListener('ended', () => {{
        pauseMedia();
        audio.currentTime = 0;
      }});
    }}

    function setupVideoEvents() {{
      video.addEventListener('play', () => {{
        isPlaying = true;
        playIcon.className = 'fa-solid fa-pause';
        renderSongListMenu();
      }});
      video.addEventListener('pause', () => {{
        if (isVideoMode) {{
          isPlaying = false;
          playIcon.className = 'fa-solid fa-play ml-1';
          renderSongListMenu();
        }}
      }});
      video.addEventListener('timeupdate', () => {{
        if (isVideoMode) updateProgress(video.currentTime, video.duration);
      }});
      video.addEventListener('loadedmetadata', () => {{
        if (isVideoMode) totalDurationEl.textContent = formatTime(video.duration);
      }});
      video.addEventListener('ended', () => {{
        pauseMedia();
        video.currentTime = 0;
      }});
    }}

    function updateProgress(current, duration) {{
      if (!duration || isNaN(duration)) return;
      const pct = (current / duration) * 100;
      progressBar.style.width = `${{pct}}%`;
      progressHandle.style.left = `${{pct}}%`;
      currentTimeEl.textContent = formatTime(current);
      totalDurationEl.textContent = formatTime(duration);
    }}

    function formatTime(sec) {{
      if (isNaN(sec)) return '00:00';
      const m = Math.floor(sec / 60);
      const s = Math.floor(sec % 60);
      return `${{m.toString().padStart(2, '0')}}:${{s.toString().padStart(2, '0')}}`;
    }}

    // ==================== LOCAL STORAGE / NOTES ====================
    function saveStudentInfo(field, value) {{
      localStorage.setItem(`gesong_stu_${{field}}`, value);
      showSavedIndicator();
    }}

    function saveNote(field, value) {{
      const songId = songsData[currentSongIndex].id;
      const key = `gesong_taipei_${{songId}}_${{field}}`;
      localStorage.setItem(key, value);
      showSavedIndicator();
    }}

    function loadSavedNotes() {{
      // Load student info (class, seat, name)
      const c = localStorage.getItem('gesong_stu_class') || '';
      const s = localStorage.getItem('gesong_stu_seat') || '';
      const n = localStorage.getItem('gesong_stu_name') || '';
      const classEl = document.getElementById('stuClass');
      const seatEl = document.getElementById('stuSeat');
      const nameEl = document.getElementById('stuName');
      if (classEl) classEl.value = c;
      if (seatEl) seatEl.value = s;
      if (nameEl) nameEl.value = n;

      const songId = songsData[currentSongIndex].id;
      ['q1', 'q2', 'q3'].forEach(f => {{
        const key = `gesong_taipei_${{songId}}_${{f}}`;
        const val = localStorage.getItem(key) || '';
        const el = document.getElementById(`${{f}}Input`);
        if (el) el.value = val;
      }});

      // Load saved emotion
      const emotionKey = `gesong_taipei_${{songId}}_emotion`;
      const savedEmotion = localStorage.getItem(emotionKey);
      document.querySelectorAll('.emotion-chip').forEach(btn => {{
        if (btn.innerText.includes(savedEmotion)) {{
          setChipActive(btn, true);
        }} else {{
          setChipActive(btn, false);
        }}
      }});
    }}

    function toggleEmotion(btn, emotionName) {{
      const songId = songsData[currentSongIndex].id;
      const emotionKey = `gesong_taipei_${{songId}}_emotion`;
      const current = localStorage.getItem(emotionKey);

      document.querySelectorAll('.emotion-chip').forEach(b => setChipActive(b, false));

      if (current === emotionName) {{
        localStorage.removeItem(emotionKey);
      }} else {{
        localStorage.setItem(emotionKey, emotionName);
        setChipActive(btn, true);
      }}
      showSavedIndicator();
    }}

    function setChipActive(btn, active) {{
      if (active) {{
        btn.classList.add('bg-purple-100', 'border-purple-400', 'text-purple-900', 'font-bold', 'shadow-xs');
        btn.classList.remove('bg-white', 'text-slate-700');
      }} else {{
        btn.classList.remove('bg-purple-100', 'border-purple-400', 'text-purple-900', 'font-bold', 'shadow-xs');
        btn.classList.add('bg-white', 'text-slate-700');
      }}
    }}

    function clearCurrentNotes() {{
      if (!confirm('確定要清空目前這首歌的課堂筆記與情緒紀錄嗎？')) return;
      const songId = songsData[currentSongIndex].id;
      ['q1', 'q2', 'q3', 'emotion'].forEach(f => {{
        localStorage.removeItem(`gesong_taipei_${{songId}}_${{f}}`);
      }});
      loadSavedNotes();
    }}

    function copyCurrentAnswers() {{
      const song = songsData[currentSongIndex];
      const stuClass = document.getElementById('stuClass') ? document.getElementById('stuClass').value.trim() : '';
      const stuSeat = document.getElementById('stuSeat') ? document.getElementById('stuSeat').value.trim() : '';
      const stuName = document.getElementById('stuName') ? document.getElementById('stuName').value.trim() : '';
      const q1 = document.getElementById('q1Input').value.trim();
      const q2 = document.getElementById('q2Input').value.trim();
      const q3 = document.getElementById('q3Input').value.trim();
      const emotion = localStorage.getItem(`gesong_taipei_${{song.id}}_emotion`) || '未選擇';

      const copyContent = `【八上閱思龍門・歌SONG臺北】《${{song.title}}》課堂探究與心得回答
班級：${{stuClass || '（未填寫）'}} ｜ 座號：${{stuSeat || '（未填寫）'}} ｜ 姓名：${{stuName || '（未填寫）'}}
演唱：${{song.artist}} ｜ 作詞：${{song.lyricist}} ｜ 作曲：${{song.composer}}

【問題一】找一找，這首歌不錯的句子有哪些？
${{q1 || '（尚未填寫）'}}

【問題二】想一想，這首歌想表達什麼？
${{q2 || '（尚未填寫）'}}

【問題三】說一說，聽完這首歌你有什麼感想？
${{q3 || '（尚未填寫）'}}

【情緒共鳴】這首歌讓我覺得：
${{emotion}}
`;

      const btn = document.getElementById('copyAnswersBtn');
      const icon = document.getElementById('copyBtnIcon');
      const textSpan = document.getElementById('copyBtnText');

      const onSuccess = () => {{
        btn.classList.replace('bg-purple-50', 'bg-emerald-50');
        btn.classList.replace('text-purple-700', 'text-emerald-700');
        btn.classList.replace('border-purple-200', 'border-emerald-300');
        icon.className = 'fa-solid fa-check text-emerald-600';
        textSpan.textContent = '已複製到剪貼簿！';

        setTimeout(() => {{
          btn.classList.replace('bg-emerald-50', 'bg-purple-50');
          btn.classList.replace('text-emerald-700', 'text-purple-700');
          btn.classList.replace('border-emerald-300', 'border-purple-200');
          icon.className = 'fa-solid fa-copy';
          textSpan.textContent = '一鍵複製回答';
        }}, 2000);
      }};

      if (navigator.clipboard && navigator.clipboard.writeText) {{
        navigator.clipboard.writeText(copyContent).then(onSuccess).catch(err => {{
          console.warn('Clipboard writeText failed, fallback:', err);
          fallbackCopyText(copyContent, onSuccess);
        }});
      }} else {{
        fallbackCopyText(copyContent, onSuccess);
      }}
    }}

    function fallbackCopyText(text, cb) {{
      const ta = document.createElement('textarea');
      ta.value = text;
      ta.style.position = 'fixed';
      ta.style.left = '-9999px';
      document.body.appendChild(ta);
      ta.select();
      try {{
        document.execCommand('copy');
        cb();
      }} catch (e) {{
        alert('請手動選取複製文字：\\n\\n' + text);
      }}
      document.body.removeChild(ta);
    }}

    function showSavedIndicator() {{
      const el = document.getElementById('savedIndicator');
      if (el) {{
        el.style.opacity = '1';
        clearTimeout(window.savedTimeout);
        window.savedTimeout = setTimeout(() => {{
          el.style.opacity = '0';
        }}, 2000);
      }}
    }}

    // Keyboard Shortcuts (Space to play/pause)
    window.addEventListener('keydown', (e) => {{
      if (e.target.tagName === 'TEXTAREA' || e.target.tagName === 'INPUT') return;
      if (e.code === 'Space') {{
        e.preventDefault();
        togglePlayPause();
      }}
    }});
  </script>
</body>
</html>
"""
    return html

# Write index.html and song pages to both taipei and 成品 directories
index_html = generate_html(is_index=True)
song_pages = {song["id"]: generate_html(current_song_id=song["id"], is_index=False) for song in songs}

import shutil
for target_dir in output_dirs:
    with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    for sid, s_html in song_pages.items():
        with open(os.path.join(target_dir, f"{sid}.html"), "w", encoding="utf-8") as f:
            f.write(s_html)
    
    # Ensure assets and media exist in each output dir if present in taipei
    src_taipei = os.path.join(script_dir, "taipei")
    if target_dir != src_taipei:
        for sub in ["assets", "media"]:
            sub_src = os.path.join(src_taipei, sub)
            sub_dst = os.path.join(target_dir, sub)
            if os.path.exists(sub_src) and not os.path.exists(sub_dst):
                shutil.copytree(sub_src, sub_dst)

print("All platform pages generated successfully in taipei and 成品!")
