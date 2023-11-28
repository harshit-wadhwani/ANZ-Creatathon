let mediaRecorder;
let recordedChunks = [];

let questionIndex = 0;
const questions = [
    'question1.mp3',
    'question2.mp3',
    'question3.mp3',
    'question4.mp3',
    'question5.mp3',
];

const questionAudio = document.getElementById('questionAudio');

function startInterview() {
    if (questionIndex < questions.length) {
        questionAudio.src = questions[questionIndex];
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
        type: 'audio/mp3'
    });

    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.style.display = 'none';
    a.href = url;
    a.download = `${email}:ans${questionIndex}.mp3`;
    document.body.appendChild(a);
    a.setAttribute('download', `answer_audio/${email}:ans${questionIndex}.mp3`);
    document.body.appendChild(a);
    a.click();
    alert('Answer saved!');
    startInterview(); 
}
