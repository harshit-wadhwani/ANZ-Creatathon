let mediaRecorder;
let recordedChunks = [];

let questionIndex = 0;
const questions = [];

fetch('../questions_audio/')
  .then(response => response.text())
  .then(data => {
    const parser = new DOMParser();
    const htmlDocument = parser.parseFromString(data, 'text/html');
    
    // Assuming your links are stored in an element with the ID 'audioLinks'
    const linksContainer = htmlDocument.getElementById('audioLinks');
    
    if (linksContainer) {
      const links = linksContainer.querySelectorAll('a');
      
      links.forEach(link => {
        if (link.href.endsWith('.mp3')) {
          questions.push(link.href);
        }
      });
      
      console.log('Fetched questions:', questions);
    } else {
      console.error('Audio links container not found');
    }
  })
  .catch(error => console.error('Error fetching questions:', error));

// const questions = [
//     'question1.mp3',
//     'question2.mp3',
//     'question3.mp3',
//     'question4.mp3',
//     'question5.mp3',
// ];

const questionAudio = document.getElementById('questionAudio');

function startInterview() {
    if (questionIndex < questions.length) {
        questionAudio.src = questions[questionIndex];
        console.log('Audio source:', questionAudio.src);
        questionAudio.play()
        .then(() => {
          console.log('Audio playback started successfully');
        })
        .catch(error => {
          console.error('Error starting audio playback:', error);
        });
        questionIndex++;
    } else {
        alert('Interview completed!');
    }
}

function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start();

            mediaRecorder.ondataavailable = function(e) {
                recordedChunks.push(e.data);
            };

            alert('Recording started...');
            mediaRecorder.onstop = function(e) {
              console.log('Recording stopped:', e);
          };
          
          mediaRecorder.onerror = function(e) {
              console.error('MediaRecorder error:', e);
          };
          
        })
        .catch(err => console.log('getUserMedia Error: ', err));
}

function saveAnswer() {
    mediaRecorder.stop();

    const blob = new Blob(recordedChunks, {
        type: 'audio/wav'
    });

    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.style.display = 'none';
    a.href = url;
    a.download = `${email}:ans${questionIndex}.wav`;
    document.body.appendChild(a);
    a.setAttribute('download', `answer_audio/${email}:ans${questionIndex}.wav`);
    document.body.appendChild(a);
    a.click();
    alert('Answer saved!');
    startInterview(); 
}
