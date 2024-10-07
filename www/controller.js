$(document).ready(function () {
    eel.expose(DisplayMessage);
    function DisplayMessage(message) {
        $(".siri-message").text(message);  // Changed from li:first to direct update
        $('.siri-message').textillate('start');
    };

    // Display hood
    eel.expose(ShowHood)
    function ShowHood() {
        $("#oval").attr("hidden", false);
        $("#siriwave").attr("hidden", true);
    }


eel.expose(senderText)
function senderText(message) {
    var chatBox = document.getElementById("chat-canvas-body");
    if (message.trim() !== "") {
        chatBox.innerHTML += `<div class="row justify-content-end mb-4">
        <div class = "width-size">
        <div class="sender_message">${message}</div>
    </div>`; 

        // Scroll to the bottom of the chat box
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}

eel.expose(receiverText)
function receiverText(message) {

    var chatBox = document.getElementById("chat-canvas-body");
    if (message.trim() !== "") {
        chatBox.innerHTML += `<div class="row justify-content-start mb-4">
        <div class = "width-size">
        <div class="receiver_message">${message}</div>
        </div>
    </div>`; 
                // Scroll to the bottom of the chat box
                chatBox.scrollTop = chatBox.scrollHeight;
            }
            
        }
    
    });        