from pytube import YouTube

YouTube('https://www.youtube.com/watch?v=IOtcSSqVIdo').streams[0].download(filename='test')
