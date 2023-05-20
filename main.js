text = '콰트로 맥시멈 미트 포커스드 어메이징 얼티밋 그릴드 패티 오브 더 비기스트 포 슈퍼 미트 프릭'
input = document.getElementById('input_typing');
input.focus();
start_typing();
for(const v in text){
    input.value = input.value + text.charAt(v);
}setTimeout(()=>{stop_typing()},1)