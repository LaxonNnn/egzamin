from pathlib import Path
p=Path('index.html')
s=p.read_text()
s=s.replace('.exam-admin-grid>.issues-panel{position:sticky;top:14px}.exam-admin-grid>.issues-panel #examIssues{max-height:675px;overflow-y:auto;padding-right:6px}.exam-counts{background:#111827;border:1px solid #334155;border-radius:12px;padding:12px}.exam-counts p{margin:6px 0}', '.exam-admin-grid>.exam-admin-side{position:sticky;top:14px;display:flex;flex-direction:column;gap:14px}.exam-admin-grid>.exam-admin-side>.issues-panel{position:static}.exam-admin-grid>.exam-admin-side>.issues-panel #examIssues{max-height:560px;overflow-y:auto;padding-right:6px}.exam-counts{background:#111827;border:1px solid #334155;border-radius:16px;padding:14px;color:#e8edf4}.exam-counts h3{margin:0 0 8px;color:#e8edf4}.exam-counts p{margin:6px 0;color:#e8edf4}')
old='<aside class="issues-panel"><h3>Aktywne zgłoszenia <span id="examIssueCount">0</span></h3><div id="examIssues"></div><hr style="border-color:#cfd8e5;margin:18px 0"><h3>Liczba pytań w blokach</h3><div id="examBlockCounts"></div></aside>'
new='<aside class="exam-admin-side"><div class="exam-counts"><h3>Liczba pytań w blokach</h3><div id="examBlockCounts"></div></div><div class="issues-panel"><h3>Aktywne zgłoszenia <span id="examIssueCount">0</span></h3><div id="examIssues"></div></div></aside>'
if old not in s: raise SystemExit('admin side target missing')
s=s.replace(old,new,1)
s=s.replace('@media(max-width:800px){.block-grid{grid-template-columns:1fr}.admin-layout,.exam-admin-grid{grid-template-columns:1fr}.issues-panel{position:static}}', '@media(max-width:800px){.block-grid{grid-template-columns:1fr}.admin-layout,.exam-admin-grid{grid-template-columns:1fr}.issues-panel,.exam-admin-grid>.exam-admin-side{position:static}}')
p.write_text(s)
