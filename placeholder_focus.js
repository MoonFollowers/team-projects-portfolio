

// 아이콘과 스팬 숨겨버리는 기능
// 헤더 검색 플레이스 홀더 값이 '검색'이라면, 아이콘과 스팬을 숨기기
function hide_fakeinput() {
    // 쿼리 셀렉터로 플레이스 홀더 값을 받아옴
    const fake_ph = document.querySelector('.searchbar_input').placeholder
    let fake_ph_el = document.getElementsByClassName('searchbar_input')
    console.log(fake_ph, fake_ph_el)
    const fake_icon = document.querySelector('.searchbar_icon')
    const fake_span = document.querySelector('.searchbar_span')
    if (fake_ph === '검색') {
        fake_icon.style.display = 'none'
        fake_span.style.display = 'none'
        fake_ph.focus()
    } else {
    }
}

// 포커스 아웃이 되거나 아이콘 버튼을 클릭하면,
// 다시 가짜 검색 아이콘과 스팬 태그가 나오기

function show_fakeinput(){

    // 헤더 검색 인풋 태그의 엘리멘트 가져오기
const is_focus = document.getElementsByClassName('searchbar_input')
// 헤더 검색 인풋 태그의 플레이스 홀더 값 가져오기
const fake_ph = document.querySelector('.searchbar_input').placeholder

// 헤더 가짜 인풋 아이템들의 값 가져오기
const fake_icon = document.querySelector('.searchbar_icon')
const fake_span = document.querySelector('.searchbar_span')

//    포커스 아웃이라면 (이벤트 리스너)
is_focus.addEventListener('focusout', (event) => {
    console.log('indside eventListener')
    // 거기에 인풋 태그가 검색이라면
    if (fake_ph === '검색') {
        fake_icon.style.display = 'block'
        fake_span.style.display = 'block'
    }
})

}



