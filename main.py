import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import Qt, QUrl


class VideoPlayer(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Video Player")
        # Initial resolution set, this will be modified in main function to actual resolution
        self.setGeometry(100, 100, 800, 600)

        self.mediaPlayer = QMediaPlayer(None)
        self.videoWidget = QVideoWidget()
        self.setCentralWidget(self.videoWidget)
        self.mediaPlayer.setVideoOutput(self.videoWidget)

    def playVideo(self, filename):
        mediaUrl = QUrl.fromLocalFile(filename)
        self.mediaPlayer.setSource(mediaUrl)
        self.mediaPlayer.play()


def main():
    app = QApplication(sys.argv)
    screens = app.screens()
    players = []

    for screen in screens:
        player = VideoPlayer()
        player.setWindowFlags(player.windowFlags() | Qt.WindowType.FramelessWindowHint)
        player.setGeometry(screen.availableGeometry())
        player.showFullScreen()
        players.append(player)

    for player in players:
        player.playVideo("/Users/vicky/personal/screenChange/mixkit-cute-gray-cat-with-dark-glasses-dancing-49057-hd-ready.mp4")

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
