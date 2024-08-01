def vigenere_encrypt(plain_text, keyword):
    cipher_text = ""  # 암호화된 결과를 저장할 빈 문자열 초기화
    i = 0
    plain_text = plain_text.upper()  # 평문을 대문자로 변환
    keyword = keyword.upper()  # 키워드를 대문자로 변환

    while i < len(plain_text):  # 평문의 모든 문자를 처리할 때까지 반복
        char = plain_text[i]  # 현재 평문 문자 가져오기
        key_char = keyword[i % len(keyword)]  # 현재 위치에 해당하는 키워드 문자 가져오기

        if char.isalpha():  # 현재 문자가 알파벳인 경우 암호화
            shift = ord(key_char) - ord('A')  # 키워드 문자에 따른 이동 값 계산 (0 ~ 25)
            # 비즈네르 암호화 공식: (평문 문자 - 'A' + 이동 값) % 26 + 'A'
            cipher_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))  
        else:  # 알파벳이 아닌 경우 그대로 추가
            cipher_text += char

        i += 1  # 다음 문자로 이동

    return cipher_text  # 암호화된 문자열 반환

def vigenere_decrypt(cipher_text, keyword):
    plain_text = ""  # 복호화된 결과를 저장할 빈 문자열 초기화
    i = 0
    cipher_text = cipher_text.upper()  # 암호문을 대문자로 변환
    keyword = keyword.upper()  # 키워드를 대문자로 변환

    while i < len(cipher_text):  # 암호문의 모든 문자를 처리할 때까지 반복
        char = cipher_text[i]  # 현재 암호문 문자 가져오기
        key_char = keyword[i % len(keyword)]  # 현재 위치에 해당하는 키워드 문자 가져오기

        if char.isalpha():  # 현재 문자가 알파벳인 경우 복호화
            shift = ord(key_char) - ord('A')  # 키워드 문자에 따른 이동 값 계산 (0 ~ 25)
            # 비즈네르 복호화 공식: (암호문 문자 - 'A' - 이동 값) % 26 + 'A'
            plain_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:  # 알파벳이 아닌 경우 그대로 추가
            plain_text += char

        i += 1  # 다음 문자로 이동

    return plain_text  # 복호화된 문자열 반환

# 기능 1 테스트: 암호화
plain_text = input("암호화할 평문을 입력하세요: ")
keyword = input("키워드를 입력하세요: ")
cipher_text = vigenere_encrypt(plain_text, keyword)
print("암호문:", cipher_text)

# 기능 2 테스트: 복호화
cipher_text = input("복호화할 암호문을 입력하세요: ")
keyword = input("키워드를 입력하세요: ")
plain_text = vigenere_decrypt(cipher_text, keyword)
print("평문:", plain_text)