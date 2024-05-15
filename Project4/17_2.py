import requests
import plotly.express as px

from operator import itemgetter

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:5]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
        submission_dicts.append(submission_dict)
    except KeyError:
        # Skip over promotional posts or posts without comments
        pass

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

titles = [submission_dict['title'] for submission_dict in submission_dicts]
comments = [submission_dict['comments'] for submission_dict in submission_dicts]
hn_links = [submission_dict['hn_link'] for submission_dict in submission_dicts]

fig = px.bar(x=titles, y=comments, labels={'x': 'Discussion Title', 'y': 'Number of Comments'},
             title='Most Active Discussions on Hacker News', hover_data={'hn_link': hn_links})
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.show()
