import glob
import os
import shutil
import tempfile
import zipfile
from pathlib import Path

import pypandoc
from dotenv import load_dotenv
from pyrogram import Client, filters

load_dotenv()

app = Client(
    'bot',
    api_id=os.environ['API_ID'],
    api_hash=os.environ['API_HASH'],
    bot_token=os.environ['BOT_TOKEN'],
)


def convert_files_to_md(
    input_dir: Path, output_dir: Path, extension_filter: list[str]
) -> int:
    counverted_files_count = 0

    for src in input_dir.rglob('*.*'):
        dest = output_dir / src.relative_to(input_dir)
        dest.parent.mkdir(parents=True, exist_ok=True)

        if src.suffix in extension_filter:
            dest = dest.with_suffix('.md')
            # filters = ['pandoc-citeproc']
            # pdoc_args = ['--mathjax', '--smart']
            filters = []
            pdoc_args = []
            print(src, '->', dest)
            pypandoc.convert_file(
                glob.escape(str(src)),
                to='markdown_strict',
                outputfile=str(dest),
                extra_args=pdoc_args,
                filters=filters,
            )

            counverted_files_count += 1
        else:
            shutil.copy(src, dest)

    return counverted_files_count


@app.on_message(filters.document)
async def on_document(client, message):
    file_name = message.document.file_name

    with tempfile.TemporaryDirectory() as temp_dir_path_str:
        temp_dir_path = Path(temp_dir_path_str)

        input_file_dir_path = temp_dir_path / 'input_file_dir'
        input_file_dir_path.mkdir()

        await message.download(file_name=input_file_dir_path / file_name)
        input_file_path = input_file_dir_path / file_name

        input_dir_path = temp_dir_path / 'input'
        input_dir_path.mkdir()
        output_dir_path = temp_dir_path / 'output'
        output_dir_path.mkdir()

        if input_file_path.suffix == '.docx':
            shutil.copy(input_file_path, input_dir_path)
        elif zipfile.is_zipfile(input_file_path):
            shutil.unpack_archive(
                input_file_path,
                extract_dir=input_dir_path,
            )
        else:
            await message.reply('???????????? ???????? ???? ?????????? ???????? ?????????????????????????? ?? md-????????????.')
            return

        converted_files_count = convert_files_to_md(
            input_dir_path, output_dir_path, extension_filter=['.docx']
        )

        if converted_files_count:
            output_dir_files = list(output_dir_path.iterdir())
            if len(output_dir_files) == 1 and output_dir_files[0].is_file():
                # ???????????? ???????? ????????
                result_file = output_dir_files[0]
            else:
                result_file = (temp_dir_path / file_name).with_suffix('.zip')
                shutil.make_archive(
                    str(result_file.with_suffix('')),
                    'zip',
                    root_dir=output_dir_path,
                )

            await message.reply_document(result_file)
        else:
            await message.reply('?????? ???????????? ?????? ?????????????????????? ?? md-????????????.')


app.run()
