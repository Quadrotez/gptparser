<h1>ParsGPT</h1>

<p>ParsGPT - Это софт, который позволяет парсить Telegram-каналы и с помощью ИИ отвечать в комментариях (Между прочим, бесплатно)</p>


<p>Для начала работы вам нужно:</p>
<ol>
  <li>Установить <a href="https://www.python.org/">Python</a></li>
  <li>Запустить терминал (В Windows надо нажать win+r и вбить в табло "cmd" без кавычек)</li>
  <li>Вписать следующее:

    pip install pyrogram freeGPT tgcrypto g4f

  </li>
  <li><a href="https://tlgrm.ru/docs/api/obtaining_api_id">Иметь API_ID и API_HASH от Telegram</a></li>
  <li>Запустить файл main.exe (В первый раз желательно от имени администратора)</li>
  <li>Следовать указаниям в терминале до того, пока не появится надпись "Клиент запущен!"</li>
  <li><h3>ЗАКРЫТЬ ФАЙЛ main.exe</h3></li>
  <li>Запустить файл add_channel.exe (Если не работает, запускайте от имени администратора)</li>
  <li>Вбить ссылки на нужные вам каналы</li>
  <li><h3>ЗАКРЫТЬ ФАЙЛ add_channel.exe</h3></li>
  <li>Запустить файл main.exe</li>
  <li>Следовать указаниям. После надписи "Клиент запущен!" от вас больше ничего не требуется и вы можете тестить результат</li>
</ol>


<h2>Краткая сводка по каждому из файлов/папок</h2>

<h3>Папки</h3>
<ol>

<li>_internal - Важное. Лучше не трогать</li>
<li>sessions (Появляется при добавлении первой сессии) - в ней хранятся все ваши сессии. Так-как софт написан на pyrogram, сессии тоже pyrogram`овские</li>
</ol>
<h3>Файлы</h3>
<ol>
<li>main.exe - основной исполняемый файл. Пока он запущен - комментарии оставляются</li>
<li>add_channels.exe - файл, благодаря которому вы можете добавлять каналы в рабочие</li>
<li>prompt.txt - файл, в который вы можете вбить промпт самостоятельно</li>
<li>config.ini (Появляется при первом запуске main.exe) - файл с данными (API_ID, API_HASH, Задержка, Макс. кол-во символов)</li>
<li>channels.txt - файл с каналами (Каждая новая строчка - новый chat_id канала)</li>
<li>icon.ico - Иконка приложения</li>
<li>black_list.txt (Появляется при добавлении первой сессии) - файл со словами, при встрече с которыми софт не работает (Подробнее ниже)</li>
</ol>

<h3>Чёрный список</h3>
<p>Чёрный список предназначен для того, чтобы предотвратить комментирование на ненужные посты. Каждая строка: Набор символов, при встрече с которым работа софта не происходит</p>
<p>Пример:</p>

    реклама
    рекламный пост

<p>В этом случае все посты со словами "реклама" и "рекламный пост" работать не будут</p>


<h3>Флаги</h3>
<p>Вероятнее всего, вам это не понадобится, так как это является вещью продвинутого уровня, однако лучше знать.
Флаги предназначены для того, чтобы настраивать фильтры и т. д. более детально.
Предположим, нам нужно, чтобы комментарии не отправлялись при отсутствии подписи к картинке.
Для этого мы заходим в файл config.ini и добавляем секцию "Flags" (В самом низу файла, с новой строки)</p>

    [FLAGS]

<p>После этого софт будет знать, что вы добавили флаги и есть смысл их проверять.
Давайте добавим флаг для отсутствия рефлекса на картинки без подписи</p>

    ImageHasNoCaption = False
<p>Таким образом мы убираем рефлекс на ИзображениеНеИмеетОписание</p>
<p>Список всех флагов:</p>
<ol>
<li>ImageHasNoCaption - Если у изображения нет описания</li>
<li>VideoHasNoCaption - Если у видео нет описания</li>
<li>PostHasNoCaption - Если пост не имеет описания</li>
<li>IsImage - Если пост является изображением</li>
<li>IsVideo - Если пост является видео</li>
<li>IsDocument - Если пост является документом</li>
<li>IsVoice - Если пост является голосовым</li>
<li>IsGif - Если пост является Gif-Изображением</li>
<li>IsSticker - Если пост является стикером</li>

</ol>





<h3>Примечания</h3>
<li>Софт не работает, пока не запущен файл main.exe</li>
<li>Софт работает только с текстом. То есть, он может реагировать только на текстовые посты или на фото/видео/голосовые/т.п. с подписью! В остальных случаях будет просто писать то, что сочтёт нужным</li>
<li>Не пишите слишком длинные промпты!</li>
<li>Одна и та же сессия не может работать параллельно</li>