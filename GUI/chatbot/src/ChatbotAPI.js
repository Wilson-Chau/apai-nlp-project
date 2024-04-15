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
                    return data.response;
                  }
                })
            );
          }
      });
    }
  };
  
  export default API;
  