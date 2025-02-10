#!/usr/bin/env python
# coding: utf-8

# In[54]:


import requests
import pandas as pd

URL = "https://openphish.com/feed.txt"

def fetch_phishing_urls():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()  

        phishing_urls = response.text.strip().split("\n") 

        df = pd.DataFrame(phishing_urls, columns=["URL"])
        df["Label"] = "bad"  

        df.to_csv("phishing_urls.csv", index=False)

        print(f"✅ Successfully saved {len(phishing_urls)} phishing URLs with labels to phishing_urls.csv")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data: {e}")

if __name__ == "__main__":
    fetch_phishing_urls()


# In[55]:


import pandas as pd

openphish_df = pd.read_csv("phishing_urls.csv")

phishtank_df = pd.read_csv(r"C:\Users\user\Desktop\phishing_site_urls.csv")

combined_df = pd.concat([openphish_df, phishtank_df]).drop_duplicates()

combined_df.to_csv("combined_phishing_urls.csv", index=False)

print(f"✅ Total phishing URLs collected: {len(combined_df)}")


# In[56]:


import pandas as pd

df = pd.read_csv("combined_phishing_urls.csv")
df


# In[58]:


df


# In[59]:


pip install requests beautifulsoup4 pandas


# In[60]:


import csv

safe_urls = [
    'https://www.google.com', 
    'https://www.wikipedia.org', 
    'https://www.amazon.com',
    'https://www.apple.com', 
    'https://www.microsoft.com', 
    'https://www.youtube.com',
    'https://www.reddit.com', 
    'https://www.bbc.com', 
    'https://www.nytimes.com',
    'https://www.cnn.com',
    'https://www.facebook.com',
    'https://www.twitter.com',
    'https://www.instagram.com',
    'https://www.linkedin.com',
    'https://www.pinterest.com',
    'https://www.yahoo.com',
    'https://www.stackoverflow.com',
    'https://www.quora.com',
    'https://www.merriam-webster.com',
    'https://www.etsy.com',
    'https://www.uber.com',
    'https://www.lyft.com',
    'https://www.spotify.com',
    'https://www.netflix.com',
    'https://www.dropbox.com',
    'https://www.salesforce.com',
    'https://www.adobe.com',
    'https://www.gitlab.com',
    'https://www.github.com',
    'https://www.imdb.com',
    'https://www.ted.com',
    'https://www.khanacademy.org',
    'https://www.nike.com',
    'https://www.asos.com',
    'https://www.bbc.co.uk',
    'https://www.chase.com',
    'https://www.bankofamerica.com',
    'https://www.wellsfargo.com',
    'https://www.citigroup.com',
    'https://www.samsung.com',
    'https://www.hpe.com',
    'https://www.intel.com',
    'https://www.ibm.com',
    'https://www.hp.com',
    'https://www.oracle.com',
    'https://www.tesla.com',
    'https://www.nasa.gov',
    'https://www.nike.com',
    'https://www.spotify.com',
    'https://www.pbs.org',
    'https://www.usps.com',
    'https://www.weather.com',
    'https://www.espn.com',
    'https://www.nationalgeographic.com',
    'https://www.theguardian.com',
    'https://www.forbes.com',
    'https://www.huffpost.com',
    'https://www.bloomberg.com',
    'https://www.wsj.com',
    'https://www.reuters.com',
    'https://www.cnbc.com',
    'https://www.theverge.com',
    'https://www.cnbc.com',
    'https://www.smithsonianmag.com',
    'https://www.livescience.com',
    'https://www.healthline.com',
    'https://www.webmd.com',
    'https://www.mayo.edu',
    'https://www.cdc.gov',
    'https://www.un.org',
    'https://www.who.int',
    'https://www.usa.gov',
    'https://www.whitehouse.gov',
    'https://www.redcross.org',
    'https://www.autotrader.com',
    'https://www.carmax.com',
    'https://www.consumerreports.org',
    'https://www.edx.org',
    'https://www.coursera.org',
    'https://www.udemy.com',
    'https://www.skillshare.com',
    'https://www.github.io',
    'https://www.heroku.com',
    'https://www.mongodb.com',
    'https://www.docker.com',
    'https://www.jupyter.org',
    'https://www.tensorflow.org',
    'https://www.scikit-learn.org',
    'https://www.undp.org',
    'https://www.apa.org'
]



with open('safe_urls.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['URL', 'Label'])

    for url in safe_urls:
        writer.writerow([url, 'safe'])

with open('safe_urls.csv', mode='r', encoding='utf-8') as file:
    print("Content of safe_urls.csv:")
    print(file.read())


# In[61]:


import pandas as pd

safe_data = pd.read_csv('safe_urls.csv')
phishing_data = pd.read_csv('phishing_urls.csv')

safe_data['Label'] = 'safe'
phishing_data['Label'] = 'phishing'

combined_data = pd.concat([safe_data[['URL', 'Label']], phishing_data[['URL', 'Label']]])

combined_data = combined_data.sample(frac=1, random_state=42).reset_index(drop=True)

combined_data.to_csv('combined_urls.csv', index=False)
print("Data combined and saved to 'combined_urls.csv'")


# In[62]:


combined_data = combined_data.drop_duplicates(subset='URL').dropna(subset=['URL'])
combined_data.reset_index(drop=True, inplace=True)


# In[63]:


from urllib.parse import urlparse

def extract_features(url):
    parsed_url = urlparse(url)
    features = {
        'url_length': len(url),
        'has_https': 1 if parsed_url.scheme == 'https' else 0,
        'num_subdomains': url.count('.') - 1
    }
    return features

features = [extract_features(url) for url in combined_data['URL']]
feature_df = pd.DataFrame(features)

final_data = pd.concat([combined_data[['Label']], feature_df], axis=1)

final_data.to_csv('final_dataset.csv', index=False)
print("Features extracted and saved to 'final_dataset.csv'")


# In[64]:


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

x = final_data.drop('Label', axis=1)
y = final_data['Label']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)



# In[73]:


print(y_pred[: 50])


# In[74]:


accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")


# In[75]:


from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))


# In[76]:


x_test


# In[77]:


pip install flask pandas scikit-learn requests


# In[82]:


from flask import Flask, request, render_template_string
import threading
import pandas as pd
from urllib.parse import urlparse
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib 

app = Flask(__name__)

print("⏳ Loading model...")
try:
    model = joblib.load('phishing_model.pkl')
    print("✅ Model loaded from 'phishing_model.pkl'")
except FileNotFoundError:
    print("🔄 Training a new model...")
    final_data = pd.read_csv('final_dataset.csv')
    x = final_data.drop('Label', axis=1)
    y = final_data['Label']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(random_state=42)
    model.fit(x_train, y_train)
    joblib.dump(model, 'phishing_model.pkl')
    print("✅ Model trained and saved to 'phishing_model.pkl'")

# Feature extraction function
def extract_features(url):
    parsed_url = urlparse(url)
    features = {
        'url_length': len(url),
        'has_https': 1 if parsed_url.scheme == 'https' else 0,
        'num_subdomains': url.count('.') - 1
    }
    return features

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_url = request.form.get('url')
        if user_url:
            features = extract_features(user_url)
            feature_df = pd.DataFrame([features])

            prediction = model.predict(feature_df)[0]
            result = "bad" if prediction == "phishing" else "safe"

            return render_template_string(html_template, result=result, url=user_url)
    return render_template_string(html_template)

# HTML Page (Using Template String)
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phishing URL Checker</title>
</head>
<body>
    <h1>Phishing URL Checker</h1>
    <form method="POST">
        <label for="url">Enter a URL:</label>
        <input type="text" id="url" name="url" placeholder="https://example.com" required>
        <button type="submit">Check</button>
    </form>
    {% if result %}
        <h2>Result:</h2>
        <p>The URL <strong>{{ url }}</strong> is classified as <strong>{{ result }}</strong>.</p>
    {% endif %}
</body>
</html>
"""

def run_flask():
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)

if __name__ == "__main__":
    thread = threading.Thread(target=run_flask)
    thread.start()


# In[ ]:




