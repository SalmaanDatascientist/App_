<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>The Molecular Man Expert Tuition Solutions</title>
<link rel="manifest" href="manifest.json">
<link rel="icon" type="image/png" href="logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;600;700&family=Exo+2:wght@300;400;700;900&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg-from: #004e92;
    --bg-to: #000428;
    --gold: #ffd700;
    --cyan: #00ffff;
    --white: #ffffff;
    --card-bg: rgba(255,255,255,0.05);
    --card-border: rgba(255,255,255,0.15);
  }

  html { scroll-behavior: smooth; }
  body {
    font-family: 'Exo 2', sans-serif;
    background: linear-gradient(135deg, var(--bg-from) 0%, var(--bg-to) 100%);
    background-attachment: fixed;
    color: var(--white);
    min-height: 100vh;
  }

  .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
  .hidden { display: none !important; }
  a { text-decoration: none; }

  @keyframes fadeInUp { from { opacity:0; transform:translateY(30px); } to { opacity:1; transform:translateY(0); } }
  @keyframes border-flow {
    0%   { border-color:rgba(255,215,0,.3); box-shadow:0 0 15px rgba(255,215,0,.1); }
    50%  { border-color:rgba(0,255,255,.5); box-shadow:0 0 25px rgba(0,255,255,.2); }
    100% { border-color:rgba(255,215,0,.3); box-shadow:0 0 15px rgba(255,215,0,.1); }
  }
  .founder-header {
    text-align:center; padding:35px 20px;
    background:linear-gradient(135deg,rgba(0,0,0,.4) 0%,rgba(0,0,0,.2) 100%);
    backdrop-filter:blur(10px); border-radius:20px;
    border:1px solid rgba(255,255,255,.1); margin-bottom:30px;
    animation:border-flow 4s infinite alternate;
  }
  .founder-headline {
    font-family:'Rajdhani',sans-serif; font-size:clamp(1.2rem,3vw,2.2rem);
    font-weight:900; letter-spacing:-.5px;
    background:linear-gradient(to right,#fff 0%,#a1c4fd 100%);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    margin-bottom:15px; animation:fadeInUp .8s ease-out forwards;
  }
  .founder-subhead { font-size:clamp(.9rem,2vw,1.2rem); color:#e2e8f0; font-weight:300; margin-bottom:15px; opacity:0; animation:fadeInUp .8s ease-out .3s forwards; }
  .founder-tagline { font-size:clamp(.75rem,1.5vw,1rem); color:var(--gold); font-weight:800; text-transform:uppercase; letter-spacing:2px; opacity:0; animation:fadeInUp .8s ease-out .6s forwards; }

  nav { background:rgba(0,0,0,.3); backdrop-filter:blur(12px); position:sticky; top:0; z-index:100; border-bottom:1px solid rgba(255,255,255,.1); }
  .nav-inner { display:flex; gap:8px; justify-content:center; flex-wrap:wrap; padding:10px 20px; }
  .nav-btn {
    background:linear-gradient(90deg,#1e3a5f,#3b6b9e,#1e3a5f);
    color:#fff; border:1px solid rgba(255,255,255,.2); border-radius:25px;
    padding:10px 22px; cursor:pointer; font-family:'Exo 2',sans-serif;
    font-size:.9rem; font-weight:600; transition:transform .2s,box-shadow .2s;
  }
  .nav-btn:hover, .nav-btn.active { transform:translateY(-2px); box-shadow:0 5px 15px rgba(0,0,0,.4); border-color:var(--cyan); }
  .nav-btn.ai-nav { background:linear-gradient(90deg,#1a0533,#6d28d9,#1a0533); border-color:rgba(167,139,250,.4); }
  .nav-btn.ai-nav:hover, .nav-btn.ai-nav.active { border-color:#a78bfa; box-shadow:0 5px 20px rgba(109,40,217,.5); }

  .divider { height:1px; background:rgba(255,255,255,.15); margin:24px 0; }
  .page { padding:20px 0 60px; animation:fadeInUp .4s ease-out; }

  .wcard { background:#fff; color:#000; padding:20px; border-radius:12px; box-shadow:0 4px 12px rgba(0,0,0,.15); margin-bottom:20px; }
  .wcard * { color:#000 !important; }
  .wcard h3 { color:#2c5282 !important; margin-bottom:10px; font-family:'Rajdhani',sans-serif; font-size:1.2rem; }
  .wcard ul { padding-left:22px; }
  .wcard li { margin-bottom:4px; font-size:.95rem; }
  .wcard p { font-size:.9rem; color:#555 !important; }

  .gcard { background:var(--card-bg); border:1px solid var(--card-border); border-radius:16px; padding:20px; }

  .grid-2 { display:grid; grid-template-columns:1fr 1fr; gap:20px; }
  .grid-3 { display:grid; grid-template-columns:repeat(3,1fr); gap:20px; }
  .grid-4 { display:grid; grid-template-columns:repeat(4,1fr); gap:20px; }
  @media(max-width:768px) { .grid-2,.grid-3,.grid-4 { grid-template-columns:1fr; } .hero-logo-row { flex-direction:column !important; } }

  .metric { text-align:center; }
  .metric-value { font-size:2rem; font-weight:900; color:var(--gold); font-family:'Rajdhani',sans-serif; }
  .metric-label { font-size:.85rem; color:#a0aec0; }

  @keyframes neon-pulse {
    0%   { box-shadow:0 0 5px var(--gold),0 0 15px var(--gold) inset; border-color:var(--gold); }
    50%  { box-shadow:0 0 20px var(--cyan),0 0 10px var(--cyan) inset; border-color:var(--cyan); }
    100% { box-shadow:0 0 5px var(--gold),0 0 15px var(--gold) inset; border-color:var(--gold); }
  }
  .hero-ad { background:rgba(0,0,0,.7); backdrop-filter:blur(12px); border:2px solid var(--gold); border-radius:20px; padding:40px 24px; margin:30px 0; text-align:center; animation:neon-pulse 4s infinite alternate; }
  .hero-ad-headline { font-size:clamp(1.2rem,3vw,2rem); font-weight:900; text-transform:uppercase; letter-spacing:1px; background:linear-gradient(to right,#fff,var(--gold)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-bottom:15px; font-family:'Rajdhani',sans-serif; }
  .hero-ad-sub { font-size:1.05rem; color:#e0e0e0; margin-bottom:20px; }
  .hero-suite-title { font-size:1.25rem; color:var(--cyan); font-weight:800; text-transform:uppercase; margin-bottom:20px; text-shadow:0 0 10px rgba(0,255,255,.5); font-family:'Rajdhani',sans-serif; }
  .hero-feature-grid { display:flex; justify-content:center; gap:24px; flex-wrap:wrap; margin-bottom:28px; }
  .hero-feature-item { background:rgba(255,255,255,.05); padding:16px 24px; border-radius:12px; border:1px solid rgba(255,255,255,.1); text-align:left; max-width:360px; min-width:220px; }
  .hero-feature-item .title { font-size:1.1rem; color:var(--gold); font-weight:700; margin-bottom:6px; }
  .hero-feature-item .desc { font-size:.9rem; color:#e0e0e0; }
  .hero-footer { font-size:.85rem; font-weight:800; color:#ff4d4d; letter-spacing:1.5px; border-top:1px solid rgba(255,255,255,.1); padding-top:15px; margin-top:10px; }

  .link-btn { display:inline-block; padding:12px 28px; background:linear-gradient(90deg,#1e3a5f,#3b6b9e,#1e3a5f); color:#fff; border:1px solid rgba(255,255,255,.3); border-radius:25px; font-family:'Exo 2',sans-serif; font-weight:700; font-size:1rem; cursor:pointer; transition:transform .2s,box-shadow .2s; }
  .link-btn:hover { transform:translateY(-2px); box-shadow:0 5px 20px rgba(0,0,0,.4); }
  .btn-center { text-align:center; margin:24px 0; }

  .hero-logo-row { display:flex; gap:20px; align-items:stretch; }
  .logo-box { flex:0 0 220px; min-width:160px; display:flex; align-items:center; justify-content:center; background:var(--card-bg); border:1px solid var(--card-border); border-radius:16px; padding:24px; }
  .logo-info { flex:1; background:var(--card-bg); border:1px solid var(--card-border); border-radius:16px; padding:28px; }
  .logo-info h1 { font-family:'Rajdhani',sans-serif; font-size:clamp(1.5rem,4vw,2.5rem); font-weight:900; }
  .logo-info h3 { font-size:clamp(.9rem,2vw,1.2rem); color:#a1c4fd; margin:8px 0; font-weight:400; }
  .logo-info p { color:#c0cfe0; font-size:.95rem; margin-bottom:16px; }

  .section-title { font-family:'Rajdhani',sans-serif; font-size:clamp(1.4rem,3vw,2rem); font-weight:900; margin:32px 0 16px; }

  .board-select-wrap { margin-bottom:24px; }
  .board-select-wrap label { display:block; margin-bottom:8px; font-weight:600; font-size:.95rem; }
  .board-select-wrap select { background:rgba(255,255,255,.1); color:#fff; border:1px solid rgba(255,255,255,.3); border-radius:8px; padding:10px 16px; font-size:1rem; font-family:'Exo 2',sans-serif; width:100%; max-width:400px; cursor:pointer; outline:none; }
  .board-select-wrap select option { background:#1e3a5f; color:#fff; }
  .board-panel { display:none; }
  .board-panel.active { display:block; }

  /* ══ TESTIMONIALS — AI CORNER STYLE ══ */
  @keyframes testi-glow {
    0%   { border-color:rgba(255,215,0,.2); box-shadow:0 0 15px rgba(255,215,0,.05); }
    50%  { border-color:rgba(0,255,255,.3); box-shadow:0 0 25px rgba(0,255,255,.1); }
    100% { border-color:rgba(255,215,0,.2); box-shadow:0 0 15px rgba(255,215,0,.05); }
  }
  @keyframes pulse-dot {
    0%,100% { transform:scale(1); opacity:1; }
    50%      { transform:scale(1.4); opacity:.7; }
  }
  @keyframes shimmer-text {
    0%   { background-position:-200% center; }
    100% { background-position:200% center; }
  }
  @keyframes marquee-t { from { transform:translateX(0); } to { transform:translateX(-50%); } }

  .testi-marquee-wrap { overflow:hidden; margin:0 0 28px; }
  .testi-marquee-track { display:flex; gap:20px; animation:marquee-t 25s linear infinite; width:max-content; }
  .testi-marquee-item { background:rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.08); border-radius:10px; padding:10px 20px; white-space:nowrap; font-size:.85rem; color:#cbd5e1; }
  .testi-marquee-item strong { color:var(--gold); }

  .testi-hero {
    position:relative; overflow:hidden;
    background:linear-gradient(135deg,rgba(0,4,40,.96) 0%,rgba(0,20,50,.95) 50%,rgba(0,8,40,.96) 100%);
    border:2px solid rgba(255,215,0,.25); border-radius:28px;
    padding:48px 32px 36px; text-align:center; margin-bottom:40px;
    animation:testi-glow 5s infinite alternate;
  }
  .testi-hero::before {
    content:''; position:absolute; inset:0;
    background:radial-gradient(ellipse at 15% 40%,rgba(255,215,0,.06) 0%,transparent 55%),
               radial-gradient(ellipse at 85% 60%,rgba(0,255,255,.05) 0%,transparent 55%);
    pointer-events:none;
  }
  .testi-hero-stars { font-size:1.5rem; letter-spacing:6px; margin-bottom:14px; }
  .testi-hero-title {
    font-family:'Rajdhani',sans-serif; font-weight:900; font-size:clamp(2rem,5vw,3.8rem);
    background:linear-gradient(135deg,#fff 0%,#ffd700 35%,#00ffff 70%,#ffd700 100%);
    background-size:200% auto; -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    background-clip:text; animation:shimmer-text 5s linear infinite; line-height:1.1; margin-bottom:10px;
  }
  .testi-hero-sub { font-size:1rem; color:#94a3b8; max-width:560px; margin:0 auto 28px; line-height:1.7; }

  .testi-tab-row { display:flex; justify-content:center; gap:12px; flex-wrap:wrap; margin-bottom:32px; }
  .testi-tab {
    padding:10px 28px; border-radius:30px; cursor:pointer; font-family:'Exo 2',sans-serif;
    font-weight:700; font-size:.95rem; border:1px solid rgba(255,255,255,.15);
    background:rgba(255,255,255,.05); color:#94a3b8; transition:all .25s;
  }
  .testi-tab:hover { border-color:rgba(255,215,0,.4); color:#fff; }
  .testi-tab.active-tab { background:rgba(255,215,0,.1); border-color:rgba(255,215,0,.5); color:var(--gold); box-shadow:0 0 16px rgba(255,215,0,.15); }

  .testi-panel { display:none; }
  .testi-panel.active { display:block; animation:fadeInUp .4s ease-out; }

  .testi-section-label {
    display:flex; align-items:center; gap:12px; margin-bottom:20px;
    font-family:'Rajdhani',sans-serif; font-size:1.1rem; font-weight:700; color:#a0aec0; text-transform:uppercase; letter-spacing:1.5px;
  }
  .testi-section-label::after { content:''; flex:1; height:1px; background:linear-gradient(to right,rgba(255,255,255,.1),transparent); }

  .tcard-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(300px,1fr)); gap:20px; margin-bottom:36px; }
  .tcard-new {
    background:rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.09);
    border-radius:20px; padding:24px; position:relative; overflow:hidden;
    transition:transform .3s, border-color .3s, box-shadow .3s;
  }
  .tcard-new:hover { transform:translateY(-5px); border-color:rgba(255,215,0,.3); box-shadow:0 12px 40px rgba(0,0,0,.4); }
  .tcard-new::before { content:''; position:absolute; top:0; left:0; right:0; height:2px; background:linear-gradient(90deg,transparent,rgba(255,215,0,.4),transparent); }
  .tcard-quote-icon { font-size:2rem; line-height:1; color:rgba(255,215,0,.25); margin-bottom:12px; font-family:Georgia,serif; }
  .tcard-text { font-size:.93rem; color:#cbd5e1; line-height:1.75; margin-bottom:18px; font-style:italic; }
  .tcard-highlight {
    display:inline-block; padding:3px 10px; border-radius:20px; font-size:.72rem; font-weight:700;
    margin-bottom:14px; text-transform:uppercase; letter-spacing:1px;
  }
  .tcard-highlight.hl-gold { background:rgba(255,215,0,.1); border:1px solid rgba(255,215,0,.3); color:var(--gold); }
  .tcard-highlight.hl-cyan { background:rgba(0,255,255,.08); border:1px solid rgba(0,255,255,.3); color:var(--cyan); }
  .tcard-highlight.hl-green { background:rgba(72,255,0,.08); border:1px solid rgba(72,255,0,.25); color:#48ff00; }
  .tcard-highlight.hl-purple { background:rgba(167,139,250,.1); border:1px solid rgba(167,139,250,.3); color:#c4b5fd; }
  .tcard-footer { display:flex; align-items:center; gap:12px; border-top:1px solid rgba(255,255,255,.07); padding-top:14px; }
  .tcard-avatar { width:40px; height:40px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:1.2rem; flex-shrink:0; background:rgba(255,255,255,.08); border:1px solid rgba(255,255,255,.15); }
  .tcard-info-name { font-weight:700; font-size:.9rem; color:#e2e8f0; }
  .tcard-info-meta { font-size:.75rem; color:#64748b; margin-top:2px; }
  .tcard-stars { font-size:.75rem; letter-spacing:2px; color:var(--gold); margin-top:3px; }

  .testi-results {
    background:rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.08); border-radius:20px;
    padding:32px; text-align:center; margin-top:36px;
  }
  .testi-results-title { font-family:'Rajdhani',sans-serif; font-size:1.5rem; font-weight:900; margin-bottom:24px; color:#e2e8f0; }
  .testi-results-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(140px,1fr)); gap:20px; }
  .testi-result-item { text-align:center; }
  .testi-result-num { font-family:'Rajdhani',sans-serif; font-size:2.2rem; font-weight:900; background:linear-gradient(to right,#ffd700,#00ffff); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
  .testi-result-label { font-size:.8rem; color:#64748b; margin-top:4px; text-transform:uppercase; letter-spacing:1px; }

  /* ── RESULTS STAT ── */
  .stat-box { text-align:center; }
  .stat-num { font-size:2.2rem; font-weight:900; color:#000; font-family:'Rajdhani',sans-serif; }
  .stat-label { font-size:.8rem; color:#666; }
  .stat-cat { font-weight:700; color:#555; font-size:.9rem; margin-bottom:4px; }

  /* ── BOOTCAMP ── */
  .bootcamp-row { display:flex; gap:24px; align-items:flex-start; }
  .bootcamp-visual { flex:0 0 40%; min-width:180px; background:var(--card-bg); border:1px solid var(--card-border); border-radius:16px; padding:40px; text-align:center; }
  .bootcamp-visual span { font-size:80px; }
  .bootcamp-visual h2 { font-family:'Rajdhani',sans-serif; font-size:2rem; margin-top:12px; }
  .bootcamp-visual h4 { color:#a1c4fd; font-weight:400; }
  .bootcamp-info { flex:1; background:var(--card-bg); border:1px solid var(--card-border); border-radius:16px; padding:24px; }
  .bootcamp-info h3 { font-family:'Rajdhani',sans-serif; font-size:1.5rem; margin-bottom:16px; }
  .info-row { margin-bottom:14px; }
  .info-row strong { display:block; font-size:1rem; margin-bottom:2px; }
  .info-row span { font-size:.85rem; color:#a0aec0; display:block; }
  details summary { cursor:pointer; padding:10px 14px; background:rgba(255,255,255,.08); border-radius:8px; font-weight:600; margin-bottom:8px; list-style:none; }
  details summary::-webkit-details-marker { display:none; }
  details[open] summary { background:rgba(255,255,255,.14); }
  details p { padding:8px 14px 2px; font-size:.9rem; color:#d0e0f0; line-height:1.7; }
  @media(max-width:768px) { .bootcamp-row { flex-direction:column; } }

  /* ── CONTACT ── */
  .contact-row { display:grid; grid-template-columns:1fr 1fr; gap:24px; }
  @media(max-width:768px) { .contact-row { grid-template-columns:1fr; } }
  .contact-info { background:var(--card-bg); border:1px solid var(--card-border); border-radius:16px; padding:24px; }
  .contact-form { background:var(--card-bg); border:1px solid var(--card-border); border-radius:16px; padding:24px; }
  .form-group { margin-bottom:14px; }
  .form-group label { display:block; font-size:.9rem; margin-bottom:6px; color:#e0e0e0; }
  .form-group input, .form-group textarea, .form-group select {
    width:100%; background:rgba(255,255,255,.1); color:#fff; border:1px solid rgba(255,255,255,.3);
    border-radius:8px; padding:10px 14px; font-family:'Exo 2',sans-serif; font-size:.95rem; outline:none; transition:border-color .2s;
  }
  .form-group input[type="file"] { padding:8px 14px; cursor:pointer; }
  .form-group input:focus, .form-group textarea:focus { border-color:var(--cyan); }
  .form-group textarea { resize:vertical; min-height:90px; }
  .form-group option { background:#1e3a5f; }
  #sendBtn { width:100%; padding:12px; background:linear-gradient(90deg,#1e3a5f,#3b6b9e,#1e3a5f); color:#fff; border:1px solid rgba(255,255,255,.3); border-radius:25px; font-size:1rem; font-family:'Exo 2',sans-serif; font-weight:700; cursor:pointer; margin-top:8px; transition:transform .2s,box-shadow .2s; opacity:.5; pointer-events:none; }
  #sendBtn.ready { opacity:1; pointer-events:auto; }
  #sendBtn.ready:hover { transform:translateY(-2px); box-shadow:0 5px 20px rgba(0,0,0,.4); }
  .send-hint { text-align:center; font-size:.75rem; color:#888; margin-top:4px; }

  @keyframes gradient-animation { 0%{background-position:0% 50%} 50%{background-position:100% 50%} 100%{background-position:0% 50%} }
  footer { border:1px solid rgba(255,255,255,.15); border-radius:16px; padding:28px 20px; margin:40px 20px 20px; text-align:center; background:var(--card-bg); }
  .footer-text { font-family:'Rajdhani',sans-serif; font-weight:800; font-size:clamp(1rem,3vw,1.5rem); text-transform:uppercase; letter-spacing:2px; background:linear-gradient(45deg,#ff0000,#ff7300,#fffb00,#48ff00,#00ffd5,#002bff,#7a00ff,#ff00c8,#ff0000); background-size:300%; -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; animation:gradient-animation 10s ease infinite; }
  .footer-copy { font-size:.75rem; color:#666; margin-top:10px; }

  .board-prompt { background:rgba(255,255,255,.05); border:1px solid rgba(255,255,255,.15); border-radius:16px; padding:40px; text-align:center; }
  .board-prompt span { font-size:40px; display:block; margin-bottom:12px; }
  .board-prompt p { font-size:1.05rem; color:#e0e0e0; }

  /* ── LIVE CLASS ── */
  .lc-view { display:none; }
  .lc-view.active { display:block; }
  .lc-role-grid { display:flex; gap:24px; justify-content:center; flex-wrap:wrap; margin-top:24px; }
  .lc-role-btn { flex:1; min-width:220px; max-width:340px; padding:40px 24px; text-align:center; background:var(--card-bg); border:1px solid var(--card-border); border-radius:16px; cursor:pointer; transition:transform .25s, box-shadow .25s, border-color .25s; backdrop-filter:blur(10px); }
  .lc-role-btn:hover { transform:translateY(-4px); box-shadow:0 8px 30px rgba(0,0,0,.4); border-color:var(--cyan); }
  .lc-role-btn .icon { font-size:48px; display:block; margin-bottom:12px; }
  .lc-role-btn .label { font-family:'Rajdhani',sans-serif; font-size:1.4rem; font-weight:700; }
  .lc-role-btn .sublabel { font-size:.85rem; color:#a0aec0; margin-top:4px; }

  .lc-login-card { max-width:420px; margin:30px auto; background:var(--card-bg); border:1px solid var(--card-border); border-radius:16px; padding:30px; backdrop-filter:blur(10px); }
  .lc-login-card h3 { font-family:'Rajdhani',sans-serif; font-size:1.5rem; margin-bottom:20px; text-align:center; }
  .lc-login-card .lc-submit { width:100%; padding:12px; margin-top:10px; background:linear-gradient(90deg,#1e3a5f,#3b6b9e,#1e3a5f); color:#fff; border:1px solid rgba(255,255,255,.3); border-radius:25px; font-family:'Exo 2',sans-serif; font-weight:700; font-size:1rem; cursor:pointer; transition:transform .2s, box-shadow .2s; }
  .lc-login-card .lc-submit:hover { transform:translateY(-2px); box-shadow:0 5px 20px rgba(0,0,0,.4); }
  .lc-back-link { text-align:center; margin-top:14px; }
  .lc-back-link a { color:var(--cyan); cursor:pointer; font-size:.9rem; }
  .lc-back-link a:hover { text-decoration:underline; }
  .lc-error { color:#ff6b6b; font-size:.85rem; text-align:center; margin-top:8px; display:none; }

  .lc-admin-header { display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:24px; }
  .lc-admin-header h2 { font-family:'Rajdhani',sans-serif; font-size:1.6rem; }
  .lc-logout-btn { padding:8px 20px; background:rgba(255,70,70,.2); border:1px solid rgba(255,70,70,.4); color:#ff6b6b; border-radius:20px; cursor:pointer; font-family:'Exo 2',sans-serif; font-weight:600; font-size:.85rem; transition:background .2s; }
  .lc-logout-btn:hover { background:rgba(255,70,70,.35); }

  .lc-create-form { display:grid; grid-template-columns:1fr 1fr; gap:12px; }
  @media(max-width:768px) { .lc-create-form { grid-template-columns:1fr; } }
  .lc-create-form .form-group { margin-bottom:0; }
  .lc-create-form .lc-submit { grid-column:1/-1; }

  .lc-student-table { width:100%; border-collapse:collapse; margin-top:16px; }
  .lc-student-table th, .lc-student-table td { padding:10px 12px; text-align:left; font-size:.85rem; border-bottom:1px solid rgba(255,255,255,.1); }
  .lc-student-table th { color:var(--gold); font-family:'Rajdhani',sans-serif; font-size:.95rem; font-weight:700; }
  .lc-student-table td img { width:36px; height:36px; border-radius:50%; object-fit:cover; border:1px solid rgba(255,255,255,.2); vertical-align:middle; }
  .lc-student-table .actions { display:flex; gap:5px; flex-wrap:wrap; }
  .lc-action-btn { padding:5px 9px; border-radius:8px; font-size:.72rem; font-weight:600; cursor:pointer; border:1px solid rgba(255,255,255,.2); font-family:'Exo 2',sans-serif; transition:opacity .2s; color:#fff; white-space:nowrap; }
  .lc-action-btn:hover { opacity:.8; }
  .lc-action-btn.link-action { background:rgba(0,255,255,.15); border-color:rgba(0,255,255,.3); }
  .lc-action-btn.msg-action  { background:rgba(255,215,0,.15); border-color:rgba(255,215,0,.3); }
  .lc-action-btn.del-action  { background:rgba(255,70,70,.15); border-color:rgba(255,70,70,.3); }
  .lc-action-btn.test-action { background:rgba(130,80,255,.2); border-color:rgba(130,80,255,.4); }
  .lc-action-btn.manage-action { background:rgba(72,255,0,.12); border-color:rgba(72,255,0,.3); }
  .lc-action-btn.reset-action { background:rgba(255,165,0,.15); border-color:rgba(255,165,0,.3); }
  .lc-empty { text-align:center; padding:30px; color:#a0aec0; font-size:.95rem; }

  /* Link expiry badge */
  .link-expiry { font-size:.7rem; color:#888; display:block; margin-top:2px; }
  .link-expiry.expired { color:#ff6b6b; }

  /* Student Dashboard */
  .lc-profile-row { display:flex; gap:20px; align-items:center; flex-wrap:wrap; }
  .lc-profile-photo { width:90px; height:90px; border-radius:50%; object-fit:cover; border:3px solid var(--cyan); }
  .lc-profile-info h3 { font-family:'Rajdhani',sans-serif; font-size:1.4rem; }
  .lc-profile-info p { font-size:.9rem; color:#a0aec0; margin-top:2px; }
  .lc-profile-badge { display:inline-block; padding:3px 10px; border-radius:12px; font-size:.75rem; font-weight:700; background:rgba(0,255,255,.15); border:1px solid rgba(0,255,255,.3); color:var(--cyan); margin-top:6px; }

  @keyframes live-glow {
    0%   { box-shadow:0 0 8px rgba(0,255,255,.3), 0 0 20px rgba(0,255,255,.1); }
    50%  { box-shadow:0 0 20px rgba(0,255,255,.6), 0 0 40px rgba(0,255,255,.25); }
    100% { box-shadow:0 0 8px rgba(0,255,255,.3), 0 0 20px rgba(0,255,255,.1); }
  }
  .lc-join-btn { display:block; width:100%; padding:18px; text-align:center; background:linear-gradient(90deg,#004e92,#00c6ff,#004e92); color:#fff; border:2px solid var(--cyan); border-radius:16px; font-family:'Rajdhani',sans-serif; font-size:1.3rem; font-weight:800; text-transform:uppercase; letter-spacing:1px; cursor:pointer; animation:live-glow 2s infinite alternate; transition:transform .2s; }
  .lc-join-btn:hover { transform:scale(1.02); }
  .lc-no-class { text-align:center; padding:28px; color:#a0aec0; }
  .lc-no-class .icon { font-size:40px; display:block; margin-bottom:8px; }

  /* Notification / message cards */
  .lc-notif-card { background:rgba(255,215,0,.08); border:1px solid rgba(255,215,0,.2); border-radius:12px; padding:14px 16px; margin-bottom:10px; }
  .lc-notif-card .time { font-size:.7rem; color:#888; margin-top:4px; }
  .lc-notif-empty { text-align:center; padding:20px; color:#a0aec0; font-size:.9rem; }

  /* Reply thread */
  .notif-with-reply { border-left:3px solid rgba(255,215,0,.3); }
  .notif-reply-box { margin-top:10px; border-top:1px solid rgba(255,255,255,.08); padding-top:10px; }
  .notif-reply-input { width:100%; background:rgba(255,255,255,.07); color:#fff; border:1px solid rgba(255,255,255,.2); border-radius:8px; padding:8px 12px; font-family:'Exo 2',sans-serif; font-size:.85rem; outline:none; resize:none; min-height:56px; }
  .notif-reply-send { margin-top:6px; padding:6px 16px; border-radius:16px; background:linear-gradient(90deg,#1e3a5f,#3b6b9e); color:#fff; border:1px solid rgba(255,255,255,.2); font-family:'Exo 2',sans-serif; font-size:.8rem; font-weight:700; cursor:pointer; }
  .reply-bubble { background:rgba(0,255,255,.08); border:1px solid rgba(0,255,255,.2); border-radius:8px; padding:8px 12px; margin-top:6px; font-size:.82rem; color:#e0e0e0; }
  .reply-bubble .reply-meta { font-size:.68rem; color:#888; margin-top:3px; }
  /* Admin reply view inside message modal */
  .student-reply-badge { display:inline-block; padding:2px 8px; border-radius:10px; font-size:.7rem; font-weight:700; background:rgba(72,255,0,.1); border:1px solid rgba(72,255,0,.25); color:#48ff00; margin-left:6px; }

  /* Tests Table */
  .tests-table { width:100%; border-collapse:collapse; margin-top:10px; }
  .tests-table th, .tests-table td { padding:10px 12px; text-align:left; font-size:.85rem; border-bottom:1px solid rgba(255,255,255,.1); }
  .tests-table th { color:var(--cyan); font-family:'Rajdhani',sans-serif; font-weight:700; font-size:.9rem; }
  .tests-table td { vertical-align:middle; }
  .test-dl-btn { display:inline-flex; align-items:center; gap:5px; padding:5px 12px; background:rgba(0,255,255,.12); border:1px solid rgba(0,255,255,.35); border-radius:20px; color:var(--cyan); font-size:.75rem; font-weight:700; font-family:'Exo 2',sans-serif; cursor:pointer; transition:background .2s; white-space:nowrap; text-decoration:none; }
  .test-dl-btn:hover { background:rgba(0,255,255,.22); }
  .marks-badge { display:inline-block; padding:3px 10px; border-radius:12px; font-size:.8rem; font-weight:700; background:rgba(255,215,0,.12); border:1px solid rgba(255,215,0,.3); color:var(--gold); }
  .marks-pending { background:rgba(255,100,100,.1); border-color:rgba(255,100,100,.3); color:#ff9999; }
  .no-tests { text-align:center; padding:20px; color:#a0aec0; font-size:.85rem; }

  /* Answer sheet submit */
  .answer-sheet-row { display:flex; align-items:center; gap:8px; margin-top:8px; flex-wrap:wrap; }
  .answer-sheet-input { flex:1; min-width:160px; background:rgba(255,255,255,.07); color:#fff; border:1px solid rgba(255,255,255,.2); border-radius:8px; padding:7px 12px; font-family:'Exo 2',sans-serif; font-size:.82rem; outline:none; }
  .answer-sheet-btn { padding:7px 14px; border-radius:16px; background:rgba(130,80,255,.2); border:1px solid rgba(130,80,255,.4); color:#c4b5fd; font-size:.78rem; font-weight:700; font-family:'Exo 2',sans-serif; cursor:pointer; white-space:nowrap; transition:background .2s; }
  .answer-sheet-btn:hover { background:rgba(130,80,255,.35); }
  .answer-sheet-link { font-size:.75rem; color:var(--cyan); display:block; margin-top:4px; word-break:break-all; }

  /* Modal overlay */
  .lc-modal-overlay { display:none; position:fixed; inset:0; background:rgba(0,0,0,.6); z-index:200; justify-content:center; align-items:center; backdrop-filter:blur(4px); }
  .lc-modal-overlay.show { display:flex; }
  .lc-modal { background:linear-gradient(135deg,#0a1628,#0f2744); border:1px solid var(--card-border); border-radius:16px; padding:28px; max-width:560px; width:90%; max-height:92vh; overflow-y:auto; }
  .lc-modal h4 { font-family:'Rajdhani',sans-serif; font-size:1.2rem; margin-bottom:16px; }
  .lc-modal .form-group { margin-bottom:12px; }
  .lc-modal-actions { display:flex; gap:10px; justify-content:flex-end; margin-top:16px; }
  .lc-modal-actions button { padding:8px 20px; border-radius:20px; font-family:'Exo 2',sans-serif; font-weight:600; font-size:.85rem; cursor:pointer; border:1px solid rgba(255,255,255,.2); color:#fff; }
  .lc-modal-actions .cancel { background:rgba(255,255,255,.1); }
  .lc-modal-actions .confirm { background:linear-gradient(90deg,#1e3a5f,#3b6b9e); }
  .lc-modal-actions .danger { background:rgba(255,70,70,.3); border-color:rgba(255,70,70,.5); }

  /* Upload status */
  .upload-status { font-size:.8rem; margin-top:6px; padding:6px 10px; border-radius:8px; display:none; }
  .upload-status.uploading { display:block; background:rgba(0,255,255,.08); color:var(--cyan); border:1px solid rgba(0,255,255,.2); }
  .upload-status.success   { display:block; background:rgba(72,255,0,.08); color:#48ff00; border:1px solid rgba(72,255,0,.2); }
  .upload-status.error     { display:block; background:rgba(255,70,70,.08); color:#ff6b6b; border:1px solid rgba(255,70,70,.2); }

  /* Manage student modal test list */
  .manage-test-row { background:rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.08); border-radius:10px; padding:12px 14px; margin-bottom:8px; }
  .manage-test-row .test-title-row { display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; }
  .manage-test-row .test-title-txt { font-weight:600; font-size:.9rem; }
  .manage-test-mark-edit { background:rgba(255,255,255,.1); color:#fff; border:1px solid rgba(255,215,0,.3); border-radius:6px; padding:5px 10px; font-size:.85rem; font-family:'Exo 2',sans-serif; outline:none; width:100px; }
  .manage-test-save-btn { padding:5px 12px; border-radius:10px; background:rgba(0,255,255,.15); border:1px solid rgba(0,255,255,.3); color:var(--cyan); font-size:.78rem; font-weight:700; cursor:pointer; font-family:'Exo 2',sans-serif; }
  .manage-test-del-btn  { padding:5px 12px; border-radius:10px; background:rgba(255,70,70,.15); border:1px solid rgba(255,70,70,.3); color:#ff6b6b; font-size:.78rem; font-weight:700; cursor:pointer; font-family:'Exo 2',sans-serif; }
  .student-answer-link-view { font-size:.75rem; color:var(--cyan); margin-top:4px; display:block; word-break:break-all; }

  /* Reset panel inside manage modal */
  .reset-panel { background:rgba(255,100,0,.07); border:1px solid rgba(255,100,0,.2); border-radius:12px; padding:16px; margin-top:16px; }
  .reset-panel h5 { font-family:'Rajdhani',sans-serif; font-size:1rem; color:#ffa366; margin-bottom:12px; }
  .reset-btn-row { display:flex; gap:8px; flex-wrap:wrap; }
  .reset-btn { padding:7px 14px; border-radius:12px; font-size:.78rem; font-weight:700; cursor:pointer; border:1px solid rgba(255,255,255,.2); color:#fff; font-family:'Exo 2',sans-serif; transition:opacity .2s; }
  .reset-btn:hover { opacity:.8; }
  .reset-btn.r-link    { background:rgba(0,255,255,.12); border-color:rgba(0,255,255,.3); }
  .reset-btn.r-tests   { background:rgba(255,70,70,.15); border-color:rgba(255,70,70,.3); }
  .reset-btn.r-notifs  { background:rgba(255,215,0,.1); border-color:rgba(255,215,0,.25); }
  .reset-btn.r-all     { background:rgba(255,50,50,.25); border-color:rgba(255,50,50,.5); }

  @media(max-width:600px) {
    .lc-student-table th:nth-child(4), .lc-student-table td:nth-child(4),
    .lc-student-table th:nth-child(5), .lc-student-table td:nth-child(5) { display:none; }
  }

  /* ══ AI CORNER STYLES (unchanged) ══ */
  @keyframes ai-glow-border {
    0%   { border-color:rgba(167,139,250,.4); box-shadow:0 0 20px rgba(109,40,217,.2), inset 0 0 20px rgba(109,40,217,.05); }
    50%  { border-color:rgba(96,165,250,.6);  box-shadow:0 0 40px rgba(59,130,246,.3), inset 0 0 30px rgba(59,130,246,.08); }
    100% { border-color:rgba(167,139,250,.4); box-shadow:0 0 20px rgba(109,40,217,.2), inset 0 0 20px rgba(109,40,217,.05); }
  }
  @keyframes float-up { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-8px)} }
  @keyframes shimmer { 0%{background-position:-200% center} 100%{background-position:200% center} }
  @keyframes particle-drift {
    0%   { transform:translateY(0) translateX(0) scale(1); opacity:.6; }
    50%  { transform:translateY(-20px) translateX(10px) scale(1.2); opacity:1; }
    100% { transform:translateY(0) translateX(0) scale(1); opacity:.6; }
  }
  @keyframes orbit { from{transform:rotate(0deg) translateX(60px) rotate(0deg)} to{transform:rotate(360deg) translateX(60px) rotate(-360deg)} }
  @keyframes pulse-ring { 0%{transform:scale(1);opacity:.8} 100%{transform:scale(1.6);opacity:0} }
  .ai-corner-hero { position:relative; overflow:hidden; background:linear-gradient(135deg,rgba(15,5,40,.95) 0%,rgba(5,15,50,.95) 50%,rgba(20,5,50,.95) 100%); border:2px solid rgba(167,139,250,.4); border-radius:28px; padding:60px 32px; text-align:center; margin:20px 0 32px; animation:ai-glow-border 5s infinite alternate; }
  .ai-corner-hero::before { content:''; position:absolute; inset:0; background:radial-gradient(ellipse at 20% 30%,rgba(109,40,217,.15) 0%,transparent 60%),radial-gradient(ellipse at 80% 70%,rgba(59,130,246,.12) 0%,transparent 60%); pointer-events:none; }
  .ai-particles { position:absolute; inset:0; pointer-events:none; overflow:hidden; }
  .ai-particle { position:absolute; width:4px; height:4px; border-radius:50%; background:var(--gold); opacity:.5; animation:particle-drift linear infinite; }
  .ai-badge { display:inline-flex; align-items:center; gap:8px; padding:6px 18px; border-radius:30px; margin-bottom:20px; background:rgba(109,40,217,.2); border:1px solid rgba(167,139,250,.4); font-size:.8rem; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:#c4b5fd; }
  .ai-badge-dot { width:8px; height:8px; border-radius:50%; background:#a78bfa; position:relative; flex-shrink:0; }
  .ai-badge-dot::after { content:''; position:absolute; inset:-4px; border-radius:50%; border:1px solid rgba(167,139,250,.5); animation:pulse-ring 1.5s ease-out infinite; }
  .ai-hero-title { font-family:'Rajdhani',sans-serif; font-weight:900; letter-spacing:-1px; font-size:clamp(2.5rem,7vw,5rem); line-height:1.1; background:linear-gradient(135deg,#fff 0%,#c4b5fd 30%,#93c5fd 60%,#ffd700 100%); background-size:200% auto; -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; animation:shimmer 4s linear infinite; margin-bottom:8px; }
  .ai-hero-sub-title { font-family:'Rajdhani',sans-serif; font-size:clamp(1rem,3vw,1.8rem); font-weight:700; color:#93c5fd; letter-spacing:2px; text-transform:uppercase; margin-bottom:20px; }
  .ai-hero-desc { font-size:clamp(.95rem,2vw,1.15rem); color:#cbd5e1; max-width:620px; margin:0 auto 36px; line-height:1.7; }
  .ai-orb-container { position:relative; width:160px; height:160px; margin:0 auto 36px; animation:float-up 4s ease-in-out infinite; }
  .ai-orb { width:160px; height:160px; border-radius:50%; background:radial-gradient(circle at 35% 35%,#c4b5fd,#7c3aed 40%,#1e1b4b 100%); box-shadow:0 0 40px rgba(124,58,237,.6),0 0 80px rgba(124,58,237,.3),inset 0 0 30px rgba(255,255,255,.1); display:flex; align-items:center; justify-content:center; font-size:64px; position:relative; }
  .ai-orb::before { content:''; position:absolute; inset:-12px; border-radius:50%; border:1px solid rgba(167,139,250,.3); animation:pulse-ring 2s ease-out infinite; }
  .ai-orb::after { content:''; position:absolute; inset:-24px; border-radius:50%; border:1px dashed rgba(147,197,253,.2); animation:orbit 8s linear infinite; }
  .orb-dot { position:absolute; width:12px; height:12px; border-radius:50%; background:var(--gold); box-shadow:0 0 10px var(--gold); top:0; left:50%; transform:translateX(-50%); animation:orbit 6s linear infinite; }
  .ai-features-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:20px; margin-bottom:40px; }
  .ai-feat-card { background:rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.08); border-radius:20px; padding:28px; text-align:left; transition:transform .3s,border-color .3s,box-shadow .3s; position:relative; overflow:hidden; }
  .ai-feat-card::before { content:''; position:absolute; inset:0; border-radius:20px; background:linear-gradient(135deg,rgba(109,40,217,.08),transparent); opacity:0; transition:opacity .3s; }
  .ai-feat-card:hover { transform:translateY(-6px); border-color:rgba(167,139,250,.4); box-shadow:0 12px 40px rgba(109,40,217,.2); }
  .ai-feat-card:hover::before { opacity:1; }
  .ai-feat-icon { font-size:2.5rem; margin-bottom:14px; display:block; }
  .ai-feat-title { font-family:'Rajdhani',sans-serif; font-size:1.3rem; font-weight:800; margin-bottom:8px; color:#e2e8f0; }
  .ai-feat-desc { font-size:.9rem; color:#94a3b8; line-height:1.6; }
  .ai-feat-tag { display:inline-block; padding:3px 10px; border-radius:20px; font-size:.7rem; font-weight:700; margin-top:12px; text-transform:uppercase; letter-spacing:1px; background:rgba(250,204,21,.1); border:1px solid rgba(250,204,21,.3); color:#fbbf24; }
  .ai-stats { display:flex; justify-content:center; gap:40px; flex-wrap:wrap; margin-bottom:40px; }

  /* ══ DOWNLOADS PAGE ══ */
  .dl-filter-bar { display:flex; gap:12px; flex-wrap:wrap; margin-bottom:24px; align-items:flex-end; }
  .dl-filter-group { display:flex; flex-direction:column; gap:6px; flex:1; min-width:160px; }
  .dl-filter-group label { font-size:.85rem; color:#a0aec0; font-weight:600; text-transform:uppercase; letter-spacing:1px; }
  .dl-filter-group select { background:rgba(255,255,255,.1); color:#fff; border:1px solid rgba(255,255,255,.3); border-radius:10px; padding:10px 14px; font-size:.9rem; font-family:'Exo 2',sans-serif; outline:none; cursor:pointer; }
  .dl-filter-group select option { background:#1e3a5f; }
  .dl-filter-reset { padding:10px 20px; background:rgba(255,255,255,.08); border:1px solid rgba(255,255,255,.2); border-radius:10px; color:#a0aec0; cursor:pointer; font-family:'Exo 2',sans-serif; font-size:.9rem; align-self:flex-end; transition:background .2s; }
  .dl-filter-reset:hover { background:rgba(255,255,255,.15); }
  .dl-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(300px,1fr)); gap:18px; }
  .dl-card { background:rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.09); border-radius:16px; padding:20px; transition:transform .25s,border-color .25s,box-shadow .25s; }
  .dl-card:hover { transform:translateY(-4px); border-color:rgba(0,255,255,.35); box-shadow:0 10px 30px rgba(0,0,0,.35); }
  .dl-card-top { display:flex; gap:12px; align-items:flex-start; margin-bottom:14px; }
  .dl-card-icon { font-size:2rem; flex-shrink:0; }
  .dl-card-title { font-weight:700; font-size:.95rem; color:#e2e8f0; margin-bottom:4px; }
  .dl-card-meta { font-size:.78rem; color:#64748b; }
  .dl-badge { display:inline-block; padding:2px 8px; border-radius:10px; font-size:.7rem; font-weight:700; text-transform:uppercase; letter-spacing:.8px; margin-right:4px; }
  .dl-badge-board { background:rgba(255,215,0,.1); border:1px solid rgba(255,215,0,.25); color:var(--gold); }
  .dl-badge-class { background:rgba(0,255,255,.08); border:1px solid rgba(0,255,255,.25); color:var(--cyan); }
  .dl-badge-subject { background:rgba(167,139,250,.1); border:1px solid rgba(167,139,250,.3); color:#c4b5fd; }
  .dl-btn { display:inline-flex; align-items:center; gap:6px; padding:8px 18px; background:linear-gradient(90deg,#1e3a5f,#3b6b9e,#1e3a5f); border:1px solid rgba(0,255,255,.3); border-radius:20px; color:var(--cyan); font-family:'Exo 2',sans-serif; font-size:.82rem; font-weight:700; cursor:pointer; text-decoration:none; transition:background .2s,box-shadow .2s; }
  .dl-btn:hover { box-shadow:0 0 14px rgba(0,255,255,.3); }
  .dl-empty { text-align:center; padding:50px 20px; color:#a0aec0; grid-column:1/-1; }
  .dl-empty span { font-size:3rem; display:block; margin-bottom:12px; }

  /* Admin public downloads section */
  .pub-dl-form { display:grid; grid-template-columns:1fr 1fr; gap:12px; }
  @media(max-width:768px) { .pub-dl-form { grid-template-columns:1fr; } }
  .pub-dl-form .lc-submit { grid-column:1/-1; }
  .pub-dl-table { width:100%; border-collapse:collapse; margin-top:16px; }
  .pub-dl-table th,.pub-dl-table td { padding:10px 12px; text-align:left; font-size:.85rem; border-bottom:1px solid rgba(255,255,255,.1); }
  .pub-dl-table th { color:var(--gold); font-family:'Rajdhani',sans-serif; font-size:.9rem; font-weight:700; }
  .pub-dl-table td a { color:var(--cyan); font-size:.8rem; word-break:break-all; }

  /* Private study notes */
  .notes-form { display:grid; grid-template-columns:1fr 1fr; gap:12px; }
  @media(max-width:600px) { .notes-form { grid-template-columns:1fr; } }
  .notes-form .lc-submit { grid-column:1/-1; }
  .notes-list { margin-top:14px; display:flex; flex-direction:column; gap:10px; }
  .note-item { background:rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.09); border-radius:12px; padding:12px 16px; display:flex; align-items:center; justify-content:space-between; gap:10px; flex-wrap:wrap; }
  .note-item-info { flex:1; }
  .note-item-subject { font-size:.75rem; font-weight:700; color:#c4b5fd; text-transform:uppercase; letter-spacing:.8px; margin-bottom:2px; }
  .note-item-title { font-size:.9rem; font-weight:600; color:#e2e8f0; }
  .note-item-date { font-size:.72rem; color:#64748b; margin-top:2px; }
  .note-dl-btn { display:inline-flex; align-items:center; gap:5px; padding:6px 14px; background:rgba(167,139,250,.15); border:1px solid rgba(167,139,250,.3); border-radius:16px; color:#c4b5fd; font-size:.78rem; font-weight:700; font-family:'Exo 2',sans-serif; text-decoration:none; transition:background .2s; white-space:nowrap; }
  .note-dl-btn:hover { background:rgba(167,139,250,.28); }
  .note-del-btn { padding:5px 10px; border-radius:10px; background:rgba(255,70,70,.15); border:1px solid rgba(255,70,70,.3); color:#ff6b6b; font-size:.75rem; font-weight:700; cursor:pointer; font-family:'Exo 2',sans-serif; }

  /* Student dash study notes */
  .sn-subject-section { margin-bottom:20px; }
  .sn-subject-label { font-family:'Rajdhani',sans-serif; font-size:1rem; font-weight:700; color:#a0aec0; text-transform:uppercase; letter-spacing:1.5px; margin-bottom:10px; display:flex; align-items:center; gap:8px; }
  .sn-subject-label::after { content:''; flex:1; height:1px; background:linear-gradient(to right,rgba(255,255,255,.12),transparent); }
  .sn-card { background:rgba(167,139,250,.06); border:1px solid rgba(167,139,250,.18); border-radius:12px; padding:12px 16px; display:flex; align-items:center; justify-content:space-between; gap:10px; margin-bottom:8px; flex-wrap:wrap; }
  .sn-card-info { flex:1; }
  .sn-card-title { font-weight:600; font-size:.9rem; color:#e2e8f0; }
  .sn-card-date { font-size:.72rem; color:#64748b; margin-top:2px; }
  .sn-empty { text-align:center; padding:30px; color:#a0aec0; font-size:.9rem; }
  .ai-stat { text-align:center; }
  .ai-stat-val { font-family:'Rajdhani',sans-serif; font-size:2.4rem; font-weight:900; line-height:1; background:linear-gradient(to right,#fbbf24,#f59e0b); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
  .ai-stat-lbl { font-size:.8rem; color:#64748b; text-transform:uppercase; letter-spacing:1px; margin-top:4px; }
  @keyframes launch-pulse { 0%{box-shadow:0 0 0 0 rgba(124,58,237,.7)} 70%{box-shadow:0 0 0 18px rgba(124,58,237,0)} 100%{box-shadow:0 0 0 0 rgba(124,58,237,0)} }
  .ai-launch-btn { display:inline-flex; align-items:center; gap:12px; padding:18px 48px; border-radius:50px; background:linear-gradient(135deg,#7c3aed,#4f46e5,#0ea5e9); background-size:200% auto; color:#fff; border:none; cursor:pointer; font-family:'Rajdhani',sans-serif; font-size:1.4rem; font-weight:800; letter-spacing:1.5px; text-transform:uppercase; transition:background-position .5s,transform .25s; animation:launch-pulse 2.5s infinite; text-decoration:none; position:relative; z-index:1; }
  .ai-launch-btn:hover { background-position:right center; transform:translateY(-3px) scale(1.04); color:#fff; }
  .ai-launch-btn .btn-icon { font-size:1.6rem; animation:float-up 2s ease-in-out infinite; }
  .ai-divider { width:100%; height:1px; margin:32px 0; background:linear-gradient(90deg,transparent,rgba(167,139,250,.4),transparent); }
  @keyframes marquee { from{transform:translateX(0)} to{transform:translateX(-50%)} }
  .ai-marquee-wrap { overflow:hidden; margin:28px 0; }
  .ai-marquee-track { display:flex; gap:24px; animation:marquee 20s linear infinite; width:max-content; }
  .ai-marquee-item { background:rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.08); border-radius:12px; padding:12px 22px; white-space:nowrap; font-size:.9rem; color:#cbd5e1; }
  .ai-marquee-item strong { color:#fbbf24; }

  /* ══════════════════════════════════════════════════════════
     ABOUT US PAGE STYLES
  ══════════════════════════════════════════════════════════ */

  /* Sub-tab navigation */
  .about-tab-bar{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-bottom:44px;}
  .about-tab{
    padding:11px 30px;border-radius:30px;cursor:pointer;
    font-family:'Exo 2',sans-serif;font-weight:700;font-size:.92rem;
    border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.04);
    color:#94a3b8;transition:all .25s;letter-spacing:.3px;
  }
  .about-tab:hover{border-color:rgba(255,215,0,.4);color:#fff;}
  .about-tab.at-active{
    background:rgba(255,215,0,.1);border-color:rgba(255,215,0,.5);
    color:var(--gold);box-shadow:0 0 24px rgba(255,215,0,.15);
  }
  .about-panel{display:none;animation:fadeInUp .4s ease-out;}
  .about-panel.ap-active{display:block;}

  /* ── Keyframes ── */
  @keyframes photo-float{0%,100%{transform:translateY(0) rotate(-1.5deg);}50%{transform:translateY(-12px) rotate(1.5deg);}}
  @keyframes tutor-border{
    0%  {border-color:rgba(255,215,0,.35);box-shadow:0 0 40px rgba(255,215,0,.1);}
    50% {border-color:rgba(0,255,255,.45); box-shadow:0 0 60px rgba(0,255,255,.15);}
    100%{border-color:rgba(255,215,0,.35);box-shadow:0 0 40px rgba(255,215,0,.1);}
  }
  @keyframes aya-border{
    0%  {border-color:rgba(167,139,250,.4);box-shadow:0 0 40px rgba(109,40,217,.2);}
    50% {border-color:rgba(96,165,250,.5); box-shadow:0 0 70px rgba(59,130,246,.25);}
    100%{border-color:rgba(167,139,250,.4);box-shadow:0 0 40px rgba(109,40,217,.2);}
  }
  @keyframes stat-glow{0%,100%{text-shadow:0 0 10px rgba(255,215,0,.4);}50%{text-shadow:0 0 30px rgba(255,215,0,.9),0 0 60px rgba(255,215,0,.4);}}
  @keyframes aya-pulse{0%,100%{transform:scale(1);opacity:.85;}50%{transform:scale(1.12);opacity:1;}}
  @keyframes orb-ring{from{transform:rotate(0deg) translateX(58px) rotate(0deg);}to{transform:rotate(360deg) translateX(58px) rotate(-360deg);}}
  @keyframes shimmer-text{0%{background-position:-200% center;}100%{background-position:200% center;}}

  /* ── Tutor hero card ── */
  .tutor-hero{
    position:relative;overflow:hidden;border-radius:28px;
    background:linear-gradient(135deg,rgba(0,4,40,.97),rgba(0,18,55,.95),rgba(0,4,40,.97));
    border:2px solid rgba(255,215,0,.35);padding:50px 44px;margin-bottom:40px;
    animation:tutor-border 7s infinite alternate;
  }
  .tutor-hero::before{
    content:'';position:absolute;inset:0;pointer-events:none;
    background:
      radial-gradient(ellipse at 8% 50%,rgba(255,215,0,.07) 0%,transparent 55%),
      radial-gradient(ellipse at 92% 30%,rgba(0,255,255,.06) 0%,transparent 55%);
  }
  .tutor-inner{position:relative;z-index:1;display:flex;gap:48px;align-items:flex-start;flex-wrap:wrap;}

  /* Photo column */
  .tutor-photo-col{flex:0 0 200px;display:flex;flex-direction:column;align-items:center;gap:14px;}
  .tutor-photo-ring{
    width:200px;height:200px;border-radius:50%;
    background:linear-gradient(135deg,var(--gold),var(--cyan),var(--gold));
    padding:3px;animation:photo-float 5.5s ease-in-out infinite;flex-shrink:0;
  }
  .tutor-photo-ring img{
    width:100%;height:100%;border-radius:50%;object-fit:cover;object-position:center top;
    border:3px solid rgba(0,4,40,.8);display:block;
  }
  .tutor-verified{
    display:inline-flex;align-items:center;gap:5px;padding:4px 13px;
    border-radius:20px;background:rgba(72,255,0,.1);border:1px solid rgba(72,255,0,.3);
    color:#48ff00;font-size:.7rem;font-weight:800;text-transform:uppercase;letter-spacing:1px;
  }

  /* Info column */
  .tutor-info-col{flex:1;min-width:260px;}
  .tutor-eyebrow{font-size:.72rem;font-weight:800;color:var(--cyan);text-transform:uppercase;letter-spacing:3px;margin-bottom:7px;}
  .tutor-name{
    font-family:'Rajdhani',sans-serif;font-size:clamp(1.9rem,5vw,3rem);font-weight:900;
    background:linear-gradient(135deg,#fff 0%,var(--gold) 50%,var(--cyan) 100%);
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;
    line-height:1.1;margin-bottom:5px;
  }
  .tutor-role{font-size:1rem;color:#94a3b8;margin-bottom:18px;font-weight:300;letter-spacing:.4px;}
  .tutor-tagline{
    font-family:'Rajdhani',sans-serif;font-size:1.12rem;font-weight:700;
    color:rgba(255,255,255,.8);font-style:italic;
    border-left:3px solid var(--gold);padding-left:16px;
    margin-bottom:26px;line-height:1.55;
  }

  /* Credentials list */
  .cred-list{list-style:none;display:flex;flex-direction:column;gap:9px;margin-bottom:26px;}
  .cred-item{display:flex;align-items:flex-start;gap:11px;font-size:.88rem;color:#cbd5e1;}
  .cred-ico{font-size:1.05rem;flex-shrink:0;margin-top:1px;}
  .cred-main{display:block;font-weight:700;color:#fff;font-size:.9rem;}
  .cred-sub{display:block;color:#64748b;font-size:.78rem;}

  /* Stats pills */
  .tutor-stats{display:flex;gap:14px;flex-wrap:wrap;}
  .stat-pill{
    background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);
    border-radius:12px;padding:12px 16px;text-align:center;flex:1;min-width:80px;
  }
  .stat-num{
    font-family:'Rajdhani',sans-serif;font-size:1.55rem;font-weight:900;display:block;line-height:1;
    background:linear-gradient(to right,var(--gold),var(--cyan));
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;
    animation:stat-glow 3.5s ease-in-out infinite;
  }
  .stat-lbl{font-size:.65rem;color:#64748b;text-transform:uppercase;letter-spacing:.7px;margin-top:3px;}

  /* Industry tags */
  .industry-tags{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0;}
  .ind-tag{
    display:inline-flex;align-items:center;gap:6px;padding:5px 13px;border-radius:16px;
    background:rgba(0,255,255,.07);border:1px solid rgba(0,255,255,.18);
    color:var(--cyan);font-size:.75rem;font-weight:700;
  }

  /* Story journey */
  .journey-grid{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:36px;}
  @media(max-width:760px){
    .journey-grid{grid-template-columns:1fr;}
    .tutor-inner{flex-direction:column;align-items:center;}
    .tutor-photo-col{flex:0 0 auto;}
    .aya-hero-wrap{padding:36px 20px;}
    .aya-feat-grid{grid-template-columns:1fr;}
    .phil-row{grid-template-columns:1fr;}
  }
  .journey-card{
    background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);
    border-radius:18px;padding:24px;position:relative;overflow:hidden;
    transition:transform .3s,border-color .3s;
  }
  .journey-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,rgba(255,215,0,.45),transparent);}
  .journey-card:hover{transform:translateY(-5px);border-color:rgba(255,215,0,.22);}
  .journey-icon{font-size:2rem;margin-bottom:12px;display:block;}
  .journey-card h3{font-family:'Rajdhani',sans-serif;font-size:1.18rem;font-weight:800;color:var(--gold);margin-bottom:9px;}
  .journey-card p{font-size:.87rem;color:#94a3b8;line-height:1.75;}

  /* Timeline */
  .tl-wrap{position:relative;padding-left:30px;margin-bottom:36px;}
  .tl-wrap::before{content:'';position:absolute;left:5px;top:6px;bottom:0;width:2px;background:linear-gradient(to bottom,var(--gold),var(--cyan),rgba(255,255,255,.08));border-radius:2px;}
  .tl-item{position:relative;margin-bottom:24px;}
  .tl-dot{position:absolute;left:-27px;top:5px;width:12px;height:12px;border-radius:50%;background:var(--gold);border:2px solid rgba(0,4,40,1);box-shadow:0 0 12px rgba(255,215,0,.7);}
  .tl-year{font-size:.7rem;font-weight:800;color:var(--cyan);text-transform:uppercase;letter-spacing:1.2px;margin-bottom:2px;}
  .tl-title{font-family:'Rajdhani',sans-serif;font-size:1rem;font-weight:800;color:#e2e8f0;margin-bottom:3px;}
  .tl-desc{font-size:.83rem;color:#64748b;line-height:1.6;}

  /* Proof / success cards */
  .proof-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:18px;margin-bottom:36px;}
  .proof-card{
    background:linear-gradient(135deg,rgba(255,215,0,.06),rgba(0,255,255,.03));
    border:1px solid rgba(255,215,0,.2);border-radius:14px;padding:22px;
    transition:transform .3s,box-shadow .3s;
  }
  .proof-card:hover{transform:translateY(-5px);box-shadow:0 12px 32px rgba(255,215,0,.1);}
  .proof-pct{
    font-family:'Rajdhani',sans-serif;font-size:2.8rem;font-weight:900;line-height:1;
    background:linear-gradient(to right,var(--gold),#fff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;
    margin-bottom:3px;
  }
  .proof-label{font-size:.85rem;color:#e2e8f0;font-weight:700;margin-bottom:3px;}
  .proof-detail{font-size:.76rem;color:#64748b;margin-bottom:8px;}
  .proof-tag{display:inline-flex;align-items:center;gap:4px;padding:3px 10px;border-radius:10px;background:rgba(72,255,0,.1);border:1px solid rgba(72,255,0,.2);color:#48ff00;font-size:.7rem;font-weight:800;}

  /* ── AyA Hero ── */
  .aya-hero-wrap{
    position:relative;overflow:hidden;border-radius:28px;
    background:linear-gradient(135deg,rgba(8,2,28,.98),rgba(4,8,48,.96),rgba(12,2,32,.98));
    border:2px solid rgba(167,139,250,.4);padding:56px 44px;margin-bottom:40px;
    animation:aya-border 5s infinite alternate;text-align:center;
  }
  .aya-hero-wrap::before{
    content:'';position:absolute;inset:0;pointer-events:none;
    background:
      radial-gradient(ellipse at 20% 40%,rgba(109,40,217,.18) 0%,transparent 60%),
      radial-gradient(ellipse at 80% 60%,rgba(59,130,246,.14) 0%,transparent 60%);
  }
  .aya-inner{position:relative;z-index:1;}
  .aya-orb-wrap{position:relative;width:140px;height:140px;margin:0 auto 28px;}
  .aya-orb{
    width:140px;height:140px;border-radius:50%;
    background:radial-gradient(circle at 35% 35%,#c4b5fd,#7c3aed 40%,#1e1b4b 100%);
    box-shadow:0 0 40px rgba(124,58,237,.7),0 0 90px rgba(124,58,237,.3);
    display:flex;align-items:center;justify-content:center;font-size:56px;
    animation:aya-pulse 3s ease-in-out infinite;position:relative;
  }
  .aya-orb::after{
    content:'';position:absolute;inset:-15px;border-radius:50%;
    border:1px dashed rgba(167,139,250,.35);
    animation:orb-ring 9s linear infinite;
  }
  .aya-title{
    font-family:'Rajdhani',sans-serif;font-weight:900;font-size:clamp(2.4rem,6vw,4.2rem);
    background:linear-gradient(135deg,#fff 0%,#c4b5fd 30%,#93c5fd 60%,#ffd700 100%);
    background-size:200% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;
    animation:shimmer-text 4s linear infinite;line-height:1.05;margin-bottom:5px;
  }
  .aya-sub{font-family:'Rajdhani',sans-serif;font-size:1.2rem;color:#93c5fd;letter-spacing:2px;text-transform:uppercase;margin-bottom:14px;}
  .aya-tagline{font-size:.98rem;color:#cbd5e1;max-width:540px;margin:0 auto 32px;line-height:1.75;}

  .aya-feat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;margin-bottom:32px;text-align:left;}
  .aya-feat{
    background:rgba(255,255,255,.04);border:1px solid rgba(167,139,250,.15);
    border-radius:14px;padding:20px;transition:transform .3s,border-color .3s;
  }
  .aya-feat:hover{transform:translateY(-5px);border-color:rgba(167,139,250,.4);}
  .aya-feat-ico{font-size:1.7rem;margin-bottom:9px;display:block;}
  .aya-feat-title{font-family:'Rajdhani',sans-serif;font-size:1rem;font-weight:800;color:#e2e8f0;margin-bottom:5px;}
  .aya-feat-desc{font-size:.83rem;color:#64748b;line-height:1.6;}
  .aya-free{
    display:inline-flex;align-items:center;gap:8px;padding:10px 26px;border-radius:30px;
    background:linear-gradient(135deg,rgba(109,40,217,.28),rgba(59,130,246,.18));
    border:1px solid rgba(167,139,250,.38);color:#c4b5fd;
    font-family:'Rajdhani',sans-serif;font-size:1.05rem;font-weight:800;
    letter-spacing:1px;text-transform:uppercase;
  }

  /* Philosophy row */
  .phil-row{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:36px;}
  .phil-block{
    background:rgba(255,255,255,.03);border:1px solid rgba(167,139,250,.14);
    border-radius:14px;padding:22px;
  }
  .phil-block h3{font-family:'Rajdhani',sans-serif;font-size:1.1rem;color:#c4b5fd;margin-bottom:10px;}
  .phil-block p,.phil-block li{font-size:.86rem;color:#94a3b8;line-height:1.72;}
  .phil-block ul{padding-left:17px;margin-top:6px;}
  .phil-block li{margin-bottom:5px;}

  /* Section headers inside About */
  .about-section-head{margin:36px 0 18px;}
  .about-section-head h2{
    font-family:'Rajdhani',sans-serif;font-size:1.65rem;font-weight:900;
    background:linear-gradient(to right,#fff,var(--gold));
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;
    margin-bottom:4px;
  }
  .about-section-head p{font-size:.87rem;color:#64748b;}

  /* FAQ */
  .faq-list{margin-bottom:40px;}
  .faq-item{
    background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);
    border-radius:13px;margin-bottom:10px;overflow:hidden;transition:border-color .25s;
  }
  .faq-item:hover{border-color:rgba(255,215,0,.22);}
  .faq-item[open]{border-color:rgba(255,215,0,.3);background:rgba(255,215,0,.04);}
  .faq-item summary{
    cursor:pointer;padding:17px 20px;
    font-family:'Rajdhani',sans-serif;font-size:1.03rem;font-weight:700;
    color:#e2e8f0;list-style:none;display:flex;justify-content:space-between;align-items:center;gap:12px;
  }
  .faq-item summary::-webkit-details-marker{display:none;}
  .faq-item summary::after{content:'＋';color:var(--gold);font-size:1.05rem;flex-shrink:0;transition:transform .3s;}
  .faq-item[open] summary::after{transform:rotate(45deg);}
  .faq-item[open] summary{color:var(--gold);}
  .faq-body{padding:2px 20px 17px;font-size:.88rem;color:#94a3b8;line-height:1.78;}
  .faq-body strong{color:#e2e8f0;}
  .faq-body a{color:var(--cyan);}

</style>

<!-- Supabase JS v2 CDN -->
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script>
  const SUPABASE_URL   = 'https://nhfgfraqhbkmtfmhdgvp.supabase.co';
  const SUPABASE_ANON  = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5oZmdmcmFxaGJrbXRmbWhkZ3ZwIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3MjA3MTU4OSwiZXhwIjoyMDg3NjQ3NTg5fQ.R67RTCJ7DL5t6xeeXYPKSsi_5f0oBccb9TUjDxKIUiU';
  const STUDENTS_TABLE = 'students';
  const AVATARS_BUCKET = 'avatars';
  const TESTS_BUCKET   = 'test_papers';
  const PUB_DL_TABLE   = 'public_downloads';

  let _supabase = null;
  function getSupabase() {
    if (!_supabase) {
      if (typeof supabase === 'undefined') throw new Error('Supabase SDK failed to load.');
      _supabase = supabase.createClient(SUPABASE_URL, SUPABASE_ANON);
    }
    return _supabase;
  }

  // ══ EARLY GLOBAL FUNCTIONS — defined here so inline onclick handlers in the
  //    body always find them, regardless of Cloudflare script injection order ══

  function showPage(id, btn) {
    document.querySelectorAll('.page').forEach(function(p){ p.classList.add('hidden'); });
    document.querySelectorAll('.nav-btn').forEach(function(b){ b.classList.remove('active'); });
    var el = document.getElementById('page-' + id);
    if (el) el.classList.remove('hidden');
    if (btn) btn.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
    if (id === 'downloads') { try { renderDownloads(); } catch(e) {} }
  }

  function showBoard(val) {
    document.querySelectorAll('.board-panel').forEach(function(p){ p.classList.remove('active'); });
    var map = {'':'board-default','ib':'board-ib','cbse':'board-cbse','icse':'board-icse','state':'board-state'};
    var el = document.getElementById(map[val] || 'board-default');
    if (el) el.classList.add('active');
  }

  function switchTestiTab(panel, btn) {
    document.querySelectorAll('.testi-panel').forEach(function(p){ p.classList.remove('active'); });
    document.querySelectorAll('.testi-tab').forEach(function(t){ t.classList.remove('active-tab'); });
    var el = document.getElementById('testi-' + panel);
    if (el) el.classList.add('active');
    if (btn) btn.classList.add('active-tab');
  }
</script>
</head>
<body>

<div class="container" style="padding-top:24px;">
  <div class="founder-header">
    <div class="founder-headline">Other Apps Were Coded by Engineers. This One Was Coded by Your Master Tutor - Mohammed Salmaan.</div>
    <div class="founder-subhead">The only online coaching service in the world running on a proprietary AI engine built by the Founder.</div>
    <div class="founder-tagline">Pure Teaching Intelligence. Zero Corporate Noise.</div>
  </div>
  <div style="margin-bottom:6px;"><p style="font-size:1rem; font-weight:700; margin-bottom:10px;">🧭 Main Menu</p></div>
</div>

<nav>
  <div class="nav-inner">
    <button class="nav-btn active" onclick="showPage('home',this)">🏠 Home</button>
    <button class="nav-btn" onclick="showPage('services',this)">📚 Services</button>
    <button class="nav-btn" onclick="showPage('testimonials',this)">💬 Testimonials</button>
    <button class="nav-btn" onclick="showPage('bootcamp',this)">🐍 Bootcamp</button>
    <button class="nav-btn" onclick="showPage('contact',this)">📞 Contact</button>
    <button class="nav-btn" onclick="showPage('live-class',this)">🔴 Login</button>
    <button class="nav-btn" onclick="showPage('downloads',this)">⬇️ Downloads</button>
    <button class="nav-btn" onclick="showPage('about',this)">👤 About Us</button>
    <button class="nav-btn ai-nav" onclick="showPage('ai-corner',this)">🤖 AI Corner</button>
  </div>
</nav>
<hr class="divider" style="margin:0; opacity:.3;">

<!-- ════ PAGE: HOME ════ -->
<div id="page-home" class="page">
<div class="container">
  <div class="hero-logo-row" style="margin-bottom:24px;">
    <div class="logo-box"><img src="logo.png" alt="The Molecular Man Logo" style="width:100%;height:100%;object-fit:contain;"></div>
    <div class="logo-info">
      <h1>Expert Tuition for Excellence 🎓</h1>
      <h3>Personalized coaching in Mathematics, Physics, Chemistry &amp; Biology</h3>
      <p>For Classes 6-12 &amp; Competitive Exams (NEET/JEE/Boards)</p>
      <a href="https://wa.me/917339315376" target="_blank" class="link-btn">📱 Book Free Trial</a>
    </div>
  </div>
  <div class="hero-ad">
    <div class="hero-ad-headline">🚨 The Education System Just Got a Reality Check</div>
    <div class="hero-ad-sub">Stop paying for "premium" test series. The corporate coaching giants are scared.</div>
    <div class="hero-suite-title">INTRODUCING: THE MOLECULAR MAN AI SUITE</div>
    <div class="hero-feature-grid">
      <div class="hero-feature-item"><div class="title">1. 🧠 AyA-AI(Beta)</div><div class="desc">She doesn't sleep. She answers instantly 24/7 × 365.</div></div>
      <div class="hero-feature-item"><div class="title">2. 📝 Infinite Mock Tests(Beta)</div><div class="desc">Generate unlimited tests for ANY Board/Subject for ₹0.</div></div>
    </div>
    <div class="hero-footer">🚫 NO SUBSCRIPTIONS. NO HIDDEN FEES. PURE TEACHING INTELLIGENCE.</div>
  </div>
  <h2 class="section-title">📊 Our Impact</h2>
  <div class="grid-4" style="margin-bottom:32px;">
    <div class="gcard metric"><div class="metric-value">500+</div><div class="metric-label">Students Taught</div></div>
    <div class="gcard metric"><div class="metric-value">100%</div><div class="metric-label">Success Rate</div></div>
    <div class="gcard metric"><div class="metric-value">24/7</div><div class="metric-label">Support</div></div>
    <div class="gcard metric"><div class="metric-value">5+ Yrs</div><div class="metric-label">Experience</div></div>
  </div>
  <h2 class="section-title">🎯 What We Offer</h2>
  <div class="grid-3" style="margin-bottom:32px;">
    <div class="gcard"><h4 style="font-family:'Rajdhani',sans-serif;font-size:1.1rem;margin-bottom:8px;">👨‍🏫 Expert Tutoring</h4><p style="color:#c0cfe0;font-size:.9rem;">One-on-one and small group classes for Classes 6-12.</p></div>
    <div class="gcard"><h4 style="font-family:'Rajdhani',sans-serif;font-size:1.1rem;margin-bottom:8px;">📚 Comprehensive Material</h4><p style="color:#c0cfe0;font-size:.9rem;">Access to curated notes, practice problems, and revision guides.</p></div>
    <div class="gcard"><h4 style="font-family:'Rajdhani',sans-serif;font-size:1.1rem;margin-bottom:8px;">🐍 Python Bootcamp</h4><p style="color:#c0cfe0;font-size:.9rem;">Weekend intensive courses in Data Science &amp; AI.</p></div>
  </div>
  <h2 class="section-title">💡 Why Parents Trust Us</h2>
  <div class="grid-3" style="margin-bottom:32px;">
    <div class="wcard"><h3>🎓 Expert Educator</h3><p>One-on-one mentoring that identifies specific learning gaps.</p></div>
    <div class="wcard"><h3>🧠 Conceptual</h3><p>No rote memorization. We focus on "Why" and "How".</p></div>
    <div class="wcard"><h3>💰 Fair Pricing</h3><p>No hidden fees. Quality education for every family.</p></div>
  </div>
  <div class="btn-center"><a href="https://wa.me/917339315376" target="_blank" class="link-btn">📱 Book Free Trial</a></div>
</div>
</div>

<!-- ════ PAGE: SERVICES ════ -->
<div id="page-services" class="page hidden">
<div class="container">
  <h1 class="section-title">📚 Our Services</h1>
  <h2 class="section-title" style="font-size:1.4rem;">🎓 Subjects We Teach</h2>
  <p style="margin-bottom:16px; color:#c0cfe0;">Select your board below to see the subjects and classes we cover:</p>
  <div class="board-select-wrap">
    <label>🏫 Choose Your Board</label>
    <select id="boardSelect" onchange="showBoard(this.value)">
      <option value="">-- Select a Board --</option>
      <option value="ib">IB &amp; IGCSE</option>
      <option value="cbse">CBSE</option>
      <option value="icse">ICSE / ISC</option>
      <option value="state">State Board</option>
    </select>
  </div>
  <div id="board-default" class="board-panel active"><div class="board-prompt"><span>🎓</span><p>Select your board above to explore the subjects and classes we cover.</p></div></div>
  <div id="board-ib" class="board-panel">
    <h3 style="font-family:'Rajdhani',sans-serif;font-size:1.4rem;margin-bottom:16px;">🌍 IB &amp; IGCSE Curriculum</h3>
    <div class="grid-2">
      <div class="wcard"><h3>📘 Classes 6 – 10</h3><ul><li>📐 Mathematics</li><li>⚡ Physics</li><li>⚗️ Chemistry</li><li>🧬 Biology</li></ul></div>
      <div class="wcard"><h3>📗 Classes 11 – 12 (Higher Level)</h3><ul><li>⚡ Physics</li><li>⚗️ Chemistry</li><li>📐 Mathematics <span style="color:#666;font-size:.8rem;">(or)</span> 🧬 Biology</li></ul><p style="margin-top:10px;">✏️ <em>Choose Math or Biology based on your stream.</em></p></div>
    </div>
  </div>
  <div id="board-cbse" class="board-panel">
    <h3 style="font-family:'Rajdhani',sans-serif;font-size:1.4rem;margin-bottom:16px;">🇮🇳 CBSE Curriculum</h3>
    <div class="grid-2">
      <div class="wcard"><h3>📘 Classes 6 – 10</h3><ul><li>🔬 Science<ul style="padding-left:16px;font-size:.85rem;color:#555;"><li>Physics</li><li>Chemistry</li><li>Biology (combined)</li></ul></li><li style="margin-top:6px;">📐 Mathematics<ul style="padding-left:16px;font-size:.85rem;color:#555;"><li>Standard</li><li>Basic</li></ul></li></ul></div>
      <div class="wcard"><h3>📗 Classes 11 – 12</h3><p style="color:#666 !important;font-size:.85rem;margin-bottom:4px;">PCM Stream</p><ul><li>⚡ Physics</li><li>⚗️ Chemistry</li><li>📐 Mathematics</li></ul><p style="color:#666 !important;font-size:.85rem;margin:12px 0 4px;">PCB Stream</p><ul><li>⚡ Physics</li><li>⚗️ Chemistry</li><li>🧬 Biology</li></ul></div>
    </div>
  </div>
  <div id="board-icse" class="board-panel">
    <h3 style="font-family:'Rajdhani',sans-serif;font-size:1.4rem;margin-bottom:16px;">📋 ICSE / ISC Curriculum</h3>
    <div class="grid-2">
      <div class="wcard"><h3>📘 Class 10 (ICSE)</h3><ul><li>📐 Mathematics</li><li>⚡ Physics</li><li>⚗️ Chemistry</li><li>🧬 Biology</li></ul></div>
      <div class="wcard"><h3>📗 Classes 11 – 12 (ISC)</h3><ul><li>⚡ Physics</li><li>⚗️ Chemistry</li><li>📐 Mathematics <span style="color:#666;font-size:.8rem;">(or)</span> 🧬 Biology</li></ul><p style="margin-top:10px;">✏️ <em>Subject choice depends on your stream selection.</em></p></div>
    </div>
  </div>
  <div id="board-state" class="board-panel">
    <h3 style="font-family:'Rajdhani',sans-serif;font-size:1.4rem;margin-bottom:16px;">🏛️ State Board Curriculum</h3>
    <div class="grid-2">
      <div class="wcard"><h3>📘 Classes 6 – 10</h3><ul><li>📐 Mathematics</li><li>🔬 Science (Combined: Physics, Chemistry &amp; Biology)</li></ul></div>
      <div class="wcard"><h3>📗 Classes 11 – 12 (Groups)</h3><p style="color:#555 !important;font-size:.85rem;font-weight:700;margin-bottom:4px;">Group 1</p><ul><li>⚡ Physics &nbsp;⚗️ Chemistry &nbsp;📐 Maths &nbsp;🧬 Biology (PCMB)</li></ul><p style="color:#555 !important;font-size:.85rem;font-weight:700;margin:10px 0 4px;">Group 2</p><ul><li>⚡ Physics &nbsp;⚗️ Chemistry &nbsp;📐 Maths &nbsp;💻 Computer Science (PCMC)</li></ul><p style="color:#555 !important;font-size:.85rem;font-weight:700;margin:10px 0 4px;">Group 3</p><ul><li>⚡ Physics &nbsp;⚗️ Chemistry &nbsp;🌿 Botany <span style="color:#666;">(or)</span> 🐾 Zoology</li></ul></div>
    </div>
  </div>
  <div style="margin-top:32px;"><div class="gcard"><h3 style="font-family:'Rajdhani',sans-serif;font-size:1.3rem;margin-bottom:16px;">🏆 Competitive Exam Preparation</h3><div class="grid-2"><div class="wcard"><h3>🔬 NEET</h3><p>Physics, Chemistry, Botany &amp; Zoology — full syllabus coverage with mock tests.</p></div><div class="wcard"><h3>⚙️ JEE</h3><p>Physics, Chemistry &amp; Mathematics — concept-first approach with problem-solving drills.</p></div></div></div></div>
  <div class="btn-center" style="margin-top:24px;"><a href="https://wa.me/917339315376" target="_blank" class="link-btn">📱 Book a Free Trial</a></div>
</div>
</div>

<!-- ════ PAGE: TESTIMONIALS (AI-Corner Style) ════ -->
<div id="page-testimonials" class="page hidden">
<div class="container">

  <!-- Marquee -->
  <div class="testi-marquee-wrap">
    <div class="testi-marquee-track">
      <div class="testi-marquee-item">🧠 <strong>AyA-AI</strong> cleared my doubts at midnight!</div>
      <div class="testi-marquee-item">📝 <strong>Infinite Mock Tests</strong> — never ran out of practice</div>
      <div class="testi-marquee-item">⭐ <strong>95% in boards</strong> after 3 months with Molecular Man</div>
      <div class="testi-marquee-item">🚀 <strong>NEET qualified</strong> — personalised care made the difference</div>
      <div class="testi-marquee-item">💬 <strong>Live Class Portal</strong> — always on time, always prepared</div>
      <div class="testi-marquee-item">🏆 <strong>JEE Advanced</strong> cracker credits Molecular Man's problem sets</div>
      <div class="testi-marquee-item">🧠 <strong>AyA-AI</strong> cleared my doubts at midnight!</div>
      <div class="testi-marquee-item">📝 <strong>Infinite Mock Tests</strong> — never ran out of practice</div>
      <div class="testi-marquee-item">⭐ <strong>95% in boards</strong> after 3 months with Molecular Man</div>
      <div class="testi-marquee-item">🚀 <strong>NEET qualified</strong> — personalised care made the difference</div>
      <div class="testi-marquee-item">💬 <strong>Live Class Portal</strong> — always on time, always prepared</div>
      <div class="testi-marquee-item">🏆 <strong>JEE Advanced</strong> cracker credits Molecular Man's problem sets</div>
    </div>
  </div>

  <!-- Hero banner -->
  <div class="testi-hero">
    <div style="position:relative;z-index:1;">
      <div class="testi-hero-stars">★★★★★</div>
      <div class="testi-hero-title">Real Results.<br>Real Students.</div>
      <div class="testi-hero-sub">Over 500 students taught. These aren't marketing copy — they are the actual voices of kids whose futures changed inside these classes.</div>
      <div style="display:flex;justify-content:center;gap:28px;flex-wrap:wrap;">
        <div style="text-align:center;"><div style="font-family:'Rajdhani',sans-serif;font-size:2rem;font-weight:900;color:var(--gold);">500+</div><div style="font-size:.75rem;color:#64748b;text-transform:uppercase;letter-spacing:1px;">Students Taught</div></div>
        <div style="text-align:center;"><div style="font-family:'Rajdhani',sans-serif;font-size:2rem;font-weight:900;color:var(--cyan);">4.3/5</div><div style="font-size:.75rem;color:#64748b;text-transform:uppercase;letter-spacing:1px;">Avg Rating</div></div>
        <div style="text-align:center;"><div style="font-family:'Rajdhani',sans-serif;font-size:2rem;font-weight:900;color:#48ff00;">100%</div><div style="font-size:.75rem;color:#64748b;text-transform:uppercase;letter-spacing:1px;">Pass Rate</div></div>
      </div>
    </div>
  </div>

  <!-- Tab switcher -->
  <div class="testi-tab-row">
    <div class="testi-tab active-tab" onclick="switchTestiTab('students',this)">🎓 Student Voices</div>
    <div class="testi-tab" onclick="switchTestiTab('parents',this)">👨‍👩‍👧 Parent Reviews</div>
  </div>

  <!-- PANEL: Students -->
  <div id="testi-students" class="testi-panel active">
    <div class="testi-section-label"><span>🎓</span> From Our Students</div>
    <div class="tcard-grid">

      <div class="tcard-new">
        <div class="tcard-quote-icon">"</div>
        <span class="tcard-highlight hl-cyan">🧠 AyA-AI</span>
        <div class="tcard-text">I used to message Sir at 11 PM for doubts, feeling guilty. Then AyA-AI arrived. I asked about Le Chatelier's principle at 1 AM and got a crystal-clear breakdown instantly. I stopped panicking about night-time study sessions entirely.</div>
        <div class="tcard-footer">
          <div class="tcard-avatar">👦</div>
          <div><div class="tcard-info-name">Arjun S.</div><div class="tcard-info-meta">Class 12, CBSE · Chemistry</div><div class="tcard-stars">★★★★★</div></div>
        </div>
      </div>

      <div class="tcard-new">
        <div class="tcard-quote-icon">"</div>
        <span class="tcard-highlight hl-gold">📝 Infinite Mock Tests</span>
        <div class="tcard-text">I attempted 47 NEET-style Chemistry mock tests in one month — completely free. Byju's was charging ₹2,500/month for the same. My accuracy went from 58% to 81%. The mock test engine is simply unmatched.</div>
        <div class="tcard-footer">
          <div class="tcard-avatar">👩</div>
          <div><div class="tcard-info-name">Meera K.</div><div class="tcard-info-meta">NEET 2024 Qualifier · Biology</div><div class="tcard-stars">★★★★★</div></div>
        </div>
      </div>

      <div class="tcard-new">
        <div class="tcard-quote-icon">"</div>
        <span class="tcard-highlight hl-green">🔴 Live Classes</span>
        <div class="tcard-text">Sir never cancels class. In 6 months, not once. The live portal sends a notification the moment the link goes live. I was attending from my hostel in Coimbatore.</div>
        <div class="tcard-footer">
          <div class="tcard-avatar">👦</div>
          <div><div class="tcard-info-name">Rahul M.</div><div class="tcard-info-meta">JEE Aspirant · Physics &amp; Maths</div><div class="tcard-stars">★★★★★</div></div>
        </div>
      </div>

      <div class="tcard-new">
        <div class="tcard-quote-icon">"</div>
        <span class="tcard-highlight hl-purple">💎 Personalised Care</span>
        <div class="tcard-text">Sir remembered that I struggle with integration by parts every single session. He sent personalised problem sets through the app and checked my uploaded answer sheets himself. No coaching centre does this. This is mentorship, not just teaching.</div>
        <div class="tcard-footer">
          <div class="tcard-avatar">👩</div>
          <div><div class="tcard-info-name">Priya N.</div><div class="tcard-info-meta">Class 12 ISC · Mathematics</div><div class="tcard-stars">★★★★★</div></div>
        </div>
      </div>

      <div class="tcard-new">
        <div class="tcard-quote-icon">"</div>
        <span class="tcard-highlight hl-gold">📊 Test Marks Dashboard</span>
        <div class="tcard-text">After every test, my marks appear in my student portal. I can see exactly where I dropped marks, download the question paper again, and submit my revised answers. This level of academic tracking — for free — is genuinely shocking.</div>
        <div class="tcard-footer">
          <div class="tcard-avatar">👦</div>
          <div><div class="tcard-info-name">Karthik B.</div><div class="tcard-info-meta">Class 11, State Board · PCM</div><div class="tcard-stars">★★★★★</div></div>
        </div>
      </div>

      <div class="tcard-new">
        <div class="tcard-quote-icon">"</div>
        <span class="tcard-highlight hl-cyan">🐍 Python Bootcamp</span>
        <div class="tcard-text">I joined the Python bootcamp knowing nothing. After 8 weekends I had built a data visualisation project on real NEET biology data. Sir explained machine learning concepts the way he explains organic mechanisms — "Why does this happen?" before "how." It clicked.</div>
        <div class="tcard-footer">
          <div class="tcard-avatar">👩</div>
          <div><div class="tcard-info-name">Divya S.</div><div class="tcard-info-meta">College 1st Year · Data Science</div><div class="tcard-stars">★★★★★</div></div>
        </div>
      </div>

    </div>
  </div>

  <!-- PANEL: Parents -->
  <div id="testi-parents" class="testi-panel">
    <div class="testi-section-label"><span>👨‍👩‍👧</span> From Our Parents</div>
    <div class="tcard-grid">

      <div class="tcard-new">
        <div class="tcard-quote-icon">"</div>
        <span class="tcard-highlight hl-gold">💰 Value for Money</span>
        <div class="tcard-text">We were paying ₹18,000/month to a corporate coaching centre. My son's marks were static at 62%. Three months with Mohammed Sir, weekly test papers in the app, personalised feedback — 84% in boards. I wish we found this platform two years earlier.</div>
        <div class="tcard-footer">
          <div class="tcard-avatar">👩</div>
          <div><div class="tcard-info-name">Mrs. Lakshmi R.</div><div class="tcard-info-meta">Parent · Madurai · CBSE Class 12</div><div class="tcard-stars">★★★★★</div></div>
        </div>
      </div>

      <div class="tcard-new">
        <div class="tcard-quote-icon">"</div>
        <span class="tcard-highlight hl-cyan">🔔 Parent Notifications</span>
        <div class="tcard-text">Sir sends a personal notification whenever my daughter's test is graded. I can see her marks, the question paper she was given, and her submitted answers — all in one place. As a working parent, this transparency is worth everything. I finally feel involved in her education.</div>
        <div class="tcard-footer">
          <div class="tcard-avatar">👨</div>
          <div><div class="tcard-info-name">Mr. Venkatesh P.</div><div class="tcard-info-meta">Parent · Chennai · NEET Aspirant</div><div class="tcard-stars">★★★★★</div></div>
        </div>
      </div>

      <div class="tcard-new">
        <div class="tcard-quote-icon">"</div>
        <span class="tcard-highlight hl-green">🧠 AyA-AI for Doubt Clearing</span>
        <div class="tcard-text">My son used to call friends asking for help with Physics.Now he uses AyA-AI and has a conversation with it until he understands.He is very confident , this confidence is priceless.</div>
        <div class="tcard-footer">
          <div class="tcard-avatar">👩</div>
          <div><div class="tcard-info-name">Mrs. Anitha K.</div><div class="tcard-info-meta">Parent · Trichy · IB Class 11</div><div class="tcard-stars">★★★★★</div></div>
        </div>
      </div>

      <div class="tcard-new">
        <div class="tcard-quote-icon">"</div>
        <span class="tcard-highlight hl-purple">🎓 NEET Success Story</span>
        <div class="tcard-text">My daughter was struggling with Maths. After one year under Mohammed Sir's personalised programme — weekly maths mock tests, unlimited practice papers, and AyA-AI for concept revision — she scored 86. We are very proud of her, I have no words to express how grateful we are.</div>
        <div class="tcard-footer">
          <div class="tcard-avatar">👨</div>
          <div><div class="tcard-info-name">Mr. Suresh M.</div><div class="tcard-info-meta">Parent · Coimbatore · </div><div class="tcard-stars">★★★★★</div></div>
        </div>
      </div>

      <div class="tcard-new">
        <div class="tcard-quote-icon">"</div>
        <span class="tcard-highlight hl-gold">📱 Always Reachable</span>
        <div class="tcard-text">I've had three tutors before. Not one of them replied to messages after 7 PM. Sir's platform has a messaging system built in. My son sends replies to Sir's notes and they have a real back-and-forth. This responsiveness is what separates this from everything else.</div>
        <div class="tcard-footer">
          <div class="tcard-avatar">👩</div>
          <div><div class="tcard-info-name">Mrs. Radha B.</div><div class="tcard-info-meta">Parent · Madurai · Class 10 ICSE</div><div class="tcard-stars">★★★★★</div></div>
        </div>
      </div>

      <div class="tcard-new">
        <div class="tcard-quote-icon">"</div>
        <span class="tcard-highlight hl-cyan">🏆 100% Ethical Teaching</span>
        <div class="tcard-text">No shortcuts. No rote learning. Sir refuses to teach shortcuts that "work only for boards." My daughter now understands why buffers resist pH change, not just what a buffer is. That's the difference.</div>
        <div class="tcard-footer">
          <div class="tcard-avatar">👨</div>
          <div><div class="tcard-info-name">Mr. Deepak T.</div><div class="tcard-info-meta">Parent · Chennai · IB Class 12</div><div class="tcard-stars">★★★★★</div></div>
        </div>
      </div>

    </div>
  </div>

  <!-- Results -->
  <div class="testi-results">
    <div class="testi-results-title">📊 The Numbers Don't Lie</div>
    <div class="testi-results-grid">
      <div class="testi-result-item"><div class="testi-result-num">83%</div><div class="testi-result-label">Avg Board Score</div></div>
      <div class="testi-result-item"><div class="testi-result-num">60%</div><div class="testi-result-label">Score Improvement</div></div>
      <div class="testi-result-item"><div class="testi-result-num">&lt; 2hr</div><div class="testi-result-label">Doubt Resolution</div></div>
      <div class="testi-result-item"><div class="testi-result-num">∞</div><div class="testi-result-label">Mock Tests Available</div></div>
      <div class="testi-result-item"><div class="testi-result-num">₹0</div><div class="testi-result-label">AI Engine Cost</div></div>
    </div>
  </div>

</div>
</div>

<!-- ════ PAGE: BOOTCAMP ════ -->
<div id="page-bootcamp" class="page hidden">
<div class="container">
  <h1 class="section-title">🐍 Python for Data Science &amp; AI</h1>
  <div class="bootcamp-row">
    <div class="bootcamp-visual"><span>🐍</span><h2>Python</h2><h4>Weekend Intensive Program</h4></div>
    <div class="bootcamp-info">
      <h3>Weekend Intensive Program</h3>
      <p style="color:#a0aec0;font-size:.95rem;margin-bottom:20px;">Master the most in-demand programming language</p>
      <div class="info-row"><strong>👨‍🏫 Instructor: Mohammed Salmaan M</strong><span>Data Science &amp; AI Expert | Created Ed-Tech Platform - The Molecular Man Expert Tuition Solutions</span></div>
      <div class="info-row"><strong>📅 Schedule: Saturdays &amp; Sundays</strong><span>1 hour per session | Morning &amp; Evening batches</span></div>
      <div class="info-row"><strong>💻 Requirements: Laptop with internet</strong><span>We'll help you setup Jupyter Notebook &amp; VS Code</span></div>
      <details><summary>📚 Curriculum Highlights</summary><p>• Python Basics &amp; Data Structures</p><p>• NumPy &amp; Pandas for Data Analysis</p><p>• Data Visualization with Matplotlib</p><p>• Introduction to Machine Learning</p><p>• Real-world Project: Build your first AI model</p></details>
      <div style="margin-top:20px;"><a href="https://wa.me/917339315376" target="_blank" class="link-btn" style="display:block;text-align:center;">📱 Enroll Now</a></div>
    </div>
  </div>
</div>
</div>

<!-- ════ PAGE: CONTACT ════ -->
<div id="page-contact" class="page hidden">
<div class="container">
  <h1 class="section-title">📞 Get In Touch</h1>
  <div class="contact-row">
    <div class="contact-info">
      <h3 style="font-family:'Rajdhani',sans-serif;font-size:1.4rem;margin-bottom:20px;">Contact Information</h3>
      <p style="margin-bottom:10px;"><strong>📱 Phone:</strong> +91 73393 15376</p>
      <p style="margin-bottom:24px;"><strong>✉️ Email:</strong> <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="483c202d662527242d2b3d24293a2529262d30382d3a3c082f25292124662b2725">[email&#160;protected]</a></p>
      <h3 style="font-family:'Rajdhani',sans-serif;font-size:1.2rem;margin-bottom:10px;">📍 Location</h3>
      <p style="margin-bottom:24px;color:#c0cfe0;">Madurai, Tamil Nadu</p>
      <a href="https://wa.me/917339315376" target="_blank" class="link-btn" style="display:block;text-align:center;">💬 Chat on WhatsApp</a>
    </div>
    <div class="contact-form">
      <h3 style="font-family:'Rajdhani',sans-serif;font-size:1.4rem;margin-bottom:20px;">Send us a Message</h3>
      <div class="form-group"><label>Name</label><input type="text" id="f-name" placeholder="Your name" oninput="checkForm()"></div>
      <div class="form-group"><label>Phone</label><input type="text" id="f-phone" placeholder="Your phone number" oninput="checkForm()"></div>
      <div class="form-group"><label>Grade</label><select id="f-grade" onchange="checkForm()"><option value="Class 6-8">Class 6-8</option><option value="Class 9-10">Class 9-10</option><option value="Class 11-12">Class 11-12</option><option value="Repeater/Other">Repeater/Other</option></select></div>
      <div class="form-group"><label>Message</label><textarea id="f-msg" placeholder="Your message..." oninput="checkForm()"></textarea></div>
      <button id="sendBtn" onclick="sendEmail()">🚀 Click to Send Email</button>
      <p class="send-hint">(Opens your default email app)</p>
    </div>
  </div>
</div>
</div>

<!-- ════ PAGE: LIVE CLASS ════ -->
<div id="page-live-class" class="page hidden">
<div class="container">

  <!-- VIEW: Role Selection -->
  <div id="lc-role-select" class="lc-view active">
    <h1 class="section-title" style="text-align:center;">🔴Login to Access your Dashboard</h1>
    <p style="text-align:center;color:#c0cfe0;margin-bottom:8px;">Choose your role to continue</p>
    <div class="lc-role-grid">
      <div class="lc-role-btn" onclick="lcShowView('lc-admin-login')"><span class="icon">🛡️</span><div class="label">Admin Login</div><div class="sublabel">Manage students &amp; classes</div></div>
      <div class="lc-role-btn" onclick="lcShowView('lc-student-login')"><span class="icon">🎓</span><div class="label">Student Login</div><div class="sublabel">Access your dashboard</div></div>
    </div>
  </div>

  <!-- VIEW: Admin Login -->
  <div id="lc-admin-login" class="lc-view">
    <div class="lc-login-card">
      <h3>🛡️ Admin Login</h3>
      <div class="form-group"><label>Username</label><input type="text" id="admin-user" placeholder="Enter username"></div>
      <div class="form-group"><label>Password</label><input type="password" id="admin-pass" placeholder="Enter password"></div>
      <button class="lc-submit" onclick="lcAdminLogin()">Login</button>
      <div id="admin-error" class="lc-error">Invalid credentials. Try again.</div>
      <div class="lc-back-link"><a onclick="lcShowView('lc-role-select')">← Back to Role Selection</a></div>
    </div>
  </div>

  <!-- VIEW: Admin Dashboard -->
  <div id="lc-admin-dash" class="lc-view">
    <div class="lc-admin-header">
      <h2>🛡️ Admin Dashboard</h2>
      <button class="lc-logout-btn" onclick="lcLogout()">Logout</button>
    </div>

    <!-- Create Student -->
    <div class="gcard" style="margin-bottom:24px;">
      <h3 style="font-family:'Rajdhani',sans-serif;font-size:1.2rem;margin-bottom:16px;">➕ Create New Student</h3>
      <div class="lc-create-form">
        <div class="form-group"><label>Student Photo</label><input type="file" id="cs-photo-file" accept="image/*"><div id="cs-photo-status" class="upload-status"></div></div>
        <div class="form-group"><label>Full Name</label><input type="text" id="cs-name" placeholder="Student full name"></div>
        <div class="form-group"><label>Username</label><input type="text" id="cs-username" placeholder="student_username"></div>
        <div class="form-group"><label>Password</label><input type="text" id="cs-password" placeholder="Set a password"></div>
        <div class="form-group"><label>Class</label><input type="text" id="cs-class" placeholder="e.g. Class 10"></div>
        <div class="form-group"><label>Board</label><select id="cs-board"><option value="CBSE">CBSE</option><option value="ICSE">ICSE / ISC</option><option value="IB">IB &amp; IGCSE</option><option value="State Board">State Board</option></select></div>
        <div class="form-group" style="grid-column:1/-1;"><label>Package Chosen</label><input type="text" id="cs-package" placeholder="e.g. Premium, Standard"></div>
        <button class="lc-submit" onclick="lcCreateStudent()">Create Student</button>
      </div>
    </div>

    <!-- Student List -->
    <div class="gcard">
      <h3 style="font-family:'Rajdhani',sans-serif;font-size:1.2rem;margin-bottom:12px;">📋 Student Database</h3>
      <div style="overflow-x:auto;">
        <table class="lc-student-table">
          <thead><tr><th>Photo</th><th>Name</th><th>Username</th><th>Class</th><th>Board</th><th>Package</th><th>Link</th><th>Actions</th></tr></thead>
          <tbody id="lc-student-tbody"></tbody>
        </table>
      </div>
      <div id="lc-no-students" class="lc-empty">No students yet. Create one above.</div>
    </div>

    <!-- ══ MESSAGES INBOX PANEL ══ -->
    <div class="gcard" id="admin-inbox-panel" style="margin-top:24px;border-color:rgba(0,255,255,.3);">
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;margin-bottom:16px;">
        <h3 style="font-family:'Rajdhani',sans-serif;font-size:1.2rem;margin:0;">📩 Messages Inbox <span id="admin-inbox-badge" style="display:none;background:#ef4444;color:#fff;font-size:.7rem;font-weight:800;padding:2px 8px;border-radius:10px;margin-left:6px;"></span></h3>
        <button onclick="lcRefreshInbox()" style="padding:6px 16px;border-radius:16px;background:rgba(0,255,255,.1);border:1px solid rgba(0,255,255,.3);color:var(--cyan);font-family:'Exo 2',sans-serif;font-size:.8rem;font-weight:700;cursor:pointer;">🔄 Refresh</button>
      </div>

      <!-- Tab bar -->
      <div style="display:flex;gap:8px;margin-bottom:16px;flex-wrap:wrap;">
        <button id="inbox-tab-student" onclick="lcInboxTab('student')" style="padding:7px 18px;border-radius:20px;background:rgba(0,255,255,.15);border:1px solid rgba(0,255,255,.4);color:var(--cyan);font-family:'Exo 2',sans-serif;font-size:.82rem;font-weight:700;cursor:pointer;">📩 Student Messages</button>
        <button id="inbox-tab-replies" onclick="lcInboxTab('replies')" style="padding:7px 18px;border-radius:20px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.15);color:#94a3b8;font-family:'Exo 2',sans-serif;font-size:.82rem;font-weight:700;cursor:pointer;">↩️ Student Replies</button>
      </div>

      <!-- Student → Admin messages panel -->
      <div id="inbox-panel-student">
        <div id="admin-inbox-list"><div style="text-align:center;color:#a0aec0;padding:20px;">Loading messages…</div></div>
      </div>

      <!-- Student replies to admin messages panel -->
      <div id="inbox-panel-replies" style="display:none;">
        <div id="admin-replies-list"><div style="text-align:center;color:#a0aec0;padding:20px;">Loading replies…</div></div>
      </div>
    </div>

    <!-- Public Downloads Management -->
    <div class="gcard" style="margin-top:24px;">
      <h3 style="font-family:'Rajdhani',sans-serif;font-size:1.2rem;margin-bottom:16px;">🌐 Manage Public Downloads</h3>
      <div class="pub-dl-form">
        <div class="form-group"><label>Title / Description</label><input type="text" id="pdl-title" placeholder="e.g. Class 12 CBSE Physics Ch.1 Notes"></div>
        <div class="form-group"><label>Board</label>
          <select id="pdl-board">
            <option value="CBSE">CBSE</option><option value="ICSE">ICSE / ISC</option><option value="IB">IB &amp; IGCSE</option><option value="State Board">State Board</option>
          </select>
        </div>
        <div class="form-group"><label>Class</label>
          <select id="pdl-class">
            <option value="6">Class 6</option><option value="7">Class 7</option><option value="8">Class 8</option><option value="9">Class 9</option><option value="10">Class 10</option><option value="11">Class 11</option><option value="12">Class 12</option>
          </select>
        </div>
        <div class="form-group"><label>Subject</label>
          <select id="pdl-subject">
            <option value="Maths">Maths</option><option value="Physics">Physics</option><option value="Chemistry">Chemistry</option><option value="Biology">Biology</option><option value="Science">Science</option>
          </select>
        </div>
        <div class="form-group" style="grid-column:1/-1;"><label>File Link (URL)</label><input type="url" id="pdl-link" placeholder="https://drive.google.com/…"></div>
        <button class="lc-submit" onclick="pdlAddEntry()">➕ Add Public Download</button>
      </div>
      <div style="overflow-x:auto;margin-top:18px;">
        <table class="pub-dl-table" id="pdl-table">
          <thead><tr><th>Title</th><th>Board</th><th>Class</th><th>Subject</th><th>Link</th><th>Actions</th></tr></thead>
          <tbody id="pdl-tbody"><tr><td colspan="6" style="text-align:center;color:#888;padding:16px;">Loading…</td></tr></tbody>
        </table>
      </div>
    </div>

  </div>

  <!-- VIEW: Student Login -->
  <div id="lc-student-login" class="lc-view">
    <div class="lc-login-card">
      <h3>🎓 Student Login</h3>
      <div class="form-group"><label>Username</label><input type="text" id="stu-user" placeholder="Enter your username"></div>
      <div class="form-group"><label>Password</label><input type="password" id="stu-pass" placeholder="Enter your password"></div>
      <button class="lc-submit" onclick="lcStudentLogin()">Login</button>
      <div id="student-error" class="lc-error">Invalid username or password.</div>
      <div class="lc-back-link"><a onclick="lcShowView('lc-role-select')">← Back to Role Selection</a></div>
    </div>
  </div>

  <!-- VIEW: Student Dashboard -->
  <div id="lc-student-dash" class="lc-view">
    <div class="lc-admin-header">
      <h2>🎓 My Dashboard</h2>
      <button class="lc-logout-btn" onclick="lcLogout()">Logout</button>
    </div>
    <div class="gcard" style="margin-bottom:20px;">
      <div class="lc-profile-row">
        <img id="sd-photo" class="lc-profile-photo" src="" alt="Student photo">
        <div class="lc-profile-info">
          <h3 id="sd-name"></h3>
          <p id="sd-class-board"></p>
          <span id="sd-package" class="lc-profile-badge"></span>
        </div>
      </div>
    </div>
    <div class="gcard" style="margin-bottom:20px;">
      <h3 style="font-family:'Rajdhani',sans-serif;font-size:1.2rem;margin-bottom:16px;">🔴 Live Class</h3>
      <div id="sd-live-area"></div>
    </div>
    <div class="gcard" style="margin-bottom:20px;">
      <h3 style="font-family:'Rajdhani',sans-serif;font-size:1.2rem;margin-bottom:16px;">📝 My Tests &amp; Marks</h3>
      <div id="sd-tests-area"></div>
    </div>
    <div class="gcard">
      <h3 style="font-family:'Rajdhani',sans-serif;font-size:1.2rem;margin-bottom:16px;">🔔 Messages from Sir</h3>
      <div id="sd-notif-area"></div>
    </div>
    <div class="gcard" style="margin-top:20px;">
      <h3 style="font-family:'Rajdhani',sans-serif;font-size:1.2rem;margin-bottom:16px;">📚 My Study Notes</h3>
      <div id="sd-notes-area"><div class="sn-empty">Loading your study notes…</div></div>
    </div>
    <div class="gcard" style="margin-top:20px;border-color:rgba(0,255,255,.25);">
      <h3 style="font-family:'Rajdhani',sans-serif;font-size:1.2rem;margin-bottom:4px;">💬 Message Your Tutor</h3>
      <p style="font-size:.82rem;color:#94a3b8;margin-bottom:14px;">Have a question or need to reach your tutor? Send a message here and you'll get a reply in your notifications above.</p>
      <div id="sd-my-messages-area" style="margin-bottom:14px;"></div>
      <textarea id="student-msg-input" placeholder="Type your message to Sir…" style="width:100%;min-height:80px;background:rgba(255,255,255,.08);color:#fff;border:1px solid rgba(0,255,255,.3);border-radius:10px;padding:10px 14px;font-family:'Exo 2',sans-serif;font-size:.92rem;resize:vertical;outline:none;margin-bottom:10px;"></textarea>
      <button onclick="lcStudentSendToAdmin()" style="padding:10px 28px;border-radius:20px;background:linear-gradient(90deg,#0ea5e9,#0284c7);color:#fff;font-family:'Exo 2',sans-serif;font-weight:700;font-size:.9rem;border:none;cursor:pointer;">📤 Send Message</button>
    </div>
  </div>

</div>
</div>

<!-- ════ PAGE: DOWNLOADS ════ -->
<div id="page-downloads" class="page hidden">
<div class="container">
  <h1 class="section-title">⬇️ Free Study Materials</h1>
  <p style="color:#c0cfe0;margin-bottom:24px;font-size:.95rem;">Browse and download free notes, formula sheets, past papers, and more — curated by Mohammed Salmaan Sir for every board and class.</p>

  <!-- Filter Bar -->
  <div class="dl-filter-bar">
    <div class="dl-filter-group">
      <label>Board</label>
      <select id="dl-filter-board" onchange="renderDownloads()">
        <option value="">All Boards</option>
        <option value="CBSE">CBSE</option>
        <option value="ICSE">ICSE / ISC</option>
        <option value="IB">IB &amp; IGCSE</option>
        <option value="State Board">State Board</option>
      </select>
    </div>
    <div class="dl-filter-group">
      <label>Class</label>
      <select id="dl-filter-class" onchange="renderDownloads()">
        <option value="">All Classes</option>
        <option value="6">Class 6</option>
        <option value="7">Class 7</option>
        <option value="8">Class 8</option>
        <option value="9">Class 9</option>
        <option value="10">Class 10</option>
        <option value="11">Class 11</option>
        <option value="12">Class 12</option>
      </select>
    </div>
    <div class="dl-filter-group">
      <label>Subject</label>
      <select id="dl-filter-subject" onchange="renderDownloads()">
        <option value="">All Subjects</option>
        <option value="Maths">Maths</option>
        <option value="Physics">Physics</option>
        <option value="Chemistry">Chemistry</option>
        <option value="Biology">Biology</option>
        <option value="Science">Science</option>
      </select>
    </div>
    <button class="dl-filter-reset" onclick="resetDlFilters()">↺ Reset</button>
  </div>

  <!-- Downloads Grid -->
  <div class="dl-grid" id="dl-grid">
    <div class="dl-empty"><span>⏳</span>Loading materials…</div>
  </div>
</div>
</div>


<!-- ════ PAGE: ABOUT US ════ -->
<div id="page-about" class="page hidden">
<div class="container">

  <div style="text-align:center;margin-bottom:36px;">
    <h2 style="font-family:'Rajdhani',sans-serif;font-size:clamp(1.8rem,4vw,2.8rem);font-weight:900;
      background:linear-gradient(to right,var(--gold),var(--cyan));
      -webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:8px;">
      Who We Are &amp; What Powers Us
    </h2>
    <p style="color:#94a3b8;font-size:.95rem;max-width:560px;margin:0 auto;">
      The mind behind the curriculum, and the intelligence that never sleeps — two stories. One mission.
    </p>
  </div>

  <!-- Sub-tab navigation -->
  <div class="about-tab-bar" role="tablist">
    <button class="about-tab at-active" onclick="switchAboutTab('tutor',this)" role="tab" aria-selected="true">🧑‍🔬 About the Tutor</button>
    <button class="about-tab" onclick="switchAboutTab('aya',this)" role="tab" aria-selected="false">🤖 About AyA AI</button>
    <button class="about-tab" onclick="switchAboutTab('faq',this)" role="tab" aria-selected="false">❓ FAQ</button>
  </div>

  <!-- ══ PANEL 1: ABOUT THE TUTOR ══════════════════════════════════ -->
  <div id="about-panel-tutor" class="about-panel ap-active">

    <!-- Hero card -->
    <div class="tutor-hero" itemscope itemtype="https://schema.org/Person">
      <div class="tutor-inner">

        <!-- Photo -->
        <div class="tutor-photo-col">
          <div class="tutor-photo-ring">
            <img src="Me.jpeg" alt="Mohammed Salmaan M — Chemistry Tutor, AI Developer" itemprop="image"
              onerror="this.parentElement.innerHTML='<div style='width:100%;height:100%;border-radius:50%;background:linear-gradient(135deg,rgba(255,215,0,.2),rgba(0,255,255,.15));display:flex;align-items:center;justify-content:center;font-size:5rem;border:3px solid rgba(0,4,40,.8);'>🧑‍🔬</div>'">
          </div>
          <div class="tutor-verified">✅ Verified Educator</div>
          <div style="display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin-top:4px;">
            <span style="font-size:.68rem;color:#64748b;text-align:center;">M.Sc Chemistry · AI Developer</span>
          </div>
        </div>

        <!-- Info -->
        <div class="tutor-info-col">
          <div class="tutor-eyebrow">The Architect of Learning</div>
          <div class="tutor-name" itemprop="name">Mohammed Salmaan M.</div>
          <div class="tutor-role" itemprop="jobTitle">Chemist. Educator. Full-Stack Developer.</div>
          <div class="tutor-tagline">
            "Great teaching isn't just about transferring knowledge; it is about engineering a catalyst for the mind."
          </div>

          <ul class="cred-list">
            <li class="cred-item">
              <span class="cred-ico">🎓</span>
              <div><span class="cred-main">Master of Science — Chemistry</span>
              <span class="cred-sub">Advanced specialisation in Organic &amp; Physical Chemistry</span></div>
            </li>
            <li class="cred-item">
              <span class="cred-ico">🏭</span>
              <div><span class="cred-main">Industrial Experience — Chemplast Sanmar</span>
              <span class="cred-sub">Chemical manufacturing &amp; process precision at scale</span></div>
            </li>
            <li class="cred-item">
              <span class="cred-ico">🔬</span>
              <div><span class="cred-main">Industrial Experience — Aurolab</span>
              <span class="cred-sub">Precision optics &amp; pharmaceutical-grade QA</span></div>
            </li>
            <li class="cred-item">
              <span class="cred-ico">💻</span>
              <div><span class="cred-main">Full-Stack Developer &amp; AI Engineer</span>
              <span class="cred-sub">Built this platform — front to back, zero outsourcing</span></div>
            </li>
            <li class="cred-item">
              <span class="cred-ico">📍</span>
              <div><span class="cred-main">Physical Tuition Centre Alumni</span>
              <span class="cred-sub" itemprop="address">Madurai, Tamil Nadu, India</span></div>
            </li>
          </ul>

          <div class="tutor-stats">
            <div class="stat-pill"><span class="stat-num">7+</span><div class="stat-lbl">Yrs Teaching</div></div>
            <div class="stat-pill"><span class="stat-num">500+</span><div class="stat-lbl">Students</div></div>
            <div class="stat-pill"><span class="stat-num">4</span><div class="stat-lbl">Boards Covered</div></div>
            <div class="stat-pill"><span class="stat-num">100%</span><div class="stat-lbl">Self-Built</div></div>
          </div>
        </div>
      </div>

      <!-- Industry tags -->
      <div class="industry-tags" style="margin-top:28px;">
        <span class="ind-tag">🏭 Chemplast Sanmar Alumnus</span>
        <span class="ind-tag">🔬 Aurolab Alumnus</span>
        <span class="ind-tag">⚛️ M.Sc Chemistry</span>
        <span class="ind-tag">🐍 Python · Data Science</span>
        <span class="ind-tag">🤖 AI / LLM Engineering</span>
        <span class="ind-tag">📐 Maths · Physics</span>
        <span class="ind-tag">🌐 Full-Stack Web Dev</span>
      </div>
    </div>

    <!-- The story -->
    <div class="about-section-head">
      <h2>The Story: From Factory Floors to Digital Classrooms</h2>
      <p>How industrial precision became the foundation of elite teaching</p>
    </div>
    <div class="journey-grid">
      <div class="journey-card">
        <span class="journey-icon">🏭</span>
        <h3>Forged in Industry</h3>
        <p>My journey did not begin in a classroom, but on the high-stakes manufacturing floors of Chemplast Sanmar and Aurolab — where a single miscalculation carries real consequences. That environment of absolute precision became the lens through which I now teach every student: accuracy matters, always.</p>
      </div>
      <div class="journey-card">
        <span class="journey-icon">💡</span>
        <h3>The Deeper Calling</h3>
        <p>Holding a Master's degree in Chemistry, I discovered that the most satisfying reaction wasn't chemical — it was the moment a student's face lit up with genuine understanding. Teaching wasn't just a career pivot; it was a calling that demanded everything my industrial training had given me.</p>
      </div>
      <div class="journey-card">
        <span class="journey-icon">🏫</span>
        <h3>The Physical Centre Years</h3>
        <p>After years of running physical tuition centres and navigating the profound highs and lows of the educational journey, I witnessed firsthand that the modern student requires more than a textbook — they require a complete ecosystem. That realisation changed everything.</p>
      </div>
      <div class="journey-card">
        <span class="journey-icon">🖥️</span>
        <h3>The Digital Leap</h3>
        <p>I didn't just design the curriculum; I taught myself to code and built this very platform. By merging academic expertise in science and mathematics with AI engineering, I created a space where pedagogy meets technology. No corporate noise. No outsourced development. Just a tutor who built his students a digital sanctuary — 24/7.</p>
      </div>
    </div>

    <!-- Timeline -->
    <div class="about-section-head">
      <h2>A Decade in the Making — Career Timeline</h2>
    </div>
    <div class="tl-wrap">
      <div class="tl-item">
        <div class="tl-dot"></div>
        <div class="tl-year">M.Sc. Chemistry</div>
        <div class="tl-title">Postgraduate Mastery in Chemistry</div>
        <div class="tl-desc">Completed an intensive Master's programme with specialisation in Organic &amp; Physical Chemistry, laying the scientific foundation for everything that followed.</div>
      </div>
      <div class="tl-item">
        <div class="tl-dot"></div>
        <div class="tl-year">Industrial Phase</div>
        <div class="tl-title">Chemplast Sanmar &amp; Aurolab</div>
        <div class="tl-desc">Hands-on experience in chemical manufacturing and pharmaceutical-grade quality assurance. Learned that precision and accountability are non-negotiable — a lesson carried directly into teaching.</div>
      </div>
      <div class="tl-item">
        <div class="tl-dot"></div>
        <div class="tl-year">Teaching Begins</div>
        <div class="tl-title">Physical Tuition Centres Launch</div>
        <div class="tl-desc">Founded and operated local tuition centres in Madurai, serving students across CBSE, ICSE, IB, and State Board curricula. Personally taught Chemistry, Physics, Maths, and Science.</div>
      </div>
      <div class="tl-item">
        <div class="tl-dot"></div>
        <div class="tl-year">Self-Taught Developer</div>
        <div class="tl-title">Mastered Python, AI &amp; Full-Stack Web Development</div>
        <div class="tl-desc">Driven by necessity and passion, independently learned Python, data science, AI engineering, and full-stack web development — eventually building this entire platform from scratch.</div>
      </div>
      <div class="tl-item">
        <div class="tl-dot" style="background:var(--cyan);box-shadow:0 0 12px rgba(0,255,255,.7);"></div>
        <div class="tl-year">Now — The Molecular Man Platform</div>
        <div class="tl-title">Digital Tuition Ecosystem + AyA AI</div>
        <div class="tl-desc">Launched The Molecular Man Expert Tuition Solutions — a fully self-built platform integrating live classes, personalised student dashboards, public study material downloads, and AyA: a 24/7 AI tutor trained on the same teaching philosophy.</div>
      </div>
    </div>

    <!-- Success proof -->
    <div class="about-section-head">
      <h2>Student Success — Results That Speak</h2>
      <p>Anonymised outcomes from real students across boards and subjects</p>
    </div>
    <div class="proof-grid">
      <div class="proof-card">
        <div class="proof-pct">94%</div>
        <div class="proof-label">CBSE Class 10 — Science</div>
        <div class="proof-detail">Student A · Board Exam · Madurai</div>
        <div class="proof-tag">↑ From 61% → 94%</div>
      </div>
      <div class="proof-card">
        <div class="proof-pct">91%</div>
        <div class="proof-label">CBSE Class 12 — Chemistry</div>
        <div class="proof-detail">Student B · Board Exam</div>
        <div class="proof-tag">↑ From 58% → 91%</div>
      </div>
      <div class="proof-card">
        <div class="proof-pct">88%</div>
        <div class="proof-label">ICSE Class 10 — Physics &amp; Chemistry</div>
        <div class="proof-detail">Student C · Combined</div>
        <div class="proof-tag">↑ From 55% → 88%</div>
      </div>
      <div class="proof-card">
        <div class="proof-pct">Top 5%</div>
        <div class="proof-label">State Board — Maths</div>
        <div class="proof-detail">Student D · District-level rank</div>
        <div class="proof-tag">🏆 District Distinction</div>
      </div>
      <div class="proof-card">
        <div class="proof-pct">85%</div>
        <div class="proof-label">NEET Preparation — Biology + Chem</div>
        <div class="proof-detail">Student E · Mock test average</div>
        <div class="proof-tag">↑ 30% mock improvement</div>
      </div>
      <div class="proof-card">
        <div class="proof-pct">500+</div>
        <div class="proof-label">Students Taught Across All Boards</div>
        <div class="proof-detail">Physical + Online · 7+ years</div>
        <div class="proof-tag">🌟 Ongoing</div>
      </div>
    </div>

    <p style="font-size:.75rem;color:#475569;text-align:center;margin-top:-20px;margin-bottom:36px;font-style:italic;">
      * All results are real. Student identities are anonymised to protect privacy. Results vary by individual effort and prior foundation.
    </p>

  </div><!-- /panel tutor -->

  <!-- ══ PANEL 2: ABOUT AyA AI ══════════════════════════════════ -->
  <div id="about-panel-aya" class="about-panel">

    <!-- AyA Hero -->
    <div class="aya-hero-wrap">
      <div class="aya-inner">
        <div class="aya-orb-wrap">
          <div class="aya-orb">🤖</div>
        </div>
        <div class="aya-title">AyA</div>
        <div class="aya-sub">Your Tireless Mentor</div>
        <div class="aya-tagline">
          Pure Teaching Intelligence. Zero Subscriptions. Infinite Potential.<br>
          Built by your tutor. Not a corporation. Not a startup. A master educator who codes.
        </div>

        <div class="aya-feat-grid">
          <div class="aya-feat">
            <span class="aya-feat-ico">⚡</span>
            <div class="aya-feat-title">Instant Clarity — 3 AM? No problem.</div>
            <div class="aya-feat-desc">Ask a complex question about thermodynamics or calculus at 3 AM and receive a crystal-clear, step-by-step breakdown. No waiting. No judgment.</div>
          </div>
          <div class="aya-feat">
            <span class="aya-feat-ico">🎯</span>
            <div class="aya-feat-title">Adaptive Brilliance</div>
            <div class="aya-feat-desc">AyA adjusts to your exact syllabus and difficulty level — CBSE, ICSE, IB, State Board, NEET, JEE — ensuring you're always challenged but never overwhelmed.</div>
          </div>
          <div class="aya-feat">
            <span class="aya-feat-ico">📝</span>
            <div class="aya-feat-title">Infinite Mock Test Engine</div>
            <div class="aya-feat-desc">Fresh, unique, board-targeted test papers — generated on demand. The corporate giants monetized your practice. We made it free forever.</div>
          </div>
          <div class="aya-feat">
            <span class="aya-feat-ico">🌐</span>
            <div class="aya-feat-title">100% Free. Always.</div>
            <div class="aya-feat-desc">No hidden fees. No paywalls. No premium tiers. No subscription trap. Just uncompromised, elite-level academic support — every student deserves it.</div>
          </div>
        </div>

        <div class="aya-free">🤖 AyA — The Great Equalizer in Modern Education</div>
        <p style="font-size:.78rem;color:#475569;margin-top:10px;">Stop buying test series. Start generating them.</p>
      </div>
    </div>

    <!-- The Problem AyA Solves -->
    <div class="about-section-head">
      <h2>The Problem AyA Was Born to Solve</h2>
      <p>Education gatekeeping disguised as "premium" services — dismantled.</p>
    </div>
    <div class="phil-row">
      <div class="phil-block">
        <h3>🔴 The Old Reality</h3>
        <ul>
          <li>Questions at midnight = no answers until tomorrow</li>
          <li>Premium test series costing thousands per year</li>
          <li>Generic AI tools with no syllabus awareness</li>
          <li>Corporate platforms with zero personal touch</li>
          <li>Students in smaller cities priced out of elite support</li>
        </ul>
      </div>
      <div class="phil-block">
        <h3>🟢 The AyA Reality</h3>
        <ul>
          <li>24/7/365 instant answers — always on, never tired</li>
          <li>Infinite board-specific mock tests — completely free</li>
          <li>Tuned to your exact syllabus and exam pattern</li>
          <li>Built by an actual teacher — not an algorithm farm</li>
          <li>Equal access for every student, everywhere in India</li>
        </ul>
      </div>
    </div>

    <!-- How AyA was built -->
    <div class="about-section-head">
      <h2>How AyA Was Built — The Architecture</h2>
      <p>The intersection of pedagogy, AI engineering, and teaching philosophy</p>
    </div>
    <div class="phil-row">
      <div class="phil-block">
        <h3>🧠 The Teaching Philosophy Layer</h3>
        <p>AyA isn't just powered by a language model — she is guided by my specific pedagogical framework: always explain the "Why" before the "How". Every prompt architecture, every response pattern, and every feedback loop is designed around how real students actually learn and where they typically get stuck.</p>
      </div>
      <div class="phil-block">
        <h3>🤖 The AI Engineering Layer</h3>
        <p>Designed, configured, prompt-engineered, and integrated by Mohammed Salmaan M. — personally. AyA is built on a frontier large language model and layered with subject-specific context for Chemistry, Physics, Mathematics, Biology, and Python/Data Science, across all major Indian and international boards.</p>
      </div>
      <div class="phil-block">
        <h3>📐 Syllabus Intelligence</h3>
        <p>Unlike generic AI assistants, AyA understands curriculum structure — CBSE Chapters, ICSE syllabi, IB unit frameworks, State Board formats, NEET/JEE topic weightages. She can generate targeted questions from specific chapters, difficulty bands, and question types.</p>
      </div>
      <div class="phil-block">
        <h3>🔒 Zero Data Exploitation</h3>
        <p>AyA does not store your conversations for corporate data harvesting. Your study sessions are your own. No behavioural profiling. No ad targeting. This is education — not surveillance capitalism.</p>
      </div>
    </div>

    <!-- What makes AyA different -->
    <div class="about-section-head">
      <h2>What Makes AyA Different From Every Other AI Tool</h2>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-bottom:36px;">
      <div style="background:rgba(167,139,250,.07);border:1px solid rgba(167,139,250,.2);border-radius:14px;padding:18px;text-align:center;">
        <div style="font-size:2rem;margin-bottom:8px;">👨‍🏫</div>
        <div style="font-family:'Rajdhani',sans-serif;font-weight:800;color:#c4b5fd;margin-bottom:5px;">Built by a Real Teacher</div>
        <div style="font-size:.8rem;color:#64748b;">Not a startup. Not a corporate product. Your actual tutor built and maintains her.</div>
      </div>
      <div style="background:rgba(167,139,250,.07);border:1px solid rgba(167,139,250,.2);border-radius:14px;padding:18px;text-align:center;">
        <div style="font-size:2rem;margin-bottom:8px;">🎓</div>
        <div style="font-family:'Rajdhani',sans-serif;font-weight:800;color:#c4b5fd;margin-bottom:5px;">Curriculum-Aware</div>
        <div style="font-size:.8rem;color:#64748b;">Knows your board, chapter, and exam pattern — not just generic science.</div>
      </div>
      <div style="background:rgba(167,139,250,.07);border:1px solid rgba(167,139,250,.2);border-radius:14px;padding:18px;text-align:center;">
        <div style="font-size:2rem;margin-bottom:8px;">♾️</div>
        <div style="font-family:'Rajdhani',sans-serif;font-weight:800;color:#c4b5fd;margin-bottom:5px;">Infinite Test Generation</div>
        <div style="font-size:.8rem;color:#64748b;">Generate unlimited mock papers. No recycled questions. No paywalls.</div>
      </div>
      <div style="background:rgba(167,139,250,.07);border:1px solid rgba(167,139,250,.2);border-radius:14px;padding:18px;text-align:center;">
        <div style="font-size:2rem;margin-bottom:8px;">🕛</div>
        <div style="font-family:'Rajdhani',sans-serif;font-weight:800;color:#c4b5fd;margin-bottom:5px;">Always Available</div>
        <div style="font-size:.8rem;color:#64748b;">3 AM panic before exams? AyA is awake, patient, and ready.</div>
      </div>
    </div>

  </div><!-- /panel aya -->

  <!-- ══ PANEL 3: FAQ ══════════════════════════════════════════ -->
  <div id="about-panel-faq" class="about-panel">

    <div class="about-section-head" style="margin-top:0;">
      <h2>Frequently Asked Questions</h2>
      <p>Everything students and parents ask before joining — answered honestly.</p>
    </div>

    <!-- Schema.org FAQ markup for SEO -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {"@type":"Question","name":"Who is Mohammed Salmaan M.?","acceptedAnswer":{"@type":"Answer","text":"Mohammed Salmaan M. is a Chemistry postgraduate (M.Sc), former industrial scientist at Chemplast Sanmar and Aurolab, and the founder of The Molecular Man Expert Tuition Solutions. He personally teaches Chemistry, Physics, Maths, Science, and Python, and also coded the entire digital platform including the AyA AI tutor."}},
        {"@type":"Question","name":"Which boards does The Molecular Man cover?","acceptedAnswer":{"@type":"Answer","text":"We cover CBSE, ICSE, IB (International Baccalaureate), and State Board (Tamil Nadu). We also support NEET and JEE preparation."}},
        {"@type":"Question","name":"What is AyA AI?","acceptedAnswer":{"@type":"Answer","text":"AyA is an AI-powered tutoring assistant built and configured by Mohammed Salmaan M. She provides 24/7 academic support, step-by-step explanations, and can generate unlimited board-specific mock test papers — completely free."}},
        {"@type":"Question","name":"Is AyA AI free to use?","acceptedAnswer":{"@type":"Answer","text":"Yes. AyA is 100% free, forever. There are no hidden fees, paywalls, or premium tiers. Every student deserves equal access to elite academic support."}},
        {"@type":"Question","name":"How is this platform different from other coaching institutes?","acceptedAnswer":{"@type":"Answer","text":"Unlike corporate coaching chains, this platform was built entirely by the tutor himself — the same person who teaches. There is no outsourced development, no generic content, and no monetized test series. Students get a personalised ecosystem: live classes, a private dashboard, downloadable study materials, and a 24/7 AI tutor."}}
      ]
    }
    </script>

    <div class="faq-list">

      <details class="faq-item">
        <summary>Who exactly is Mohammed Salmaan M. and what are his qualifications?</summary>
        <div class="faq-body">
          Mohammed Salmaan M. holds a <strong>Master of Science in Chemistry</strong> and has hands-on industrial experience from <strong>Chemplast Sanmar</strong> (chemical manufacturing) and <strong>Aurolab</strong> (pharmaceutical-grade precision optics). He then transitioned into education, running physical tuition centres before building this full digital platform — including the AI tutoring system — entirely himself. He personally teaches Chemistry, Physics, Maths, Science, and Python/Data Science.
        </div>
      </details>

      <details class="faq-item">
        <summary>Which boards and subjects do you teach?</summary>
        <div class="faq-body">
          We cover <strong>CBSE, ICSE, IB (International Baccalaureate), and Tamil Nadu State Board</strong> for Classes 8–12. Subjects include <strong>Chemistry, Physics, Mathematics, Biology/Science, and Python/Data Science</strong>. We also offer dedicated <strong>NEET and JEE preparation</strong> tracks with targeted mock testing through AyA.
        </div>
      </details>

      <details class="faq-item">
        <summary>What is AyA AI and how does she work?</summary>
        <div class="faq-body">
          AyA is an AI tutoring assistant designed, configured, and maintained by Mohammed Salmaan — not a generic product. She is powered by a frontier large language model, layered with <strong>subject-specific pedagogy and board-aware curriculum context</strong>. She can answer complex questions with step-by-step explanations, generate infinite mock test papers for your specific board and chapter, and is available 24 hours a day, 365 days a year. She is accessed via the AI Corner tab.
        </div>
      </details>

      <details class="faq-item">
        <summary>Is AyA AI actually free? What's the catch?</summary>
        <div class="faq-body">
          There is no catch. <strong>AyA is 100% free, forever.</strong> No subscription. No paywall. No "premium" tier. The mission of The Molecular Man platform is to democratise elite academic support — and that mission is not compatible with paywalling the AI tutor. The platform is self-funded and self-built, which means zero corporate overhead and zero need to monetize your learning.
        </div>
      </details>

      <details class="faq-item">
        <summary>How do I join live classes? What does the student dashboard include?</summary>
        <div class="faq-body">
          Students are enrolled by the tutor directly through the <strong>Live Class portal</strong>. Once enrolled, you receive a private login to your <strong>Student Dashboard</strong> — where you can access your personalised live class link, download test papers, view your marks and feedback, receive direct messages from the tutor, submit answer sheets, and access your private study notes curated just for you.
        </div>
      </details>

      <details class="faq-item">
        <summary>Can AyA generate mock tests for NEET and JEE?</summary>
        <div class="faq-body">
          Yes. AyA's <strong>Infinite Mock Test Engine</strong> can generate targeted practice papers for NEET (Biology, Chemistry, Physics) and JEE (Mathematics, Physics, Chemistry) — tailored to specific chapters, difficulty levels, and question types. You can specify exactly what you want and receive a fresh, unique paper instantly. No recycled questions. No cost.
        </div>
      </details>

      <details class="faq-item">
        <summary>How is this different from other online coaching platforms?</summary>
        <div class="faq-body">
          The core difference is <strong>authenticity and ownership</strong>. This platform was built entirely by the tutor himself — the same person who teaches every class. There is no corporate structure, no outsourced developers, no generic AI bolted onto a coaching brand. Everything here — the curriculum, the platform, the AI, and the teaching — flows from a single, accountable source: Mohammed Salmaan M.
        </div>
      </details>

      <details class="faq-item">
        <summary>Where is The Molecular Man Expert Tuition Solutions based?</summary>
        <div class="faq-body">
          We are based in <strong>Madurai, Tamil Nadu, India</strong>, and serve students both in-person (local) and fully online across India and internationally for IB and CBSE students abroad.
        </div>
      </details>

    </div><!-- /faq-list -->

    <div style="text-align:center;margin-top:8px;padding:28px;background:rgba(255,215,0,.04);border:1px solid rgba(255,215,0,.15);border-radius:16px;">
      <p style="font-size:1rem;color:#e2e8f0;margin-bottom:14px;">Have a question not answered here?</p>
      <button onclick="showPage('contact',document.querySelector('[onclick*=contact]'))" style="padding:11px 28px;border-radius:24px;background:linear-gradient(90deg,var(--gold),rgba(255,215,0,.6));color:#000;font-family:'Rajdhani',sans-serif;font-weight:800;font-size:1rem;border:none;cursor:pointer;letter-spacing:.5px;">📞 Contact Directly</button>
    </div>

  </div><!-- /panel faq -->

</div><!-- /container -->
</div><!-- /page-about -->

<!-- ════ PAGE: AI CORNER ════ -->
<div id="page-ai-corner" class="page hidden">
<div class="container">
  <div class="ai-marquee-wrap">
    <div class="ai-marquee-track">
      <div class="ai-marquee-item">🧠 <strong>AyA-AI</strong> — Your 24/7 Study Partner</div>
      <div class="ai-marquee-item">📝 <strong>Unlimited Mock Tests</strong> — Zero Cost, Infinite Practice</div>
      <div class="ai-marquee-item">🚀 <strong>AI-Powered</strong> — Built by Your Tutor, Not a Corporation</div>
      <div class="ai-marquee-item">⚡ <strong>Instant Answers</strong> — Any Subject, Any Time</div>
      <div class="ai-marquee-item">🏆 <strong>NEET / JEE Ready</strong> — Targeted Practice Engine</div>
      <div class="ai-marquee-item">🌐 <strong>100% Free</strong> — No Subscriptions, No Catch</div>
      <div class="ai-marquee-item">🧠 <strong>AyA-AI</strong> — Your 24/7 Study Partner</div>
      <div class="ai-marquee-item">📝 <strong>Unlimited Mock Tests</strong> — Zero Cost, Infinite Practice</div>
      <div class="ai-marquee-item">🚀 <strong>AI-Powered</strong> — Built by Your Tutor, Not a Corporation</div>
      <div class="ai-marquee-item">⚡ <strong>Instant Answers</strong> — Any Subject, Any Time</div>
      <div class="ai-marquee-item">🏆 <strong>NEET / JEE Ready</strong> — Targeted Practice Engine</div>
      <div class="ai-marquee-item">🌐 <strong>100% Free</strong> — No Subscriptions, No Catch</div>
    </div>
  </div>
  <div class="ai-corner-hero">
    <div class="ai-particles" id="aiParticles"></div>
    <div style="position:relative;z-index:1;">
      <div class="ai-badge"><div class="ai-badge-dot"></div>Now Live — Powered by The Molecular Man</div>
      <div class="ai-orb-container"><div class="ai-orb">🤖<div class="orb-dot"></div></div></div>
      <div class="ai-hero-title">AyA-AI</div>
      <div class="ai-hero-sub-title">Your Intelligent Study Companion</div>
      <div class="ai-hero-desc">Meet <strong style="color:#c4b5fd;">AyA</strong> — the AI that never sleeps, never judges, and answers every question the moment you ask it. Coupled with an <strong style="color:#fbbf24;">Unlimited Mock Test Engine</strong>, this is the most powerful free study tool ever built for Indian students.</div>
      <div class="ai-stats">
        <div class="ai-stat"><div class="ai-stat-val">∞</div><div class="ai-stat-lbl">Mock Tests</div></div>
        <div class="ai-stat"><div class="ai-stat-val">24/7</div><div class="ai-stat-lbl">Availability</div></div>
        <div class="ai-stat"><div class="ai-stat-val">₹0</div><div class="ai-stat-lbl">Cost Forever</div></div>
        <div class="ai-stat"><div class="ai-stat-val">10+</div><div class="ai-stat-lbl">Subjects Covered</div></div>
      </div>
      <a href="https://molecularmanapp.streamlit.app/" target="_blank" class="ai-launch-btn"><span class="btn-icon">🚀</span>Launch AI Engine</a>
      <div style="margin-top:18px;font-size:.8rem;color:#64748b;letter-spacing:1px;text-transform:uppercase;">Free Forever · No Login Required · Instant Access</div>
    </div>
  </div>
  <h2 class="section-title" style="text-align:center;background:linear-gradient(to right,#c4b5fd,#93c5fd);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">What's Inside the AI Engine?</h2>
  <div class="ai-features-grid">
    <div class="ai-feat-card"><span class="ai-feat-icon">🧠</span><div class="ai-feat-title">AyA-AI Assistant</div><div class="ai-feat-desc">Ask any science or maths question and get a clear, detailed explanation instantly. No waiting, no judgement, just answers — at 3AM if you need them.</div><span class="ai-feat-tag">Always On</span></div>
    <div class="ai-feat-card"><span class="ai-feat-icon">📝</span><div class="ai-feat-title">Unlimited Mock Tests</div><div class="ai-feat-desc">Generate fresh, unique test papers for any subject and class — CBSE, ICSE, IB, State Board — every single time. Never run out of practice material again.</div><span class="ai-feat-tag">Infinite</span></div>
    <div class="ai-feat-card"><span class="ai-feat-icon">🏆</span><div class="ai-feat-title">NEET / JEE Prep Mode</div><div class="ai-feat-desc">Targeted question generation focused on competitive exam patterns. Practice exactly the style of questions that appear in real entrance exams.</div><span class="ai-feat-tag">Exam Ready</span></div>
    <div class="ai-feat-card"><span class="ai-feat-icon">⚡</span><div class="ai-feat-title">Instant Doubt Clearing</div><div class="ai-feat-desc">Stuck on a concept at midnight? AyA breaks down the toughest topics — organic chemistry, thermodynamics, calculus — into simple, understandable steps.</div><span class="ai-feat-tag">Step-by-Step</span></div>
    <div class="ai-feat-card"><span class="ai-feat-icon">📊</span><div class="ai-feat-title">Custom Difficulty Engine</div><div class="ai-feat-desc">Choose from beginner, intermediate, or advanced difficulty. The engine adapts your practice to where you actually are in the syllabus.</div><span class="ai-feat-tag">Adaptive</span></div>
    <div class="ai-feat-card"><span class="ai-feat-icon">🌐</span><div class="ai-feat-title">Zero Cost. Always.</div><div class="ai-feat-desc">Built by a tutor who believes quality education shouldn't cost a fortune. No subscriptions, no credits, no hidden fees. Ever. This is our promise.</div><span class="ai-feat-tag">100% Free</span></div>
  </div>
  <div class="ai-divider"></div>
  <div style="text-align:center;padding:40px 0;">
    <div style="font-family:'Rajdhani',sans-serif;font-size:clamp(1.3rem,3vw,2rem);font-weight:900;margin-bottom:12px;color:#e2e8f0;">Stop Buying Test Series.<br><span style="background:linear-gradient(to right,#fbbf24,#f59e0b);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">Start Generating Them.</span></div>
    <div style="color:#94a3b8;font-size:1rem;max-width:500px;margin:0 auto 28px;">Join thousands of students already using the Molecular Man AI Engine to study smarter, not harder.</div>
    <a href="https://molecularmanapp.streamlit.app/" target="_blank" class="ai-launch-btn" style="font-size:1.2rem;padding:16px 42px;"><span>🤖</span> Open AyA-AI Now</a>
  </div>
</div>
</div>

<!-- ════ MODAL: Live Class Link ════ -->
<div id="lc-link-modal" class="lc-modal-overlay" onclick="if(event.target===this)lcCloseModal('lc-link-modal')">
  <div class="lc-modal">
    <h4>🔗 Set Live Class Link</h4>
    <div class="form-group"><label>Paste meeting link (leave empty to clear)</label><input type="text" id="modal-link-input" placeholder="https://meet.google.com/..."></div>
    <p style="font-size:.8rem;color:#a0aec0;margin-top:-8px;margin-bottom:12px;">⏰ Link will automatically expire after <strong style="color:var(--gold);">10 hours</strong>. Admin can reset manually at any time.</p>
    <input type="hidden" id="modal-link-target">
    <div class="lc-modal-actions">
      <button class="cancel" onclick="lcCloseModal('lc-link-modal')">Cancel</button>
      <button class="confirm" onclick="lcSaveLink()">Save &amp; Set</button>
    </div>
  </div>
</div>

<!-- ════ MODAL: Send Message / Notification ════ -->
<div id="lc-msg-modal" class="lc-modal-overlay" onclick="if(event.target===this)lcCloseModal('lc-msg-modal')">
  <div class="lc-modal">
    <h4>💬 Send Message to Student</h4>
    <div class="form-group">
      <label>Message</label>
      <textarea id="modal-msg-input" placeholder="Type a message or assignment note..." style="width:100%;background:rgba(255,255,255,.1);color:#fff;border:1px solid rgba(255,255,255,.3);border-radius:8px;padding:10px 14px;font-family:'Exo 2',sans-serif;font-size:.95rem;outline:none;resize:vertical;min-height:80px;"></textarea>
    </div>
    <input type="hidden" id="modal-msg-target">
    <!-- Student replies preview -->
    <div id="modal-msg-replies" style="margin-top:12px;"></div>
    <div class="lc-modal-actions">
      <button class="cancel" onclick="lcCloseModal('lc-msg-modal')">Cancel</button>
      <button class="confirm" onclick="lcSendMessage()">Send</button>
    </div>
  </div>
</div>

<!-- ════ MODAL: Upload Test Paper ════ -->
<div id="lc-test-modal" class="lc-modal-overlay" onclick="if(event.target===this)lcCloseModal('lc-test-modal')">
  <div class="lc-modal">
    <h4>📄 Upload Test Paper &amp; Marks</h4>
    <div class="form-group"><label>Test Title</label><input type="text" id="modal-test-title" placeholder="e.g. Chapter 5 — Organic Chemistry Test"></div>
    <div class="form-group"><label>Test Paper (PDF / Doc / Image)</label><input type="file" id="modal-test-file" accept=".pdf,.doc,.docx,.jpg,.jpeg,.png"><div id="modal-test-file-status" class="upload-status"></div></div>
    <div class="form-group"><label>Marks Achieved <span style="color:#888;font-size:.8rem;">(optional — can be added later)</span></label><input type="text" id="modal-test-marks" placeholder="e.g. 45/60 — leave blank if not yet graded"></div>
    <input type="hidden" id="modal-test-target">
    <div class="lc-modal-actions">
      <button class="cancel" onclick="lcCloseModal('lc-test-modal')">Cancel</button>
      <button class="confirm" onclick="lcUploadTest()">Upload &amp; Save</button>
    </div>
  </div>
</div>

<!-- ════ MODAL: Manage Student (marks, resets, replies) ════ -->
<div id="lc-manage-modal" class="lc-modal-overlay" onclick="if(event.target===this)lcCloseModal('lc-manage-modal')">
  <div class="lc-modal" style="max-width:620px;">
    <h4>⚙️ Manage Student: <span id="manage-student-name" style="color:var(--cyan);"></span></h4>
    <input type="hidden" id="manage-student-username">

    <!-- Tests with mark editing -->
    <div style="margin-bottom:16px;">
      <div style="font-family:'Rajdhani',sans-serif;font-size:1rem;font-weight:700;color:#a0aec0;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;">📝 Tests &amp; Mark Management</div>
      <div id="manage-tests-list"></div>
    </div>

    <!-- Reset Panel -->
    <div class="reset-panel">
      <h5>🔄 Manual Reset Controls</h5>
      <div class="reset-btn-row">
        <button class="reset-btn r-link" onclick="lcResetField('liveLink','')">🔗 Clear Live Link</button>
        <button class="reset-btn r-notifs" onclick="lcResetField('notifications',[])">🔔 Clear Notifications</button>
        <button class="reset-btn r-tests" onclick="lcResetField('tests',[])">📝 Clear All Tests</button>
        <button class="reset-btn r-all" onclick="lcResetAll()">⚠️ Reset Everything</button>
      </div>
      <p style="font-size:.72rem;color:#888;margin-top:10px;">⚠️ Reset actions are permanent and cannot be undone. Student account is preserved.</p>
    </div>

    <!-- Private Study Notes -->
    <div style="margin-top:20px;border-top:1px solid rgba(255,255,255,.1);padding-top:18px;">
      <div style="font-family:'Rajdhani',sans-serif;font-size:1rem;font-weight:700;color:#a0aec0;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px;">📚 Private Study Notes for this Student</div>
      <div class="notes-form">
        <div class="form-group"><label>Subject</label>
          <select id="note-subject">
            <option value="Maths">Maths</option><option value="Chemistry">Chemistry</option><option value="Physics">Physics</option><option value="Biology">Biology</option>
          </select>
        </div>
        <div class="form-group"><label>Note Title / Description</label><input type="text" id="note-title" placeholder="e.g. Organic Chemistry — Chapter 5 Summary"></div>
        <div class="form-group" style="grid-column:1/-1;"><label>File Link (URL)</label><input type="url" id="note-link" placeholder="https://drive.google.com/…"></div>
        <button class="lc-submit" onclick="lcAddStudentNote()">➕ Add Note</button>
      </div>
      <div class="notes-list" id="manage-notes-list"></div>
    </div>

    <div class="lc-modal-actions" style="margin-top:12px;">
      <button class="cancel" onclick="lcCloseModal('lc-manage-modal')">Close</button>
    </div>
  </div>
</div>

<!-- FOOTER -->
<footer>
  <div class="footer-text">PRECISE • PASSIONATE • PROFESSIONAL</div>
  <div class="footer-copy">© 2026 The Molecular Man Expert Tuition Solutions | Mohammed Salmaan M. All Rights Reserved.</div>
</footer>

<!-- ════ STUDENT MESSAGES MODAL (Admin View) ════ -->
<div id="lc-student-msgs-modal" class="lc-modal-overlay" onclick="if(event.target===this)lcCloseModal('lc-student-msgs-modal')">
  <div class="lc-modal">
    <button class="modal-close" onclick="lcCloseModal('lc-student-msgs-modal')">✕</button>
    <h3 style="font-family:'Rajdhani',sans-serif;font-size:1.2rem;margin-bottom:4px;">📩 Messages from <span id="student-msgs-name"></span></h3>
    <input type="hidden" id="student-msgs-username">
    <p style="font-size:.8rem;color:#94a3b8;margin-bottom:16px;">Messages initiated by the student. Reply via the 💬 Msg button.</p>
    <div id="student-msgs-list" style="max-height:340px;overflow-y:auto;"></div>
    <div class="lc-modal-actions" style="margin-top:14px;">
      <button class="cancel" onclick="lcCloseModal('lc-student-msgs-modal')">Close</button>
    </div>
  </div>
</div>

<script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script>
<script>
/* ══════════════════════════════════════════════════════════════════
   MAIN APPLICATION SCRIPT — v4 (schema-safe, fully defensive)
   
   SUPABASE SETUP — run this SQL in your Supabase SQL Editor:
   ─────────────────────────────────────────────────────────────────
   -- 1. Add missing columns to students table
   ALTER TABLE students
     ADD COLUMN IF NOT EXISTS "liveLinkSetAt"    TEXT,
     ADD COLUMN IF NOT EXISTS "studyNotes"       JSONB DEFAULT '[]'::jsonb,
     ADD COLUMN IF NOT EXISTS "liveLink"         TEXT,
     ADD COLUMN IF NOT EXISTS "notifications"    JSONB DEFAULT '[]'::jsonb,
     ADD COLUMN IF NOT EXISTS "tests"            JSONB DEFAULT '[]'::jsonb,
     ADD COLUMN IF NOT EXISTS "photo"            TEXT,
     ADD COLUMN IF NOT EXISTS "class"            TEXT,
     ADD COLUMN IF NOT EXISTS "board"            TEXT,
     ADD COLUMN IF NOT EXISTS "package"          TEXT,
     ADD COLUMN IF NOT EXISTS "studentMessages"  JSONB DEFAULT '[]'::jsonb;

   -- 2. Create public_downloads table
   CREATE TABLE IF NOT EXISTS public_downloads (
     id          BIGSERIAL PRIMARY KEY,
     title       TEXT NOT NULL,
     board       TEXT NOT NULL,
     class       TEXT NOT NULL,
     subject     TEXT NOT NULL,
     link        TEXT NOT NULL,
     created_at  TIMESTAMPTZ DEFAULT NOW()
   );
   ALTER TABLE public_downloads ENABLE ROW LEVEL SECURITY;
   DROP POLICY IF EXISTS "Public read" ON public_downloads;
   DROP POLICY IF EXISTS "Service role write" ON public_downloads;
   CREATE POLICY "Public read"        ON public_downloads FOR SELECT USING (true);
   CREATE POLICY "Service role write" ON public_downloads FOR ALL    USING (true);
   ─────────────────────────────────────────────────────────────────
══════════════════════════════════════════════════════════════════ */

// ══ CONTACT FORM ═══════════════════════════════════════════════
function checkForm() {
  var name  = document.getElementById('f-name').value.trim();
  var phone = document.getElementById('f-phone').value.trim();
  var msg   = document.getElementById('f-msg').value.trim();
  document.getElementById('sendBtn').classList.toggle('ready', !!(name && phone && msg));
}
function sendEmail() {
  var name  = document.getElementById('f-name').value.trim();
  var phone = document.getElementById('f-phone').value.trim();
  var grade = document.getElementById('f-grade').value;
  var msg   = document.getElementById('f-msg').value.trim();
  window.location.href = 'mailto:the.molecularmanexpert@gmail.com?subject='
    + encodeURIComponent('Tuition Inquiry from ' + name)
    + '&body=' + encodeURIComponent('Name: ' + name + '\nPhone: ' + phone + '\nGrade: ' + grade + '\n\nMessage:\n' + msg);
}

// ══ AI CORNER PARTICLES ════════════════════════════════════════
(function () {
  var c = document.getElementById('aiParticles');
  if (!c) return;
  var cols = ['#ffd700','#a78bfa','#93c5fd','#34d399','#f472b6'];
  for (var i = 0; i < 18; i++) {
    var el = document.createElement('div');
    el.className = 'ai-particle';
    el.style.left   = Math.random() * 100 + '%';
    el.style.top    = Math.random() * 100 + '%';
    el.style.background       = cols[Math.floor(Math.random() * cols.length)];
    el.style.width  = el.style.height = (Math.random() * 5 + 2) + 'px';
    el.style.animationDuration = (Math.random() * 6 + 4) + 's';
    el.style.animationDelay    = (Math.random() * 4) + 's';
    c.appendChild(el);
  }
})();

// ══ CONSTANTS & STATE ══════════════════════════════════════════
var lcLoggedStudent      = null;
var LC_LINK_EXPIRY_HOURS = 10;
var SUBJECT_ICONS = { Maths:'📐', Physics:'⚛️', Chemistry:'🧪', Biology:'🌿', Science:'🔬' };

/* ── safe JSON parse helper ─────────────────────────────────────
   Supabase returns JSONB columns as already-parsed JS objects.
   But if the column came back as a string or null, we handle it. */
function safeArr(val) {
  if (!val) return [];
  if (Array.isArray(val)) return val;
  try { var p = JSON.parse(val); return Array.isArray(p) ? p : []; } catch(e) { return []; }
}

// ══ SUPABASE HELPERS ═══════════════════════════════════════════
async function lcGetStudents() {
  var res = await getSupabase().from(STUDENTS_TABLE).select('*');
  if (res.error) throw new Error(res.error.message);
  return res.data || [];
}
async function lcGetStudent(username) {
  var res = await getSupabase().from(STUDENTS_TABLE).select('*').eq('username', username).single();
  if (res.error) throw new Error(res.error.message);
  return res.data;
}
async function lcSaveStudent(s) {
  var payload = {};
  Object.keys(s).forEach(function(k){ if (k !== '_id') payload[k] = s[k]; });
  var res = await getSupabase().from(STUDENTS_TABLE).upsert(payload, { onConflict: 'username' });
  if (res.error) throw new Error(res.error.message);
}
async function lcUpdateStudent(username, updates) {
  var res = await getSupabase().from(STUDENTS_TABLE).update(updates).eq('username', username);
  if (res.error) throw new Error(res.error.message);
}
async function lcDeleteStudentByUsername(username) {
  var res = await getSupabase().from(STUDENTS_TABLE).delete().eq('username', username);
  if (res.error) throw new Error('Cannot delete student: ' + res.error.message);
}
async function lcUploadFile(bucket, path, file) {
  var sb = getSupabase();
  var up = await sb.storage.from(bucket).upload(path, file, { upsert: true });
  if (up.error) throw new Error('Upload failed: ' + up.error.message);
  return sb.storage.from(bucket).getPublicUrl(path).data.publicUrl;
}

// ══ PUBLIC DOWNLOADS HELPERS ═══════════════════════════════════
async function pdlGetAll() {
  var res = await getSupabase().from(PUB_DL_TABLE).select('*').order('created_at', { ascending: false });
  if (res.error) throw new Error(res.error.message);
  return res.data || [];
}
async function pdlInsert(entry) {
  var res = await getSupabase().from(PUB_DL_TABLE).insert(entry);
  if (res.error) throw new Error(res.error.message);
}
async function pdlDeleteRow(id) {
  var res = await getSupabase().from(PUB_DL_TABLE).delete().eq('id', id);
  if (res.error) throw new Error(res.error.message);
}

// ══ UTILITY ════════════════════════════════════════════════════
function lcIsLinkExpired(linkSetAt) {
  if (!linkSetAt) return true;
  return (Date.now() - new Date(linkSetAt).getTime()) > LC_LINK_EXPIRY_HOURS * 3600 * 1000;
}

function lcShowView(viewId) {
  document.querySelectorAll('#page-live-class .lc-view').forEach(function(v){ v.classList.remove('active'); });
  var el = document.getElementById(viewId);
  if (el) el.classList.add('active');
  document.querySelectorAll('.lc-error').forEach(function(e){ e.style.display='none'; });
}

function lcCloseModal(id) {
  var el = document.getElementById(id);
  if (el) el.classList.remove('show');
}

var _loadingTimer = null;
function lcSetLoading(on) {
  var el = document.getElementById('lc-loading-overlay');
  if (!el) {
    el = document.createElement('div');
    el.id = 'lc-loading-overlay';
    el.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:99999;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:12px;pointer-events:all;';
    el.innerHTML = '<div style="color:#fff;font-family:Rajdhani,sans-serif;font-size:1.4rem;letter-spacing:2px;">⏳ Loading…</div>'
      + '<div id="lc-loading-msg" style="color:#aaa;font-size:.85rem;font-family:\'Exo 2\',sans-serif;max-width:300px;text-align:center;"></div>';
    document.body.appendChild(el);
  }
  if (on) {
    el.style.display = 'flex';
    clearTimeout(_loadingTimer);
    _loadingTimer = setTimeout(function(){ lcSetLoading(false); }, 20000);
  } else {
    el.style.display = 'none';
    clearTimeout(_loadingTimer);
  }
}
function lcSetLoadingMsg(msg) {
  var el = document.getElementById('lc-loading-msg');
  if (el) el.textContent = msg;
}
function showUploadStatus(id, type, msg) {
  var el = document.getElementById(id);
  if (!el) return;
  el.className = 'upload-status ' + type;
  el.textContent = msg;
}

// ══ AUTH ═══════════════════════════════════════════════════════
function lcAdminLogin() {
  var u = document.getElementById('admin-user').value.trim();
  var p = document.getElementById('admin-pass').value.trim();
  if (u === 'Admin' && p === 'qwerty1234') {
    document.getElementById('admin-user').value = '';
    document.getElementById('admin-pass').value = '';
    lcShowView('lc-admin-dash');
    lcRenderStudentTable();
    pdlRenderAdminTable();
    lcRequestNotifPermission();
    lcStartPollingAdmin();
    lcRefreshInbox();
  } else {
    var err = document.getElementById('admin-error');
    if (err) err.style.display = 'block';
  }
}

async function lcStudentLogin() {
  var u = document.getElementById('stu-user').value.trim();
  var p = document.getElementById('stu-pass').value.trim();
  if (!u || !p) { alert('Please enter your username and password.'); return; }
  lcSetLoading(true);
  lcSetLoadingMsg('Verifying credentials…');
  try {
    var students = await lcGetStudents();
    var found = null;
    for (var i = 0; i < students.length; i++) {
      if (students[i].username === u && students[i].password === p) { found = students[i]; break; }
    }
    if (found) {
      document.getElementById('stu-user').value = '';
      document.getElementById('stu-pass').value = '';
      lcLoggedStudent = found.username;
      localStorage.setItem('lc_logged_student', found.username);
      lcShowView('lc-student-dash');
      lcRenderStudentDash(found.username);
      lcRequestNotifPermission();
      lcStartPollingStudent(found.username);
    } else {
      var err = document.getElementById('student-error');
      if (err) err.style.display = 'block';
    }
  } catch(err) { alert('❌ Login error: ' + err.message); }
  finally { lcSetLoading(false); }
}

function lcLogout() {
  lcLoggedStudent = null;
  localStorage.removeItem('lc_logged_student');
  lcStopPollingStudent();
  lcStopPollingAdmin();
  lcShowView('lc-role-select');
}

// ══ CREATE STUDENT ═════════════════════════════════════════════
async function lcCreateStudent() {
  var photoFile = document.getElementById('cs-photo-file').files[0];
  var name      = document.getElementById('cs-name').value.trim();
  var username  = document.getElementById('cs-username').value.trim();
  var password  = document.getElementById('cs-password').value.trim();
  var cls       = document.getElementById('cs-class').value.trim();
  var board     = document.getElementById('cs-board').value;
  var pkg       = document.getElementById('cs-package').value.trim();
  if (!name || !username || !password) { alert('Name, Username and Password are required.'); return; }
  lcSetLoading(true);
  lcSetLoadingMsg('Checking for duplicate username…');
  var photoUrl = '';
  try {
    var students = await lcGetStudents();
    for (var i = 0; i < students.length; i++) {
      if (students[i].username === username) { lcSetLoading(false); alert('Username already exists!'); return; }
    }
    if (photoFile) {
      lcSetLoadingMsg('Uploading student photo…');
      showUploadStatus('cs-photo-status','uploading','⏳ Uploading photo…');
      try {
        var ext = photoFile.name.split('.').pop();
        photoUrl = await lcUploadFile(AVATARS_BUCKET, username + '_' + Date.now() + '.' + ext, photoFile);
        showUploadStatus('cs-photo-status','success','✅ Photo uploaded!');
      } catch(e) { showUploadStatus('cs-photo-status','error','❌ ' + e.message); }
    }
    lcSetLoadingMsg('Saving student…');
    await lcSaveStudent({
      photo: photoUrl, name: name, username: username, password: password,
      class: cls, board: board, package: pkg,
      liveLink: '', liveLinkSetAt: null,
      notifications: [], tests: [], studyNotes: []
    });
    ['cs-name','cs-username','cs-password','cs-class','cs-package'].forEach(function(id){
      document.getElementById(id).value = '';
    });
    document.getElementById('cs-photo-file').value = '';
    document.getElementById('cs-photo-status').className = 'upload-status';
    lcSetLoading(false);
    lcRenderStudentTable();
    alert('✅ Student "' + name + '" created!');
  } catch(err) { lcSetLoading(false); alert('❌ ' + err.message); }
}

// ══ ADMIN STUDENT TABLE ════════════════════════════════════════
async function lcRenderStudentTable() {
  var tbody = document.getElementById('lc-student-tbody');
  var empty = document.getElementById('lc-no-students');
  if (!tbody) return;
  tbody.innerHTML = '<tr><td colspan="8" style="text-align:center;color:#a0aec0;padding:20px;">Loading from Supabase…</td></tr>';
  if (empty) empty.style.display = 'none';
  try {
    var students = await lcGetStudents();
    if (!students.length) {
      tbody.innerHTML = '';
      if (empty) empty.style.display = 'block';
      return;
    }
    if (empty) empty.style.display = 'none';
    tbody.innerHTML = students.map(function(s) {
      var expired   = lcIsLinkExpired(s.liveLinkSetAt);
      var linkBadge = s.liveLink
        ? (expired ? '<span style="color:#ff6b6b;font-size:.8rem;">⚠️ Expired</span>'
                   : '<span style="color:#48ff00;font-size:.8rem;">✅ Active</span>')
        : '<span style="color:#888;font-size:.8rem;">None</span>';
      var notifs     = safeArr(s.notifications);
      var replyCount = notifs.filter(function(n){ return n.reply; }).length;
      var replyBadge = replyCount ? '<span class="student-reply-badge">' + replyCount + '</span>' : '';
      var stuMsgs    = Array.isArray(s.studentMessages) ? s.studentMessages : [];
      var unreadMsgs = stuMsgs.filter(function(m){ return !m.read; }).length;
      var inboxBadge = unreadMsgs ? '<span class="student-reply-badge" style="background:#ef4444;">' + unreadMsgs + '</span>' : '';
      var uSafe = s.username.replace(/'/g, "\\'");
      return '<tr>'
        + '<td>' + (s.photo ? '<img src="' + s.photo + '" alt="' + s.name + '" style="width:36px;height:36px;border-radius:50%;object-fit:cover;">' : '<span style="color:#666;font-size:.8rem;">N/A</span>') + '</td>'
        + '<td style="font-weight:600;">' + s.name + '</td>'
        + '<td style="color:#a0aec0;">' + s.username + '</td>'
        + '<td>' + (s.class || '—') + '</td>'
        + '<td>' + (s.board || '—') + '</td>'
        + '<td><span style="color:var(--cyan);">' + (s.package || '—') + '</span></td>'
        + '<td>' + linkBadge + '</td>'
        + '<td><div class="actions">'
        + '<button class="lc-action-btn link-action"   onclick="lcOpenLinkModal(\''   + uSafe + '\')">🔗 Link</button>'
        + '<button class="lc-action-btn msg-action"    onclick="lcOpenMsgModal(\''    + uSafe + '\')">💬 Msg' + replyBadge + '</button>'
        + '<button class="lc-action-btn msg-action"    onclick="lcOpenStudentMessages(\'' + uSafe + '\')" style="background:rgba(14,165,233,.15);border-color:rgba(14,165,233,.4);">📩 Inbox' + inboxBadge + '</button>'
        + '<button class="lc-action-btn test-action"   onclick="lcOpenTestModal(\''   + uSafe + '\')">📄 Test</button>'
        + '<button class="lc-action-btn manage-action" onclick="lcOpenManageModal(\'' + uSafe + '\')">⚙️ Manage</button>'
        + '<button class="lc-action-btn del-action"    onclick="lcDeleteStudent(\''   + uSafe + '\')">🗑️</button>'
        + '</div></td>'
        + '</tr>';
    }).join('');
  } catch(err) {
    tbody.innerHTML = '<tr><td colspan="8" style="text-align:center;color:#ff6b6b;padding:20px;">❌ ' + err.message + '</td></tr>';
  }
}

async function lcDeleteStudent(username) {
  if (!confirm('Delete student "' + username + '" permanently?')) return;
  lcSetLoading(true);
  try { await lcDeleteStudentByUsername(username); lcRenderStudentTable(); }
  catch(err) { alert('❌ ' + err.message); }
  finally { lcSetLoading(false); }
}

// ══ MODAL: LIVE LINK ═══════════════════════════════════════════
function lcOpenLinkModal(username) {
  document.getElementById('modal-link-input').value  = '';
  document.getElementById('modal-link-target').value = username;
  document.getElementById('lc-link-modal').classList.add('show');
  lcGetStudent(username).then(function(s) {
    if (s) document.getElementById('modal-link-input').value = s.liveLink || '';
  }).catch(function(){});
}
async function lcSaveLink() {
  var username = document.getElementById('modal-link-target').value;
  var link     = document.getElementById('modal-link-input').value.trim();
  lcSetLoading(true);
  lcSetLoadingMsg('Saving link…');
  try {
    await lcUpdateStudent(username, {
      liveLink: link,
      liveLinkSetAt: link ? new Date().toISOString() : null
    });
    lcCloseModal('lc-link-modal');
    lcRenderStudentTable();
  } catch(err) { alert('❌ ' + err.message); }
  finally { lcSetLoading(false); }
}

// ══ MODAL: MESSAGE ═════════════════════════════════════════════
function lcOpenMsgModal(username) {
  document.getElementById('modal-msg-input').value   = '';
  document.getElementById('modal-msg-target').value  = username;
  document.getElementById('modal-msg-replies').innerHTML = '';
  document.getElementById('lc-msg-modal').classList.add('show');
  lcGetStudent(username).then(function(s) {
    if (!s) return;
    var notifs = safeArr(s.notifications).filter(function(n){ return n.reply; });
    if (!notifs.length) return;
    var html = '<div style="margin-bottom:10px;font-size:.82rem;color:#94a3b8;font-family:Rajdhani,sans-serif;text-transform:uppercase;letter-spacing:1px;">Student Replies</div>';
    notifs.forEach(function(n) {
      html += '<div class="reply-bubble">'
        + '<div style="color:#ffd700;font-size:.78rem;font-weight:700;margin-bottom:4px;">📩 Re: '
        + n.text.substring(0,50) + (n.text.length > 50 ? '…' : '') + '</div>'
        + '<div>' + n.reply + '</div>'
        + '<div class="reply-meta">' + (n.replyAt || '') + '</div>'
        + '</div>';
    });
    document.getElementById('modal-msg-replies').innerHTML = html;
  }).catch(function(){});
}
async function lcSendMessage() {
  var username = document.getElementById('modal-msg-target').value;
  var msg      = document.getElementById('modal-msg-input').value.trim();
  if (!msg) { alert('Please type a message.'); return; }
  lcSetLoading(true);
  try {
    var s        = await lcGetStudent(username);
    var existing = safeArr(s ? s.notifications : []);
    await lcUpdateStudent(username, {
      notifications: existing.concat([{
        id: Date.now(), text: msg,
        time: new Date().toLocaleString(),
        reply: null, replyAt: null
      }])
    });
    lcCloseModal('lc-msg-modal');
    alert('✅ Message sent to ' + (s ? s.name : username) + '!');
  } catch(err) { alert('❌ ' + err.message); }
  finally { lcSetLoading(false); }
}

// ══ MODAL: UPLOAD TEST ═════════════════════════════════════════
function lcOpenTestModal(username) {
  document.getElementById('modal-test-title').value  = '';
  document.getElementById('modal-test-file').value   = '';
  document.getElementById('modal-test-marks').value  = '';
  document.getElementById('modal-test-target').value = username;
  var st = document.getElementById('modal-test-file-status');
  st.className = 'upload-status'; st.textContent = '';
  document.getElementById('lc-test-modal').classList.add('show');
}
async function lcUploadTest() {
  var username = document.getElementById('modal-test-target').value;
  var title    = document.getElementById('modal-test-title').value.trim();
  var file     = document.getElementById('modal-test-file').files[0];
  var marks    = document.getElementById('modal-test-marks').value.trim();
  if (!title) { alert('Please enter a test title.'); return; }
  if (!file)  { alert('Please select a file to upload.'); return; }
  lcSetLoading(true);
  lcSetLoadingMsg('Uploading test paper…');
  showUploadStatus('modal-test-file-status','uploading','⏳ Uploading file…');
  try {
    var ext      = file.name.split('.').pop();
    var filePath = username + '/' + Date.now() + '_' + title.replace(/\s+/g,'_') + '.' + ext;
    var fileUrl  = await lcUploadFile(TESTS_BUCKET, filePath, file);
    showUploadStatus('modal-test-file-status','success','✅ File uploaded!');
    var s        = await lcGetStudent(username);
    var existing = safeArr(s ? s.tests : []);
    await lcUpdateStudent(username, {
      tests: existing.concat([{
        id: Date.now(), title: title, fileUrl: fileUrl,
        marks: marks || 'Pending',
        uploadedAt: new Date().toLocaleString(),
        answerSheet: null
      }])
    });
    lcCloseModal('lc-test-modal');
    alert('✅ Test uploaded for ' + (s ? s.name : username) + '!');
  } catch(err) {
    showUploadStatus('modal-test-file-status','error','❌ ' + err.message);
    alert('❌ ' + err.message);
  }
  finally { lcSetLoading(false); }
}

// ══ MODAL: MANAGE STUDENT ══════════════════════════════════════
async function lcOpenManageModal(username) {
  var modal = document.getElementById('lc-manage-modal');
  if (!modal) return;
  document.getElementById('manage-student-username').value = username;
  document.getElementById('manage-student-name').textContent = 'Loading…';
  document.getElementById('manage-tests-list').innerHTML = '<div style="color:#a0aec0;font-size:.85rem;padding:10px;">Loading…</div>';
  var nl = document.getElementById('manage-notes-list');
  if (nl) nl.innerHTML = '<div style="color:#a0aec0;font-size:.85rem;padding:8px 0;">Loading…</div>';
  var nt = document.getElementById('note-title'); if (nt) nt.value = '';
  var nk = document.getElementById('note-link');  if (nk) nk.value = '';
  modal.classList.add('show');
  try {
    var s     = await lcGetStudent(username);
    document.getElementById('manage-student-name').textContent = s.name;
    var tests = safeArr(s.tests);
    if (!tests.length) {
      document.getElementById('manage-tests-list').innerHTML =
        '<div style="color:#888;font-size:.85rem;padding:10px 0;">No tests uploaded yet.</div>';
    } else {
      var uSafe = username.replace(/'/g,"\\'");
      document.getElementById('manage-tests-list').innerHTML = tests.map(function(t, i) {
        var ans = t.answerSheet
          ? '<a class="student-answer-link-view" href="' + t.answerSheet + '" target="_blank">📎 Answer: ' + t.answerSheet + '</a>'
          : '<span style="font-size:.72rem;color:#666;margin-top:4px;display:block;">No answer sheet yet.</span>';
        return '<div class="manage-test-row">'
          + '<div class="test-title-row">'
          + '<div><span class="test-title-txt">' + t.title + '</span>'
          + '<span style="font-size:.75rem;color:#888;margin-left:8px;">' + (t.uploadedAt||'') + '</span></div>'
          + '<div style="display:flex;gap:6px;align-items:center;flex-wrap:wrap;">'
          + '<input type="text" class="manage-test-mark-edit" id="mark-edit-' + i + '" value="' + (t.marks||'Pending') + '" placeholder="e.g. 45/60">'
          + '<button class="manage-test-save-btn" onclick="lcSaveMark(\'' + uSafe + '\',' + i + ')">💾 Save</button>'
          + '<button class="manage-test-del-btn"  onclick="lcDeleteTest(\'' + uSafe + '\',' + i + ')">🗑️</button>'
          + '</div></div>' + ans + '</div>';
      }).join('');
    }
    _renderManageNotesList(username, safeArr(s.studyNotes));
  } catch(err) {
    document.getElementById('manage-student-name').textContent = 'Error';
    alert('❌ ' + err.message);
  }
}

async function lcSaveMark(username, idx) {
  var newMark = document.getElementById('mark-edit-' + idx);
  if (!newMark || !newMark.value.trim()) { alert('Enter a mark value.'); return; }
  lcSetLoading(true);
  try {
    var s     = await lcGetStudent(username);
    var tests = safeArr(s.tests).slice();
    if (!tests[idx]) { alert('Test not found.'); return; }
    tests[idx] = Object.assign({}, tests[idx], { marks: newMark.value.trim() });
    await lcUpdateStudent(username, { tests: tests });
    alert('✅ Mark updated!');
  } catch(err) { alert('❌ ' + err.message); }
  finally { lcSetLoading(false); }
}

async function lcDeleteTest(username, idx) {
  if (!confirm('Delete this test permanently?')) return;
  lcSetLoading(true);
  try {
    var s     = await lcGetStudent(username);
    var tests = safeArr(s.tests).slice();
    tests.splice(idx, 1);
    await lcUpdateStudent(username, { tests: tests });
    lcOpenManageModal(username);
  } catch(err) { alert('❌ ' + err.message); }
  finally { lcSetLoading(false); }
}

// ══ RESET CONTROLS ═════════════════════════════════════════════
async function lcResetField(field, value) {
  var username = document.getElementById('manage-student-username').value;
  if (!username) return;
  if (!confirm('Reset "' + field + '" for this student?')) return;
  lcSetLoading(true);
  try {
    var upd = {}; upd[field] = value;
    if (field === 'liveLink') upd.liveLinkSetAt = null;
    await lcUpdateStudent(username, upd);
    alert('✅ Reset complete.');
    lcCloseModal('lc-manage-modal');
    lcRenderStudentTable();
  } catch(err) { alert('❌ ' + err.message); }
  finally { lcSetLoading(false); }
}

async function lcResetAll() {
  var username = document.getElementById('manage-student-username').value;
  if (!username) return;
  if (!confirm('⚠️ Clear live link, ALL notifications and ALL tests for this student? This cannot be undone.')) return;
  lcSetLoading(true);
  try {
    await lcUpdateStudent(username, {
      liveLink: '', liveLinkSetAt: null, notifications: [], tests: []
    });
    alert('✅ Full reset complete. Student account is intact.');
    lcCloseModal('lc-manage-modal');
    lcRenderStudentTable();
  } catch(err) { alert('❌ ' + err.message); }
  finally { lcSetLoading(false); }
}

// ══ STUDENT DASHBOARD ══════════════════════════════════════════
async function lcRenderStudentDash(usernameOrObj) {
  lcSetLoading(true);
  lcSetLoadingMsg('Loading your dashboard…');
  try {
    var username = typeof usernameOrObj === 'string' ? usernameOrObj : usernameOrObj.username;
    var s = await lcGetStudent(username);
    if (!s) throw new Error('Could not load student data.');

    // Profile
    var photoEl = document.getElementById('sd-photo');
    if (s.photo) { photoEl.src = s.photo; photoEl.style.display = 'block'; }
    else { photoEl.style.display = 'none'; }
    document.getElementById('sd-name').textContent        = s.name || '';
    document.getElementById('sd-class-board').textContent = (s.class||'N/A') + ' • ' + (s.board||'N/A');
    document.getElementById('sd-package').textContent     = s.package || 'N/A';

    // Live class link
    var liveArea = document.getElementById('sd-live-area');
    if (s.liveLink && !lcIsLinkExpired(s.liveLinkSetAt)) {
      liveArea.innerHTML = '<a href="' + s.liveLink + '" target="_blank" class="lc-join-btn">🔴 JOIN LIVE CLASS NOW</a>';
    } else if (s.liveLink && lcIsLinkExpired(s.liveLinkSetAt)) {
      liveArea.innerHTML = '<div class="lc-no-class"><span class="icon">⏰</span><p style="color:#ff9999;">The class link has expired (10-hour limit).</p><p style="font-size:.8rem;color:#666;margin-top:4px;">Your tutor will set a new link before the next session.</p></div>';
    } else {
      liveArea.innerHTML = '<div class="lc-no-class"><span class="icon">📡</span><p>No active classes right now.</p><p style="font-size:.8rem;color:#666;margin-top:4px;">Check back later or contact your tutor.</p></div>';
    }

    // Tests & Marks
    var testsArea = document.getElementById('sd-tests-area');
    var tests     = safeArr(s.tests);
    if (tests.length) {
      var uSafe = username.replace(/'/g,"\\'");
      var rows  = tests.slice().reverse().map(function(t, i) {
        var realIdx = tests.length - 1 - i;
        var inputId = t.id || ('t' + realIdx);
        var ansCell = t.answerSheet
          ? '<a href="' + t.answerSheet + '" target="_blank" class="test-dl-btn" style="color:#c4b5fd;border-color:rgba(196,181,253,.35);">📎 View</a>'
          : '<div class="answer-sheet-row">'
              + '<input type="url" class="answer-sheet-input" id="as-' + inputId + '" placeholder="Paste answer sheet link…">'
              + '<button class="answer-sheet-btn" onclick="lcSubmitAnswerSheet(\'' + uSafe + '\',' + realIdx + ',\'' + inputId + '\')">Submit</button>'
            + '</div>';
        return '<tr>'
          + '<td style="color:#a0aec0;">' + (i+1) + '</td>'
          + '<td style="font-weight:600;">' + t.title + '</td>'
          + '<td><span class="marks-badge ' + (t.marks==='Pending'?'marks-pending':'') + '">' + (t.marks||'—') + '</span></td>'
          + '<td style="color:#a0aec0;font-size:.8rem;">' + (t.uploadedAt||'—') + '</td>'
          + '<td><a href="' + t.fileUrl + '" target="_blank" class="test-dl-btn">⬇️ Download</a></td>'
          + '<td>' + ansCell + '</td>'
          + '</tr>';
      }).join('');
      testsArea.innerHTML = '<div style="overflow-x:auto;"><table class="tests-table">'
        + '<thead><tr><th>#</th><th>Test Title</th><th>Marks</th><th>Date</th><th>Paper</th><th>Answer Sheet</th></tr></thead>'
        + '<tbody>' + rows + '</tbody></table></div>';
    } else {
      testsArea.innerHTML = '<div class="no-tests">📭 No test papers uploaded yet. Check back after your next assessment!</div>';
    }

    // Notifications
    var notifArea = document.getElementById('sd-notif-area');
    var notifs    = safeArr(s.notifications);
    if (notifs.length) {
      var uSafe2 = username.replace(/'/g,"\\'");
      notifArea.innerHTML = notifs.slice().reverse().map(function(n, i) {
        var realIdx = notifs.length - 1 - i;
        var replyHtml = n.reply
          ? '<div class="reply-bubble" style="margin-top:8px;"><span style="font-size:.7rem;color:#48ff00;font-weight:700;">Your Reply:</span><br>' + n.reply + '<div class="reply-meta">' + (n.replyAt||'') + '</div></div>'
          : '<div class="notif-reply-box">'
              + '<textarea class="notif-reply-input" id="reply-' + realIdx + '" placeholder="Reply to this message…"></textarea>'
              + '<button class="notif-reply-send" onclick="lcStudentReply(\'' + uSafe2 + '\',' + realIdx + ')">Send Reply</button>'
            + '</div>';
        return '<div class="lc-notif-card ' + (n.reply?'notif-with-reply':'') + '">'
          + '<p style="font-size:.9rem;">' + n.text + '</p>'
          + '<div class="time">' + n.time + '</div>'
          + replyHtml + '</div>';
      }).join('');
    } else {
      notifArea.innerHTML = '<div class="lc-notif-empty">No messages yet.</div>';
    }

    // Study Notes
    renderStudentNotes(safeArr(s.studyNotes));

    // Student's own sent messages history
    var myMsgsArea = document.getElementById('sd-my-messages-area');
    if (myMsgsArea) {
      var stuMsgs = Array.isArray(s.studentMessages) ? s.studentMessages
                  : (s.studentMessages ? (() => { try { return JSON.parse(s.studentMessages); } catch(e){ return []; } })() : []);
      if (stuMsgs.length) {
        myMsgsArea.innerHTML = '<div style="font-size:.78rem;color:#94a3b8;margin-bottom:8px;font-weight:700;text-transform:uppercase;letter-spacing:.8px;">Your Previous Messages</div>'
          + stuMsgs.slice().reverse().slice(0,3).map(function(m){
              return '<div style="background:rgba(14,165,233,.08);border:1px solid rgba(14,165,233,.2);border-radius:8px;padding:8px 12px;margin-bottom:6px;">'
                + '<div style="font-size:.85rem;color:#e2e8f0;">' + m.text + '</div>'
                + '<div style="font-size:.7rem;color:#64748b;margin-top:3px;">' + (m.sentAt||'') + '</div>'
                + '</div>';
            }).join('');
      } else {
        myMsgsArea.innerHTML = '';
      }
    }

  } catch(err) { alert('❌ Dashboard error: ' + err.message); }
  finally { lcSetLoading(false); }
}

async function lcSubmitAnswerSheet(username, testIdx, inputId) {
  var el   = document.getElementById('as-' + inputId);
  var link = el ? el.value.trim() : '';
  if (!link) { alert('Please paste a link for your answer sheet.'); return; }
  lcSetLoading(true);
  try {
    var s     = await lcGetStudent(username);
    var tests = safeArr(s.tests).slice();
    if (!tests[testIdx]) { alert('Test index mismatch. Please reload.'); return; }
    tests[testIdx] = Object.assign({}, tests[testIdx], { answerSheet: link });
    await lcUpdateStudent(username, { tests: tests });
    alert('✅ Answer sheet submitted!');
    lcRenderStudentDash(username);
  } catch(err) { alert('❌ ' + err.message); }
  finally { lcSetLoading(false); }
}

async function lcStudentReply(username, notifIdx) {
  var el        = document.getElementById('reply-' + notifIdx);
  var replyText = el ? el.value.trim() : '';
  if (!replyText) { alert('Please type a reply.'); return; }
  lcSetLoading(true);
  try {
    var s      = await lcGetStudent(username);
    var notifs = safeArr(s.notifications).slice();
    if (!notifs[notifIdx]) { alert('Message index mismatch. Please reload.'); return; }
    notifs[notifIdx] = Object.assign({}, notifs[notifIdx], {
      reply: replyText, replyAt: new Date().toLocaleString()
    });
    await lcUpdateStudent(username, { notifications: notifs });
    alert('✅ Reply sent!');
    lcRenderStudentDash(username);
  } catch(err) { alert('❌ ' + err.message); }
  finally { lcSetLoading(false); }
}

// ══ PRIVATE STUDENT NOTES ══════════════════════════════════════
async function lcAddStudentNote() {
  var username = document.getElementById('manage-student-username').value;
  var subject  = document.getElementById('note-subject').value;
  var title    = document.getElementById('note-title').value.trim();
  var link     = document.getElementById('note-link').value.trim();
  if (!title) { alert('Please enter a note title/description.'); return; }
  if (!link)  { alert('Please enter a file link (URL).'); return; }
  if (!link.startsWith('http')) { alert('Please enter a valid URL starting with http:// or https://'); return; }
  lcSetLoading(true);
  lcSetLoadingMsg('Saving note…');
  try {
    var s        = await lcGetStudent(username);
    var existing = safeArr(s.studyNotes);
    var newNote  = { id: Date.now(), subject: subject, title: title, link: link, addedAt: new Date().toLocaleString() };
    await lcUpdateStudent(username, { studyNotes: existing.concat([newNote]) });
    document.getElementById('note-title').value = '';
    document.getElementById('note-link').value  = '';
    alert('✅ Note added for ' + s.name + '!');
    _renderManageNotesList(username, existing.concat([newNote]));
  } catch(err) { alert('❌ ' + err.message); }
  finally { lcSetLoading(false); }
}

function _renderManageNotesList(username, notes) {
  var el = document.getElementById('manage-notes-list');
  if (!el) return;
  var notesArr = safeArr(notes);
  if (!notesArr.length) {
    el.innerHTML = '<div style="color:#888;font-size:.85rem;padding:8px 0;">No notes added yet.</div>';
    return;
  }
  var uSafe = username.replace(/'/g,"\\'");
  el.innerHTML = notesArr.map(function(n, i) {
    var icon = SUBJECT_ICONS[n.subject] || '📄';
    return '<div class="note-item">'
      + '<div class="note-item-info">'
      + '<div class="note-item-subject">' + icon + ' ' + n.subject + '</div>'
      + '<div class="note-item-title">' + n.title + '</div>'
      + '<div class="note-item-date">' + (n.addedAt||'') + '</div>'
      + '</div>'
      + '<div style="display:flex;gap:6px;align-items:center;">'
      + '<a href="' + n.link + '" target="_blank" class="note-dl-btn">🔗 View</a>'
      + '<button class="note-del-btn" onclick="lcDeleteStudentNote(\'' + uSafe + '\',' + i + ')">🗑️</button>'
      + '</div></div>';
  }).join('');
}

async function lcDeleteStudentNote(username, idx) {
  if (!confirm('Delete this note permanently?')) return;
  lcSetLoading(true);
  try {
    var s     = await lcGetStudent(username);
    var notes = safeArr(s.studyNotes).slice();
    notes.splice(idx, 1);
    await lcUpdateStudent(username, { studyNotes: notes });
    _renderManageNotesList(username, notes);
  } catch(err) { alert('❌ ' + err.message); }
  finally { lcSetLoading(false); }
}

function renderStudentNotes(notes) {
  var el = document.getElementById('sd-notes-area');
  if (!el) return;
  var arr = safeArr(notes);
  if (!arr.length) {
    el.innerHTML = '<div class="sn-empty">📭 No study notes have been added for you yet. Check back soon!</div>';
    return;
  }
  var subjects = ['Maths','Physics','Chemistry','Biology'];
  var html = '';
  subjects.forEach(function(subj) {
    var filtered = arr.filter(function(n){ return n.subject === subj; });
    if (!filtered.length) return;
    html += '<div class="sn-subject-section">'
      + '<div class="sn-subject-label">' + (SUBJECT_ICONS[subj]||'📄') + ' ' + subj + '</div>'
      + filtered.map(function(n){
          return '<div class="sn-card">'
            + '<div class="sn-card-info">'
            + '<div class="sn-card-title">' + n.title + '</div>'
            + '<div class="sn-card-date">' + (n.addedAt||'') + '</div>'
            + '</div>'
            + '<a href="' + n.link + '" target="_blank" class="note-dl-btn">⬇️ Download</a>'
            + '</div>';
        }).join('')
      + '</div>';
  });
  var others = arr.filter(function(n){ return subjects.indexOf(n.subject) === -1; });
  if (others.length) {
    html += '<div class="sn-subject-section">'
      + '<div class="sn-subject-label">📄 Other</div>'
      + others.map(function(n){
          return '<div class="sn-card">'
            + '<div class="sn-card-info">'
            + '<div class="sn-card-title">' + n.subject + ' — ' + n.title + '</div>'
            + '<div class="sn-card-date">' + (n.addedAt||'') + '</div>'
            + '</div>'
            + '<a href="' + n.link + '" target="_blank" class="note-dl-btn">⬇️ Download</a>'
            + '</div>';
        }).join('')
      + '</div>';
  }
  el.innerHTML = html;
}

// ══ PUBLIC DOWNLOADS ═══════════════════════════════════════════
async function pdlAddEntry() {
  var title   = document.getElementById('pdl-title').value.trim();
  var board   = document.getElementById('pdl-board').value;
  var cls     = document.getElementById('pdl-class').value;
  var subject = document.getElementById('pdl-subject').value;
  var link    = document.getElementById('pdl-link').value.trim();
  if (!title) { alert('Please enter a title/description.'); return; }
  if (!link)  { alert('Please enter a file link.'); return; }
  if (!link.startsWith('http')) { alert('Please enter a valid URL starting with http:// or https://'); return; }
  lcSetLoading(true);
  lcSetLoadingMsg('Saving download entry…');
  try {
    await pdlInsert({ title:title, board:board, class:cls, subject:subject, link:link, created_at:new Date().toISOString() });
    document.getElementById('pdl-title').value = '';
    document.getElementById('pdl-link').value  = '';
    alert('✅ Public download added!');
    pdlRenderAdminTable();
  } catch(err) { alert('❌ ' + err.message); }
  finally { lcSetLoading(false); }
}

async function pdlRenderAdminTable() {
  var tbody = document.getElementById('pdl-tbody');
  if (!tbody) return;
  tbody.innerHTML = '<tr><td colspan="6" style="text-align:center;color:#a0aec0;padding:16px;">Loading…</td></tr>';
  try {
    var items = await pdlGetAll();
    if (!items.length) {
      tbody.innerHTML = '<tr><td colspan="6" style="text-align:center;color:#888;padding:16px;">No public downloads yet. Add one above.</td></tr>';
      return;
    }
    tbody.innerHTML = items.map(function(it) {
      return '<tr>'
        + '<td style="font-weight:600;">' + it.title + '</td>'
        + '<td><span class="dl-badge dl-badge-board">'   + it.board   + '</span></td>'
        + '<td><span class="dl-badge dl-badge-class">Cl.' + it.class + '</span></td>'
        + '<td><span class="dl-badge dl-badge-subject">' + it.subject + '</span></td>'
        + '<td><a href="' + it.link + '" target="_blank" style="color:var(--cyan);font-size:.82rem;">🔗 View</a></td>'
        + '<td><button class="lc-action-btn del-action" onclick="pdlDeleteEntry(' + it.id + ')">🗑️ Delete</button></td>'
        + '</tr>';
    }).join('');
  } catch(err) {
    tbody.innerHTML = '<tr><td colspan="6" style="color:#ff6b6b;text-align:center;padding:16px;">❌ ' + err.message + '<br><small>Have you run the SQL setup in Supabase?</small></td></tr>';
  }
}

async function pdlDeleteEntry(id) {
  if (!confirm('Delete this public download permanently?')) return;
  lcSetLoading(true);
  try {
    await pdlDeleteRow(id);
    pdlRenderAdminTable();
    if (document.getElementById('dl-grid')) renderDownloads();
  } catch(err) { alert('❌ ' + err.message); }
  finally { lcSetLoading(false); }
}

async function renderDownloads() {
  var grid = document.getElementById('dl-grid');
  if (!grid) return;
  var boardEl   = document.getElementById('dl-filter-board');
  var clsEl     = document.getElementById('dl-filter-class');
  var subjectEl = document.getElementById('dl-filter-subject');
  var board   = boardEl   ? boardEl.value   : '';
  var cls     = clsEl     ? clsEl.value     : '';
  var subject = subjectEl ? subjectEl.value : '';
  grid.innerHTML = '<div class="dl-empty"><span>⏳</span><p>Loading materials…</p></div>';
  try {
    var items = await pdlGetAll();
    if (board)   items = items.filter(function(it){ return it.board === board; });
    if (cls)     items = items.filter(function(it){ return String(it.class) === cls; });
    if (subject) items = items.filter(function(it){ return it.subject === subject; });
    if (!items.length) {
      grid.innerHTML = '<div class="dl-empty"><span>📭</span><p>No materials found. Try different filters.</p></div>';
      return;
    }
    grid.innerHTML = items.map(function(it) {
      var icon = SUBJECT_ICONS[it.subject] || '📄';
      return '<div class="dl-card">'
        + '<div class="dl-card-top">'
        + '<div class="dl-card-icon">' + icon + '</div>'
        + '<div>'
        + '<div class="dl-card-title">' + it.title + '</div>'
        + '<div class="dl-card-meta">'
        + '<span class="dl-badge dl-badge-board">'   + it.board   + '</span> '
        + '<span class="dl-badge dl-badge-class">Class ' + it.class + '</span> '
        + '<span class="dl-badge dl-badge-subject">' + it.subject + '</span>'
        + '</div></div></div>'
        + '<a href="' + it.link + '" target="_blank" class="dl-btn">⬇️ Download / View</a>'
        + '</div>';
    }).join('');
  } catch(err) {
    grid.innerHTML = '<div class="dl-empty"><span>❌</span><p>Failed to load: ' + err.message + '</p>'
      + '<p style="font-size:.8rem;margin-top:8px;color:#888;">Please run the SQL setup script in your Supabase SQL Editor.</p></div>';
  }
}

function resetDlFilters() {
  ['dl-filter-board','dl-filter-class','dl-filter-subject'].forEach(function(id){
    var el = document.getElementById(id);
    if (el) el.value = '';
  });
  renderDownloads();
}

// ══ BACKGROUND TASKS ═══════════════════════════════════════════
setInterval(async function() {
  var dash = document.getElementById('lc-admin-dash');
  if (!dash || !dash.classList.contains('active')) return;
  try {
    var students = await lcGetStudents();
    for (var i = 0; i < students.length; i++) {
      var s = students[i];
      if (s.liveLink && lcIsLinkExpired(s.liveLinkSetAt)) {
        await lcUpdateStudent(s.username, { liveLink: '', liveLinkSetAt: null });
      }
    }
  } catch(e) { /* silent */ }
}, 5 * 60 * 1000);

// ══ PERSISTENT SESSION RESTORE ═════════════════════════════════
(function lcRestoreSession() {
  var saved = localStorage.getItem('lc_logged_student');
  if (!saved) return;
  setTimeout(async function() {
    try {
      var students = await lcGetStudents();
      var found = null;
      for (var i = 0; i < students.length; i++) {
        if (students[i].username === saved) { found = students[i]; break; }
      }
      if (!found) { localStorage.removeItem('lc_logged_student'); return; }
      lcLoggedStudent = found.username;
      var liveClassPage = document.getElementById('page-live-class');
      if (liveClassPage && !liveClassPage.classList.contains('hidden')) {
        lcShowView('lc-student-dash');
        lcRenderStudentDash(found.username);
        lcRequestNotifPermission();
        lcStartPollingStudent(found.username);
      } else {
        window._lcPendingRestore = found.username;
      }
    } catch(e) { /* silent */ }
  }, 800);
})();

// ══ BROWSER PUSH NOTIFICATIONS (Web Notifications API) ═════════
function lcRequestNotifPermission() {
  if (!('Notification' in window)) return;
  if (Notification.permission === 'default') {
    Notification.requestPermission().then(function(perm) {
      if (perm === 'granted') {
        lcShowBrowserNotif('\u{1F514} Notifications Enabled', 'You will now receive messages even when browsing other tabs!');
      }
    });
  }
}

function lcShowBrowserNotif(title, body) {
  if (!('Notification' in window)) return;
  if (Notification.permission !== 'granted') return;
  try {
    var n = new Notification(title, {
      body: body,
      icon: 'logo.png',
      requireInteraction: false,
      tag: 'molman-' + Date.now()
    });
    n.onclick = function() { window.focus(); n.close(); };
    setTimeout(function(){ n.close(); }, 8000);
  } catch(e) {}
}

// ══ POLLING — STUDENT SIDE (detects new admin messages) ═══════
var _studentPollTimer     = null;
var _studentPollLastCount = -1;

function lcStartPollingStudent(username) {
  lcStopPollingStudent();
  _studentPollLastCount = -1;
  _studentPollTimer = setInterval(async function() {
    if (!lcLoggedStudent) { lcStopPollingStudent(); return; }
    try {
      var s = await lcGetStudent(username);
      if (!s) return;
      var notifs = Array.isArray(s.notifications) ? s.notifications : [];
      if (_studentPollLastCount === -1) {
        _studentPollLastCount = notifs.length;
        return;
      }
      if (notifs.length > _studentPollLastCount) {
        var latest = notifs[notifs.length - 1];
        if (latest && latest.text) {
          lcShowBrowserNotif('\u{1F4E9} New Message from Sir', latest.text.substring(0, 120));
        }
        _studentPollLastCount = notifs.length;
        lcRenderStudentDash(username);
      }
    } catch(e) {}
  }, 10000);
}

function lcStopPollingStudent() {
  if (_studentPollTimer) { clearInterval(_studentPollTimer); _studentPollTimer = null; }
  _studentPollLastCount = -1;
}

// ══ POLLING — ADMIN SIDE (detects new student messages) ═══════
var _adminPollTimer    = null;
var _adminPollSnapshot = {};

function lcStartPollingAdmin() {
  lcStopPollingAdmin();
  _adminPollSnapshot = {};
  _adminPollTimer = setInterval(async function() {
    try {
      var students = await lcGetStudents();
      students.forEach(function(s) {
        var msgs = Array.isArray(s.studentMessages) ? s.studentMessages : [];
        var prev = _adminPollSnapshot[s.username];
        if (prev === undefined) {
          _adminPollSnapshot[s.username] = msgs.length;
          return;
        }
        if (msgs.length > prev) {
          var latest = msgs[msgs.length - 1];
          lcShowBrowserNotif('\u{1F4E9} New message from ' + (s.name || s.username), latest ? latest.text.substring(0,120) : 'New student message');
          _adminPollSnapshot[s.username] = msgs.length;
          lcUpdateAdminInboxBadge(students);
          lcRefreshInbox();
          lcRenderStudentTable();
        }
      });
    } catch(e) {}
  }, 12000);
}

function lcStopPollingAdmin() {
  if (_adminPollTimer) { clearInterval(_adminPollTimer); _adminPollTimer = null; }
  _adminPollSnapshot = {};
}

// ══ ADMIN INBOX BADGE ════════════════════════════════════════
function lcUpdateAdminInboxBadge(students) {
  var badge = document.getElementById('admin-inbox-badge');
  if (!badge) return;
  var total = 0;
  (students || []).forEach(function(s) {
    var msgs = Array.isArray(s.studentMessages) ? s.studentMessages : [];
    total += msgs.filter(function(m){ return !m.read; }).length;
  });
  if (total > 0) {
    badge.textContent = total + ' unread';
    badge.style.display = 'inline';
  } else {
    badge.style.display = 'none';
  }
}

// ══ ADMIN INBOX PANEL — TABS ══════════════════════════════════
var _inboxActiveTab = 'student';

function lcInboxTab(tab) {
  _inboxActiveTab = tab;
  ['student','replies'].forEach(function(t) {
    var btn   = document.getElementById('inbox-tab-' + t);
    var panel = document.getElementById('inbox-panel-' + t);
    var active = t === tab;
    if (btn) {
      btn.style.background  = active ? 'rgba(0,255,255,.15)' : 'rgba(255,255,255,.06)';
      btn.style.borderColor = active ? 'rgba(0,255,255,.4)'  : 'rgba(255,255,255,.15)';
      btn.style.color       = active ? 'var(--cyan)'         : '#94a3b8';
    }
    if (panel) panel.style.display = active ? 'block' : 'none';
  });
  lcRefreshInbox();
}

async function lcRefreshInbox() {
  try {
    var students = await lcGetStudents();
    lcUpdateAdminInboxBadge(students);
    if (_inboxActiveTab === 'student') lcRenderInboxStudentMessages(students);
    else                               lcRenderInboxReplies(students);
  } catch(e) {}
}

function lcRenderInboxStudentMessages(students) {
  var el = document.getElementById('admin-inbox-list');
  if (!el) return;
  var allMsgs = [];
  students.forEach(function(s) {
    var msgs = Array.isArray(s.studentMessages) ? s.studentMessages : [];
    msgs.forEach(function(m) { allMsgs.push({ student: s, msg: m }); });
  });
  allMsgs.sort(function(a,b){ return (b.msg.id||0) - (a.msg.id||0); });

  if (!allMsgs.length) {
    el.innerHTML = '<div style="text-align:center;padding:30px;color:#64748b;font-size:.9rem;"><div style="font-size:2rem;margin-bottom:8px;">&#128235;</div>No messages from students yet.</div>';
    return;
  }
  el.innerHTML = '';
  allMsgs.forEach(function(item) {
    var s = item.student, m = item.msg;
    var unread = !m.read;
    var card = document.createElement('div');
    card.style.cssText = 'background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,' + (unread?'.25':'.1') + ');border-left:3px solid ' + (unread?'#ef4444':'rgba(255,255,255,.1)') + ';border-radius:12px;padding:14px 16px;margin-bottom:10px;';
    card.innerHTML = '<div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;margin-bottom:8px;">'
      + '<div style="display:flex;align-items:center;gap:8px;">'
      + (unread ? '<span style="width:8px;height:8px;border-radius:50%;background:#ef4444;display:inline-block;flex-shrink:0;"></span>' : '')
      + (s.photo ? '<img src="' + s.photo + '" style="width:28px;height:28px;border-radius:50%;object-fit:cover;">' : '<span style="font-size:1.2rem;">&#128100;</span>')
      + '<span style="font-weight:700;color:#e2e8f0;">' + s.name + '</span>'
      + '<span style="font-size:.75rem;color:#64748b;">@' + s.username + '</span>'
      + '</div>'
      + '<div style="display:flex;gap:6px;" class="inbox-btn-row"></div>'
      + '</div>'
      + '<div style="font-size:.9rem;color:#cbd5e1;line-height:1.6;margin-bottom:6px;">' + m.text + '</div>'
      + '<div style="font-size:.72rem;color:#475569;">' + (m.sentAt||'') + '</div>';

    var btnRow = card.querySelector('.inbox-btn-row');

    var replyBtn = document.createElement('button');
    replyBtn.textContent = '💬 Reply';
    replyBtn.style.cssText = 'padding:5px 12px;border-radius:14px;background:rgba(255,215,0,.1);border:1px solid rgba(255,215,0,.3);color:var(--gold);font-family:"Exo 2",sans-serif;font-size:.75rem;font-weight:700;cursor:pointer;';
    replyBtn.onclick = function(){ lcAdminReplyFromInbox(s.username); };
    btnRow.appendChild(replyBtn);

    var readBtn = document.createElement('button');
    readBtn.textContent = '✓ Read';
    readBtn.style.cssText = 'padding:5px 12px;border-radius:14px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.15);color:#94a3b8;font-family:"Exo 2",sans-serif;font-size:.75rem;font-weight:700;cursor:pointer;';
    readBtn.onclick = function(){ lcMarkStudentMsgRead(s.username, m.id); };
    btnRow.appendChild(readBtn);

    var delBtn = document.createElement('button');
    delBtn.textContent = '🗑️ Delete';
    delBtn.style.cssText = 'padding:5px 12px;border-radius:14px;background:rgba(239,68,68,.15);border:1px solid rgba(239,68,68,.4);color:#f87171;font-family:"Exo 2",sans-serif;font-size:.75rem;font-weight:700;cursor:pointer;';
    delBtn.onclick = function(){ lcDeleteStudentMsg(s.username, m.id); };
    btnRow.appendChild(delBtn);

    el.appendChild(card);
  });
}

function lcRenderInboxReplies(students) {
  var el = document.getElementById('admin-replies-list');
  if (!el) return;
  el.innerHTML = '';
  var allReplies = [];
  students.forEach(function(s) {
    var notifs = Array.isArray(s.notifications) ? s.notifications : [];
    notifs.forEach(function(n) {
      if (n.reply) allReplies.push({ student: s, notif: n });
    });
  });
  allReplies.sort(function(a,b){
    var ta = a.notif.replyAt ? new Date(a.notif.replyAt).getTime() : 0;
    var tb = b.notif.replyAt ? new Date(b.notif.replyAt).getTime() : 0;
    return tb - ta;
  });
  if (!allReplies.length) {
    el.innerHTML = '<div style="text-align:center;padding:30px;color:#64748b;font-size:.9rem;"><div style="font-size:2rem;margin-bottom:8px;">&#128235;</div>No replies from students yet.</div>';
    return;
  }
  allReplies.forEach(function(item) {
    var s = item.student, n = item.notif;

    var card = document.createElement('div');
    card.style.cssText = 'background:rgba(255,255,255,.04);border:1px solid rgba(72,255,0,.15);border-radius:12px;padding:14px 16px;margin-bottom:10px;';

    // Header row
    var header = document.createElement('div');
    header.style.cssText = 'display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;margin-bottom:10px;';

    var info = document.createElement('div');
    info.style.cssText = 'display:flex;align-items:center;gap:8px;';
    info.innerHTML = (s.photo ? '<img src="' + s.photo + '" style="width:28px;height:28px;border-radius:50%;object-fit:cover;">' : '<span style="font-size:1.2rem;">&#128100;</span>')
      + '<span style="font-weight:700;color:#e2e8f0;">' + s.name + '</span>'
      + '<span style="font-size:.75rem;color:#64748b;">@' + s.username + '</span>';

    var delBtn = document.createElement('button');
    delBtn.textContent = '🗑️ Delete';
    delBtn.style.cssText = 'padding:5px 12px;border-radius:14px;background:rgba(239,68,68,.15);border:1px solid rgba(239,68,68,.4);color:#f87171;font-family:"Exo 2",sans-serif;font-size:.75rem;font-weight:700;cursor:pointer;';
    delBtn.onclick = function(){ lcDeleteNotifReply(s.username, n.id); };

    header.appendChild(info);
    header.appendChild(delBtn);
    card.appendChild(header);

    // Original message block
    var origBlock = document.createElement('div');
    origBlock.style.cssText = 'background:rgba(255,215,0,.06);border:1px solid rgba(255,215,0,.2);border-radius:8px;padding:10px 12px;margin-bottom:8px;';
    origBlock.innerHTML = '<div style="font-size:.7rem;color:var(--gold);font-weight:700;margin-bottom:4px;">YOUR MESSAGE:</div>'
      + '<div style="font-size:.88rem;color:#94a3b8;">' + n.text + '</div>';
    card.appendChild(origBlock);

    // Reply block
    var replyBlock = document.createElement('div');
    replyBlock.style.cssText = 'background:rgba(72,255,0,.06);border:1px solid rgba(72,255,0,.2);border-radius:8px;padding:10px 12px;';
    replyBlock.innerHTML = '<div style="font-size:.7rem;color:#48ff00;font-weight:700;margin-bottom:4px;">STUDENT REPLY:</div>'
      + '<div style="font-size:.88rem;color:#e2e8f0;">' + n.reply + '</div>'
      + '<div style="font-size:.7rem;color:#475569;margin-top:4px;">' + (n.replyAt||'') + '</div>';
    card.appendChild(replyBlock);

    el.appendChild(card);
  });
}
async function lcAdminReplyFromInbox(username) {
  lcOpenMsgModal(username);
}

async function lcMarkStudentMsgRead(username, msgId) {
  try {
    var s    = await lcGetStudent(username);
    var msgs = Array.isArray(s.studentMessages) ? s.studentMessages : [];
    msgs = msgs.map(function(m){ return m.id === msgId ? Object.assign({}, m, {read:true}) : m; });
    await lcUpdateStudent(username, { studentMessages: msgs });
    lcRefreshInbox();
    lcRenderStudentTable();
  } catch(e) { alert('❌ ' + e.message); }
}

async function lcDeleteStudentMsg(username, msgId) {
  if (!confirm('Delete this message permanently?')) return;
  try {
    var s    = await lcGetStudent(username);
    var msgs = Array.isArray(s.studentMessages) ? s.studentMessages : [];
    msgs = msgs.filter(function(m){ return m.id !== msgId; });
    await lcUpdateStudent(username, { studentMessages: msgs });
    lcRefreshInbox();
    lcRenderStudentTable();
  } catch(e) { alert('❌ ' + e.message); }
}

async function lcDeleteNotifReply(username, notifId) {
  if (!confirm('Delete this reply permanently?')) return;
  try {
    var s      = await lcGetStudent(username);
    var notifs = Array.isArray(s.notifications) ? s.notifications : [];
    // Clear the reply from the matching notification (keep the original message, just remove the reply)
    notifs = notifs.map(function(n){
      return n.id === notifId ? Object.assign({}, n, { reply: null, replyAt: null }) : n;
    });
    await lcUpdateStudent(username, { notifications: notifs });
    lcRefreshInbox();
  } catch(e) { alert('❌ ' + e.message); }
}

// ══ STUDENT-INITIATED MESSAGE TO ADMIN ═════════════════════════
async function lcStudentSendToAdmin() {
  var username = lcLoggedStudent;
  if (!username) return;
  var msgEl = document.getElementById('student-msg-input');
  var msg   = msgEl ? msgEl.value.trim() : '';
  if (!msg) { alert('Please type a message first.'); return; }
  lcSetLoading(true);
  lcSetLoadingMsg('Sending message to tutor\u2026');
  try {
    var s        = await lcGetStudent(username);
    var existing = Array.isArray(s.studentMessages) ? s.studentMessages : [];
    var newMsg   = { id: Date.now(), text: msg, sentAt: new Date().toLocaleString(), read: false };
    await lcUpdateStudent(username, { studentMessages: existing.concat([newMsg]) });
    if (msgEl) msgEl.value = '';
    alert('\u2705 Message sent to your tutor!');
    lcRenderStudentDash(username);
  } catch(err) { alert('\u274C ' + err.message); }
  finally { lcSetLoading(false); }
}

// ══ PATCH: restore session when navigating to live class ═══════
var _origShowPage = window.showPage;
window.showPage = function(page, el) {
  if (_origShowPage) _origShowPage(page, el);
  if (page === 'live-class' && window._lcPendingRestore) {
    var u = window._lcPendingRestore;
    window._lcPendingRestore = null;
    setTimeout(async function() {
      try {
        var s = await lcGetStudent(u);
        if (s) {
          lcLoggedStudent = u;
          lcShowView('lc-student-dash');
          lcRenderStudentDash(u);
          lcRequestNotifPermission();
          lcStartPollingStudent(u);
        }
      } catch(e) {}
    }, 300);
  }
};


function switchAboutTab(panel, btn) {
  document.querySelectorAll('.about-panel').forEach(function(p){ p.classList.remove('ap-active'); });
  document.querySelectorAll('.about-tab').forEach(function(b){ b.classList.remove('at-active'); b.setAttribute('aria-selected','false'); });
  var el = document.getElementById('about-panel-' + panel);
  if (el) el.classList.add('ap-active');
  if (btn) { btn.classList.add('at-active'); btn.setAttribute('aria-selected','true'); }
}

// ══ KEYBOARD SHORTCUTS ═════════════════════════════════════════
document.addEventListener('keydown', function(e) {
  if (e.key !== 'Enter') return;
  var av = document.querySelector('#page-live-class .lc-view.active');
  if (!av) return;
  if (av.id === 'lc-admin-login')   lcAdminLogin();
  else if (av.id === 'lc-student-login') lcStudentLogin();
});

</script>
</body>
</html>
