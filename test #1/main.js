// import SocketIO
var s = document.createElement("script");
s.type = "text/javascript";
s.src = "https://cdnjs.cloudflare.com/ajax/libs/socket.io/2.2.0/socket.io.js";
$('body').append(s);

var socket = io('http://localhost:7777');
// listening
var listenList = ['EURUSD'];
listenList.forEach(currency => {
    var element = document.querySelector(`.${currency}-priceAsk`);
    var observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.type == "attributes") {
                var toSendObj = {
                    'cur': currency,
                    'val': element.attributes['data-value'].value
                };
                console.log(toSendObj);
                socket.emit('newPrice', toSendObj);
            }
        });
    });
    observer.observe(element, {
        attributes: true //configure it to listen to attribute changes
    });
});