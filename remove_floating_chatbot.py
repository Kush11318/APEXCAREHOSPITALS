import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the floating Chatbot Widget block
    pattern = re.compile(r'<!-- AI Chatbot Widget -->.*?<!-- End AI Chatbot Widget -->\n', re.DOTALL)
    if pattern.search(content):
        content = pattern.sub('', content)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Removed floating chatbot from {file}")
