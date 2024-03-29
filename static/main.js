document.addEventListener("DOMContentLoaded", function(event) {

    // определяем элементы ввода вывода
    const userName = document.querySelector('#userName')
    const content = document.querySelector('#content')
    const msgInput = document.querySelector('#text')
    const sendMessage = document.querySelector('#sendMessage')
    const uri_base = "https://cloozis.pythonanywhere.com/"

    document.addEventListener( 'keyup', event => {
        // нажимаем enter
        if( event.code === 'Enter' ){
            focus_msg_field()
            // console.log('enter was pressed');
        }
    });

    sendMessage.onclick = () => {
        // нажимаем конпку отправить сообщение
        focus_msg_field()
        // console.log('click button');
    };

    function focus_msg_field(){
        // фокусируем курсор на полее ввода сообщения
        add_message()
        msgInput.focus()
    }

    function getTimeNow(){
        // получаем время
        let timestamp = Date.now();
        return new Date(timestamp).toLocaleTimeString("en-US")
    }

    function html_template_msg(data){
        // рендерим сообщения на доску сообщений
        return '<a href="#" class="list-group-item list-group-item-action list-group-item-light"><div class="d-flex w-100 justify-content-between"><h6 class="mb-1">'+data.username+'</h6><small>'+data.timeNow+'</small></div><p class="mb-1">'+data.text+'</p></a>'

    }

    function add_message(){
        let uri = uri_base+"send";
        let data = [];
        // добавляем сообщение
        data.username = userName.value
        data.text = msgInput.value
        data.timeNow = getTimeNow()

        if(containsMat(data.username)){
            data.username = ''
            alert('Будте любезны, соблюдайте цензуру')
        }

        if(containsMat(data.text)){
            data.text = ''
            alert('Будте любезны, соблюдайте цензуру')
        }

        if(data.username && data.text){
            html = html_template_msg(data)

            post_data = {
                id: Date.now(),
                name: data.username,
                msg: data.text,
                time: data.timeNow
            }

            $.ajax({
                type: "POST",
                url: uri,
                data: JSON.stringify(post_data),
                contentType: "application/json"
                // success: function (result) {
                //     console.log(result);
                // },
                // error: function (result, status) {
                //     console.log(result);
                // }
            });

            content.innerHTML += html;
            content.scrollTo(0, content.scrollHeight);
        } else {
            alert("Введите имя и сообщение")
        }

        msgInput.value = ''

    }

    function add_items_to_main_container(data){
        // добавляем полученные элементы из файла json на доску сообщений
        let items = JSON.parse(data);

        items.forEach((item) => {
            let ndata = {
                'username':item.name,
                'timeNow':item.time,
                'text':item.msg
            }

            let html = html_template_msg(ndata)
            content.innerHTML += html;

            // console.log(item)
        })

        content.scrollTo(0, content.scrollHeight);

    }

    function loadMessages(){
        // загружаем сообщения с бекенда
        let uri = uri_base+"get_messages";

        $.post(uri, { get_message: "get_message" }, function(res){
            // console.log(res)
            content.innerHTML = '';
            add_items_to_main_container(res)
        })
    }


    setInterval(loadMessages, 5000)

    // console.log("dom loaded")
});