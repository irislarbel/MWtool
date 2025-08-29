from pathlib import Path
import csv
import sys
extention = answer = None
data_result = {}
FIRST_CHECK = True
modes = [
    '기본',
    'mbti전용(기본 + e:i추가)',
    '최대최소최빈값평균',
    '자동(전투력유니온아티팩트등등에쓰세요.. 적당한단위로잘라서분류해줌)'
]

while extention != ".txt":
    file_path_user = input("txt파일을 끌어넣어 주세요.\n파일 경로: ")
    file_path = Path(file_path_user)
    extention = file_path.suffix.lower()

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        data_all = list(reader)
        data_index = data_all[0]
        data_body = data_all[1:]
except Exception as e:
    print(f"오류 발생 배승민에게 연락주세요 {e}")

data_index[-1] = data_index[-1].strip()
print(data_index)

while answer != "Y":
    for i in range(len(data_index)):
        print(f"{i} : {data_index[i]}")
    no_use_index = input("\n이 중 사용하지 않을 목차의 번호를 3 5 6과 같은 형식으로 입력하되, 없다면 엔터키를 누르세요: ")
    no_use_index_list = no_use_index.split()

    try:
        print("\n사용하지 않는 목차는 다음과 같습니다.\n")
        temp = set(no_use_index_list)
        no_use_index_list = list(temp)
        for i in no_use_index_list:
            print(data_index[int(i)])
    except Exception:
        print('잘못된 입력입니다.')
        continue
    answer = input("\n제대로 입력했나요? (Y/N) : ")
    

use_index = list(range(len(data_index)))

for i in range(len(no_use_index_list)):
    use_index.remove(int(no_use_index_list[i]))
    
data_result = {data_index[k] : {} for k in use_index}
    
print("데이터 분류를 시작합니다.")


for split_data in data_body:
    
    
    split_data[-1] = split_data[-1].strip()
    for i in use_index:
        if split_data[i] in data_result[data_index[i]]:
            
            data_result[data_index[i]][split_data[i]] += 1
            
        else:
            data_result[data_index[i]][split_data[i]] = 1
            

        
while True:
    for k,i in enumerate(use_index):
        print(f'{data_index[i]} : {k}')
    check_num = input('\n분류가 완료되었습니다. 확인하고 싶은 목차의 번호를 입력하세요: ')
    if isinstance(check_num, int) :
        print('입력이 잘못되었습니다.')
        continue
    for k, i in enumerate(modes):
        print(f'\n{i} : {k}')
    check_num = int(check_num)
    mode_num = input(f'\n{data_index[use_index[check_num]]} 목차를 선택하셨습니다. 처리 모드를 선택하세요: ')
    
    if isinstance(mode_num, int) :
        print('입력이 잘못되었습니다.')
        continue
    elif int(mode_num) > len(modes):
        print('입력이 잘못되었습니다.')
        continue
    mode_num = int(mode_num)
    if input(f'{data_index[use_index[check_num]]}를 {modes[mode_num]} 모드를 사용하여 처리할까요? (Y/N): ') != 'Y':
        continue
    if mode_num == 0:
        print(f'\n{data_index[use_index[check_num]]}')
        for i in range(data_result[data_index[use_index[check_num]]].keys):
            print(f'{data_result[data_index[use_index[check_num]]].keys}: {data_result[data_index[use_index[check_num]]][data_result[data_index[use_index]].keys]}명')
        isquit = input('종료를 원하시면 Y, 다른 목차를 처리하고 싶으시면 N을 입력하세요: ')
        if isquit == 'Y':
            sys.quit()
        else:
            continue