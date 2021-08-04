## 1. CSS Layout

1. Float

   - flexbox 및 그리드 레이아웃과 같은 기술이 나오기 이전에 Float은 열 레이아웃을 만드는데 사용됨

   - flexbox와 gird의 출현과 함께 결국 원래 텍스트 블록 내에서 float 이미지를 위한 역할로 돌아감

     (mdn 에서는 더 새롭고 나은 레이아웃 기술이 나와있으므로 레거시 레이아웃 기술로 분류해놓기도)

   - 웹에서 여전히 사용하는 경우도 있음(ex. naver nav bar)

     

2. Flexbox

   - display: flex : 정렬하려는 부모 요소에 작성

   - flex-direction : item이 쌓이는 방향 설정

   - flex-wrap : 요소들이 강제로 한 줄에 배치 되게 할 것인지 여부 설정

   - flex-flow : flex-direction과 flex-wrap의 shorthand

   - justify-content : main 축 정렬

   - align-items : cross 축 정렬

   - align-self : 개별 item에 적용하는 속성

   - order : 작은 숫자 일수록 앞(우선 쌓이는 방향)으로 이동

   - flew-grow : 주축에서 남는 공간을 항목들에게 분배하는 방법

     

3. Bootstrap

   - spacing : margin, padding, 위치, 크기 등을 지정

   - color : 색 지정

   - Components : Badge, Card 등의 요소 지정

   - Grid system : flexbox로 제작, container, rows, column으로 컨텐츠를 배치하고 정렬

     

