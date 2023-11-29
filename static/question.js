// let mediaRecorder;
// let recordedChunks = [];

// let questionIndex = 0;
// const questions = [];
// console.log("testing here")
// let startInterview = document.getElementById('startInterview');
// startInterview.disabled = true;
// //testing
// fetch('../questions_audio/')
//   .then(response => response.text())
//   .then(data => {
//     const parser = new DOMParser();
//     const htmlDocument = parser.parseFromString(data, 'text/html');
//     const links = htmlDocument.querySelectorAll('a');
//     links.forEach(link => {
//       if (link.href.endsWith('.mp3')) {
//         questions.push(link.href.split('/').pop());
//       }
//     });
//     console.log(questions); // Debugging statement
//     startInterview.disabled = false; // Enable the button after questions have been fetched
//   })
//   .catch(error => console.error('Error fetching questions:', error));


// const questionAudio = document.getElementById('questionAudio');
// // questionAudio.play();

// function startInterview() {
//     if (questionIndex < questions.length) {
//         questionAudio.src = '../questions_audio/'+ questions[questionIndex];
//         questionAudio.play();
//         questionIndex++;
//     } else {
//         alert('Interview completed!');
//     }
// }

// function startRecording() {
//     navigator.mediaDevices.getUserMedia({ audio: true })
//         .then(stream => {
//             mediaRecorder = new MediaRecorder(stream);
//             mediaRecorder.start();

//             mediaRecorder.ondataavailable = function(e) {
//                 recordedChunks.push(e.data);
//             };

//             alert('Recording started...');
//             mediaRecorder.onstop = function(e) {
//               console.log('Recording stopped:', e);
//           };
          
//           mediaRecorder.onerror = function(e) {
//               console.error('MediaRecorder error:', e);
//           };
          
//         })
//         .catch(err => console.log('getUserMedia Error: ', err));
// }

// function startRecording() {
//   console.log(started)
//   navigator.mediaDevices.getUserMedia({ audio: true })
//     .then(function(stream) {
//       mediaRecorder = new MediaRecorder(stream);
//       mediaRecorder.start();
//     })
//     .catch(function(err) {
//       console.log('Error: ' + err);
//     });
// }
// function stopRecording() {
//   if (mediaRecorder && mediaRecorder.state === 'recording') {
//     mediaRecorder.stop(); // Stop the recording if it's currently in the recording state
//   }
// }

// function saveAnswer(email) {
//     mediaRecorder.stop();

//     const blob = new Blob(recordedChunks, {
//         type: 'audio/wav'
//     });

//     const url = URL.createObjectURL(blob);
//     const a = document.createElement('a');
//     a.style.display = 'none';
//     a.href = url;
//     a.download = `${email}:ans${questionIndex}.wav`;
//     document.body.appendChild(a);
//     a.setAttribute('download', `../ans_audio/${email}:ans${questionIndex}.wav`);
//     document.body.appendChild(a);
//     a.click();
//     alert('Answer saved!');
//     startInterview(); 
// }
