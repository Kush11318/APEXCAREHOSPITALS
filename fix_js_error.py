import glob

html_files = glob.glob('*.html')

broken_js = """        // Convert newlines to br and simple markdown bold to HTML
        let formattedText = text.replace(/
/g, '<br/>').replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');"""

fixed_js = """        // Convert newlines to br and simple markdown bold to HTML
        let formattedText = text.replace(/\\n/g, '<br/>').replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>');"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if broken_js in content:
        content = content.replace(broken_js, fixed_js)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed JS syntax error in {file}")
