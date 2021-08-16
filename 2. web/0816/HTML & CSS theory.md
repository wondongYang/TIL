## HTML & CSS

#### HTML

- 웹 표준, WHATWG 기준
- HTML = Hyper Text Markup Language
  - 웹 페이지를 작성하기 위한 언어
  - 웹 컨텐츠의 의미와 구조를 정의

- 시맨틱 태그
  - HTML5에서 의미론적 요소를 담은 태그의 등장
  - 대표적 태그
    - header : 문서 전체나 섹션의 헤더(머릿말 부분)
    - nav : 내비게이션
    - aside : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
    - section : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
    - article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
    - footer : 문서 전체나 섹션의 푸터(마지막 부분)



#### CSS

- 스타일, 레이아웃 등을 통해 문서(HTML)를 표시하는 방법을 지정하는 언어
- CSS 구문은 선택자와 함께 열림
- 선택자를 통해 스타일을 지정할 HTML 요소를 선택
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 실행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
  - 속성 : 어떤 스타일 기능을 변경할지 결정
  - 값 : 어떻게 스타일 기능을 변경할지 결정

- CSS 정의 방법
  - 인라인
  - 내부참조 <style>
  - 외부참조 - 분리된 CSS 파일

- 선택자
  - HTML 문서에서 특정한 요소를 선택하여 스타일링 하기 위해서는 반드시 선택자라는 개념이 필요하다.
  - 기본 선택자
    - 전체 선택자, 요소 선택자
    - 클래스 선택자, 아이디 선택자, 속성 선택자
  - 결합자 
    - 자손 결합자, 자식 결합자
    - 일반 형제 결합자, 인접 형제 결합자

- CSS Box model
  - content : 내용
  - padding : 내부 여백
  - border : 테두리
  - margin : 외부 여백

- CSS Position
  - relative : 상대 위치
  - absolute : 절대 위치
  - fixed : 고정 위치
- CSS Layout
  - Display
  - Position
  - Float
  - Flexbox : 요소 / 축
    - 배치방향 설정 : flex-direction
    - 메인축 방향 정렬 : justify-content
      - flex-start, flex-end, center, space-between, space-around, space-evenly
    - 교차축 방향 정렬 : align-items, align-self, align-content
      - align-items : flex-start, flex-end, center, stretch, baseline
      - align-content : flex-start, flex-end, center, stretch, space-between, space-around
      - align-self : auto, flex-start, flex-end, center, baseline, stretch
    - 기타 : flex-wrap, flex-flow, flex-grow, order
  - Grid system