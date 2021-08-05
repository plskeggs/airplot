# store in ~/.plotly/.credentials
#{
#    "username": "plskeggs",
#    "stream_ids": ["otado15o61", "n6hijlp47b", "7nh82jg9qe", "63r093ymbs", "46dyjqvm0s", "zedjqolnfx"],
#    "api_key": "eddlcIONoLyfQTjQrhe9"
#}
# username: plskeggs
# api key: eddlcIONoLyfQTjQrhe9
# streaming tokens:
# otado15o61
# n6hijlp47b
# 7nh82jg9qe
# 63r093ymbs
# 46dyjqvm0s
# zedjqolnfx

import numpy as np
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go

# stream_ids = [u'otado15o61', u'n6hijlp47b', u'7nh82jg9qe', u'63r093ymbs', u'46dyjqvm0s', u'zedjqolnfx']
stream_ids = tls.get_credentials_file()['stream_ids']

# Get stream id from stream id list 
stream_id = stream_ids[0]

# Make instance of stream id object 
stream_1 = go.Stream(
    token=stream_id,  # link stream id to 'token' key
    maxpoints=80      # keep a max of 80 pts on screen
)

# Initialize trace of streaming plot by embedding the unique stream_id
trace1 = go.Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=stream_1         # (!) embed stream id, 1 per trace
)

data = go.Data([trace1])

# Add title to layout object
layout = go.Layout(title='Time Series')

# Make a figure object
fig = go.Figure(data=data, layout=layout)

# We will provide the stream link object the same token that's associated with the trace we wish to stream to
s = py.Stream(stream_id)

# We then open a connection
s.open()

# (*) Import module keep track and format current time
import datetime
import time

i = 0    # a counter
k = 5    # some shape parameter

# Delay start of stream by 5 sec (time to switch tabs)
time.sleep(5)

while True:

    # Current time on x-axis, random numbers on y-axis
    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    y = (np.cos(k*i/50.)*np.cos(i/50.)+np.random.randn(1))[0]

    # Send data to your plot
    s.write(dict(x=x, y=y))

    #     Write numbers to stream to append current data on plot,
    #     write lists to overwrite existing data on plot

    time.sleep(1)  # plot a point every second    
# Close the stream when done plotting
s.close()

