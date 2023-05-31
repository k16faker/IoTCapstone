# import torch
# import cv2
# import numpy as np
# import time

# def POINTS(event, x, y, flags, param):
#     if event == cv2.EVENT_MOUSEMOVE :  
#         colorsBGR = [x, y]
#         print(colorsBGR)

# cv2.namedWindow('ROI')
# cv2.setMouseCallback('ROI', POINTS)

# cap=cv2.VideoCapture('vid4.mp4')
# bg = cv2.imread('background.jpg')
# bg = cv2.resize(bg, (1920, 1080))

# model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
# num_of_people = 0
# isUsed = False
# start_time = time.time()
# no_rectangle_start_time = None

# # 저장할 이미지 파일 이름 설정
# output_filename = 'heatmap.jpg'

# # 원형을 그릴 반경 설정 (픽셀)
# radius = 50

# # 원형을 그릴 색상 설정 (BGR)
# circle_color = (0, 0, 255)

# # 사각형이 그려진 위치의 중심점들을 저장할 리스트 생성
# center_points = []

# while True:
#     ret,frame=cap.read()
#     if not ret:
#         break

#     frame=cv2.resize(frame,(1920,1080))
#     num_of_people = 0
#     num_people_treadmil = 0  # 범위 안에 있는 사람의 수를 저장할 변수
#     num_of_lag = 0  # 범위 안에 있는 사람의 수를 저장할 변수
#     results = model(frame)

#     for index, row in results.pandas().xyxy[0].iterrows():
#         x1 = int(row['xmin'])
#         y1 = int(row['ymin'])
#         x2 = int(row['xmax'])
#         y2 = int(row['ymax'])
#         name = row['name']
#         if name == 'person':
#             cv2.rectangle(frame, (x1,y1),(x2,y2),(0,255,0),2)
#             num_of_people += 1

#             # 사각형의 중심점 계산
#             cx = int((x1 + x2) / 2)
#             cy = int((y1 + y2) / 2)

#             # 중심점이 범위 안에 있는지 검사하고 사람 수 세기
#             if cx >= 1116 and cx <= 1584 and cy >= 500 and cy <= 925:
#                 num_people_treadmil += 1
#             if cx >= 770 and cx <= 914 and cy >= 146 and cy <= 356:
#                 num_of_lag += 1

#             center_points.append((cx, cy))  # 중심점 리스트에 추가

#     # 범위를 둘러싸는 사각형 그리기
#     cv2.rectangle(frame, (1116, 500), (1584, 925), (0, 0, 255), 2)
#     cv2.rectangle(frame, (770, 146), (914, 356), (0, 0, 255), 2)

#     # 사각형 안에 있는 사람의 수 표시하기
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     cv2.putText(frame, f'Number of peoples: {num_of_people}', (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

#     # Treadmil 안에 있는 사람의 수 표시하기
#     cv2.putText(frame, f'Treadmil: {num_people_treadmil}', (1116, 925), font, 0.8, (0, 255, 255), 2, cv2.LINE_AA)

#     # Lag 안에 있는 사람의 수 표시하기
#     cv2.putText(frame, f'Lag: {num_of_lag}', (770, 356), font, 0.8, (0, 255, 255), 2, cv2.LINE_AA)

#     cv2.imshow("ROI",frame)
#     if cv2.waitKey(1)&0xFF==27:
#         break




# # 중심점 리스트를 사용하여 히트맵 생성
# heatmap = np.zeros_like(bg)
# for center_point in center_points:
#     # 중심점과 다른 중심점들 사이의 거리 계산
#     distances = [np.sqrt((center_point[0]-x)**2 + (center_point[1]-y)**2) for x,y in center_points]

#     # 거리에 따른 가중치 계산
#     weights = [np.exp(-d/50) for d in distances]

# # 가중치를 곱한 값을 사용하여 원형을 그림
#     for i, weight in enumerate(weights):
#         color = (0, 0, int(255*weight))
#         cv2.circle(heatmap, center_points[i], int(radius*weight), color, -1)

# # 배경 이미지에 히트맵을 더해서 저장
# heatmap_alpha = cv2.cvtColor(heatmap.astype(np.uint8), cv2.COLOR_BGR2GRAY)
# heatmap_alpha = cv2.GaussianBlur(heatmap_alpha, (31, 31), 0)

# # 값 범위를 [0, 255]로 정규화
# heatmap_alpha = cv2.normalize(heatmap_alpha, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# # 적절한 색상 맵 적용
# heatmap_alpha = cv2.applyColorMap(heatmap_alpha, cv2.COLORMAP_JET)

# # 적절한 색상 맵 적용
# heatmap_alpha = cv2.cvtColor(heatmap_alpha, cv2.COLOR_BGR2GRAY)
# heatmap_alpha = cv2.normalize(heatmap_alpha, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
# heatmap_alpha = cv2.applyColorMap(heatmap_alpha, cv2.COLORMAP_JET)

# # 배경 이미지와 히트맵 이미지 합성
# result = cv2.addWeighted(bg, 0.7, heatmap_alpha, 0.3, 0)

# # 결과 이미지 저장
# cv2.imwrite(output_filename, result)



# cap.release()
# cv2.destroyAllWindows()

#이 위로 기본 모델


import torch
import cv2
import numpy as np
import time
import firebase_admin
from datetime import datetime
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("/Users/sjyj98/Desktop/IoTCapstone/SmartGym/iotcapstone-4b75d-firebase-adminsdk-t68ac-2214561ca8.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
prev_upload_time=None


def points(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)

cv2.namedWindow('ROI')
cv2.setMouseCallback('ROI', points)

cap = cv2.VideoCapture('vid4.mp4')
#cap = cv2.VideoCapture('http://192.168.35.135:81/stream')
bg = cv2.imread('background.jpg')
bg = cv2.resize(bg, (1920, 1080))

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
num_of_people = 0
isUsed = False
start_time = time.time()

# 저장할 이미지 파일 이름 설정
output_filename = 'heatmap.jpg'

# 원형을 그릴 반경 설정 (픽셀)
radius = 50

# 원형을 그릴 색상 설정 (BGR)
circle_color = (0, 0, 255)

# 사각형이 그려진 위치의 중심점들을 저장할 리스트 생성
center_points = []

def upload_firestore(num_peoples, num_people_treadmil, number_of_lag,num_of_machine1):
    doc_ref = db.collection(u'object_count').document(u'current_counts')
    doc_ref.set({
        u'num_peoples': num_peoples,
        u'num_people_treadmil': num_people_treadmil,
        u'number_of_lag': number_of_lag,
        u'number_of_machine1': num_of_machine1
    })

def upload_if_needed(num_peoples, num_people_treadmil, number_of_lag,num_of_machine1, num_of_machine2):
    global prev_num_peoples, prev_num_people_treadmil, prev_number_of_lag, prev_num_of_machine1, prev_num_of_machine2
    global prev_upload_time  # prev_upload_time 변수 선언
    now = time.monotonic()
    if prev_upload_time is None or now - prev_upload_time > 5.0:
        if prev_num_peoples != num_peoples:
            db.collection(u'object_count').document(u'current_counts').update({u'num_rectangles': num_peoples})
            prev_num_peoples = num_peoples
        if prev_num_people_treadmil != num_people_treadmil:
            db.collection(u'object_count').document(u'current_counts').update({u'num_people_treadmil': num_people_treadmil})
            prev_num_people_treadmil = num_people_treadmil
        if prev_number_of_lag != number_of_lag:
            db.collection(u'object_count').document(u'current_counts').update({u'num_of_lag': number_of_lag})
            prev_number_of_lag = number_of_lag
        if prev_num_of_machine1 != num_of_machine1:
            db.collection(u'object_count').document(u'current_counts').update({u'num_of_machine1': num_of_machine1})
            prev_num_of_machine1 = num_of_machine1
        if prev_num_of_machine2 != num_of_machine2:
            db.collection(u'object_count').document(u'current_counts').update({u'num_of_machine2': num_of_machine2})
            prev_num_of_machine2 = num_of_machine2
        prev_upload_time = now  # prev_upload_time 변수에 현재 시간 할당



last_upload_time = None

def check_the_hour(num_peoples):
    global last_upload_time
    now = datetime.now()
    
    # 이전에 업로드한 시간과 현재 시간을 비교하여,
    # 일정 시간 이상이 지난 경우에만 업로드를 진행합니다.
    #if now.second == 0:
    if now.minute == 0:
        if last_upload_time is None or (now - last_upload_time).seconds >= 3:
            doc_ref = db.collection(u'object_count').document(str(now.hour))

            # 'counted_number' 필드가 존재하면 값을 증가시키고,
            # 존재하지 않으면 초기값을 1로 설정합니다.
            doc_ref.update({
                u'num_peoples': firestore.Increment(num_peoples),
                u'counted_number': firestore.Increment(1)
            })

            # 업로드한 시간을 저장합니다.
            last_upload_time = now



prev_num_peoples = -1
prev_num_people_treadmil = -1
prev_number_of_lag = -1
prev_num_of_machine1 = -1
prev_num_of_machine2 = -1

tracked_paths = []

while True:
    nowtime = datetime.now()
    cur_time = nowtime.strftime("%H:%M:%S")
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (1920, 1080))
    num_of_people = 0
    num_people_treadmil = 0  #런닝머신 범위 안에 있는 사람의 수를 저장할 변수
    num_of_lag = 0  # 랙 범위 안에 있는 사람의 수를 저장할 변수
    num_of_machine1 = 0  # 머신1 범위 안에 있는 사람의 수를 저장할 변수
    num_of_machine2 = 0  # 머신2 범위 안에 있는 사람의 수를 저장할 변수
    results = model(frame)

    for index, row in results.pandas().xyxy[0].iterrows():
        x1 = int(row['xmin'])
        y1 = int(row['ymin'])
        x2 = int(row['xmax'])
        y2 = int(row['ymax'])
        name = row['name']
        if name == 'person':
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            num_of_people += 1

            # 사각형의 중심점 계산
            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)

            # 중심점이 범위 안에 있는지 검사하고 사람 수 세기
            if 1116 <= cx <= 1584 and 500 <= cy <= 925:
                num_people_treadmil += 1
                
            if 770 <= cx <= 914 and 146 <= cy <= 356:
                num_of_lag += 1

            if 187 <= cx <= 397 and 139 <= cy <= 200:
                num_of_machine1 += 1

            if 180 <= cx <= 375 and 310 <= cy <= 449:
                num_of_machine2 += 1

            center_points.append((cx, cy))  # 중심점 리스트에 추가
            

    # 범위를 둘러싸는 사각형 그리기
    cv2.rectangle(frame, (1116, 500), (1584, 925), (0, 0, 255), 2)
    cv2.rectangle(frame, (770, 146), (914, 356), (0, 0, 255), 2)
    cv2.rectangle(frame, (187, 139), (397, 200), (0, 0, 255), 2)
    cv2.rectangle(frame, (180, 310), (375, 449), (0,0,255), 2)

    font = cv2.FONT_HERSHEY_SIMPLEX
    # 사각형 안에 있는 사람의 수 표시하기
    cv2.putText(frame, f'Number of peoples: {num_of_people}', (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

    # Treadmil 안에 있는 사람의 수 표시하기
    cv2.putText(frame, f'Treadmil: {num_people_treadmil}', (1116, 925), font, 0.8, (0, 255, 255), 2, cv2.LINE_AA)

    # Machine1 안에 있는 사람의 수 표시하기
    cv2.putText(frame, f'Machine1: {num_of_machine1}', (187, 200), font, 0.8, (0, 255, 255), 2, cv2.LINE_AA)

    cv2.putText(frame, f'Machine2: {num_of_machine2}', (180, 449), font, 0.8, (0, 255, 255), 2, cv2.LINE_AA)

    # Lag 안에 있는 사람의 수 표시하기
    cv2.putText(frame, f'Lag: {num_of_lag}', (770, 356), font, 0.8, (0, 255, 255), 2, cv2.LINE_AA)

    cv2.putText(frame, f'Time:{cur_time}', (50,100), font, 1, (0, 255, 255), 2, cv2.LINE_AA)



    for i, center_point in enumerate(center_points):
        if i >= len(tracked_paths):
            tracked_paths.append([])

        tracked_paths[i].append(center_point)  # 현재 중심점을 해당 사람의 이동 경로에 추가

        # 이동 경로를 선으로 그리기
        for j in range(1, len(tracked_paths[i])):
            prev_point = tracked_paths[i][j - 1]
            curr_point = tracked_paths[i][j]
            cv2.line(bg, prev_point, curr_point, (0, 0, 255), 2)



    cv2.imshow("SmartGym", frame)

    upload_if_needed(num_of_people, num_people_treadmil, num_of_lag, num_of_machine1, num_of_machine2)
    check_the_hour(num_of_people)

    if cv2.waitKey(1) & 0xFF == 27:
        break





# 히트맵 구역 7x7로 나누기
region_width = bg.shape[1] // 7
region_height = bg.shape[0] // 7

# 각 구역의 빨간 점 개수를 저장할 배열
region_counts = np.zeros((49,), dtype=int)

# 각 구역의 빨간 점 개수를 계산
for centroid in center_points:
    region_x = centroid[0] // region_width
    region_y = centroid[1] // region_height
    region_index = region_y * 7 + region_x

    # 범위를 벗어나는 경우 무시
    if region_index < 49:
        region_counts[region_index] += 1

# 가장 많은 빨간 점 개수 계산
max_count = np.max(region_counts)

# 히트맵 이미지 생성
overlay = np.zeros_like(bg, dtype=np.uint8)

# 각 구역의 빨간 점 개수에 따라 색칠
for region_index, count in enumerate(region_counts):
    # 구역의 좌표 계산
    region_x = (region_index % 7) * region_width
    region_y = (region_index // 7) * region_height

    # 빨간 점 개수에 따라 색 결정
    color = (0, int(255 * (count / max_count)), int(255 * (count / max_count)))

    # 이미지 위에 사각형 그리기
    cv2.rectangle(overlay, (region_x, region_y), (region_x + region_width, region_y + region_height),
                  color, -1)

# 히트맵 이미지와 원본 이미지를 합성
heatmap = cv2.addWeighted(overlay, 0.5, bg, 0.5, 0)

# 히트맵 이미지 저장
cv2.imwrite(output_filename, heatmap)

cap.release()
cv2.destroyAllWindows()


