from pathlib import Path
extention = answer = None
data_result = {}

while extention != ".txt":
    file_path_user = input("txt파일을 끌어넣어 주세요.\n파일 경로: ")
    file_path = Path(file_path_user)
    extention = file_path.suffix.lower()

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        raw_data = file.readline()  # 첫 번째 줄만 읽기
        data_index = raw_data.split('	')  # 탭 문자를 기준으로 분리
except Exception as e:
    print(f"오류 발생 배승민에게 연락주세요 {e}")

data_index[-1] = data_index[-1][:-1]
print(data_index)

while answer != "Y":
    for i in range(len(data_index)):
        print(f"{i} : {data_index[i]}")
    no_use_index = input("\n이 중 사용하지 않을 목차의 번호를 3 5 6과 같은 형식으로 입력하되, 없다면 엔터키를 누르세요: ")
    no_use_index_list = no_use_index.split()
    print("\n사용하지 않는 목차는 다음과 같습니다.\n")
    for i in no_use_index_list:
        print(data_index[int(i)])
        
    answer = input("제대로 입력했나요? (Y/N) : ")
    

use_index = list(range(len(data_index)))

for i in range(len(no_use_index_list)):
    use_index.remove(int(no_use_index_list[i]))
    
data_result.fromkeys(use_index)
    
print("데이터 처리를 시작합니다. 진행도:")

n = 1
with open(file_path, 'r', encoding='utf-8') as file:
    while True:
        
        
        raw_data = file.readline(n)
        if not raw_data : break

        split_data = raw_data.split('	')
        for i in range(len(data_index)):
            
            if split_data[i] in data_result[use_index[i]]:
                data_result[use_index[i]] += 1
            else:
                data_result[use_index[i]].append({split_data[i] : 1})

        n += 1
        
print(data_result)