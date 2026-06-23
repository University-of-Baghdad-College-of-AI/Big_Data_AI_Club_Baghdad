import re, json, os

# All files are in the same Baghdad repo
activity_files = {
    'workshops':     'workshops.html',
    'researches':    'researches.html',
    'projects':      'projects.html',
    'lectures':      'lectures.html',
    'presentations': 'presentations.html',
    'seminars':      'seminars.html',
    'conferences':   'conferences.html',
    'field-visits':  'field-visits.html',
    'students':      'students-index.html',    # copy of Students repo index
    'professors':    'professors-index.html',  # copy of Professors repo index
}

all_data = {}
for name, path in activity_files.items():
    if not os.path.exists(path):
        print(f"SKIP (not found): {path}")
        all_data[name] = []
        continue
    with open(path) as f:
        content = f.read()
    m = re.search(r'var allData = (\[.*?\]);', content, re.DOTALL)
    if m:
        try:
            all_data[name] = json.loads(m.group(1))
            print(f"  {name}: {len(all_data[name])} items")
        except Exception as e:
            all_data[name] = []
            print(f"  ERROR {name}: {e}")
    else:
        all_data[name] = []
        print(f"  {name}: no allData found")

stats_js = "var STATS_DATA = {\n"
for name, data in all_data.items():
    stats_js += f"  '{name}': {json.dumps(data, ensure_ascii=False)},\n"
stats_js += "};"

with open('index.html') as f:
    content = f.read()

new_content = re.sub(
    r'var STATS_DATA = \{.*?\};',
    stats_js,
    content,
    flags=re.DOTALL
)

if new_content != content:
    with open('index.html', 'w') as f:
        f.write(new_content)
    print("index.html updated!")
else:
    print("No changes needed.")
