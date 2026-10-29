html_content = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>釜山賞楓與美食之旅 2026 🍁</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Kalam:wght@400;700&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
  
  <style>
    :root {
      --bg-color: #FFFDF9;
      --text-color: #4A3E3D;
      --card-bg: #FFFFFF;
      --border-color: #4A3E3D;
      --accent-color: #E76F51;
      --accent-secondary: #2A9D8F;
      --accent-yellow: #E9C46A;
      --shadow-color: rgba(74, 62, 61, 0.15);
      --font-doodle: 'Kalam', 'Noto Sans TC', cursive, sans-serif;
      --font-body: 'Noto Sans TC', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    [data-theme="dark"] {
      --bg-color: #2B2625;
      --text-color: #F4F1DE;
      --card-bg: #383231;
      --border-color: #D4C5B9;
      --accent-color: #F4A261;
      --accent-secondary: #76C893;
      --accent-yellow: #E9C46A;
      --shadow-color: rgba(0, 0, 0, 0.4);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background-color: var(--bg-color);
      color: var(--text-color);
      font-family: var(--font-body);
      line-height: 1.6;
      padding-bottom: 80px;
      transition: background-color 0.3s, color 0.3s;
    }

    .doodle-card {
      background-color: var(--card-bg);
      border: 2px solid var(--border-color);
      border-radius: 12px 20px 15px 25px/20px 15px 25px 12px;
      padding: 16px;
      margin-bottom: 16px;
      box-shadow: 4px 5px 0px var(--shadow-color);
    }

    header {
      position: sticky; top: 0; z-index: 1000;
      background-color: var(--bg-color);
      border-bottom: 2px solid var(--border-color);
      padding: 10px 16px;
      display: flex; justify-content: space-between; align-items: center;
    }

    .logo {
      font-family: var(--font-doodle);
      font-size: 1.2rem; font-weight: 700;
      color: var(--accent-color); white-space: nowrap;
    }

    nav {
      display: flex; gap: 6px; overflow-x: auto; padding: 4px 0;
      -webkit-overflow-scrolling: touch;
    }
    nav::-webkit-scrollbar { display: none; }

    .nav-btn {
      background: none; border: 1.5px solid var(--border-color);
      border-radius: 15px 5px 12px 5px/5px 12px 5px 15px;
      padding: 6px 10px; font-size: 0.85rem; font-weight: 700;
      color: var(--text-color); cursor: pointer; white-space: nowrap;
    }
    .nav-btn.active { background-color: var(--accent-color); color: #FFF; }

    .theme-toggle {
      background: none; border: 2px solid var(--border-color);
      border-radius: 50%; width: 36px; height: 36px;
      cursor: pointer; font-size: 1.1rem; flex-shrink: 0;
      display: flex; align-items: center; justify-content: center;
    }

    main { max-width: 600px; margin: 0 auto; padding: 16px; }
    .tab-content { display: none; }
    .tab-content.active { display: block; }

    .day-selector { display: flex; gap: 8px; overflow-x: auto; margin-bottom: 20px; padding-bottom: 6px; }
    .day-btn {
      background-color: var(--card-bg); border: 2px solid var(--border-color);
      border-radius: 10px; padding: 8px 12px; font-size: 0.85rem;
      font-weight: bold; color: var(--text-color); cursor: pointer; white-space: nowrap; flex-shrink: 0;
    }
    .day-btn.active { background-color: var(--accent-secondary); color: white; }

    .timeline-item {
      position: relative; padding-left: 18px;
      border-left: 3px dashed var(--accent-color); margin-bottom: 20px;
    }
    .timeline-time {
      font-family: var(--font-doodle); font-size: 1.4rem;
      font-weight: 700; color: var(--accent-color); display: inline-block; margin-bottom: 4px;
    }

    .transport-tag {
      display: inline-block; padding: 2px 8px; border-radius: 12px;
      font-size: 0.75rem; font-weight: bold; color: white; margin-bottom: 6px;
    }
    .bg-walk { background-color: #2A9D8F; }
    .bg-bus { background-color: #E76F51; }
    .bg-subway { background-color: #457B9D; }
    .bg-taxi { background-color: #E9C46A; color: #333; }

    .action-btn {
      background-color: var(--card-bg); border: 1.5px solid var(--border-color);
      border-radius: 6px; padding: 4px 10px; font-size: 0.8rem; font-weight: bold;
      color: var(--text-color); cursor: pointer; margin-top: 8px; margin-right: 6px;
      display: inline-flex; align-items: center; gap: 4px; text-decoration: none;
    }

    .input-control {
      width: 100%; padding: 8px 12px; border: 2px solid var(--border-color);
      border-radius: 8px; background-color: var(--bg-color); color: var(--text-color); font-size: 1rem;
    }

    .quick-btn {
      background: var(--bg-color); border: 1.5px solid var(--border-color);
      border-radius: 6px; padding: 4px 8px; font-size: 0.8rem; cursor: pointer; font-weight: bold; color: var(--text-color);
    }

    /* 雲朵動畫 */
    @keyframes floatClouds {
      0% { transform: translateX(-10px); }
      50% { transform: translateX(10px); }
      100% { transform: translateX(-10px); }
    }
    .animated-cloud {
      animation: floatClouds 6s ease-in-out infinite;
    }
    @media (prefers-reduced-motion: reduce) {
      .animated-cloud { animation: none !important; }
    }
  </style>
</head>
<body>

  <header>
    <div class="logo">釜山行 2026 🍁</div>
    <nav>
      <button class="nav-btn active" onclick="switchTab('home')">首頁</button>
      <button class="nav-btn" onclick="switchTab('flights')">航班</button>
      <button class="nav-btn" onclick="switchTab('itinerary')">每日行程</button>
      <button class="nav-btn" onclick="switchTab('backup')">備用資料</button>
      <button class="nav-btn" onclick="switchTab('expense')">記帳</button>
      <button class="nav-btn" onclick="switchTab('hotels')">住宿</button>
      <button class="nav-btn" onclick="switchTab('todo')">待辦</button>
    </nav>
    <button class="theme-toggle" id="theme-btn" onclick="toggleTheme()">🌙</button>
  </header>

  <main>
    <!-- 1. 首頁 -->
    <section id="tab-home" class="tab-content active">
      <div class="doodle-card" style="text-align: center; padding: 24px 16px;">
        <svg class="animated-cloud" width="80" height="40" viewBox="0 0 100 50" style="margin: 0 auto 10px;">
          <path d="M20,40 Q10,40 10,30 Q10,20 25,20 Q30,10 45,10 Q60,10 65,20 Q80,20 80,30 Q80,40 70,40 Z" fill="none" stroke="var(--border-color)" stroke-width="3" stroke-linecap="round"/>
        </svg>
        <h1 style="font-family: var(--font-doodle); color: var(--accent-color); font-size: 1.8rem; margin-bottom: 8px;">Busan Travel Handbook</h1>
        <p style="font-size: 0.95rem; font-weight: 500;">2026/10/31 - 11/06 釜山賞楓與美食之旅 🍁</p>
      </div>

      <div class="doodle-card">
        <h3 style="margin-bottom: 10px; color: var(--accent-secondary);">📌 本次行程重點概覽</h3>
        <ul style="padding-left: 20px; font-size: 0.9rem; line-height: 1.8;">
          <li>海雲台藍線公園膠囊列車 🚃</li>
          <li>釜山市民公園楓葉步道 🍁</li>
          <li>韓式烤肉、海鮮帝王蟹與炸雞饗宴 🥩</li>
          <li>廣安里無人機秀與海景咖啡廳 ☕</li>
          <li>海雲台 Spa Land 汗蒸幕放鬆 ♨️</li>
        </ul>
      </div>
    </section>

    <!-- 2. 航班 -->
    <section id="tab-flights" class="tab-content">
      <h2 style="font-family: var(--font-doodle); margin-bottom: 16px;">✈️ 航班資訊</h2>
      <div class="doodle-card">
        <p><strong>去程：</strong>10/31 18:25 抵達金海國際機場 (PUS)</p>
        <p><strong>備註：</strong>抵達後至國際線 1 樓 Gate 3 領取 Busan Pass，搭乘機場巴士前往廣安里。</p>
      </div>
      <div class="doodle-card">
        <p><strong>回程：</strong>11/06 12:00 金海國際機場起飛 (回高雄)</p>
        <p><strong>備註：</strong>09:30 Check-out，10:00 前搭 Uber (約 30 分鐘) 抵達機場。</p>
      </div>
    </section>

    <!-- 3. 每日行程 -->
    <section id="tab-itinerary" class="tab-content">
      <div class="day-selector">
        <button class="day-btn active" onclick="switchDay(1)">10/31 (六)</button>
        <button class="day-btn" onclick="switchDay(2)">11/01 (日)</button>
        <button class="day-btn" onclick="switchDay(3)">11/02 (一)</button>
        <button class="day-btn" onclick="switchDay(4)">11/03 (二)</button>
        <button class="day-btn" onclick="switchDay(5)">11/04 (三)</button>
        <button class="day-btn" onclick="switchDay(6)">11/05 (四)</button>
        <button class="day-btn" onclick="switchDay(7)">11/06 (五)</button>
      </div>
      <div id="day-container"></div>
    </section>

    <!-- 4. 備用資料 -->
    <section id="tab-backup" class="tab-content">
      <h2 style="font-family: var(--font-doodle); margin-bottom: 12px;">📚 備用景點與餐廳</h2>
      <div class="doodle-card">
        <h4 style="margin-bottom: 8px;">🥩 晚餐備選餐廳</h4>
        <p>• Samhwan Chuksan Gwangan (삼환축산 광안점)</p>
        <p>• 釜山宅 (부산댁)</p>
        <p>• 제주옥탑 해운대점 (佳誼推薦烤肉)</p>
        <p>• 미친막창 (密亲烤腸 / 西面八爪魚)</p>
        <p>• 李在模披薩 / 元祖西面牛排骨肉</p>
      </div>
    </section>

    <!-- 5. 記帳與即時雙向匯率試算器 -->
    <section id="tab-expense" class="tab-content">
      <h2 style="font-family: var(--font-doodle); margin-bottom: 16px;">💰 記帳與即時匯率</h2>

      <!-- 即時匯率與試算器卡片 -->
      <div class="doodle-card" style="background: #FFF9E6; border-color: var(--border-color);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
          <span style="font-weight: bold; color: #5A4A42;">💱 即時匯率：</span>
          <span id="rate-text" style="font-weight: bold; color: var(--accent-secondary);">載入中...</span>
          <button onclick="fetchLiveRate()" class="quick-btn" style="background: var(--accent-yellow);">🔄 更新</button>
        </div>

        <div style="margin-top: 12px; border-top: 1px dashed var(--border-color); padding-top: 12px;">
          <label style="font-size: 0.85rem; font-weight: bold; display: block; margin-bottom: 4px;">🇰🇷 韓元 (KRW)</label>
          <input type="number" id="krw-input" class="input-control" placeholder="輸入韓元金額..." oninput="convertKrwToTwd()">

          <div style="display: flex; gap: 6px; margin: 8px 0;">
            <button class="quick-btn" onclick="addKrw(10000)">+1萬</button>
            <button class="quick-btn" onclick="addKrw(50000)">+5萬</button>
            <button class="quick-btn" onclick="addKrw(100000)">+10萬</button>
            <button class="quick-btn" onclick="clearCalc()" style="margin-left: auto;">清空</button>
          </div>

          <label style="font-size: 0.85rem; font-weight: bold; display: block; margin-bottom: 4px; margin-top: 8px;">🇹🇼 約合台幣 (TWD)</label>
          <input type="number" id="twd-input" class="input-control" placeholder="約合台幣..." oninput="convertTwdToKrw()">
        </div>
      </div>

      <!-- 記帳表單與列表 -->
      <div class="doodle-card">
        <h3 style="margin-bottom: 12px;">✍️ 新增花費</h3>
        <input type="text" id="expense-title" class="input-control" placeholder="項目名稱 (例如：炸雞)" style="margin-bottom: 8px;">
        <input type="number" id="expense-amount" class="input-control" placeholder="金額 (KRW 韓元)" style="margin-bottom: 12px;">
        <button onclick="addExpense()" class="action-btn" style="width: 100%; justify-content: center; background: var(--accent-color); color: white; padding: 8px;">➕ 新增紀錄</button>
      </div>

      <div class="doodle-card">
        <h3 style="margin-bottom: 8px;">📋 消費明細</h3>
        <div id="expense-list"></div>
        <hr style="margin: 12px 0; border: none; border-top: 1px dashed var(--border-color);">
        <div style="display: flex; justify-content: space-between; font-weight: bold; font-size: 1.1rem;">
          <span>總計：</span>
          <span id="expense-total" style="color: var(--accent-color);">₩0 (NT$ 0)</span>
        </div>
      </div>
    </section>

    <!-- 6. 住宿 -->
    <section id="tab-hotels" class="tab-content">
      <h2 style="font-family: var(--font-doodle); margin-bottom: 16px;">🏨 飯店住宿</h2>
      <div class="doodle-card">
        <h3>1. Kent Hotel Gwangalli by Kensington</h3>
        <p style="font-size: 0.85rem;">켄트호텔 광안리 by 켄싱턴 (廣安里海景)</p>
      </div>
      <div class="doodle-card">
        <h3>2. Homers Hotel</h3>
        <p style="font-size: 0.85rem;"> (走路 2 分鐘即可更換換宿)</p>
      </div>
      <div class="doodle-card">
        <h3>3. Urban Groove Hotel</h3>
        <p style="font-size: 0.85rem;"> (接近田浦咖啡街與南浦洞區域)</p>
      </div>
    </section>

    <!-- 7. 待辦 -->
    <section id="tab-todo" class="tab-content">
      <h2 style="font-family: var(--font-doodle); margin-bottom: 16px;">✅ 行前待辦與清單</h2>
      <div class="doodle-card">
        <label style="display: block; margin-bottom: 8px;"><input type="checkbox"> 護照與韓國 Visit Korea Year 電子入境申請</label>
        <label style="display: block; margin-bottom: 8px;"><input type="checkbox"> 網卡 / eSIM 準備</label>
        <label style="display: block; margin-bottom: 8px;"><input type="checkbox"> 轉接頭與行動電源</label>
        <label style="display: block; margin-bottom: 8px;"><input type="checkbox"> NAVER Map / Kakao T App 下載</label>
      </div>
    </section>
  </main>

  <script>
    let currentKrwRate = 0.024; 

    function switchTab(tabId) {
      document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.nav-btn').forEach(el => el.classList.remove('active'));
      
      const target = document.getElementById('tab-' + tabId);
      if (target) target.classList.add('active');
      
      const navBtn = Array.from(document.querySelectorAll('.nav-btn')).find(b => b.getAttribute('onclick').includes(tabId));
      if (navBtn) navBtn.classList.add('active');

      localStorage.setItem('active_tab', tabId);
    }

    const itineraryData = {
      1: [{ time: "18:25", title: "抵達金海機場", desc: "國際線1樓Gate3換busan pass，搭機場巴士往廣安里入住 Kent Hotel", tag: "公車", tagClass: "bg-bus" },
          { time: "20:00", title: "廣安里無人機秀 & 83 haechi 候位", desc: "晚餐備選：삼환축산 광안점 / 부산댁", tag: "步行", tagClass: "bg-walk" }],
      2: [{ time: "09:00", title: "換至 Homers hotel", desc: "走路約 2 分鐘即可抵達新飯店辦理寄存", tag: "步行", tagClass: "bg-walk" },
          { time: "10:30", title: "Skyline Luge & 海東龍宮寺", desc: "搭乘纜車/滑車，隨後走訪海邊龍宮寺", tag: "公車", tagClass: "bg-bus" },
          { time: "13:00", title: "hai 水產吃蟹", desc: "新鮮帝王蟹與海鮮饗宴", tag: "步行", tagClass: "bg-walk" },
          { time: "15:00", title: "樂天 Outlet & 新世界百貨", desc: "逛街購物行程 (備選晚餐：제주옥탑 해운대점 佳誼推薦烤肉)", tag: "捷運", tagClass: "bg-subway" }],
      3: [{ time: "09:00", title: "早餐 All Sunday & 新世界百貨", desc: "先至新世界百貨 3 樓換會員卡，享用 Spa Land (20:30關)", tag: "捷運", tagClass: "bg-subway" },
          { time: "12:30", title: "海雲台傳統市場", desc: "大海鮑魚粥、名品糖餅、老虎冰淇淋大福", tag: "步行", tagClass: "bg-walk" },
          { time: "15:30", title: "藍線公園膠囊列車", desc: "尾浦站到青沙浦 ➔ Liberta ☕ ➔ 海岸列車回", tag: "電車", tagClass: "bg-bus" },
          { time: "18:30", title: "晚餐：獵奇辣炒年糕 & Puradak 炸雞", desc: "享受在地經典韓式炸雞與辣年糕", tag: "步行", tagClass: "bg-walk" }],
      4: [{ time: "09:00", title: "早餐：水邊豬肉湯飯 / 安木 / ANCIEN", desc: "品嚐明太子法棍，隨後漫步 Scentica 與廣安里海岸", tag: "步行", tagClass: "bg-walk" },
          { time: "12:00", title: "Check in Urban Groove Hotel", desc: "辦理入住或寄放行李", tag: "計程車", tagClass: "bg-taxi" },
          { time: "14:00", title: "釜山市民公園賞楓 & 田浦咖啡街", desc: "享受秋季楓葉步道與特色咖啡廳", tag: "捷運", tagClass: "bg-subway" },
          { time: "18:00", title: "南浦洞 BIFF 廣場", desc: "晚餐：미친막창 (密亲烤腸) / 西面八爪魚，宵夜南浦洞 54 號布帳馬車", tag: "捷運", tagClass: "bg-subway" }],
      5: [{ time: "09:00", title: "甘川洞文化村 (9:00-10:30)", desc: "尋找小王子、買襪子、bada sand 伴手禮", tag: "公車", tagClass: "bg-bus" },
          { time: "11:00", title: "新東亞市場 85/87/100號 吃帝王蟹", desc: "享用新鮮平價帝王蟹海鮮大餐", tag: "步行", tagClass: "bg-walk" },
          { time: "13:30", title: "松島纜車來回 & 白淺灘文化村", desc: "絕美海景步道與纜車 (也可順遊 Arte Museum)", tag: "公車", tagClass: "bg-bus" },
          { time: "18:00", title: "南浦洞時尚街 / 樂天百貨", desc: "晚餐：元祖西面牛排骨肉 / Samhwan 韓牛 / 李在模披薩", tag: "步行", tagClass: "bg-walk" }],
      6: [{ time: "09:00", title: "醫美行程 (09:00 - 13:00)", desc: "預約好的美學護理與行程", tag: "捷運", tagClass: "bg-subway" },
          { time: "18:00", title: "美食晚餐巡禮", desc: "備選：元祖西面牛排骨肉 / Samhwan 韓牛 / 李在模披薩", tag: "步行", tagClass: "bg-walk" }],
      7: [{ time: "09:30", title: "飯店 Check Out", desc: "整理行李，準備出發前往金海機場", tag: "步行", tagClass: "bg-walk" },
          { time: "10:00", title: "抵達金海國際機場", desc: "搭乘 Uber 約 30 分鐘，12:00 起飛返回高雄！", tag: "計程車", tagClass: "bg-taxi" }]
    };

    function switchDay(day) {
      document.querySelectorAll('.day-btn').forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');

      const container = document.getElementById('day-container');
      const items = itineraryData[day] || [];
      
      container.innerHTML = items.map(item => `
        <div class="timeline-item">
          <div class="timeline-time">${item.time}</div>
          <span class="transport-tag ${item.tagClass}">${item.tag}</span>
          <h3 style="font-size: 1.1rem; margin-bottom: 4px;">${item.title}</h3>
          <p style="font-size: 0.88rem; color: var(--text-color);">${item.desc}</p>
          <a href="https://map.naver.com/v5/search/${encodeURIComponent(item.title)}" target="_blank" class="action-btn">🗺️ NAVER Map 導航</a>
        </div>
      `).join('');
    }

    async function fetchLiveRate() {
      const rateText = document.getElementById('rate-text');
      if (rateText) rateText.innerText = "更新中...";

      try {
        const res = await fetch('https://open.er-api.com/v6/latest/KRW');
        const data = await res.json();
        if (data && data.rates && data.rates.TWD) {
          currentKrwRate = data.rates.TWD;
          localStorage.setItem('cached_krw_rate', currentKrwRate);
          if (rateText) rateText.innerText = `1 KRW ≈ ${currentKrwRate.toFixed(4)} TWD`;
          convertKrwToTwd();
          renderExpenses();
        }
      } catch (e) {
        const cached = localStorage.getItem('cached_krw_rate');
        if (cached) currentKrwRate = parseFloat(cached);
        if (rateText) rateText.innerText = `1 KRW ≈ ${currentKrwRate.toFixed(4)} TWD (離線)`;
      }
    }

    function convertKrwToTwd() {
      const krw = parseFloat(document.getElementById('krw-input').value) || 0;
      document.getElementById('twd-input').value = Math.round(krw * currentKrwRate);
    }

    function convertTwdToKrw() {
      const twd = parseFloat(document.getElementById('twd-input').value) || 0;
      document.getElementById('krw-input').value = Math.round(twd / currentKrwRate);
    }

    function addKrw(amount) {
      const input = document.getElementById('krw-input');
      const current = parseFloat(input.value) || 0;
      input.value = current + amount;
      convertKrwToTwd();
    }

    function clearCalc() {
      document.getElementById('krw-input').value = '';
      document.getElementById('twd-input').value = '';
    }

    let expenses = JSON.parse(localStorage.getItem('busan_expenses') || '[]');

    function addExpense() {
      const title = document.getElementById('expense-title').value.trim();
      const amount = parseFloat(document.getElementById('expense-amount').value);

      if (!title || !amount) { alert('請填寫完整項目與金額！'); return; }

      expenses.push({ id: Date.now(), title, amount });
      localStorage.setItem('busan_expenses', JSON.stringify(expenses));
      document.getElementById('expense-title').value = '';
      document.getElementById('expense-amount').value = '';
      renderExpenses();
    }

    function deleteExpense(id) {
      expenses = expenses.filter(e => e.id !== id);
      localStorage.setItem('busan_expenses', JSON.stringify(expenses));
      renderExpenses();
    }

    function renderExpenses() {
      const list = document.getElementById('expense-list');
      const totalEl = document.getElementById('expense-total');
      if (!list) return;

      if (expenses.length === 0) {
        list.innerHTML = '<p style="font-size: 0.85rem; color: #888;">目前尚無消費紀錄</p>';
        if (totalEl) totalEl.innerText = '₩0 (NT$ 0)';
        return;
      }

      let totalKrw = 0;
      list.innerHTML = expenses.map(e => {
        totalKrw += e.amount;
        const twd = Math.round(e.amount * currentKrwRate);
        return `
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; font-size: 0.9rem;">
            <span>${e.title}</span>
            <div>
              <span style="font-weight: bold; margin-right: 8px;">₩${e.amount.toLocaleString()} (NT$${twd.toLocaleString()})</span>
              <button onclick="deleteExpense(${e.id})" style="background: none; border: none; color: #E76F51; cursor: pointer; font-weight: bold;">✕</button>
            </div>
          </div>
        `;
      }).join('');

      const totalTwd = Math.round(totalKrw * currentKrwRate);
      if (totalEl) totalEl.innerText = `₩${totalKrw.toLocaleString()} (NT$ ${totalTwd.toLocaleString()})`;
    }

    function toggleTheme() {
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      document.getElementById('theme-btn').innerText = next === 'dark' ? '☀️' : '🌙';
      localStorage.setItem('user_theme', next);
    }

    document.addEventListener('DOMContentLoaded', () => {
      const savedTheme = localStorage.getItem('user_theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
      document.documentElement.setAttribute('data-theme', savedTheme);
      document.getElementById('theme-btn').innerText = savedTheme === 'dark' ? '☀️' : '🌙';

      const savedTab = localStorage.getItem('active_tab') || 'home';
      switchTab(savedTab);
      switchDay(1);
      fetchLiveRate();
      renderExpenses();
    });
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML file generated successfully.")