<kbd style="width: 2em; height: 2em;"><a href="#en">ENGLISH</a></kbd> | <kbd><a href="#ru">РУССКИЙ</a></kbd> | <kbd>[日本語](#ja)</kbd>

<h1 name="en" id="en">Moodle Automation: mass-fill in the questions bank in one click!</h1>

<b>The current version is written for a very specific school in mind. You might need to adapt the code and the urls to target Your school Moodle. You definetely need to have Your active Moodle username and password.</b>

To automatically generate your own `xml` file with questions, answers and dummies, You might want to cast an eye on my another repository: <a href="https://github.com/nakigoe/any-test-ru-reaper" target="_blank">github.com/nakigoe/any-test-ru-reaper</a>

## How To Use

### Change:

  •  The link to Your school Moodle login page `login_page`

  •  Your Moodle login `username`
  
  •  Your Moodle password `password`
  
  •  Generate Your own `questions-answers-dummies.xml` file, see <a href="https://github.com/nakigoe/any-test-ru-reaper" target="_blank">github.com/nakigoe/any-test-ru-reaper</a>
    
  •  The link to the Moodle pre-created course page `course_page`
    
  •  The link to the Moodle question creation page `question_url`
  
  •  You might need to change some selectors in the `moodle-fill-in.py` file inside the `open_new_question()` and `input_data_from_xml_into_the_form()` FUNCTIONS, since it could very well be Your customized school Moodle.

Be sure to write me to nakigoetenshi@gmail.com if You would like me to customize either the script or the `xml` file for Your school. And remember, there is a default PHP script to import a customized Moodle `xml` file with questions inside Your Moodle system also!
    
### Install Python:

  •  https://www.python.org/downloads/

### Install PIP If it Has Not been Installed With Python Automatically:

  •  https://pip.pypa.io/en/stable/installation/

### Install Libraries (please open the command line interface):

  •  Selenium `pip install selenium`

### Moodleの問題銀行に記入してください！

  •  double-click on `start.bat`

<hr>

<p style="margin: 0 auto" align="center">© <a href="https://nakigoe.org" target="_blank">NAKIGOE.ORG</a></p> 

<p style="margin: 0 auto" align="center">All rights reserved and no permissions are granted.</p>

<p style="margin: 0 auto" align="center">Please add stars to the repositories!</p>

<hr>

<h1 name="ja" id="ja">Moodle 自動化: 一回のクリックで Moodle 問題銀行を大量に記入！</h1>
<b>現在のバージョンは非常に特定の学校のために書かれています。自分の学校の Moodle を対象とするためにコードと URL を適応させる必要があるかもしれません。Moodle のユーザー名とパスワードを持っている必要が絶対にあります。</b>

自動的に質問、回答、ダミーの xml ファイルを生成する場合、補完プロジェクトも見てみるとよいでしょう: <a href="https://github.com/nakigoe/any-test-ru-reaper" target="_blank">github.com/nakigoe/any-test-ru-reaper</a>

使い方
変更:
• 学校の Moodle ログインページへのリンク `login_page`

• Moodle のログイン `username`

• Moodle のパスワード `password`

• 自分自身の `questions-answers-dummies.xml` ファイルを生成するには、<a href="https://github.com/nakigoe/any-test-ru-reaper" target="_blank">github.com/nakigoe/any-test-ru-reaper</a> を参照してください

• Moodle の事前作成されたコースページへのリンク `course_page`

• Moodle の問題作成ページへのリンク `question_url`

• 学校カスタム Moodle の場合、`moodle-fill-in.py` ファイル内の `open_new_question()` と `input_data_from_xml_into_the_form()` 関数内でセレクターを変更する必要があるかもしれません。

学校用にスクリプトまたは `xml` ファイルをカスタマイズしてほしい場合は、nakigoetenshi@gmail.com に連絡してください。そして、Moodle システムの Moodle Questions Bank に質問と回答の Moodle xml ファイルをインポートするデフォルトの PHP スクリプトも存在することを忘れないでください！
  
### Python をインストールなさってください：

  •  https://www.python.org/downloads/

### PIP が Python とともに自動的にインストールされていない場合は、PIP をインストールします:

  •  https://pip.pypa.io/en/stable/installation/

### Python ライブラリをインストールなさってください (コマンド プロンプトを開いてください)：

  •  Selenium `pip install selenium`

### すべての方々へ友達リクエストとメッセージをお送りくださいませ！

  •  `start.bat` をダブルクリックをなさってください。

<hr>

<p style="margin: 0 auto" align="center">© <a href="https://nakigoe.org/ja" target="_blank">NAKIGOE.ORG</a></p> 

<p style="margin: 0 auto" align="center">全ての権利を保有し、許可は一切与えられません。</p>

<p style="margin: 0 auto" align="center">リポジトリに星を付けてください！</p>

<hr>

<h1 name="ru" id="ru">Автоматизация Moodle: массовое заполнение банка вопросов Moodle одним кликом!</h1>

<b>Данный код написан имея в виду конкретный ВУЗ. Для использования ПО для Вашей школы, скорее всего, потребуется внести изменения в код и селекторы. Наличие актуального логина и пароля к Вашему Moodle обязательно.</b>

Чтобы автоматически сгенерировать Ваш собственный файл `xml` с вопросами и ответами (правильными и неправильными), смотрите мой проект <a href="https://github.com/nakigoe/any-test-ru-reaper" target="_blank">github.com/nakigoe/any-test-ru-reaper</a>

## Инструкция

### Замените:

  •  сноску на страницу логина в Moodle Вашей школы `login_page`

  •  имя пользователя `username`
  
  •  пароль `password`
  
  •  сгенерируйте Вас собственный файл `questions-answers-dummies.xml`, смотрите <a href="https://github.com/nakigoe/any-test-ru-reaper" target="_blank">github.com/nakigoe/any-test-ru-reaper</a>
    
  •  сноску на заранее созданный курс Moodle `course_page`
    
  •  сноску на создание вопроса Moodle `question_url`
  
  •  Вероятно, потребуется заменить селекторы внутри файла `moodle-fill-in.py` в ФУНКЦИЯХ `open_new_question()` и `input_data_from_xml_into_the_form()` так как это кастомизированный Moodle Вашей конкретной школы.

Пишите мне на почту nakigoetenshi@gmail.com, если необходимо кастомизировать скрипт либо файл `xml` специально для Вашей школы. Помните о наличии встоенного в Moodle скрипта PHP для импорта файла `xml` в специальном формате Moodle внутри системы Moodle Вашей школы!
   
### Установите Python:

  •  https://www.python.org/downloads/

### Установите PIP, если он не установился с Python автоматически:

  •  https://pip.pypa.io/en/stable/installation/

### Установите библиотеки (откройте командную строку):

  •  Selenium `pip install selenium`
  
### Запускайте и массово заполняйте банк вопросов Moodle одним мановением руки!

  •  двойной щелчок мыши по `start.bat`

<hr>

<p style="margin: 0 auto" align="center">© <a href="https://nakigoe.org/ru" target="_blank">NAKIGOE.ORG</a></p> 

<p style="margin: 0 auto" align="center">Все права сохраняются и никаких разрешений не предоставляется.</p>

<p style="margin: 0 auto" align="center">Ставьте звёзды на репозитории!</p>

<hr>

<br>
<p style="margin: 0 auto" align="center">Please cast an eye on my website:</p>
<h1><a href="https://nakigoe.org/" style="background-color: black;" target="_blank">
  <img style="display: block; width: calc(100vw - (100vw - 100%));"
    src="https://nakigoe.org/_IMG/logo.png" 
    srcset="https://nakigoe.org/_IMG/logo.png 4800w,
      https://nakigoe.org/_SRC/logo-3840.png 3840w,
      https://nakigoe.org/_SRC/logo-2560.png 2560w,
      https://nakigoe.org/_SRC/logo-2400.png 2400w,
      https://nakigoe.org/_SRC/logo-2048.png 2048w,
      https://nakigoe.org/_SRC/logo-1920.png 1920w,
      https://nakigoe.org/_SRC/logo-1600.png 1600w,
      https://nakigoe.org/_SRC/logo-1440.png 1440w,
      https://nakigoe.org/_SRC/logo-1280.png 1280w,
      https://nakigoe.org/_SRC/logo-1200.png 1200w,
      https://nakigoe.org/_SRC/logo-1080.png 1080w,
      https://nakigoe.org/_SRC/logo-960.png 960w,
      https://nakigoe.org/_SRC/logo-720.png 720w,
      https://nakigoe.org/_SRC/logo-600.png 600w,
      https://nakigoe.org/_SRC/logo-480.png 480w,
      https://nakigoe.org/_SRC/logo-300.png 300w"
    alt="NAKIGOE.ORG">
<img class="blend" style="display: block; width: calc(100vw - (100vw - 100%));" 
  src="https://nakigoe.org/_IMG/nakigoe-academy-night.jpg" 
  srcset="https://nakigoe.org/_IMG/nakigoe-academy-night.jpg 2800w,
    https://nakigoe.org/_SRC/nakigoe-academy-night-2048.jpg 2048w"
  alt="Nakigoe Academy">
  <img class="blend" style="display: block; width: calc(100vw - (100vw - 100%)); padding-bottom: 0.05em;"
    src="https://nakigoe.org/_IMG/logo-hot-bevel.png" 
    srcset="https://nakigoe.org/_IMG/logo-hot-bevel.jpg 4800w,
      https://nakigoe.org/_SRC/logo-hot-bevel-3840.jpg 3840w,
      https://nakigoe.org/_SRC/logo-hot-bevel-2560.jpg 2560w,
      https://nakigoe.org/_SRC/logo-hot-bevel-2400.jpg 2400w,
      https://nakigoe.org/_SRC/logo-hot-bevel-2048.jpg 2048w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1920.jpg 1920w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1600.jpg 1600w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1440.jpg 1440w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1280.jpg 1280w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1200.jpg 1200w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1080.jpg 1080w,
      https://nakigoe.org/_SRC/logo-hot-bevel-960.jpg 960w,
      https://nakigoe.org/_SRC/logo-hot-bevel-720.jpg 720w,
      https://nakigoe.org/_SRC/logo-hot-bevel-600.jpg 600w,
      https://nakigoe.org/_SRC/logo-hot-bevel-480.jpg 480w,
      https://nakigoe.org/_SRC/logo-hot-bevel-300.jpg 300w"
    alt="NAKIGOE.ORG">
</a></h1>

<p style="margin: 0 auto" align="center">© NAKIGOE.ORG</p> 

<p style="margin: 0 auto" align="center">All rights reserved and no permissions are granted.</p>

<p style="margin: 0 auto" align="center">Please add stars to the repositories!</p>
