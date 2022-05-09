#!/usr/bin/python
# -*- coding: utf-8 -*-
"""NLP Homework #1: Address Detection in Chat Messages

This is a skeleton file for NLP homework.
Please complete your task with respect to the given guideline.
"""

def contain_address(text):
    '''
    Determine the given text whether the given text include a (Korean-style) address or not

    Parameters
    ----------
    text : string
        The given text

    Returns
    -------
    bool
        True if the given text contains an address or False otherwise

    Notes
    -----
    * My name: 정동하
    * My student ID: 18101269
    * My accuracy (max. 1): 0.8 (예: 0.999)
    * Brief description
      - 크게 두 가지 형태로 봤습니다.
        1. %s(로|길) %d
        2. %s(읍|동|아파트|힐|빌라) %d
    * Discussion
      - 주어진 데이터셋의 format을 알기 어려웠다. 무엇은 주소로 인식하고 어떤 것은 인식하지 못하였다. 예를들면 은총빌라 201호인데
        같은 지역에 거주한다면 인식을 잘 하겠지만 만약 다른 지역 사람이라면 이를 인지하기 힘들 것이다.
      - 따라서 주어진 테스트 데이터셋의 format에 맞춰 정규식을 작성했다. 그래서 다른 데이터셋으로 돌렸을 경우 높은 정확도가 나오기 힘들 것이다.
    * Collaborators:
    * References
      - [우하한 형제들 기술 블로그](https://techblog.woowahan.com/2505/)
      - [당근마켓 팀블로그](https://medium.com/daangn/%EC%A3%BC%EC%86%8C-%EC%9D%B8%EC%8B%9D%EC%9D%84-%EC%9C%84%ED%95%9C-%EC%82%BD%EC%A7%88%EC%9D%98-%EA%B8%B0%EB%A1%9D-df2d8f82d25)
    '''
    import re
    # PLEASE WRITE YOUR CODE HERE
    regex = re.compile(r"(([가-힣A-Za-z·\d~\-\.]{2,}(로|길).[\d]+)|([가-힣A-Za-z·\d~\-\.]+(읍|동|아파트|힐|빌라)\s)[\d]+)")
    return True if regex.findall(text) else False


# Define the test data
test_dataset = [
    {'text': '안녕하세요', 'truth': False},
    {'text': '내일 문앞에 두시면 가지러 가도 괜찮을지요^^? 오전9시정도..ㅎㅎ', 'truth': False},
    {'text': '안녕하세요. 카시트 구매하고 싶어 연락드립니다.', 'truth': False},
    {'text': '주소 부탁드릴께요^^', 'truth': False},
    {'text': '상어힐 222동 901호이고,', 'truth': True},
    {'text': '콩순이 중독 딸아이있는데 받고 싶어요!', 'truth': False},
    {'text': '1번이십니다.', 'truth': False},
    {'text': '사과마을5단지 512동 3335호입니다. 현관 앞에 걸어 놓을테니 편한 시간에 가져가세요.', 'truth': True},
    {'text': '아동복이 11호여서 6~7세까지 입을 수 있습니다.', 'truth': False},
    {'text': '암운아파트 505동2701호입니다.', 'truth': True},
    {'text': '저기.. 혹시 이거 리모콘 별도 인가요?', 'truth': False},
    {'text': '리모콘이 없는 모델입니다', 'truth': False},
    {'text': '죄송해요 예약중입니다~', 'truth': False},
    {'text': '제가 살께요', 'truth': False},
    {'text': '청솔아파트 103-1404 현관에 걸어두겠습니다', 'truth': True},
    {'text': '제 전화번호는 010-321-7654입니다.', 'truth': False},
    {'text': '판매되었나요', 'truth': False},
    {'text': '구매하고싶어요', 'truth': False},
    {'text': '9시 쯤 괜찮으실까요?', 'truth': False},
    {'text': '동명아파트 가동 104호입니다.', 'truth': True},
    {'text': '남편 보냈어요. 10분 안에 도착할 것 같습니다.', 'truth': False},
    {'text': '주소가 어떻게 되나요?', 'truth': False},
    {'text': '은노동이시지요? 이따 10시쯤 연락드리고 찾아뵈어도 될까요?', 'truth': False},
    {'text': '계세요 저기.장말 죄송한데요 오늘 10시전후에 뵙기로 했는데 그시간에 가기 어령울거 같아 앵해를 구합니다 내일 저녁에 찾아뵈어도 될까요?', 'truth': False},
    {'text': '님 제가 은노가면 8:40쯔 될것 가아요 짐 방문 드려도 괜찮을까요?', 'truth': False},
    {'text': '예! 은노역 5번 출구입니다.', 'truth': False},
    {'text': '네, 가능합니다! 8시~9시 사이 방문하면 늦을까요?', 'truth': False},
    {'text': '관찮습니다. 아리수로50길 50 222-901입니다!', 'truth': True},
    {'text': '오늘 퇴근하고 오후 7시 이후에 집에 있을 예정입니다. 은총빌라 201호인데, 혹시 직접 방문 가능하신지요?', 'truth': True},
    {'text': '잘쓸게요 고맙습니다', 'truth': False},
    {'text': '네~그럼 방문 전 한번 더 채팅 남겨두고 출발할께요. 기하동이라 10분 정도 걸릴 것 같아요. 저녁에 뵈어요!', 'truth': False},
    {'text': '301호 인터폰하시면 내려가겠습니다.', 'truth': False},
    {'text': '예약되어 오늘 저녁에 오시기로 하였서요. 혹시 안오시면 연락드리겠습니다.', 'truth': False},
    {'text': '네~^^ 구매하고 싶은데~직접 받으러 갈수 있습니다!', 'truth': False},
    {'text': '위치가 어디신가요?', 'truth': False},
    {'text': '저는 광금2동 3512번지 2층입니다.', 'truth': True},
    {'text': '지금 출발하는데요~ 10분 후 도착할 예정이에요.', 'truth': False},
    {'text': '확인하였습니다! 잠시 뒤에 뵙지요. 벨 누르시면 됩니다.', 'truth': False},
    {'text': '내일 가능합니다! 일하다보면 그럴 수 있지요', 'truth': False},
    {'text': '예! 명광로335번길 21-24입니다. 대문 앞에서 뵙지요.', 'truth': True},
    {'text': '네넵 길이가 30센티정도 됩니다', 'truth': False},
    {'text': '회사가 좀 늦게 마쳐서요', 'truth': False},
    {'text': '고맙습니다 내일 뵐께요', 'truth': False},
    {'text': '잠시 뒤에 뵙겠습니다. 은노역 건너편 별다방 앞에 있겠습니다.', 'truth': False},
    {'text': '아이아빠가 올라갔습니당~', 'truth': False},
    {'text': '애들이랑 일찍 잠에 빠져 이제 메세지 남깁니다.', 'truth': False},
    {'text': '예! 저희 회사는 성유구 정가로 211입니다. 회사 앞에서 뵙지요.', 'truth': True},
]

# Run and evaluate the given algorithm
results = [contain_address(test['text']) for test in test_dataset]
correct = sum([res == test_dataset[idx]['truth']
              for idx, res in enumerate(results)])
accuracy = correct / len(test_dataset)

# Print the results
print(f'### My results')
print(f'* The total number of questions: {len(test_dataset)}')
print(f'* The number of correct answers: {correct}')
print(f'* My accuracy: {accuracy:.3}')


'''
한글 코드 범위
ㄱ ~ ㅎ: 0x3131 ~ 0x314e
ㅏ ~ ㅣ: 0x314f ~ 0x3163
가 ~ 힣: 0xac00 ~ 0xd7a3

출처: https://jokergt.tistory.com/52 [Gun's Knowledge Base]
'''

'''
# True

상어힐 222동 901호이고,
사과마을5단지 512동 3335호입니다. 현관 앞에 걸어 놓을테니 편한 시간에 가져가세요.
암운아파트 505동2701호입니다.
청솔아파트 103-1404 현관에 걸어두겠습니다
동명아파트 가동 104호입니다.
관찮습니다. 아리수로50길 50 222-901입니다!
오늘 퇴근하고 오후 7시 이후에 집에 있을 예정입니다. 은총빌라 201호인데, 혹시 직접 방문 가능하신지요?
저는 광금2동 3512번지 2층입니다.
예! 명광로335번길 21-24입니다. 대문 앞에서 뵙지요.
예! 저희 회사는 성유구 정가로 211입니다. 회사 앞에서 뵙지요.
'''

'''
상어힐 222동 901호
사과마을5단지 512동 3335호
암운아파트 505동2701호
청솔아파트 103-1404 
동명아파트 가동 104호
아리수로50길 50 222-901
은총빌라 201호
광금2동 3512번지 2층
명광로335번길 21-24
성유구 정가로 211
'''

'''
# False

안녕하세요
내일 문앞에 두시면 가지러 가도 괜찮을지요^^? 오전9시정도..ㅎㅎ
안녕하세요. 카시트 구매하고 싶어 연락드립니다.
주소 부탁드릴께요^^
콩순이 중독 딸아이있는데 받고 싶어요!
1번이십니다.
아동복이 11호여서 6~7세까지 입을 수 있습니다.
저기.. 혹시 이거 리모콘 별도 인가요?
리모콘이 없는 모델입니다
죄송해요 예약중입니다~
제가 살께요
제 전화번호는 010-321-7654입니다.
판매되었나요
구매하고싶어요
9시 쯤 괜찮으실까요?
남편 보냈어요. 10분 안에 도착할 것 같습니다.
주소가 어떻게 되나요?
은노동이시지요? 이따 10시쯤 연락드리고 찾아뵈어도 될까요?
계세요 저기.장말 죄송한데요 오늘 10시전후에 뵙기로 했는데 그시간에 가기 어령울거 같아 앵해를 구합니다 내일 저녁에 찾아뵈어도 될까요?
님 제가 은노가면 8:40쯔 될것 가아요 짐 방문 드려도 괜찮을까요?
예! 은노역 5번 출구입니다.
네, 가능합니다! 8시~9시 사이 방문하면 늦을까요?
잘쓸게요 고맙습니다
네~그럼 방문 전 한번 더 채팅 남겨두고 출발할께요. 기하동이라 10분 정도 걸릴 것 같아요. 저녁에 뵈어요!
301호 인터폰하시면 내려가겠습니다.
예약되어 오늘 저녁에 오시기로 하였서요. 혹시 안오시면 연락드리겠습니다.
네~^^ 구매하고 싶은데~직접 받으러 갈수 있습니다!
위치가 어디신가요?
지금 출발하는데요~ 10분 후 도착할 예정이에요.
확인하였습니다! 잠시 뒤에 뵙지요. 벨 누르시면 됩니다.
내일 가능합니다! 일하다보면 그럴 수 있지요
네넵 길이가 30센티정도 됩니다
회사가 좀 늦게 마쳐서요
고맙습니다 내일 뵐께요
잠시 뒤에 뵙겠습니다. 은노역 건너편 별다방 앞에 있겠습니다.
아이아빠가 올라갔습니당~
애들이랑 일찍 잠에 빠져 이제 메세지 남깁니다.
'''