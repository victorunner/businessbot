# businessbot

# Конвертация docx-файлов в md-формат

В ответ на отправленный боту zip-архив будет возвращен zip-архив, в котором все docx-файлы будут заменены на соответствующие
им md-файлы. Структура архива будет сохранена.

Также, можно отправить боту отдельный docx-файл, в ответ будет возвращен соответствующий ему md-файл.

Для конвертации файлов в markdown используется `pypandoc`.

- https://pandoc.org/
- https://docs.pyrogram.org/
- https://pypi.org/project/pypandoc/

## Фильтры

INPUT --reader--> AST --filter--> AST --writer--> OUTPUT

## Расширения

Extensions can be individually enabled or disabled by appending +EXTENSION or -EXTENSION to the format name.

In addition to pandoc’s extended Markdown, the following Markdown variants are supported:

- markdown_phpextra (PHP Markdown Extra)
- markdown_github (deprecated GitHub-Flavored Markdown)
- markdown_mmd (MultiMarkdown)
- markdown_strict (Markdown.pl)
- commonmark (CommonMark)
- gfm (Github-Flavored Markdown)
- commonmark_x (CommonMark with many pandoc extensions)

To see which extensions are supported for a given format, and which are enabled by default, you can use the command

`pandoc --list-extensions=FORMAT`

where FORMAT is replaced with the name of the format.

# Проблемы

ModuleNotFoundError: No module named '_sqlite3'

Решение

```
sudo apt install libsqlite3-dev
```
Затем переустановить Python (с помощью pyenv).
