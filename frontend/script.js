function sendMessage() {
    
    const userInput = document.getElementById("user_input").value;
    document.getElementById("user_input").value = ""; 
  
    
    const chatbox = document.getElementById("chatbox");
    chatbox.innerHTML += `<p><b>You:</b> ${userInput}</p>`; 
  
    
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/get_response", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function () {
      if (this.readyState === 4 && this.status === 200) {
        const response = JSON.parse(this.responseText).response;
  
        
        chatbox.innerHTML += `<p><b>Bot:</b> ${response}</p>`; 
      }
    };
    xhr.send(`user_input=${userInput}`); 
  }