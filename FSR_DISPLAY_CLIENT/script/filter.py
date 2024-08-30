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
					

def setGaussianFilter(size, sigma):
	#중심에서부터의 거리 계산
	array = np.arange((size//2)*(-1), (size//2)+1)
	
	
	#x^2+y^2 배열 초기화
	xx_yy_array = np.zeros((size, size))
	
	for x in range(size):
		for y in range(size):
			#중심에서부터의 거리를 제곱합으로 계산
			xx_yy_array[x,y] = array[x]**2+array[y]**2
	
	# 필터 초기화
	Gaussian_filter = np.zeros((size, size))#size X size 형태의 2차원 배열
	
	for x in range(size):
		for y in range(size):
			# 수학적 수식 구현부
			Gaussian_filter[x,y] = 1 / (2 * np.pi * sigma**2) * np.exp(-xx_yy_array[x,y]/(2 * sigma**2))
	
	# Scaling
	Gaussian_threshold = Gaussian_filter.sum()/ size*size
	
	return Gaussian_threshold