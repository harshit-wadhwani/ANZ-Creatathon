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
    // Add logic to start recording audio (requires additional libraries or APIs)
    alert('Recording started...');
}

function saveAnswer() {
    // Add logic to save the recorded audio as ans1, ans2, etc.
    alert('Answer saved!');
    startInterview(); // Move to the next question after saving the answer
}
