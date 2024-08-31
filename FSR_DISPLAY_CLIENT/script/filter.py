from script.config import *
from static_vars import static_vars
import numpy as np


#이동평균 필터
def setMAFilter(fsr_matrix): 

	#analogValue = [[[0 for col in range(SENSOR_Y_MAX)] for row in range(SENSOR_X_MAX)] for depth in range(20)] # 3차원 빈 리스트 생성
	#FilterTotal = [[0 for col in range(SENSOR_Y_MAX)] for row in range(SENSOR_X_MAX)]  #2차원 배열
	#FilterAver =  [[0 for col in range(SENSOR_Y_MAX)] for row in range(SENSOR_X_MAX)] #필터링 평균값

	analogValue = np.zeros((SENSOR_X_MAX, SENSOR_Y_MAX, 20))
	FilterTotal = np.zeros((SENSOR_X_MAX, SENSOR_Y_MAX))
	FilterAver = np.zeros((SENSOR_X_MAX, SENSOR_Y_MAX))
	
	for y in range(SENSOR_Y_MAX):
		
		for x in range(SENSOR_X_MAX):

			analogValue[x][y][0]=np.delete(analogValue[x][y][19],fsr_matrix[x][y]) #가장 오래된 (리스트 가장 왼쪽값) 제거	
			analogValue[x][y][19]=np.append(analogValue[x][y][19],fsr_matrix[x][y]) #fsr센서값 리스트 가장 오른쪽에 추가

			for z in range(20): #평균값 구하기
				FilterTotal[x][y] += analogValue[x][y][z]
	
			FilterAver[x][y] = FilterTotal[x][y] / 20
 
	return FilterAver


#저주파 통과 필터 (Low Pass Filter)
@static_vars(xLPF=np.zeros((SENSOR_X_MAX, SENSOR_Y_MAX)), counter=0)
def setLPFilter(fsr_matrix, alpha=0.7): 

	# When first run
	if setLPFilter.counter == 0:
		setLPFilter.xLPF = fsr_matrix
		setLPFilter.counter+=1

	else:
		#저주파 통과 필터값
		setLPFilter.xLPF = alpha*setLPFilter.xLPF+(1-alpha)*(fsr_matrix) 
				
	return setLPFilter.xLPF
					


