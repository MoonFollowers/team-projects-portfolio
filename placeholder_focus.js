// 아이콘과 스팬 숨겨버리는 기능
// 헤더 검색 플레이스 홀더 값이 '검색'이라면, 아이콘과 스팬을 숨기기
function hide_fakeinput() {
    // 쿼리 셀렉터로 플레이스 홀더 값을 받아옴
    const fake_ph = document.querySelector('.searchbar_input').placeholder
    const fake_ph_el = document.getElementsByClassName('searchbar_input')
    console.log(fake_ph_el)
    const fake_icon = document.querySelector('.searchbar_icon')
    const fake_span = document.querySelector('.searchbar_span')
    if (fake_ph == '검색') {
        fake_icon.style.display = 'none'
        fake_span.style.display = 'none'
    } else {
    }
    console.log(fake_icon)
}

