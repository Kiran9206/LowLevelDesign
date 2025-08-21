'''
Simple Factory Pattern for Audio Player
Problem Statement
You are developing an audio player application that supports different audio formats, such as MP3, WAV, and FLAC. Each audio format requires a specific
decoder and player implementation. To keep your audio player extensible and maintainable, you decide to implement the Simple Factory pattern to create
audio player objects based on the audio format.

Assignment
Your task is to implement the Simple Factory pattern to create audio players for different audio formats in the audio player application. The Simple Factory
 pattern allows you to encapsulate the creation logic of audio player objects, making it easy to add support for new audio formats in the future.

Task 1 - Creating Audio Player Classes (Product Hierarchy)
Complete the common product class AudioPlayer: Start by completing the parent AudioPlayer class. This is going to be the parent class for each supported
audio format. Each audio player class should implement the same set of methods for playing, pausing, and stopping audio playback. Additionally, each class
should have attributes that store information about the audio file, such as the volume and playback rate. Make sure to use the same names of the methods
and attributes in the parent class. Also, abstract common methods with the same implementation in the parent class.

Modify the concrete product classes (e.g., MP3AudioPlayer, WAVAudioPlayer, FLACAudioPlayer): Implement the concrete audio player classes for each supported
audio format. Each class should inherit from the AudioPlayer class and implement the methods to play, pause, and stop audio playback.

Task 2 - Implementing the Simple Factory
Next, complete the AudioPlayerFactory class that follows the Simple Factory pattern. This class should provide a static method create_audio_player to create
an audio player objects based on the audio format. The factory class should take care of instantiating the appropriate audio player class based on the format
provided and the relevant arguments. Remember you have to create the actual concrete audio player objects in the factory class so pass the required
arguments to the factory method.

Instructions
Implement the AudioPlayer class as a common parent class for all audio players. Include attributes and methods that are common to all audio players.

Implement the AudioPlayerFactory class that implements the Simple Factory pattern. Add a method create_audio_player to create audio player objects based
on the audio format and relevant arguments (volume, playback_rate).

Run the provided test cases in the AudioPlayerTest class to verify the correctness of your implementation. The tests will check if all audio player classes
are implemented correctly and if the factory class is able to create audio player objects for different audio formats.
'''

from abc import ABC, abstractmethod

class AudioPlayer(ABC):

    def __init__(self, volume: int = 50, playback_rate: float = 1.0):
        self.volume = volume
        self.playback_rate = playback_rate


    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class MP3AudioPlayer(AudioPlayer):

    def play(self):
        print("Playing MP3 audio")

    def pause(self):
        print("pausing MP3 audio")

    def stop(self):
        print("stopping MP3 audio")

class WAVAudioPlayer(AudioPlayer):
    def play(self):
        print("Playing WAV audio")

    def pause(self):
        print("pausing WAV audio")

    def stop(self):
        print("stopping WAV audio")

class FLACAudioPlayer(AudioPlayer):
    def play(self):
        print("Playing FLAC audio")

    def pause(self):
        print("pausing FLAC audio")

    def stop(self):
        print("stopping FLAC audio")


class AudioPlayerFactory:

    @staticmethod
    def create_audio_player(audio_format:str,volume: int = 50, playback_rate: float = 1.0):
        if audio_format == "MP3":
            return MP3AudioPlayer(volume,playback_rate)
        elif audio_format == "WAV":
            return WAVAudioPlayer(volume,playback_rate)
        elif audio_format == "FLAC":
            return FLACAudioPlayer(volume,playback_rate)
        else:
            raise ValueError(f"Unsupported audio format: {audio_format}")


class AudioPlayerTest:
    @staticmethod
    def test_audio_players():
        mp3_player = AudioPlayerFactory.create_audio_player("MP3", volume=70, playback_rate=1.2)
        assert isinstance(mp3_player, MP3AudioPlayer)
        mp3_player.play()
        mp3_player.pause()
        mp3_player.stop()

        wav_player = AudioPlayerFactory.create_audio_player("WAV", volume=80, playback_rate=1.0)
        assert isinstance(wav_player, WAVAudioPlayer)
        wav_player.play()
        wav_player.pause()
        wav_player.stop()

        flac_player = AudioPlayerFactory.create_audio_player("FLAC", volume=60, playback_rate=1.5)
        assert isinstance(flac_player, FLACAudioPlayer)
        flac_player.play()
        flac_player.pause()
        flac_player.stop()

        # unknown_player = AudioPlayerFactory.create_audio_player('unknown')

if __name__ == "__main__":
    AudioPlayerTest.test_audio_players()
    print("All audio player tests passed successfully.")


