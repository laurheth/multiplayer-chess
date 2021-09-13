declare const io: any;

const socket = io();

socket.on('connect', function() {
    console.log("Connected!");
    socket.send({data: 'I\'m connected!'});
    socket.emit("test", {data: 'I\'m connected!'});
});

socket.on('message', (event:any)=>{
    console.log(event);
});

socket.on('test', (event:any)=>{
    console.log(event, "!!!!!!!!!");
});