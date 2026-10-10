import json, os, sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data'

total_qs = 0
long_opt_counts = 0 # options > 25 chars
very_long_opt_counts = 0 # options > 35 chars
chapter_stats = []

for ch in range(1, 21):
    fpath = os.path.join(data_dir, f'chapter{ch:02d}.json')
    with open(fpath, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    
    qs = data.get('questions', [])
    total_qs += len(qs)
    
    ch_lens = []
    ch_long_qs = []
    
    for q in qs:
        opts = q.get('options', {})
        lens = [len(v) for v in opts.values()]
        max_l = max(lens) if lens else 0
        avg_l = sum(lens) / len(lens) if lens else 0
        ch_lens.append(avg_l)
        
        # Check if any option is long
        if max_l >= 25:
            ch_long_qs.append((q['id'], q['question'], opts, max_l, q.get('type')))
            long_opt_counts += 1
            if max_l >= 35:
                very_long_opt_counts += 1
                
    chapter_stats.append({
        'chapter': ch,
        'title': data.get('chapter_title', ''),
        'q_count': len(qs),
        'avg_opt_len': sum(ch_lens) / len(ch_lens) if ch_lens else 0,
        'long_qs_count': len(ch_long_qs),
        'long_samples': ch_long_qs[:2]
    })

print(f"Total Questions Analyzed: {total_qs}")
print(f"Questions with options >= 25 chars: {long_opt_counts} ({long_opt_counts/total_qs*100:.1f}%)")
print(f"Questions with options >= 35 chars: {very_long_opt_counts} ({very_long_opt_counts/total_qs*100:.1f}%)")
print("\n--- Chapter Breakdown ---")
for s in chapter_stats:
    print(f"Ch {s['chapter']:02d}: {s['title'][:18]:<18} | Avg Opt Len: {s['avg_opt_len']:.1f} chars | Long Opt Qs (>=25): {s['long_qs_count']}/40")
