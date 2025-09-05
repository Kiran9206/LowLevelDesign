'''
Strategy Pattern for Video Streaming Quality Adjustment
Problem Statement
You are developing a video streaming platform that offers different streaming qualities, such as low, standard, and high definition.
The platform should dynamically adjust the streaming quality based on the user's network conditions to ensure smooth playback.
Additionally, more quality adjustment algorithms may be added in the future. Your task is to implement this dynamic quality adjustment
system using the Strategy pattern.

Assignment
Your assignment is to implement the Strategy pattern to create strategies for adjusting video streaming quality.
The existing code provides a starting point, but you need to complete the implementation.

Task 1: Implement Strategy Interface
Use the existing QualityAdjustmentStrategy interface, which defines the supportsType method that returns the VideoQuality
supported by the strategy.
Add a new method adjust to the QualityAdjustmentStrategy interface that accepts a Video object and returns a modified Video
object with adjusted quality settings.
Task 2: Implement Concrete Strategies
Create three concrete strategy classes, each corresponding to a different video quality (LOW, MEDIUM, HIGH). Implement the
supportsType method to return the supported quality.
Implement the adjust method for each concrete strategy to adjust the Video object's quality settings based on the quality level.
Copy the implementation code from the original VideoStreamingManager class.
Task 3: Update VideoStreamingManager
Modify the VideoStreamingManager class to accept a QualityAdjustmentStrategy object in the constructor.
Implement the streamVideo method in the VideoStreamingManager class to use the provided strategy to adjust the video's quality settings.
Testing Instructions
Ensure that you have implemented the Strategy pattern correctly by passing the provided test cases in the VideoStreamingManagerTest class.
The test cases validate that there are three concrete strategies, that the QualityAdjustmentStrategy interface has the required methods,
and that the VideoStreamingManager class is correctly updated to use the strategy for quality adjustment.
Make sure that the adjust method in each strategy class correctly adjusts the video's quality settings based on the supported quality.
Remember to refactor the existing code to use the Strategy pattern and ensure that your tests pass successfully. Good luck with your assignment!
'''

from abc import ABC, abstractmethod

class Video:

    def __init__(self, title, quality):
        self.title = title
        self.quality = quality

    def __str__(self):
        return f'Video quality is {self.quality}'



# step1: create strategy interface
class QualityAdjustmentStrategy(ABC):

    @abstractmethod
    def supports_type(self, type:str)->bool:
        pass

    @abstractmethod
    def adjust(self, video):
        pass

# step2: create concrete strategy
class LowStrategy(QualityAdjustmentStrategy):

    def supports_type(self, type:str):
        quality = "LOW"
        return quality == type

    def adjust(self, video: Video):
        video.quality = "LOW"
        return video

class MediumStrategy(QualityAdjustmentStrategy):

    def supports_type(self, type):
        quality = "MEDIUM"
        return quality == type

    def adjust(self, video: Video):
        video.quality = "MEDIUM"
        return video

class HighStrategy(QualityAdjustmentStrategy):

    def supports_type(self, type):
        quality = "HIGH"
        return quality == type

    def adjust(self, video: Video):
        video.quality = "HIGH"
        return video

# step3: create quality manager factory

class QualityManagerFactory:

    @staticmethod
    def get_strategy(quality):
        if quality == "LOW":
            return LowStrategy()
        elif quality == "MEDIUM":
            return MediumStrategy()
        elif quality == "HIGH":
            return HighStrategy()
        else:
            raise ValueError("Unsupported quality type")


# step4: create VideoStreamingManager class

class VideoStreamingManager:

    def __init__(self, strategy: QualityAdjustmentStrategy):
        self.strategy = strategy

    def stream_video(self, video: Video):
        return self.strategy.adjust(video)

if __name__ == "__main__":

    video_1 = Video('video_1', 'LOW')
    video_2 = Video('video_2', 'MEDIUM')
    video_3 = Video('video_3', 'HIGH')

    strategy = QualityManagerFactory.get_strategy('LOW')
    low_stream = VideoStreamingManager(strategy)
    print(low_stream.stream_video(video_3))

    strategy = QualityManagerFactory.get_strategy('MEDIUM')
    medium_stream = VideoStreamingManager(strategy)
    print(medium_stream.stream_video(video_1))


    strategy = QualityManagerFactory.get_strategy('HIGH')
    high_stream = VideoStreamingManager(strategy)
    print(high_stream.stream_video(video_2))

