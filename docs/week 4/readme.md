# 4주차 과제

## 주의사항

```
[공지] 미션 PREVIEW 설명

미션 문제에 대한 상세한 설명 등이 담기게 되는 것이라, 녹화 영상을 강사님 유튜브를 통해 저희가 제공을 하되, 이에 대한 녹화 및 유포, 복제등이
발생하는 경우 본 익스턴십 참여 부터, 관련된 모든 법적제재의 대상이 될수 있으므로 본 영상은 시청용으로만 이용 가능 하시다는것 유념 부탁드리겠습니다.

감사합니다.

```

## 개요

- 3주차 작업물에서 이어서 진행합니다.
- DRF를 사용합니다.
- 마켓관리자용 상품 CRUD REST API를 구현합니다.
- JWT 인증을 구현합니다.
- 엘라스틱서치에 상품정보를 동기화합니다.
- 엘라스틱서치를 이용한 상품검색을 구현합니다.

## 출제자의 의도

- 주어진 제약사항 내에서 최선의 기술적 판단
- 유지보수와 작업효율을 고려하여 아키텍쳐 설계 및 라이브러리 선택

## 학습목표

- 마켓관리자용 상품 CRUD REST API를 구현합니다.
- JWT 인증을 구현합니다.
- 리액트를 사용하여 상품 리스팅(추가미션)
- 리액트를 사용하여 상품 삭제(추가미션)
- 리액트에서 JWT를 통한 인증(추가미션)
- 엘라스틱서치에 상품정보를 동기화합니다.(추가미션)
- 엘라스틱서치를 이용한 상품검색을 구현합니다.(추가미션)

## 필수과제 배경

- 마켓관리자는 자신의 마켓에 속한 상품만 관리할 수 있습니다.
- 그렇게 하기 위해서는 인증과 인가가 필수 입니다.
- 디버깅할 때 POSTMAN을 사용하는 것을 추천드립니다. 추천사항일 뿐, 다른 툴도 사용가능합니다.

## 필수과제

- 마켓관리자용 상품 CRUD REST API를 구현합니다.
- JWT 인증을 구현합니다.

## 추가과제 배경

- 리액트 관련 예제는 codepen.io/pen 에서 진행하셔도 됩니다.
  - 이 경우 과제제출시에는 codepen의 소스코드를 zip으로 export하는 기능을 사용하시면 됩니다.
- 리액트예제는 어떠한 방식으로 만드셔도 괜찮습니다.
- JWT 관련 장고 라이브러리로는 simple jwt를 추천드립니다.
  - https://github.com/jazzband/djangorestframework-simplejwt
- JWT 토큰은 리프레시와 엑세스토큰을 둘다 다뤄야 합니다.
- 엘라스틱서치는 운영환경에 도커로 설치해도 되고, 운영체제에 직접설치해도 됩니다.
  - 엘라스틱서치는 전체 메모리가 4기가 이하인 컴퓨터에서는 수행하기가 어렵습니다.
  - 엘라스틱서치 같은 경우, 과제제출시 직접 구상한 엘라스틱서치 설치 및 운영 방법을 메뉴얼(md, 마크다운형식)파일로 만들어서 형식으로 보내주세요.
    - 이 부분은 간단하게 작성하시면 됩니다.

## 추가과제

- 리액트를 사용하여 상품 리스팅
- 리액트를 사용하여 상품 삭제
- 리액트에서 JWT를 통한 인증
- 엘라스틱서치에 상품정보를 동기화합니다.
- 엘라스틱서치를 이용한 상품검색을 구현합니다.

## Q&A

### Q01. Django rest framwork를 사용해서 구현해야 하나요?

- 네, MTV는 사용하지 않습니다.

### Q02. 제출은 강사님 깃으로 하면 되나요?

- Discord의 공지사항 유튜브 주소를 참고하시어 진행하시면 되겠습니다. 또한 수업페이지에도 주소가 있으니 참고하시면 되겠습니다.
  - [과제 제출방법 1부](https://youtu.be/QAHEWqFDo5U)
  - [과제 제출방법 2부](https://youtu.be/biZXRksAm4U)
  - [과제 수행인증영상 예시](https://youtu.be/g0p_GsjAHRA)

### Q03. 제출할 때 수행인증영상도 촬영해야 하나요?

- 아래 예시와 같이, 촬영하시면 됩니다.
- 해당 영상을 유튜브에 업로드(일부공개로) 하신 후, 영상의 주소를 checklist.md 파일에 남겨주시면 됩니다.
- [과제 수행인증영상 예시](https://youtu.be/g0p_GsjAHRA)

### Q04. back 폴더는 뭔가요?

- 미션의 과제결과물 중 장고결과물을 그 안에 담아주시면 됩니다.

### Q05. front 폴더는 뭔가요?

- 미션의 과제결과물 중 리액트결과물을 그 안에 담아주시면 됩니다.

### Q06. infra 폴더는 뭔가요?

- 미션의 과제결과물 중 인프라(엘라스틱서치)결과물 그 안에 담아주시면 됩니다.
  - 다만 인프라의 경우 제출이 어렵기 때문에, 소스코드 말고 운영메뉴얼.md 파일을 제출해주세요.
    - 운영메뉴얼.md 에는 다음과 같은 내용이 담겨야 합니다.
      - 엘라스틱서치가 설치된 서버IP
      - 엘라스틱서치 관리자(키바나) 접속주소
      - 엘라스틱서치 설치방법