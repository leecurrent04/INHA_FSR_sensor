from script.config import *
import numpy as np

def setMAFilter(fsr_matrix): #이동편균 필터

	analogValue= [[[0 for col in range(SENSOR_Y_MAX)] for row in range(SENSOR_X_MAX)] for depth in range(20)] # 3차원 빈 리스트 생성
	
	FilterTotal = [[0 for col in range(SENSOR_Y_MAX)] for row in range(SENSOR_X_MAX)]  #2차원 배열
	FilterAver =  [[0 for col in range(SENSOR_Y_MAX)] for row in range(SENSOR_X_MAX)] #필터링 평균값

	for y in range(SENSOR_Y_MAX):
		
		for x in range(SENSOR_X_MAX):

			analogValue[x][y][0]=np.delete(analogValue[x][y][19],fsr_matrix[x][y]) #가장 오래된 (리스트 가장 왼쪽값) 제거	
			analogValue[x][y][19]=np.append(analogValue[x][y][19],fsr_matrix[x][y]) #fsr센서값 리스트 가장 오른쪽에 추가

			for z in range(20): #평균값 구하기
				FilterTotal[x][y] += analogValue[x][y][z]
	
			FilterAver[x][y] = FilterTotal[x][y] / 20
 
			return FilterAver[x][y]



def setLPFilter(fsr_matrix): #저주파 통과필터

	prevValue = 0; #직전 추정값 초기화
	FirstRun =1
	xLPF = 0
	for y in range(SENSOR_Y_MAX):

		for x in range(SENSOR_X_MAX):

			if FirstRun == 1:
				#직전 추정값 첫번째 측정데이터로 초기화
				prevValue = fsr_matrix[x][y] 
				FirstRun = FirstRun + 1
		
			else:
				alpha=0.7 #가중치
				xLPF = alpha*prevValue+(1-alpha)*(fsr_matrix[x][y]) #저주파 통과 필터값
				prevValue = xLPF
				return xLPF #저주파 통과필터값 반환
			
			

