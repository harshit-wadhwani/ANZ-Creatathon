let mediaRecorder;
let recordedChunks = [];

let questionIndex = 0;
const questions = [];

let startInterview = document.getElementById('startInterview');
startInterview.disabled = true;

fetch('../questions_audio/')
  .then(response => response.text())
  .then(data => {
    const parser = new DOMParser();
    const htmlDocument = parser.parseFromString(data, 'text/html');
    const links = htmlDocument.querySelectorAll('a');
    links.forEach(link => {
      if (link.href.endsWith('.mp3')) {
        questions.push(link.href.split('/').pop());
      }
    });
    console.log(questions); // Debugging statement
    startInterview.disabled = false; // Enable the button after questions have been fetched
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
// questionAudio.play();

function startInterview() {
    if (questionIndex < questions.length) {
        questionAudio.src = '../questions_audio/'+ questions[questionIndex];
        questionAudio.play();
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
    a.setAttribute('download', `../ans_audio/${email}:ans${questionIndex}.wav`);
    document.body.appendChild(a);
    a.click();
    alert('Answer saved!');
    startInterview(); 
}
