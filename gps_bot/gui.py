import sys
import io
import folium
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import uic


class GuiGPS(QMainWindow):
    def __init__(self):
        super(GuiGPS, self).__init__()
        uic.loadUi(r'gui.ui', self)
        self.setWindowTitle('GPS Bot')

        spot = self.findChild(QVBoxLayout, 'main_spot')

        fime_1 = [25.725123035154194, -100.31350035231671]

        coordinate = fime_1
        m = folium.Map(
        	tiles='Stamen Terrain',
        	zoom_start=20,
        	location=coordinate
        )

        folium.Marker(location=fime_1,
                      popup='Your Location',
                      icon=folium.Icon(icon='arrow-up', prefix='fa')).add_to(m)

        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        spot.addWidget(webView)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 35px;
        }
    ''')
    
    myApp = GuiGPS()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')