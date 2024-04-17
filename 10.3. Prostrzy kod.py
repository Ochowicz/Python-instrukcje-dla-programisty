from pathlib import Path
path = Path('learning_python.txt')
content = path.read_text(encoding='utf-8')
for line in content.splitlines():
	if 'pythonie' in line:
		print(line.replace('pythonie', 'C').rstrip())