# IoTCapstone

<h1>SmartGym 사용법</h1>

<p>1. SmartGym 폴더에서 터미널 오픈 후 pip install requirements.txt 실행</p>
<p>2. 코드 내부 firebase 인증서 경로를 다운받은 환경에 맞게 수정 </p>
<p>3. cap = VideoCapture("vid4.mp4")를 단순 연결된 웹캠의 영상으로 사용하고싶다면 cap = VideoCapture(0)으로,
  esp32cam 모델과 함께 사용하고싶다면 cap = VideoCapture("해당 ip주소")로 변경 </p>
  
 <p>4. python yolo52.py 로 실행 </p>
 
 
 <h1> 애플리케이션 사용법 </h1>
 <p> 1. React_Native_App 폴더에서 터미널을 열고 npm install 실행 </p>
 <p> 2. 모바일에서 expo 애플리케이션 다운 </p>
 <p> 3. 폴더에서 npm start를 실행하면 나오는 qr코드를 expo 앱의 qr 스캔 기능으로 스캔(단, 컴퓨터와 스마트폰이 동일한 인터넷환경을 사용중일것 ex) 동일한 wifi등)</p>
