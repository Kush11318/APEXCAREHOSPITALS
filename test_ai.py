with open('index.html', encoding='utf-8') as f:
    text = f.read()
    print("Widget count:", text.count('id="ai-chat-widget"'))
