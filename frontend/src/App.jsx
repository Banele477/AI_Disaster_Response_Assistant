import React, { useState } from 'react';

export default function DisasterApp() {
  const [disaster, setDisaster] = useState('Earthquake');
  const [lang, setLang] = useState('English');
  const [chat, setChat] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [location, setLocation] = useState(null);

  const handleShareLocation = () => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition((pos) => {
        setLocation({ lat: pos.coords.latitude.toFixed(4), lng: pos.coords.longitude.toFixed(4) });
      });
    } else {
      alert("Geolocation is not supported by this browser.");
    }
  };

  const handleSendMessage = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = { sender: 'user', text: input };
    setChat((prev) => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    // Hit your running Termux backend API
    try {
      const response = await fetch(`/api/disaster-guidance?type=${disaster}&latitude=${location?.lat || 0}&longitude=${location?.lng || 0}`);
      const data = await response.json();
      
      const aiResponse = { 
        sender: 'ai', 
        text: lang === 'Hindi' 
          ? "सुरक्षित रहें। अपने सिर को सुरक्षित रखें और मजबूत मेज के नीचे छिप जाएं।" 
          : data.instructions.join(" ") 
      };
      setChat((prev) => [...prev, aiResponse]);
    } catch (error) {
      setChat((prev) => [...prev, { sender: 'ai', text: "Error contacting the live assistant server." }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-900 text-white p-4 font-sans">
      <header className="flex justify-between items-center border-b border-slate-700 pb-4 mb-6">
        <h1 className="text-2xl font-bold text-red-500">🚨 AI Emergency Assistant</h1>
        <button 
          onClick={() => setLang(lang === 'English' ? 'Hindi' : 'English')}
          className="bg-slate-700 px-4 py-2 rounded text-sm hover:bg-slate-600 transition"
        >
          🌐 Language: {lang}
        </button>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Control Panel & Map */}
        <div className="space-y-6">
          <div className="bg-slate-800 p-6 rounded-lg shadow-lg">
            <h2 className="text-xl font-semibold mb-4">1. Incident Setup</h2>
            <label className="block text-sm text-slate-400 mb-2">Select Active Disaster:</label>
            <select 
              value={disaster} 
              onChange={(e) => setDisaster(e.target.value)}
              className="w-full bg-slate-700 border border-slate-600 rounded p-2 mb-4"
            >
              <option value="Earthquake">Earthquake</option>
              <option value="Flood">Flood</option>
              <option value="Hurricane">Hurricane</option>
            </select>

            <button 
              onClick={handleShareLocation}
              className="w-full bg-red-600 hover:bg-red-700 transition font-medium py-2 rounded text-center"
            >
              📍 {location ? `Location: ${location.lat}, ${location.lng}` : "Share GPS Location"}
            </button>
          </div>

          <div className="bg-slate-800 p-6 rounded-lg shadow-lg h-64 flex flex-col justify-between">
            <h2 className="text-xl font-semibold mb-2">Interactive Shelters Map</h2>
            <div className="bg-slate-700 rounded h-40 flex items-center justify-center border border-dashed border-slate-500">
              <span className="text-slate-400">
                {location ? `Leaflet Active (Centered at ${location.lat}, ${location.lng})` : "Awaiting user location coordinates..."}
              </span>
            </div>
          </div>
        </div>

        {/* Chat Module */}
        <div className="bg-slate-800 p-6 rounded-lg shadow-lg flex flex-col h-[500px]">
          <h2 className="text-xl font-semibold border-b border-slate-700 pb-2 mb-4">💬 IBM Granite AI Assistant</h2>
          <div className="flex-1 overflow-y-auto space-y-3 mb-4 pr-2">
            {chat.map((msg, idx) => (
              <div key={idx} className={`p-3 rounded-lg max-w-[85%] ${msg.sender === 'user' ? 'bg-blue-600 ml-auto' : 'bg-slate-700'}`}>
                <p className="text-sm">{msg.text}</p>
              </div>
            ))}
            {loading && <div className="text-slate-400 text-sm animate-pulse">Assistant is compiling response...</div>}
          </div>
          <form onSubmit={handleSendMessage} className="flex gap-2">
            <input 
              type="text" 
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask for guidance or shelter directions..."
              className="flex-1 bg-slate-700 border border-slate-600 rounded px-3 py-2 text-white outline-none"
            />
            <button type="submit" className="bg-blue-500 hover:bg-blue-600 transition px-6 py-2 rounded font-medium">Send</button>
          </form>
        </div>
      </div>
    </div>
  );
}
