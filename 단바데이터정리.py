from pathlib import Path
import csv
import sys
extention = answer = None
data_result = {}
FIRST_CHECK = True
modes = [
    '기본',
    'mbti전용(기본 + e:i추가)',
    '최대최소중앙값평균',
    '자동(전투력유니온아티팩트등등에쓰세요.. 적당한단위로잘라서분류해줌)',
    '결과미합산잇는항목은 이거쓰세요 제외가능'
]
mbti = [
    'INTP',
    'ENTP',
    'INTJ',
    'ENTJ',
    'INFP',
    'INFJ',
    'ENFP',
    'ENFJ',
    'ISTP',
    'ESFP',
    'ISFP',
    'ESTP',
    'ISTJ',
    'ISFJ',
    'ESFJ',
    'ESTJ'
]

def count_mbti(type1, type2, data, locate):
    print(f'\n{type1}/{type2}')
    count_1 = count_2 = 0
    for i in data:
        if i[locate] == type1 :
            count_1 += data[i]
        else:
            count_2 += data[i]
    print(f'{type1} {count_1}명 {round((count_1/(count_1+count_2))*100,4)}%, {type2} {count_2}명 {round((count_2/(count_1+count_2))*100,4)}% 입니다.')

def result_print(data, m_num, mb = None):
    all_count = 0
    r_keys = list(data.keys())
    for i in r_keys:
        all_count += data[i]
        
    if m_num == 1:
        for i in r_keys:
            print(f'{i}: {data[i]}명  {round((data[i]/all_count)*100,4)}%')
            mb.remove(i)
        return mb
    else:
        for i in r_keys:
            print(f'{i}: {data[i]}명  {round((data[i]/all_count)*100,4)}%')

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
    try:
        check_num = int(check_num)
    except:
        print('입력이 잘못되었습니다.')
        continue
    
    if check_num > len(use_index) or check_num < 0 :
        print('입력이 잘못되었습니다.')
        continue

    for k, i in enumerate(modes):
        print(f'\n{i} : {k}')
    check_num = int(check_num)
    mode_num = input(f'\n{data_index[use_index[check_num]]} 목차를 선택하셨습니다. 처리 모드를 선택하세요: ')
    
    try:
        mode_num = int(mode_num)
    except:
        print('입력이 잘못되었습니다.')
        continue
    
    if mode_num > len(modes) or mode_num < 0 :
        print('입력이 잘못되었습니다.')
        continue
    
    mode_num = int(mode_num)
    if input(f'{data_index[use_index[check_num]]} 목차를 {modes[mode_num]} 모드를 사용하여 처리할까요? (Y/N): ') != 'Y':
        continue
    
    if mode_num == 0:
        data_result[data_index[use_index[check_num]]] = dict(sorted(data_result[data_index[use_index[check_num]]].items()))
        result_print(data_result[data_index[use_index[check_num]]], mode_num)
        isquit = input('종료를 원하시면 Y, 다른 목차를 처리하고 싶으시면 N을 입력하세요: ')
        if isquit == 'Y':
            sys.quit()
        else:
            continue
        
    if mode_num == 1:
        data_result[data_index[use_index[check_num]]] = dict(sorted(data_result[data_index[use_index[check_num]]].items(), key=lambda x: x[1], reverse=True))
        print(data_result[data_index[use_index[check_num]]])
        result_keys = list(data_result[data_index[use_index[check_num]]].keys())
        try:
            for i in range(len(result_keys)):
                result_keys[i] = result_keys[i].upper().strip()
                if result_keys[i] not in mbti:
                    print('mbti가 아닌 데이터가 포함되어 있습니다.')
                    print(result_keys[i])
        except:
            print('데이터에 오류가 있습니다. mbti가 아닌 데이터가 있는지 확인 해 주세요. 데이터는 EnTP와 같이 대/소문자를 가리지 않으나, 엔팁 또는 2엔티피로 입력할 시 인식할 수 없습니다.')
            sys.exit()
            
        mbti = result_print(data_result[data_index[use_index[check_num]]], mode_num, mbti)
        if len(result_keys) < 16:
            for i in mbti:
                print(f'{i}: 0명  0%')
                
        count_mbti('I','E',data_result[data_index[use_index[check_num]]], 0)
        count_mbti('N','S',data_result[data_index[use_index[check_num]]], 1)
        count_mbti('T','F',data_result[data_index[use_index[check_num]]], 2)
        count_mbti('J','P',data_result[data_index[use_index[check_num]]], 3)
        
        isquit = input('종료를 원하시면 Y, 다른 목차를 처리하고 싶으시면 N을 입력하세요: ')
        if isquit == 'Y':
            sys.quit()
        else:
            continue
        
    if mode_num == 2:
        middle_num = 0
        data_result[data_index[use_index[check_num]]] = dict(sorted(data_result[data_index[use_index[check_num]]].items(), reverse = True))
        result_keys = list(data_result[data_index[use_index[check_num]]].keys())
        
        print(f'최댓값은 {result_keys[0]} 입니다.')
        print(f'최솟값은 {result_keys[-1]} 입니다.')
        for i in result_keys:
            middle_num += int(data_result[data_index[use_index[check_num]]][i])
        if middle_num%2 == 0:
            middle_num = int(middle_num/2)
            middle_num = (int(result_keys[middle_num-1]) + int(result_keys[middle_num]))/2
        else:
            middle_num = middle_num/2 + 0.5
            for i in result_keys:
                
                middle_num - int(data_result[data_index[use_index[check_num]]][i])
                if middle_num <= 0:
                    middle_num = int(i)
                    continue
            middle_num = result_keys[middle_num-1]
        print(f'중앙값은 {middle_num} 입니다.')
        aver_sum = aver_count = 0
        for i in result_keys:
            aver_sum += int(i)*int(data_result[data_index[use_index[check_num]]][i])
            
            aver_count += int(data_result[data_index[use_index[check_num]]][i])
            
        print(f'평균은 {round(aver_sum/aver_count, 3)}입니다')
        isquit = input('종료를 원하시면 Y, 다른 목차를 처리하고 싶으시면 N을 입력하세요: ')
        if isquit == 'Y':
            sys.quit()
        else:
            continue