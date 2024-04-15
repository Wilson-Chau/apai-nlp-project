import React, { useState, useEffect } from "react";
import ReactDOM from "react-dom";

import BotMessage from "./components/BotMessage";
import UserMessage from "./components/UserMessage";
import Messages from "./components/Messages";
import Input from "./components/Input";

import "./styles.css";
import Header from "./components/Header";

var msgHist = "";

function Chatbot() {
  const [messages, setMessages] = useState([]);

  const API = {
    GetChatbotResponse: async message => {
      return new Promise(function(resolve, reject) {
          if (message === "hi") resolve("Welcome to chatbot!");
          else {
            resolve(
              fetch("http://127.0.0.1:5000/ask",{
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json',
                },
                body: JSON.stringify({message: message})
              })
                .then(res => res.json())
                .then(data => {
                  if (data.response){
                    msgHist = msgHist + "response:" + data.response
                    return data.response;
                  }
                })
            );
          }
      });
    }
  };

  useEffect(() => {
    async function loadWelcomeMessage() {
      setMessages([
        <BotMessage
          key="0"
          fetchMessage={async () => "Hello! I'm your personal AI counsellor. How can I help you today?"}
        />
      ]);
    }
    loadWelcomeMessage();
  }, []);

  const send = text => {
    msgHist = msgHist + "user:" + text
    console.log(msgHist);
    const newMessages = messages.concat(
      <UserMessage key={messages.length + 1} text={text} />,
      <BotMessage
        key={messages.length + 2}
        fetchMessage={async () => await API.GetChatbotResponse(msgHist)}
      />
    );
    setMessages(newMessages);
  };

  return (
    <div className="chatbot">
      <Header />
      <Messages messages={messages} />
      <Input onSend={send} />
    </div>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<Chatbot />, rootElement);
