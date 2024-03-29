# проект "Элизиум"

> "Эллизиум: Выживание в забытом мире"

## как установить?

1. (рекомендуеться) установите python 3.10.3 [здесь](https://www.python.org/ftp/python/3.10.3/python-3.10.3-amd64.exe)
2. (рекомендуеться) установите библиотеку pygame `pip install pygame`
3. скопируйте репозиторий в вашу рабочую папку с помощью `git clone git@github.com:Shadowino/Ellizium.git` 
4. откройте папку в вашей IDE и приступайте!

> работайте из папки `Scripts`. включена поддержка виртуального окружения `venv`

## Общая идея:
"Эллизиум" - это игра о выживании в забытом мире, где игроки оказываются в суровых условиях и должны использовать свою смекалку и навыки, чтобы приспособиться к окружающей среде, найти ресурсы и выжить.

Основные механики:

1. Реалистичные потребности персонажа: Игроки должны следить за уровнем голода, жажды, усталости и здоровья своего персонажа. Поиск пищи, воды, отдыха и медицинских принадлежностей является критически важным.
2. Изучение мира и сбор ресурсов: Игроки исследуют мир "Эллизиума" в поисках ресурсов, создают оружие, инструменты и укрепленные укрытия, используя найденные материалы.
3. Перемещение и навигация: Игроки должны ориентироваться в мире, исследовать местность, избегать опасностей и находить маршруты, чтобы достичь целей.
4. Динамичная дикая природа: В мире "Эллизиум" игроки сталкиваются с ледниковыми пустошами, густыми джунглями, опасными хищниками и другими угрозами, которые представляют вызов для выживания.
5. Личное развитие и адаптация: Геймплей "Эллизиума" подчеркивает важность развития личных навыков, изучения окружающей среды и принятия решений в условиях экстремальных ситуаций.

Заключение

"Эллизиум: Выживание в забытом мире" обещает обеспечить игроков захватывающим и реалистичным опытом выживания, с фокусом на взоимодействия между игроками.

# стек технологий

ожидаются технологии:
* python (в качестве сервера)
* http+css+JS (в качестве клиента)
* SQLlite для сохранения миров (сомнительно)

# струтура проекта

> пока не решена. `.gitignore` это файл необходимый для правильной работы git (игнорирет лишние файлы) 

* server - директория с исходным кодом сервера 
* site - frontend часть (да, технически тоже исходный код)
* site/img - все картинки если надо сюда
