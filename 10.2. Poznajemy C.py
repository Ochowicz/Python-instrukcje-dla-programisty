from pathlib import Path
path = Path('learning_python.txt')
content = path.read_text(encoding='utf-8')
lines = content.splitlines()
for line in lines:
	if 'pythonie' in line:
		replaced = line.replace('pythonie', 'C')
		print (replaced.strip())