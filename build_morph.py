import re

filepath = 'index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the old Search Bar block
old_search_pattern = re.compile(r'<!-- Search Bar \(Smart AI\) -->.*?</div>\s*</div>', re.DOTALL)

new_search_html = """<!-- Search-to-Chat Morph AI -->
            <div class="w-full max-w-3xl mx-auto mb-10 relative z-[60] h-[64px]" id="morph-wrapper">
                <!-- The Expanding Container -->
                <div id="morph-container" class="absolute top-0 left-0 right-0 bg-[#053229]/60 backdrop-blur-md border border-white/20 rounded-full shadow-2xl transition-all duration-500 ease-[cubic-bezier(0.4,0,0.2,1)] overflow-hidden flex flex-col h-[64px]">
                    
                    <!-- Chat Header (Hidden initially) -->
                    <div id="morph-header" class="px-6 py-4 border-b border-white/10 flex justify-between items-center opacity-0 hidden transition-opacity duration-300">
                        <div class="flex items-center gap-3">
                            <span class="material-symbols-outlined text-white text-2xl text-yellow-400">auto_spark</span>
                            <span class="text-white font-bold">Apex AI Assistant</span>
                        </div>
                        <button onclick="closeMorph()" class="text-white/70 hover:text-white">
                            <span class="material-symbols-outlined">close</span>
                        </button>
                    </div>

                    <!-- Chat Messages Area (Hidden initially) -->
                    <div id="morph-messages" class="flex-grow p-6 overflow-y-auto hidden opacity-0 transition-opacity duration-300 flex-col gap-4 hidden-scrollbar">
                        <div class="flex gap-3">
                            <div class="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center shrink-0">
                                <span class="material-symbols-outlined text-white text-sm">smart_toy</span>
                            </div>
                            <div class="bg-white/10 p-3 rounded-2xl rounded-tl-sm text-sm text-white shadow-sm border border-white/10 max-w-[85%]">
                                Hello! I'm the Apex Care AI Assistant. How can I help you today?
                            </div>
                        </div>
                    </div>

                    <!-- The Input Area (Always visible, morphs slightly) -->
                    <div class="relative flex items-center p-2 pl-6 shrink-0 h-[64px] border-t border-transparent" id="morph-input-area">
                        <span class="material-symbols-outlined text-yellow-400 mr-2 absolute left-6 transition-all duration-300" id="morph-sparkle">auto_spark</span>
                        <input type="text" id="morph-input" autocomplete="off" placeholder="Ask AI Assistant or Search for Doctors..." class="bg-transparent text-white placeholder-white/70 outline-none border-none ring-0 focus:ring-0 w-full text-sm lg:text-base font-medium pl-8 transition-all duration-300" onfocus="openMorph()">
                        <button onclick="handleMorphSubmit()" class="w-10 h-10 lg:w-12 lg:h-12 flex-shrink-0 bg-[#E87121] hover:bg-[#d66115] transition-colors rounded-full flex items-center justify-center text-white shadow-lg z-10" id="morph-submit">
                            <span class="material-symbols-outlined text-[20px] lg:text-[24px]">arrow_upward</span>
                        </button>
                    </div>
                </div>
            </div>"""

content = old_search_pattern.sub(new_search_html, content)


# Replace the old Smart Search AI Logic script
old_script_pattern = re.compile(r'<!-- Smart Search AI Logic -->.*?</script>', re.DOTALL)

new_script_html = """<!-- Morph AI Logic -->
<script>
    const morphContainer = document.getElementById('morph-container');
    const morphHeader = document.getElementById('morph-header');
    const morphMessages = document.getElementById('morph-messages');
    const morphInputArea = document.getElementById('morph-input-area');
    const morphInput = document.getElementById('morph-input');
    const morphSparkle = document.getElementById('morph-sparkle');
    const morphSubmit = document.getElementById('morph-submit');
    let isMorphOpen = false;

    function openMorph() {
        if (isMorphOpen) return;
        isMorphOpen = true;

        // Animate Container Expansion
        morphContainer.classList.remove('h-[64px]', 'rounded-full', 'bg-[#053229]/60');
        morphContainer.classList.add('h-[450px]', 'rounded-3xl', 'bg-[#053229]/95', 'shadow-[0_30px_60px_rgba(0,0,0,0.5)]', '-translate-y-4');
        
        // Show Header & Messages
        morphHeader.classList.remove('hidden');
        morphMessages.classList.remove('hidden');
        morphInputArea.classList.replace('border-transparent', 'border-white/10');
        
        setTimeout(() => {
            morphHeader.classList.remove('opacity-0');
            morphMessages.classList.remove('opacity-0');
        }, 300);
    }

    function closeMorph() {
        if (!isMorphOpen) return;
        isMorphOpen = false;

        morphHeader.classList.add('opacity-0');
        morphMessages.classList.add('opacity-0');
        
        setTimeout(() => {
            morphHeader.classList.add('hidden');
            morphMessages.classList.add('hidden');
            
            morphContainer.classList.remove('h-[450px]', 'rounded-3xl', 'bg-[#053229]/95', 'shadow-[0_30px_60px_rgba(0,0,0,0.5)]', '-translate-y-4');
            morphContainer.classList.add('h-[64px]', 'rounded-full', 'bg-[#053229]/60');
            morphInputArea.classList.replace('border-white/10', 'border-transparent');
            morphInput.value = '';
            morphInput.blur();
        }, 200);
    }

    function addMorphMessageToUI(text, isUser) {
        const msgDiv = document.createElement('div');
        msgDiv.className = `flex gap-3 ${isUser ? 'flex-row-reverse' : ''}`;
        
        let avatar = '';
        if (!isUser) {
            avatar = `<div class="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center shrink-0 mt-1">
                        <span class="material-symbols-outlined text-white text-sm">smart_toy</span>
                      </div>`;
        }

        let formattedText = text.replace(/\\n/g, '<br/>').replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>');

        const bubble = `
            ${avatar}
            <div class="${isUser ? 'bg-[#E87121] text-white' : 'bg-white/10 text-white border border-white/10'} p-3 rounded-2xl ${isUser ? 'rounded-tr-sm' : 'rounded-tl-sm'} text-sm shadow-sm max-w-[85%]">
                ${formattedText}
            </div>
        `;
        
        msgDiv.innerHTML = bubble;
        morphMessages.appendChild(msgDiv);
        morphMessages.scrollTop = morphMessages.scrollHeight;
    }

    function addMorphTypingIndicator() {
        const id = 'typing-' + Date.now();
        const msgDiv = document.createElement('div');
        msgDiv.id = id;
        msgDiv.className = `flex gap-3`;
        
        const bubble = `
            <div class="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center shrink-0 mt-1">
                <span class="material-symbols-outlined text-white text-sm">smart_toy</span>
            </div>
            <div class="bg-white/10 p-4 rounded-2xl rounded-tl-sm text-sm shadow-sm border border-white/10 flex items-center gap-1">
                <div class="w-1.5 h-1.5 bg-white/70 rounded-full animate-bounce" style="animation-delay: 0ms"></div>
                <div class="w-1.5 h-1.5 bg-white/70 rounded-full animate-bounce" style="animation-delay: 150ms"></div>
                <div class="w-1.5 h-1.5 bg-white/70 rounded-full animate-bounce" style="animation-delay: 300ms"></div>
            </div>
        `;
        
        msgDiv.innerHTML = bubble;
        morphMessages.appendChild(msgDiv);
        morphMessages.scrollTop = morphMessages.scrollHeight;
        return id;
    }

    async function handleMorphSubmit() {
        if (!isMorphOpen) openMorph();
        
        const message = morphInput.value.trim();
        if (!message) return;

        addMorphMessageToUI(message, true);
        morphInput.value = '';
        morphSubmit.disabled = true;

        const typingId = addMorphTypingIndicator();

        try {
            const response = await fetch("http://localhost:3000/api/triage", {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ question: message })
            });

            document.getElementById(typingId).remove();
            
            if (!response.ok) {
                addMorphMessageToUI("Our automated guidance system is currently busy. Please call emergency services.", false);
                return;
            }

            const data = await response.json();
            if (data.answer) {
                addMorphMessageToUI(data.answer, false);
            } else {
                addMorphMessageToUI("Sorry, I encountered an error formatting the response.", false);
            }
            
        } catch (error) {
            document.getElementById(typingId).remove();
            addMorphMessageToUI("Server offline. Please ensure the local backend server (Node.js) is running.", false);
        } finally {
            morphSubmit.disabled = false;
            morphInput.focus();
        }
    }

    // Handle Enter key
    morphInput.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            handleMorphSubmit();
        }
    });

    // Close when clicking outside
    document.addEventListener('click', (e) => {
        if (isMorphOpen && !morphContainer.contains(e.target)) {
            closeMorph();
        }
    });
</script>"""

if old_script_pattern.search(content):
    content = old_script_pattern.sub(new_script_html, content)
else:
    # Append if not found
    content = content.replace('</body>', new_script_html + '\n</body>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected Morphing Search-to-Chat UI into index.html")
