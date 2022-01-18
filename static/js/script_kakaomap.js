// 지도를 표시할 div
    var mapContainer = document.getElementById('map'),
        mapOption = {
            center: new kakao.maps.LatLng(35.767656775135855, 128.1321971735885), // 지도의 중심좌표
            level: 13, // 지도의 확대 레벨
            mapTypeId: kakao.maps.MapTypeId.ROADMAP // 지도종류
        };

    // 지도를 생성한다
    var map = new kakao.maps.Map(mapContainer, mapOption);

     // 마커 클러스터러를 생성합니다
    var clusterer = new kakao.maps.MarkerClusterer({
        map: map, // 마커들을 클러스터로 관리하고 표시할 지도 객체
        averageCenter: true, // 클러스터에 포함된 마커들의 평균 위치를 클러스터 마커 위치로 설정
        minLevel: 10 // 클러스터 할 최소 지도 레벨
    });

    var markers = [];
        for (var i = 0; i < 데이터.length; i++) {
            // 지도에 마커를 생성하고 표시한다
            var marker = new kakao.maps.Marker({
                position: new kakao.maps.LatLng(데이터[i][0], 데이터[i][1]), // 마커의 좌표
                map: map // 마커를 표시할 지도 객체
            });
            // 인포윈도우를 생성합니다
            var infowindow = new kakao.maps.InfoWindow({
                content: 데이터[i][2]
            });

            markers.push(marker);
            kakao.maps.event.addListener(marker, 'mouseover', makeOverListener(map, marker, infowindow));
            kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(infowindow));
        }

    // 클러스터러에 마커들을 추가합니다
    clusterer.addMarkers(markers);


    // 인포윈도우를 표시하는 클로저를 만드는 함수입니다
    function makeOverListener(map, marker, infowindow) {
        return function () {
            infowindow.open(map, marker);
        };
    }

    // 인포윈도우를 닫는 클로저를 만드는 함수입니다
    function makeOutListener(infowindow) {
        return function () {
            infowindow.close();
        };
    }



// 지도 위치 지정 기능
// 지도 스크립트_드롭다운 클릭 시 해당 지역으로 지도 포커싱

function seoul() {
        var moveLatLon = new kakao.maps.LatLng(37.54952047275068, 126.9877909044856);
        map.setLevel(8)
        map.setCenter(moveLatLon);
    }
    function daejeon() {
        var moveLatLon = new kakao.maps.LatLng(36.35840744048402, 127.35169517129687);
        map.setLevel(8)
        map.setCenter(moveLatLon);
    }
    function busan() {
        var moveLatLon = new kakao.maps.LatLng(35.15937088229944, 129.04982359237417);
        map.setLevel(8)
        map.setCenter(moveLatLon);
    }
    function daegu() {
        var moveLatLon = new kakao.maps.LatLng(35.862809292506554, 128.57617295097683);
        map.setLevel(8)
        map.setCenter(moveLatLon);
    }
    function gwangju() {
        var moveLatLon = new kakao.maps.LatLng(35.16120532030494, 126.82293416919757);
        map.setLevel(8)
        map.setCenter(moveLatLon);
    }
    function ulsan() {
        var moveLatLon = new kakao.maps.LatLng(35.54329980358315, 129.3456479445236);
        map.setLevel(8)
        map.setCenter(moveLatLon);
    }
    function incheon() {
        var moveLatLon = new kakao.maps.LatLng(37.47350369548072, 126.67023750511827);
        map.setLevel(8)
        map.setCenter(moveLatLon);
    }
    function jeju() {
        var moveLatLon = new kakao.maps.LatLng(33.49969019108693, 126.52553511531994);
        map.setLevel(8)
        map.setCenter(moveLatLon);
    }

// 마커를 표시할 위치와 내용을 가지고 있는 객체 배열입니다
    var 데이터 = [
            //서울맛집
            [37.57749233274407, 126.98604658739973, '<div class="mark_info">카페노티드 안국</div>'],
            [37.56255207348654, 126.98559827156627, '<div class="mark_info">명동교자 본점</div>'],
            [37.52462817792284, 127.04263461358946, '<div class="mark_info">스케줄 청담</div>'],
            [37.53598448259359, 126.97222047156214, '<div class="mark_info">몽탄</div>'],
            [37.53598448259359, 126.97222047156214, '<div class="mark_info">로우앤슬로우</div>'],
            [37.525406603963155, 127.03670987205962, '<div class="mark_info">호족반 청담</div>'],
            [37.57402057288615, 126.98967147181573, '<div class="mark_info">온천집 익선</div>'],
            [37.56834566038699, 126.9304775827864, '<div class="mark_info">목란</div>'],
            //대전맛집
            [36.35840744048402, 127.35169517129687, '<div class="mark_info">임진강장어</div>'],
            [36.789307936278504, 127.12754087155112, '<div class="mark_info">당산오돌</div>'],
            [36.32769009073234, 127.42729080041626, '<div class="mark_info">성심당 본점</div>'],
            [36.32681173513397, 127.39545214291932, '<div class="mark_info">태평소국밥 본점</div>'],
            [36.36457500694532, 127.34128242883602, '<div class="mark_info">카페 인터뷰</div>'],
            [36.33404610239948, 127.43782665764611, '<div class="mark_info">치앙마이방콕</div>'],
            [36.359227133688, 127.42662606515651,   '<div class="mark_info">오문창순대국밥</div>'],
            [36.36699532478072, 127.38054973121982, '<div class="mark_info">베스타뷔페</div>'],
            //부산맛집
            [35.153162778549465, 129.12478444858584, '<div class="mark_info">좋은한우</div>'],
            [35.203429960431244, 129.08385729969294, '<div class="mark_info">오꼬식당</div>'],
            [35.19705833668, 129.09971547227406, '<div class="mark_info">고메밀면 동래본점</div>'],
            [35.163215865466945, 129.16638306351865, '<div class="mark_info">해운대암소갈비집</div>'],
            [35.16887267158675, 129.16636200039707, '<div class="mark_info">해운대가야밀면</div>'],
            [35.15678020362044, 129.1342897290217, '<div class="mark_info">수변최고돼지국밥</div>'],
            [35.14842417840112, 129.11385727152978, '<div class="mark_info">동경밥상</div>'],
            [35.10209565674584, 129.03081932492717, '<div class="mark_info">이재모피자</div>'],
            //대구맛집
            [35.83855813828949, 128.5791395770442, '<div class="mark_info">조조칼국수 앞산본점</div>'],
            [35.85637944710946, 128.58849757154763, '<div class="mark_info">대쿠이 본점</div>'],
            [35.85531294402579, 128.65034736159353, '<div class="mark_info">리안</div>'],
            [35.868590812505495, 128.59348979951432, '<div class="mark_info">삼송빵집 본점</div>'],
            [35.83365578756154, 128.57767343806148, '<div class="mark_info">앞산주택</div>'],
            [35.981722656574824, 128.6351607831935, '<div class="mark_info">헤이마</div>'],
            [35.885506679240066, 128.58154052994416, '<div class="mark_info">걸리버막창</div>'],
            //광주맛집
            [35.154963711193005, 126.85440773596108, '<div class="mark_info">상무초밥 상무점</div>'],
            [35.147757154830245, 126.91761728672508, '<div class="mark_info">궁전제과 충장본점</div>'],
            [35.1911466699724, 126.8304838207219, '<div class="mark_info">초돈</div>'],
            [35.138970637650836, 126.79486517716452, '<div class="mark_info">송정떡갈비 1호점</div>'],
            [35.15432486469979, 126.91801085387208, '<div class="mark_info">나주식당</div>'],
            [35.14991673290416, 126.92481189759543, '<div class="mark_info">스트럭트</div>'],
            [35.124798461377054, 126.90922878890916, '<div class="mark_info">카페304 충장점</div>'],
            //울산맛집
            [35.56532668133025, 129.1224605296966, '<div class="mark_info">언양기와집불고기</div>'],
            [35.56860325557732, 129.32869231922922, '<div class="mark_info">농도</div>'],
            [35.56860325557732, 129.32869231922922, '<div class="mark_info">함양집</div>'],
            [35.54281679351544, 129.3389467626508, '<div class="mark_info">헤이다이닝</div>'],
            [35.35868095298546, 129.35640810393096, '<div class="mark_info">카페리베리베</div>'],
            [35.538656231420745, 129.33636780638804, '<div class="mark_info">이중생업</div>'],
            [37.47265131147812, 126.62475475260705, '<div class="mark_info">온센 본점</div>'],
            [37.47547269346376, 126.61785233810375, '<div class="mark_info">신승반점 본점</div>'],
            [37.491287363751724, 126.72887964017917, '<div class="mark_info">바베큐광장 화로구이</div>'],
            [36.36457500694532, 127.34128242883602, '<div class="mark_info">로니로티 부평점</div>'],
            [37.43927855691396, 126.43085669493034, '<div class="mark_info">스타파이브</div>'],
            [37.51453473014412, 126.64927676258034, '<div class="mark_info">경인면옥</div>'],
            //제주맛집
            [33.2588794598111, 126.40724334591556, '<div class="mark_info">연돈</div>'],
            [33.49692277226924, 126.50871809874401, '<div class="mark_info">제주김만복 본점</div>'],
            [33.51151639111576, 126.52003692513769, '<div class="mark_info">우진해장국</div>'],
            [33.516824664191134, 126.51707330719294, '<div class="mark_info">자매국수 본점</div>'],
            [33.50240105680744, 126.51076285478193, '<div class="mark_info">칠돈가 본점</div>'],
            [33.21769869385963, 126.24989758780404, '<div class="mark_info">미영이네식당</div>'],
            [33.51008457746911, 126.53104430929686, '<div class="mark_info">용초밥</div>'],

            ]