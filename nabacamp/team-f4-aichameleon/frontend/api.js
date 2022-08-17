console.log('api script on load')

async function uploadSelfie() {
    const selfieData = document.getElementById("file").files[0]
    console.log(selfieData)

    let form_data = new FormData()
    form_data.enctype = "multipart/form-data"
    form_data.append("file_give", selfieData)
    console.log(form_data.get("file_give"))

    const response = await fetch('http://127.0.0.1:5000/saveselfie', {
        method: 'POST',
        body: form_data,
    })

    console.log('셀피를 보내고 받아옵시다')
    response_json = await response.json()
    console.log(response_json)
    const filename = response_json['filename']
    const recent_selfie_id = response_json['recent_selfie_id']

    handleGif(filename, recent_selfie_id)
}

async function handleGif(filename, recent_selfie_id) {
    alert("모델이 돌아가는 중입니다 10초만 대기해주세요")
    // request
    let form_data = new FormData()
    form_data.append("filename", filename)
    form_data.append("recent_selfie_id", recent_selfie_id)
    console.log(form_data.get("filename"), form_data.get("recent_selfie_id"))
    // ajax
    const response = await fetch('http://127.0.0.1:5000/savegif', {
        method: 'POST',
        body: form_data
    })

    // response
    console.log(response.json())
    // localStorage.setItem("current_time", response_json['current_time'])
    window.location.replace('http://127.0.0.1:5500/frontend/result.html')
}


async function load_gif() {
    // let current_time = localStorage.current_time
    // console.log(current_time)
    let response = await fetch(`http://127.0.0.1:5000/loadgif?current_time`, {
        method: 'GET'
    })
    let response_json = await response.json()
    console.log('response 는 뭐냐면!!! ' + response_json)
    let current_time = response_json['current_time']
    let path = '../backend/static/image/gif/' + current_time + '.gif'
    const inner_card = document.getElementById("inner_card")
    console.log('inner card : ' + inner_card)
    inner_card.style.backgroundImage = "url(" + path + ")"
    const download = document.getElementById("download")
    download.href = path
    // 의사코드 작성
    // 뿌려주기
    // 스테이터스 코드 활용 해서 작업
    // 얼러트, 리플레이스, 콘솔로그, temp_html appending
}


async function select_music() {
    console.log('셀렉트 뮤직 진입!!!!')

    let response = await fetch('http://127.0.0.1:5000/emotion', {
        method: 'GET'
    })

    let response_json = await response.json()
    console.log('감정인식 : ' + response_json)

    const emotional_music = response_json['music_index'] + '.mp3'
    const music_path = '../frontend/audio/' + emotional_music

    const audioSource = document.getElementById("audioSource")
    audioSource.src = music_path

    // const musicSelect = document.getElementById("musicSelect")
    // musicSelect.style.display = "none"

    // const musicStart = document.getElementById("musicStart")
    // musicStart.style.display = "block"


}