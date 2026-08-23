const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

// The exact function provided by the user for failover
async function getMedicalAIResponse(patientQuestion) {
    console.log("Processing AI request for:", patientQuestion);
    
    // Simulate network delay for realism
    await new Promise(resolve => setTimeout(resolve, 1500));
    
    const lowerQ = patientQuestion.toLowerCase();
    
    if (lowerQ.includes("headache") || lowerQ.includes("fever")) {
        return "For mild symptoms like headache or fever, ensure you stay hydrated and rested. You can book an appointment with our General Medicine department for a checkup.";
    } else if (lowerQ.includes("heart") || lowerQ.includes("chest") || lowerQ.includes("pain")) {
        return "Severe pain, especially in the chest, can be a medical emergency. Please head to the Emergency Room immediately or call emergency services.";
    } else if (lowerQ.includes("doctor") || lowerQ.includes("appointment")) {
        return "You can easily book an appointment by clicking the 'Book Appointment' button in the navigation bar. We have specialists in Cardiology, Neurology, and more.";
    } else if (lowerQ.includes("hello") || lowerQ.includes("hi")) {
        return "Hello! I am the Apex Care AI Assistant. How can I help you with your medical inquiries or hospital navigation today?";
    } else {
        return "Thank you for reaching out. I'm a simulated AI assistant for Apex Care. In a production environment, I would connect to a real medical LLM to answer: '" + patientQuestion + "'";
    }
}

// Example Express API route for your frontend website to call anonymously
app.post('/api/triage', async (req, res) => {
    const { question } = req.body;
    if (!question) return res.status(400).json({ error: "Missing patient question" });
    
    const aiAnswer = await getMedicalAIResponse(question);
    res.json({ answer: aiAnswer });
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Backend server running on http://localhost:${PORT}`);
    console.log(`Failover AI System Ready.`);
});
