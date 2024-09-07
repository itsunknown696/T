import logging   #Bot Created by @SudoR2spr
import subprocess   #Bot Created by @SudoR2spr
import datetime   #Bot Created by @SudoR2spr
import asyncio   #Bot Created by @SudoR2spr
import os   #Bot Created by @SudoR2spr
import requests   #Bot Created by @SudoR2spr
import time   #Bot Created by @SudoR2spr
from p_bar import progress_bar   #Bot Created by @SudoR2spr
import aiohttp   #Bot Created by @SudoR2spr
import aiofiles   #Bot Created by @SudoR2spr
import tgcrypto   #Bot Created by @SudoR2spr
import concurrent.futures   #Bot Created by @SudoR2spr
import subprocess   #Bot Created by @SudoR2spr
from pyrogram.types import Message   #Bot Created by @SudoR2spr
from pyrogram import Client, filters   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
def duration(filename):   #Bot Created by @SudoR2spr
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",   #Bot Created by @SudoR2spr
                             "format=duration", "-of",   #Bot Created by @SudoR2spr
                             "default=noprint_wrappers=1:nokey=1", filename],   #Bot Created by @SudoR2spr
        stdout=subprocess.PIPE,   #Bot Created by @SudoR2spr
        stderr=subprocess.STDOUT)   #Bot Created by @SudoR2spr
    return float(result.stdout)   #Bot Created by @SudoR2spr
       #Bot Created by @SudoR2spr
def exec(cmd):   #Bot Created by @SudoR2spr
        process = subprocess.run(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE)   #Bot Created by @SudoR2spr
        output = process.stdout.decode()   #Bot Created by @SudoR2spr
        print(output)   #Bot Created by @SudoR2spr
        return output   #Bot Created by @SudoR2spr
        #err = process.stdout.decode()   #Bot Created by @SudoR2spr
def pull_run(work, cmds):   #Bot Created by @SudoR2spr
    with concurrent.futures.ThreadPoolExecutor(max_workers=work) as executor:   #Bot Created by @SudoR2spr
        print("Waiting for tasks to complete")   #Bot Created by @SudoR2spr
        fut = executor.map(exec,cmds)   #Bot Created by @SudoR2spr
async def aio(url,name):   #Bot Created by @SudoR2spr
    k = f'{name}.pdf'   #Bot Created by @SudoR2spr
    async with aiohttp.ClientSession() as session:   #Bot Created by @SudoR2spr
        async with session.get(url) as resp:   #Bot Created by @SudoR2spr
            if resp.status == 200:   #Bot Created by @SudoR2spr
                f = await aiofiles.open(k, mode='wb')   #Bot Created by @SudoR2spr
                await f.write(await resp.read())   #Bot Created by @SudoR2spr
                await f.close()   #Bot Created by @SudoR2spr
    return k   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
async def download(url,name):   #Bot Created by @SudoR2spr
    ka = f'{name}.pdf'   #Bot Created by @SudoR2spr
    async with aiohttp.ClientSession() as session:   #Bot Created by @SudoR2spr
        async with session.get(url) as resp:   #Bot Created by @SudoR2spr
            if resp.status == 200:   #Bot Created by @SudoR2spr
                f = await aiofiles.open(ka, mode='wb')   #Bot Created by @SudoR2spr
                await f.write(await resp.read())   #Bot Created by @SudoR2spr
                await f.close()   #Bot Created by @SudoR2spr
    return ka   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
def parse_vid_info(info):   #Bot Created by @SudoR2spr
    info = info.strip()   #Bot Created by @SudoR2spr
    info = info.split("\n")   #Bot Created by @SudoR2spr
    new_info = []   #Bot Created by @SudoR2spr
    temp = []   #Bot Created by @SudoR2spr
    for i in info:   #Bot Created by @SudoR2spr
        i = str(i)   #Bot Created by @SudoR2spr
        if "[" not in i and '---' not in i:   #Bot Created by @SudoR2spr
            while "  " in i:   #Bot Created by @SudoR2spr
                i = i.replace("  ", " ")   #Bot Created by @SudoR2spr
            i.strip()   #Bot Created by @SudoR2spr
            i = i.split("|")[0].split(" ",2)   #Bot Created by @SudoR2spr
            try:   #Bot Created by @SudoR2spr
                if "RESOLUTION" not in i[2] and i[2] not in temp and "audio" not in i[2]:   #Bot Created by @SudoR2spr
                    temp.append(i[2])   #Bot Created by @SudoR2spr
                    new_info.append((i[0], i[2]))   #Bot Created by @SudoR2spr
            except:   #Bot Created by @SudoR2spr
                pass   #Bot Created by @SudoR2spr
    return new_info   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
def vid_info(info):   #Bot Created by @SudoR2spr
    info = info.strip()   #Bot Created by @SudoR2spr
    info = info.split("\n")   #Bot Created by @SudoR2spr
    new_info = dict()   #Bot Created by @SudoR2spr
    temp = []   #Bot Created by @SudoR2spr
    for i in info:   #Bot Created by @SudoR2spr
        i = str(i)   #Bot Created by @SudoR2spr
        if "[" not in i and '---' not in i:   #Bot Created by @SudoR2spr
            while "  " in i:   #Bot Created by @SudoR2spr
                i = i.replace("  ", " ")   #Bot Created by @SudoR2spr
            i.strip()   #Bot Created by @SudoR2spr
            i = i.split("|")[0].split(" ",3)   #Bot Created by @SudoR2spr
            try:   #Bot Created by @SudoR2spr
                if "RESOLUTION" not in i[2] and i[2] not in temp and "audio" not in i[2]:   #Bot Created by @SudoR2spr
                    temp.append(i[2])   #Bot Created by @SudoR2spr
                       #Bot Created by @SudoR2spr
                    # temp.update(f'{i[2]}')   #Bot Created by @SudoR2spr
                    # new_info.append((i[2], i[0]))   #Bot Created by @SudoR2spr
                    #  mp4,mkv etc ==== f"({i[1]})"    #Bot Created by @SudoR2spr
                       #Bot Created by @SudoR2spr
                    new_info.update({f'{i[2]}':f'{i[0]}'})   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
            except:   #Bot Created by @SudoR2spr
                pass   #Bot Created by @SudoR2spr
    return new_info   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
async def run(cmd):   #Bot Created by @SudoR2spr
    proc = await asyncio.create_subprocess_shell(   #Bot Created by @SudoR2spr
        cmd,   #Bot Created by @SudoR2spr
        stdout=asyncio.subprocess.PIPE,   #Bot Created by @SudoR2spr
        stderr=asyncio.subprocess.PIPE)   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
    stdout, stderr = await proc.communicate()   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
    print(f'[{cmd!r} exited with {proc.returncode}]')   #Bot Created by @SudoR2spr
    if proc.returncode == 1:   #Bot Created by @SudoR2spr
        return False   #Bot Created by @SudoR2spr
    if stdout:   #Bot Created by @SudoR2spr
        return f'[stdout]\n{stdout.decode()}'   #Bot Created by @SudoR2spr
    if stderr:   #Bot Created by @SudoR2spr
        return f'[stderr]\n{stderr.decode()}'   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
       #Bot Created by @SudoR2spr
       #Bot Created by @SudoR2spr
       #Bot Created by @SudoR2spr
def old_download(url, file_name, chunk_size = 1024 * 10):   #Bot Created by @SudoR2spr
    if os.path.exists(file_name):   #Bot Created by @SudoR2spr
        os.remove(file_name)   #Bot Created by @SudoR2spr
    r = requests.get(url, allow_redirects=True, stream=True)   #Bot Created by @SudoR2spr
    with open(file_name, 'wb') as fd:   #Bot Created by @SudoR2spr
        for chunk in r.iter_content(chunk_size=chunk_size):   #Bot Created by @SudoR2spr
            if chunk:   #Bot Created by @SudoR2spr
                fd.write(chunk)   #Bot Created by @SudoR2spr
    return file_name   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
def human_readable_size(size, decimal_places=2):   #Bot Created by @SudoR2spr
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:   #Bot Created by @SudoR2spr
        if size < 1024.0 or unit == 'PB':   #Bot Created by @SudoR2spr
            break   #Bot Created by @SudoR2spr
        size /= 1024.0   #Bot Created by @SudoR2spr
    return f"{size:.{decimal_places}f} {unit}"   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
def time_name():   #Bot Created by @SudoR2spr
    date = datetime.date.today()   #Bot Created by @SudoR2spr
    now = datetime.datetime.now()   #Bot Created by @SudoR2spr
    current_time = now.strftime("%H%M%S")   #Bot Created by @SudoR2spr
    return f"{date} {current_time}.mp4"   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
async def download_video(url,cmd, name):   #Bot Created by @SudoR2spr
    download_cmd = f'{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args "aria2c: -x 16 -j 32"'   #Bot Created by @SudoR2spr
    global failed_counter   #Bot Created by @SudoR2spr
    print(download_cmd)   #Bot Created by @SudoR2spr
    logging.info(download_cmd)   #Bot Created by @SudoR2spr
    k = subprocess.run(download_cmd, shell=True)   #Bot Created by @SudoR2spr
    if "visionias" in cmd and k.returncode != 0 and failed_counter <= 10:   #Bot Created by @SudoR2spr
        failed_counter += 1   #Bot Created by @SudoR2spr
        await asyncio.sleep(5)   #Bot Created by @SudoR2spr
        await download_video(url, cmd, name)   #Bot Created by @SudoR2spr
    failed_counter = 0   #Bot Created by @SudoR2spr
    try:   #Bot Created by @SudoR2spr
        if os.path.isfile(name):   #Bot Created by @SudoR2spr
            return name   #Bot Created by @SudoR2spr
        elif os.path.isfile(f"{name}.webm"):   #Bot Created by @SudoR2spr
            return f"{name}.webm"   #Bot Created by @SudoR2spr
        name = name.split(".")[0]   #Bot Created by @SudoR2spr
        if os.path.isfile(f"{name}.mkv"):   #Bot Created by @SudoR2spr
            return f"{name}.mkv"   #Bot Created by @SudoR2spr
        elif os.path.isfile(f"{name}.mp4"):   #Bot Created by @SudoR2spr
            return f"{name}.mp4"   #Bot Created by @SudoR2spr
        elif os.path.isfile(f"{name}.mp4.webm"):   #Bot Created by @SudoR2spr
            return f"{name}.mp4.webm"   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
        return name   #Bot Created by @SudoR2spr
    except FileNotFoundError as exc:   #Bot Created by @SudoR2spr
        return os.path.isfile.splitext[0] + "." + "mp4"   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
async def send_doc(bot: Client, m: Message,cc,ka,cc1,prog,count,name):   #Bot Created by @SudoR2spr
    reply = await m.reply_text(f"Uploading - `{name}`")   #Bot Created by @SudoR2spr
    time.sleep(1)   #Bot Created by @SudoR2spr
    start_time = time.time()   #Bot Created by @SudoR2spr
    await m.reply_document(ka,caption=cc1)   #Bot Created by @SudoR2spr
    count+=1   #Bot Created by @SudoR2spr
    await reply.delete (True)   #Bot Created by @SudoR2spr
    time.sleep(1)   #Bot Created by @SudoR2spr
    os.remove(ka)   #Bot Created by @SudoR2spr
    time.sleep(3)    #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
async def send_vid(bot: Client, m: Message,cc,filename,thumb,name,prog):   #Bot Created by @SudoR2spr
       #Bot Created by @SudoR2spr
    subprocess.run(f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"', shell=True)   #Bot Created by @SudoR2spr
    await prog.delete (True)   #Bot Created by @SudoR2spr
    reply = await m.reply_text(f"**Uploading ...** - `{name}`")   #Bot Created by @SudoR2spr
    try:   #Bot Created by @SudoR2spr
        if thumb == "no":   #Bot Created by @SudoR2spr
            thumbnail = f"{filename}.jpg"   #Bot Created by @SudoR2spr
        else:   #Bot Created by @SudoR2spr
            thumbnail = thumb   #Bot Created by @SudoR2spr
    except Exception as e:   #Bot Created by @SudoR2spr
        await m.reply_text(str(e))   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
    dur = int(duration(filename))   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
    start_time = time.time()   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
    try:   #Bot Created by @SudoR2spr
        await m.reply_video(filename,caption=cc, supports_streaming=True,height=720,width=1280,thumb=thumbnail,duration=dur, progress=progress_bar,progress_args=(reply,start_time))   #Bot Created by @SudoR2spr
    except Exception:   #Bot Created by @SudoR2spr
        await m.reply_document(filename,caption=cc, progress=progress_bar,progress_args=(reply,start_time))   #Bot Created by @SudoR2spr
    os.remove(filename)   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
    os.remove(f"{filename}.jpg")   #Bot Created by @SudoR2spr
    await reply.delete (True)   #Bot Created by @SudoR2spr
       #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
