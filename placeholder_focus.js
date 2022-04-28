function hide_fakeinput() {
    const fake_ph = document.querySelector('.searchbar_input').placeholder
    console.log(fake_ph)
    const fake_icon = document.querySelector('.searchbar_icon')
    const fake_span = document.querySelector('.searchbar_span')
    if (fake_ph == '검색') {
        fake_icon.style.display = 'none'
        fake_span.style.display = 'none'
    } else {
    }
    console.log(fake_icon)
}