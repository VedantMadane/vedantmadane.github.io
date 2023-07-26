// Put variables in global scope to make them available to the browser console.
console.log("hello siddhesh");
const video = document.querySelector("video");
const constraints = {
  audio: false,
  video: true,
};
function Check(){
navigator.mediaDevices
  .getUserMedia(constraints)
  .then((stream) => {
    const videoTracks = stream.getVideoTracks();
    console.log("Got stream with constraints:", constraints);
    console.log(`Using video device: ${videoTracks[0].label}`);
    stream.onremovetrack = () => {
      console.log("Stream ended");
    };
    video.srcObject = stream;
  })
  .catch((error) => {
    if (error.name === "OverconstrainedError") {
      console.error(
        `The resolution ${constraints.video.width.exact}x${constraints.video.height.exact} px is not supported by your device.`,
      );
    } else if (error.name === "NotAllowedError") {
      console.error(
        "You need to grant this page permission to access your camera and microphone.",
      );
    } else {
      console.error(`getUserMedia error: ${error.name}`, error);
    }
  });
};
  function check1(){
  navigator.mediaDevices.enumerateDevices()
  .then(devices => {
    // Check the connected devices
    console.log(devices);  
  });

  };


    function check2(){
    navigator.mediaDevices.addEventListener('devicechange', () => {
  // Do whatever you need to with the devices
  // Maybe use enumerateDevices() to see what connected
      enumerateDevices()
      console.log("device changed");
      alert("Device dis/connected");
});
  };
