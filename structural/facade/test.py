from structural.facade.VideoConversionFacade import VideoConversionFacade

if __name__ == "__main__":
    converter: VideoConversionFacade = VideoConversionFacade()
    mp4_file: str = converter.convert_video("ducktyping.ogg", "mp4")
    print(mp4_file)