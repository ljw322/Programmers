def solution(new_id):
    answer = ''
    # 검사
    # 1step
    new_id = new_id.lower()
    # print(new_id)
    # 2step
    for value in new_id:
        letter_index = ord(value)
        if ord('a') <= letter_index <= ord('z'):
            continue
        if ord('0') <= letter_index <= ord('9'):
            continue
        elif ord('-') == letter_index:
            continue
        elif ord('_') == letter_index:
            continue
        elif ord('.') == letter_index:
            continue
        else:
            new_id = new_id.replace(value,"")
    # print(new_id)
    # 3step
    temp_id = new_id[0]
    for i in range(1, len(new_id)):
        if temp_id[-1] == new_id[i] and new_id[i] == '.':
            continue
        else:
            temp_id += new_id[i]
    # print(temp_id)
    # 4step
    temp_id = temp_id.strip('.')
    # print(temp_id)
    # 5step
    if temp_id == '':
        temp_id = 'a'
    # print(temp_id)
    # 6step
    if len(temp_id)>=16:
        temp_id = temp_id[:15]
    # print(len(temp_id))
    # print(temp_id)
    if temp_id[-1] == '.':
        temp_id = temp_id[:-1]
    print(temp_id)
    # 7step
    n = len(temp_id)
    if n<=2:
        temp_id += temp_id[-1]*(3-n)
    print(temp_id)
    
    answer = temp_id
    
    
    return answer